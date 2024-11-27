import sys

import pygame

from controller.Controlador import Controlador
from settings import SCREEN
from view.GameOverView import GameOverView


class GameOverViewControlador(Controlador):
    def __init__(self):
        super().__init__()
        self._view = GameOverView(SCREEN)
        self.__puntos_ganado = None
        self.__goles = None

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.JugarViewControlador import JugarController
        from controller.MenuViewControlador import MenuController

        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._view.get_botones()["salir"].checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if self._view.get_botones()["jugar_de_nuevo"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    self.__jugar = JugarController()
                    self.__jugar.main_loop()
                if self._view.get_botones()["menu_principal"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    menu_principal = MenuController()
                    menu_principal.main_loop()
                    
    def main_loop(self):
        self._view.set_resultado(self.__puntos_ganado, self.__goles)
        return super().main_loop()
    
    def set_puntos_ganado(self, puntos_ganado):
        self.__puntos_ganado = puntos_ganado
    
    def set_goles(self, goles):
        self.__goles = goles
