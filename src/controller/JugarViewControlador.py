import sys

import pygame

from settings import *
from view.JugarView import JugarView
from model.logic.EquipoLogico import EquipoLogico
from .CanchaViewControlador import CanchaController
from .Controlador import Controlador


class JugarController(Controlador):
    def __init__(self):
        super().__init__()
        self._view = JugarView(pygame.display.set_mode((ANCHO, ALTO)))
        self.__cancha = CanchaController(pygame.display.set_mode((ANCHO, ALTO)))
        self.__formacion_actual = FORMACION_PREDETERMINADA
        self.__comienza_partida = False
        self.__genero_equipo = EquipoLogico("Equipo 1", 1)

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        from controller.MenuViewControlador import MenuController

        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["dado"].checkForInput(mouse_pos):  # Boton del Dado
                    self.__genero_equipo.nuevo_equipo()
                    self._view.renderizar_estadisticas(self.__genero_equipo._jugadores)
                    self.__comienza_partida = True
                elif botones["comienza"].checkForInput(
                    mouse_pos
                ):  # Boton Comenzar Partia
                    if self.__comienza_partida:
                        self.__cancha.main_loop()
                elif botones["atras"].checkForInput(mouse_pos):  # Boton Back
                    menu_principal = MenuController()
                    menu_principal.main_loop()
                elif botones["cambiar_formacion_atras"].checkForInput(
                    mouse_pos
                ) or botones["cambiar_formacion_adelante"].checkForInput(
                    mouse_pos
                ):  # flechas para cambiar formacion
                    if self.__formacion_actual == "4-4-2":
                        self.__formacion_actual = "4-3-3"
                    else:
                        self.__formacion_actual = "4-4-2"
                    self._view.texto_formacion(self.__formacion_actual)
                elif botones["cambiar_estadio_adelante"].checkForInput(mouse_pos):
                    self.__cambiar_estadio("Adelante")
                elif botones["cambiar_estadio_atras"].checkForInput(mouse_pos):
                    self.__cambiar_estadio("Atras")

        clock.tick(FPS)
        pygame.display.update()

    def main_loop(self):
        self._view.renderizar_estadisticas(self.__genero_equipo._jugadores)
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self._view.mostrar()  # Mostrar el menú
            self._view.dibujar_formaciones(
                self._view._pantalla,
                FORMACIONES,
                self.__formacion_actual,
                self.__genero_equipo._jugadores,
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
