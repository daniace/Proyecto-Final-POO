import sys
import time

import gif_pygame
import pygame

from model.logic.Cronometro import Cronometro
from model.logic.Dificultades import *
from model.logic.EquipoLogico import EquipoLogico

from .Controlador import Controlador


class CanchaController(Controlador):
    def __init__(self, pantalla, dificultad: Dificultad, jugador: EquipoLogico):
        super().__init__()
        self.__boton_actual = None
        self._view = CanchaView(pantalla)
        self._dificultad = dificultad
        self._jugador = jugador
        self._partido = Partido(jugador, dificultad, self)
        self._indice_seleccionado = 0
        self.boton_actual = None
        self.boton_mouse = None
        self.boton_texto = None  # esto se saca
        self.espera_intercepcion = False
        self.__pase_seleccionado = False
        self.__cronometro = Cronometro()

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.JugarViewControlador import JugarController

        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._view.ocultar_visibilidad()
                    jugar = JugarController()
                    jugar.main_loop()
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

        # print(self.boton_texto)  # ESTO SE SACA ES PARA VER SI SE CAMBIABA LOS BOTONES

    def main_loop(self):
        self._view.renderizar_acciones()
        # self._view.renderizar()
        ATAJADA_GIF = gif_pygame.load(ATAJADA, loops=-1)
        print("Empieza partido")
        self.__cronometro.start()
        self._partido._partido_en_curso = True
        while True:
            if self._view.get_visibilidad():
                if self.__cronometro._evento_partido_terminado.is_set():
                    self._partido_en_curso = False
                    self._partido.mostrar_resultado()
                    break

                ATAJADA_GIF.render(
                    self._view._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
                )
                mouse_pos = pygame.mouse.get_pos()
                self._view.mostrar()  # Mostrar el menú
                eventos = pygame.event.get()  # Manejar eventos
                self._view.cambiar_equipo(self._partido.get_equipo_con_posesion())
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
                    self.espera_intercepcion = self._partido._jugar_turno_cpu()
                    self.manejar_eventos(eventos, mouse_pos)

                if self.boton_actual is not None:  # and self.boton_mouse == None:
                    self.boton_actual.mantener_color()
                    self.boton_actual.update(self._view._pantalla)

                clock.tick(60)
                pygame.display.update()

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
            print("PRIMER BUCLE")
            if nombre_boton_seleccionado == "pase":
                cantidad_pases = len(self._partido.mostrar_pases())
                self._view.set_pase_seleccionado(cantidad_pases)
                pases_disponibles = self._partido.mostrar_pases()
                jugadores = self._partido.imprimir_jugadores(pases_disponibles)
                self._view.renderizar_carta(jugadores)
                self.__pase_seleccionado = True
            elif nombre_boton_seleccionado == "tiro":
                self._view.set_accion("tiro_al_arco")
                self._view.mostrar()
                time.sleep(1.5)
                accion = self._partido.jugar_turno_jugador(2)
                self._view.set_accion(accion)
            elif nombre_boton_seleccionado == "gambeta":
                accion = self._partido.jugar_turno_jugador(3)
        elif self.__pase_seleccionado:
            pases_disponibles = self._partido.mostrar_pases()
            # jugadores = self._partido.imprimir_jugadores(pases_disponibles)
            if nombre_boton_seleccionado == "pase1":
                # print(pases_disponibles[0][0])
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
            if (
                self._partido.get_equipo_con_posesion() == 2
                and self.espera_intercepcion
            ):
                nombre_boton_seleccionado == "interceptar"
                self.espera_intercepcion = False
                accion = self._partido.realizar_intercepcion()
            self.__pase_seleccionado = False
            self.boton_actual = None
            self._view.deseleccionar_pase()
            self._view.set_accion(accion)

    def set_estadio(self, estadio):
        self._view.set_estadio(estadio)
        self._view.setear_estadio_cancha()


"NOTA PARA SEGUIRLO -> EL BOTON ACTUAL ES EL BOTON SELECCIONADO, HAY QUE HACER QUE EL BOTON QUE SELECCIONA EL MOUSE SEA EL BOTON ACTUAL, ADEMAS DE CAMBIAR"
"EL INDICE DEL EJECUTAR ACCION AL BOTON ACTUAL, PARA QUE SE ELIJA ESA OPCION"
"MAÑANA LO SIGO - LEO"
