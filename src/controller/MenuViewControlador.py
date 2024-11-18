import sys

import pygame

from .Controlador import Controlador
from settings import *
from view.MenuView import MenuView
from .RankingViewControlador import RankingController
from .OpcionesViewControlador import OpcionesController

# from .LoginViewControlador import LoginController


class MenuController(Controlador):
    def __init__(self):
        self._view = MenuView(pygame.display.set_mode((ANCHO, ALTO)))
        self.__ranking = RankingController()
        self.__opciones = OpcionesController()

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0].checkForInput(mouse_pos):
                    pass
                if botones[1].checkForInput(mouse_pos):
                    pass
                if botones[2].checkForInput(mouse_pos):
                    self.__opciones.main_loop()
                if botones[3].checkForInput(mouse_pos):
                    self.__ranking.main_loop()
                if botones[4].checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
