import sys
import time

import gif_pygame
import pygame

from controller.ReproductorMusica import ReproductorMusica
from model.logic.Cronometro import Cronometro
from model.logic.Dificultades import *
from model.logic.EquipoLogico import EquipoLogico
from model.logic.Partido import Partido
from settings import *
from settings import dificultad_actual
from view.CanchaView import CanchaView
from view.PantallaCargaView import CargaView

from .Controlador import Controlador
from .GameOverViewControlador import GameOverViewControlador


class CanchaController(Controlador):
    def __init__(self, pantalla, jugador: EquipoLogico):
        super().__init__()
        self.__boton_actual = None
        self._view = CanchaView(pantalla, jugador.get_nombre())
        self.__dificultad = dificultad_actual().get_dificultad()
        self._jugador = jugador
        self._indice_seleccionado = 0
        self.boton_actual = None
        self.boton_mouse = None
        self.boton_texto = None  
        self.espera_intercepcion = False
        self.__pase_seleccionado = False
        self.__cronometro = None
        self.__diccionario_posiciones_jugadores = None
        self.__pantalla_de_carga = CargaView(SCREEN)
        self.__formacion = None
        self.__reproductor = ReproductorMusica()

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.JugarViewControlador import JugarController

        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self._indice_seleccionado = (self._indice_seleccionado - 1) % len(
                        botones
                    )
                    self.actualizar_seleccion()
                elif event.key == pygame.K_UP:
                    self._indice_seleccionado = (self._indice_seleccionado + 1) % len(
                        botones
                    )
                    self.actualizar_seleccion()
                elif event.key == pygame.K_RETURN:
                    self.ejecutar_accion()

    def cambiar_boton_actual(self):
        botones = self._view.get_botones()
        for indice, (boton_texto, boton) in enumerate(botones.items()):
            if boton.hovering:
                self.boton_actual = boton
                self._indice_seleccionado = indice
                self.boton_texto = boton_texto
            elif boton.seleccionado:
                self.boton_actual = boton
                self._indice_seleccionado = indice
                self.boton_texto = boton_texto

    def main_loop(self):
        self.__reproductor.detener()
        self.__pantalla_de_carga.main_loop()
        self._partido = Partido(self._jugador, self.__dificultad, self._view)
        self.relacionar_posiciones(self._partido.get_diccionario(), self.__formacion)
        if self.__cronometro is None or not self.__cronometro.is_alive():
            self.__cronometro = Cronometro()
        self._view.renderizar_acciones()
        self._view.renderizar()
        self.__cronometro.start()
        self._partido._partido_en_curso = True
        while True:
            if self._view.get_visibilidad():
                self._view.set_goles(self._partido.get_goles())
                if self.__cronometro._evento_partido_terminado.is_set():
                    self._partido_en_curso = False
                    self._partido.mostrar_resultado()
                    self._view.ocultar_visibilidad()
                    game_over = GameOverViewControlador()
                    game_over.set_goles(self._partido.get_goles())
                    game_over.set_puntos_ganado(self._partido.mostrar_resultado())
                    game_over.main_loop()
                self.mostrar_pelota()  
                mouse_pos = None
                self._view.mostrar(self.__cronometro.get_contador())  
                eventos = pygame.event.get()  
                self._view.cambiar_equipo(self._partido.get_equipo_con_posesion())
                if self._view.get_gif_terminado or self.__pase_seleccionado:
                    if (
                        self._partido.get_equipo_con_posesion() == 1
                        or self.espera_intercepcion == True
                    ):
                        self.manejar_eventos(eventos, mouse_pos)
                        self.cambiar_boton_actual()
                    elif (
                        self._partido.get_equipo_con_posesion() == 2
                        and self.espera_intercepcion != True
                    ):
                        self._view.ultima_jugada(2)
                        self.espera_intercepcion = self._partido._jugar_turno_cpu()
                        accion_cpu = self._partido.get_accion_cpu()
                        self._view.set_accion_cpu(accion_cpu)
                        self.manejar_eventos(eventos, mouse_pos)
                        self.cambiar_boton_actual()

                    if self.boton_actual is not None:  
                        self.boton_actual.mantener_color()
                        self.boton_actual.update(self._view._pantalla)

                clock.tick(60)
                pygame.display.update()
        self.__cronometro.join()

    def actualizar_seleccion(self):
        botones = self._view.get_botones()
        for indice, (boton) in enumerate(botones.values()):
            if indice == self._indice_seleccionado:
                boton.seleccionar()
                self.cambiar_boton_actual()
            else:
                boton.deseleccionar()

    def ejecutar_accion(self):
        botones = self._view.get_botones()
        nombre_boton_seleccionado = list(botones.keys())[self._indice_seleccionado]
        if (
            not self.__pase_seleccionado
            and not self.espera_intercepcion
            and self._partido.get_equipo_con_posesion() == 1
        ):
            if nombre_boton_seleccionado == "pase":
                self._view.ultima_jugada(1)
                cantidad_pases = len(self._partido.mostrar_pases())
                self.mostrar_aliados()
                self._view.set_pase_seleccionado(cantidad_pases)
                pases_disponibles = self._partido.mostrar_pases()
                jugadores = self._partido.imprimir_jugadores(pases_disponibles)
                self._view.renderizar_carta(jugadores)
                self.__pase_seleccionado = True
            elif nombre_boton_seleccionado == "tiro":
                self._view.ultima_jugada(1)
                self._view.set_accion("tiro_al_arco")
                self._view.mostrar(self.__cronometro.get_contador())
                accion = self._partido.jugar_turno_jugador(2)
                self._view.set_accion(accion)
            elif nombre_boton_seleccionado == "gambeta":
                self._view.ultima_jugada(1)
                accion = self._partido.jugar_turno_jugador(3)
                self._view.set_accion(accion)
        elif self.__pase_seleccionado:
            pases_disponibles = self._partido.mostrar_pases()
            self.boton_actual = None
            self._view.mostrar(self.__cronometro.get_contador())
            if nombre_boton_seleccionado == "pase1":
                self.__pase_seleccionado = False
                accion = self._partido.jugar_turno_jugador(
                    1, aliado_pase=pases_disponibles[0][0]
                )

            elif nombre_boton_seleccionado == "pase2":
                self.__pase_seleccionado = False
                accion = self._partido.jugar_turno_jugador(
                    1, aliado_pase=pases_disponibles[1][0]
                )
            elif nombre_boton_seleccionado == "pase3":
                self.__pase_seleccionado = False
                accion = self._partido.jugar_turno_jugador(
                    1, aliado_pase=pases_disponibles[2][0]
                )
            elif nombre_boton_seleccionado == "pase4":
                self.__pase_seleccionado = False
                accion = self._partido.jugar_turno_jugador(
                    1, aliado_pase=pases_disponibles[3][0]
                )

            self.__pase_seleccionado = False
            self._view.deseleccionar_pase()
            self.cambiar_boton_actual()
            self._view.set_accion(accion)

            self.boton_actual = None

        if self._partido.get_equipo_con_posesion() == 2 and self.espera_intercepcion:
            if nombre_boton_seleccionado == "interceptar":
                self._view.ultima_jugada(1)
                self.espera_intercepcion = False
                accion = self._partido.realizar_intercepcion()
                self._view.set_accion(accion)

    def set_estadio(self, estadio):
        self._view.set_estadio(estadio)
        self._view.setear_estadio_cancha()

    def set_formacion(self, formacion):
        self.__formacion = formacion

    def relacionar_posiciones(self, diccionario_1, formacion_actual):
        formacion_usuario = FORMACION_USUARIO[formacion_actual]
        formacion_cpu = FORMACION_CPU["4-3-3"]

        posiciones = {
            0: ("portero", formacion_usuario),
            1: ("defensas", formacion_usuario),
            2: ("delanteros", formacion_cpu),
            3: ("mediocampistas", formacion_usuario),
            4: ("mediocampistas", formacion_cpu),
            5: ("delanteros", formacion_usuario),
            6: ("defensas", formacion_cpu),
            7: ("portero", formacion_cpu),
        }
        "PONER QUE SE PUEDA CAMBIAR DE FORMACION"

        indices = {i: 0 for i in range(8)}
        diccionario_jugadores = {}

        for coordenada in diccionario_1.keys():
            tipo, formacion = posiciones[coordenada[0]]
            diccionario_jugadores[coordenada] = formacion[tipo][indices[coordenada[0]]]
            indices[coordenada[0]] += 1
        self._view.set_lista_jugadores(diccionario_jugadores)
        self.__diccionario_posiciones_jugadores = diccionario_jugadores

    def mostrar_pelota(self):
        posicion = self.__diccionario_posiciones_jugadores[
            self._partido.get_posicion_pelota()
        ]
        self._view.set_posicion_pelota(posicion)

    def mostrar_aliados(self):
        pases = []
        lista = self._partido.mostrar_pases()
        for aliados in lista:
            pases.append(self.__diccionario_posiciones_jugadores[aliados[0]])
        self._view.set_pases(pases)



