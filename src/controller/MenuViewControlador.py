import sys

import pygame

from .Controlador import Controlador
from settings import *
from view.MenuView import MenuView
from controller.RankingViewControlador import RankingController
from controller.OpcionesViewControlador import OpcionesController
from controller.LoginViewControlador import LoginController
from controller.JugarViewControlador import JugarController

# from .LoginViewControlador import LoginController


class MenuController(Controlador):
    def __init__(self):
        self._view = MenuView(pygame.display.set_mode((ANCHO, ALTO)))
        self.__ranking = RankingController()
        self.__opciones = OpcionesController()
        self.__login = LoginController()
        self.__jugar = JugarController()

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0].checkForInput(mouse_pos):
                    self.__login.main_loop()
                if botones[1].checkForInput(mouse_pos):
                    self.__jugar.main_loop()
                if botones[2].checkForInput(mouse_pos):
                    self.__opciones.main_loop()
                if botones[3].checkForInput(mouse_pos):
                    self.__ranking.main_loop()
                if botones[4].checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
