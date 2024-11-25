import sys

import pygame

from model.logic.Dificultades import *
from model.logic.EquipoLogico import EquipoLogico
from model.logic.formacion import *
from model.logic.Partido import Partido
from settings import *
from view.JugarView import JugarView
from model.database.AbmEquipo import AbmEquipo
from .CanchaViewControlador import CanchaController
from .Controlador import Controlador
from controller.LoginJugarViewControlador import LoginJugarViewControlador
from model.database.AbmUsuario import AbmUsuario
from model.database.Usuario import Usuario
from controller.EquipoJugarViewControlador import EquipoJugarViewControlador
from model.database.Equipo import Equipo


class JugarController(Controlador):
    def __init__(self):
        super().__init__()
        self._view = JugarView(SCREEN)
        self.__estadio_actual = camp_nou
        self.__genero_equipo = EquipoLogico("Equipo FC")
        self.__nombre_usuario = Usuario()
        self.__equipo = Equipo(None, "EquipoFC", None, 0)
        self.__formacion_actual = FORMACION_PREDETERMINADA
        self.__usuario_ingresado = False
        self.__equipo_ingresado = False
        self.__dado_apretado = False
        self.__cancha = CanchaController(SCREEN, "Facil", self.__genero_equipo)
        self.__LoginUsuario = LoginJugarViewControlador(SCREEN, self)
        self.__LoginEquipo = EquipoJugarViewControlador(SCREEN, self.__equipo, self)

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        from controller.MenuViewControlador import MenuController

        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["dado"].checkForInput(mouse_pos):  # Boton del Dado
                    print("HOLAHOLAHOLAOHLAasdsdasdsadasdas", self.__equipo_ingresado)
                    self.__dado_apretado = True
                    self.__genero_equipo.nuevo_equipo()
                    self.__equipo.set_cartas(self.__genero_equipo._jugadores)
                    self._view.renderizar(self.__genero_equipo._jugadores)
                elif botones["comienza"].checkForInput(mouse_pos):
                    if (
                        self.__dado_apretado
                        and self.__equipo_ingresado
                        and self.__usuario_ingresado
                    ):
                        abmusuario = AbmUsuario()
                        nombre_usuario = self.__nombre_usuario.get_nombre()
                        print(nombre_usuario)
                        self.__usuario = abmusuario.get_por_usuario(nombre_usuario)
                        abmequipo = AbmEquipo()
                        self.__genero_equipo.set_nombre(self.__equipo.get_nombre())
                        self.__equipo.set_id_usuario(self.__usuario.get_id())
                        abmequipo.insertar(self.__equipo)
                        abmequipo.close()
                        self._view.ocultar_visibilidad()
                        self.__cancha.main_loop()
                elif botones["atras"].checkForInput(mouse_pos):  # Boton Back
                    self._view.ocultar_visibilidad()
                    menu_principal = MenuController()
                    menu_principal.main_loop()
                elif botones["cambiar_formacion_atras"].checkForInput(
                    mouse_pos
                ) or botones["cambiar_formacion_adelante"].checkForInput(
                    mouse_pos
                ):  # flechas para cambiar formacion
                    if self.__formacion_actual == "4-4-2":
                        self.__formacion_actual = "4-3-3"
                        self.__genero_equipo.set_formacion(Formacion433())
                    else:
                        self.__formacion_actual = "4-4-2"
                        self.__genero_equipo.set_formacion(Formacion442())
                    self._view.texto_formacion(self.__formacion_actual)
                elif botones["cambiar_estadio_adelante"].checkForInput(mouse_pos):
                    self.__cambiar_estadio("Adelante")
                elif botones["cambiar_estadio_atras"].checkForInput(mouse_pos):
                    self.__cambiar_estadio("Atras")
                elif botones["usuario"].checkForInput(mouse_pos):
                    if not self.__usuario_ingresado:
                        self._view.ocultar_visibilidad()
                        self.__LoginUsuario.main_loop()
                elif botones["equipo"].checkForInput(mouse_pos):
                    if not self.__equipo_ingresado:
                        self._view.ocultar_visibilidad()
                        self.__LoginEquipo.main_loop()
            clock.tick(FPS)
            pygame.display.update()

    def main_loop(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self._view.mostrar()  # Mostrar el menú
            self._view.dibujar_formaciones(
                self._view._pantalla,
                FORMACIONES,
                self.__formacion_actual,
                self.__genero_equipo._jugadores,
                self.__dado_apretado,
            )
            self._view.texto_formacion(self.__formacion_actual)
            eventos = pygame.event.get()  # Manejar eventos
            self.manejar_eventos(eventos, mouse_pos)
            clock.tick(60)
            pygame.display.update()

    def __cambiar_estadio(self, donde):
        estadios = [
            camp_nou,
            monumental,
            bernabeu,
            bombonera,
            azteca,
            malasia,
            old_traford,
        ]
        estadio_actual = self._view.get_estadio()
        indice_actual = estadios.index(estadio_actual)
        if donde == "Adelante":
            nuevo_indice = (indice_actual + 1) % len(estadios)
        else:
            nuevo_indice = (indice_actual - 1) % len(estadios)
        self._view.cambiar_estadio(estadios[nuevo_indice])
        self.__estadio_actual = estadios[nuevo_indice]
        self.__cancha.set_estadio(self.__estadio_actual)

    def set_nombre_usuario(self, nombre):
        self.__nombre_usuario.set_nombre(nombre)

    def set_usuario_ingresado(self):
        self.__usuario_ingresado = True

    def set_equipo_ingresado(self):
        self.__equipo_ingresado = True

    def get_equipo_ingresado(self):
        return self.__equipo_ingresado

    def get_usuario_ingresado(self):
        return self.__usuario_ingresado
