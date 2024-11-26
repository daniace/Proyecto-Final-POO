import sys
import pygame
import gif_pygame
from settings import *
from view.CanchaView import CanchaView
from model.logic.Partido import Partido
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

    def iniciar_partido(self):
        self._partido.jugar_partido()

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
        # self._view.renderizar_acciones()
        # self._view.renderizar()
        ATAJADA_GIF = gif_pygame.load(ATAJADA, loops=-1)
        while True:
            if self._view.get_visibilidad():
                ATAJADA_GIF.render(
                    self._view._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
                )
                mouse_pos = pygame.mouse.get_pos()
                self._view.mostrar()  # Mostrar el menú
                eventos = pygame.event.get()  # Manejar eventos
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
                    self.espera_intercepcion = self._partido.jugar_turno_cpu()
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
        if not self.__pase_seleccionado:
            if nombre_boton_seleccionado == "pase":
                self._view.set_pase_seleccionado()
                print("hizo pasee")
                self.__pase_seleccionado = True
            elif nombre_boton_seleccionado == "tiro":
                self._partido.jugar_turno_jugador(2)
                print("hizo tiro")
            elif nombre_boton_seleccionado == "gambeta":
                self._partido.jugar_turno_jugador(3)
                print("hizo gambeta")
            elif nombre_boton_seleccionado == "interceptar":
                self.espera_intercepcion = False
                self._partido.realizar_intercepcion()
        else:
            pases_disponibles = self._partido.mostrar_pases()
            # jugadores = self._partido.imprimir_jugadores(pases_disponibles)
            if nombre_boton_seleccionado == "pase1":
                self._partido.jugar_turno_jugador(1, pases_disponibles[0][0])
            elif nombre_boton_seleccionado == "pase2":
                self._partido.jugar_turno_jugador(1, pases_disponibles[1][0])
            elif nombre_boton_seleccionado == "pase3":
                self._partido.jugar_turno_jugador(1, pases_disponibles[2][0])
            elif nombre_boton_seleccionado == "pase4":
                self._partido.jugar_turno_jugador(1, pases_disponibles[3][0])
            self.__pase_seleccionado = False

    def set_estadio(self, estadio):
        self._view.set_estadio(estadio)
        self._view.setear_estadio_cancha()

    def turnos_partido(self):
        pass


"NOTA PARA SEGUIRLO -> EL BOTON ACTUAL ES EL BOTON SELECCIONADO, HAY QUE HACER QUE EL BOTON QUE SELECCIONA EL MOUSE SEA EL BOTON ACTUAL, ADEMAS DE CAMBIAR"
"EL INDICE DEL EJECUTAR ACCION AL BOTON ACTUAL, PARA QUE SE ELIJA ESA OPCION"
"MAÑANA LO SIGO - LEO"
