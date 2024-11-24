import pygame
import sys
from settings import *
from view.LoginJugarView import LoginEquipoView
from .Controlador import Controlador


class LoginJugarViewControlador(Controlador):
    def __init__(self, pantalla):
        self._view = LoginEquipoView(pantalla)
        self.__texto_usuario = ""

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.JugarViewControlador import JugarController

        boton = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.__texto_usuario = self.__texto_usuario[:-1]
                else:
                    self.__texto_usuario += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton["volver_atras"].checkForInput(mouse_pos):
                    jugar = JugarController()
                    self._view.ocultar_visibilidad()
                    jugar.main_loop()
        self._view.mostrar_texto_usuario(self.__texto_usuario)

    def main_loop(self):
        self._view.renderizar()
        super().main_loop()
