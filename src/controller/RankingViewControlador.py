import sys

import pygame

from settings import *
from view.RankingView import RankingView
from .ControladorBD import ControladorBD
from .Controlador import Controlador


class RankingController(Controlador):
    def __init__(self):
        super().__init__()
        self._view = RankingView(pygame.display.set_mode((ANCHO, ALTO)))
        self.__bd = ControladorBD().get_usuarios_ranking()

    def manejar_eventos(self, eventos, mouse_pos):
        self._view.mostrar_ranking(self.__bd)
        from controller.MenuViewControlador import MenuController

        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["actualizar"].checkForInput(mouse_pos):
                    self.__bd = ControladorBD().get_usuarios_ranking()
                # usuarios_actualizado = abmusuario.get_all()
                # actualizar_ranking(usuarios_actualizado)
                if botones["atras"].checkForInput(mouse_pos):
                    menu_principal = MenuController()
                    menu_principal.main_loop()
