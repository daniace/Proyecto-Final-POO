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
        self._partido = Partido(jugador, dificultad, self._view)
        self._indice_seleccionado = 0
        self.boton_actual = None
        self.boton_mouse = None
        self.boton_texto = None  # esto se saca

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.JugarViewControlador import JugarController

        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if botones["pase"].checkForInput(mouse_pos):
            #         self.actualizar_seleccion()
            #         self.ejecutar_accion()
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

        # print(self.boton_texto) #ESTO SE SACA ES PARA VER SI SE CAMBIABA LOS BOTONES

    def main_loop(self):
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
                self.manejar_eventos(eventos, mouse_pos)
                self.cambiar_boton_actual()
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

        if nombre_boton_seleccionado == "atras":
            from controller.JugarViewControlador import JugarController

            menu_jugar = JugarController()
            menu_jugar.main_loop()
        elif nombre_boton_seleccionado == "pase":
            print("hizo pasee")
        elif nombre_boton_seleccionado == "tiro":
            print("hizo tiro")
        elif nombre_boton_seleccionado == "gambeta":
            print("hizo gambeta")
        elif nombre_boton_seleccionado == "interceptar":
            print("hizo interceptar")

    def set_estadio(self, estadio):
        self._view.set_estadio(estadio)
        self._view.setear_estadio_cancha()


"NOTA PARA SEGUIRLO -> EL BOTON ACTUAL ES EL BOTON SELECCIONADO, HAY QUE HACER QUE EL BOTON QUE SELECCIONA EL MOUSE SEA EL BOTON ACTUAL, ADEMAS DE CAMBIAR"
"EL INDICE DEL EJECUTAR ACCION AL BOTON ACTUAL, PARA QUE SE ELIJA ESA OPCION"
"MAÑANA LO SIGO - LEO"
