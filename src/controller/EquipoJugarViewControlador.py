import pygame
import sys
from settings import *
from .Controlador import Controlador
from view.EquipoJugarView import EquipoJugarView


class EquipoJugarViewControlador(Controlador):
    def __init__(self, pantalla, equipo, jugar):
        self.__jugar = jugar
        self._view = EquipoJugarView(pantalla)
        self.__texto_equipo = ""
        self.__Equipo = equipo
        self.__equipo_ingresado = False
        self.__ingresado = False

    def manejar_eventos(self, eventos, mouse_pos):
        boton = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not self.__ingresado:
                    self.__equipo_ingresado = True
                    if event.key == pygame.K_BACKSPACE:
                        self.__texto_equipo = self.__texto_equipo[:-1]
                    else:
                        self.__texto_equipo += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton["volver_atras"].checkForInput(mouse_pos):
                    if self.__ingresado:
                        self.__jugar.get_equipo_ingresado()
                        self._view.ocultar_visibilidad()
                        self.__jugar.main_loop()
                    else:
                        self._view.set_no_ingresado(True)
                if boton["aceptar"].checkForInput(mouse_pos):
                    if len(self.__texto_equipo) < 10:
                        if self.__equipo_ingresado:
                            self.__jugar.set_equipo_ingresado()
                            self.__Equipo.set_nombre(self.__texto_equipo)
                            self.__jugar.set_equipo_cancha(self.__texto_equipo)
                            self.__texto_equipo = ""
                            self._view.set_no_ingresado(False)
                            self._view.set_ingresado(True)
                            self.__ingresado = True
                    else:
                        self._view.set_texto_excedido(True)
        self._view.mostrar_texto_equipo(self.__texto_equipo)

    def main_loop(self):
        self._view.renderizar()
        super().main_loop()
