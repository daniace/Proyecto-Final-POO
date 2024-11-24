import sys

import pygame
from model.logic.Dificultades import *
from controller.JugarViewControlador import JugarController
from controller.LoginViewControlador import LoginController
from controller.OpcionesViewControlador import OpcionesController
from controller.RankingViewControlador import RankingController
from settings import *
from view.MenuView import MenuView

from .Controlador import Controlador

# from .LoginViewControlador import LoginController


class MenuController(Controlador):
    def __init__(self, dificultad=Medio):
        super().__init__()
        self._view = MenuView(SCREEN)
        self._dificultad = dificultad  # dificultad predeterminada#
        self.__ranking = RankingController()
        self.__opciones = OpcionesController(self._dificultad)
        self.__login = LoginController()
        self.__jugar = JugarController()

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["login"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    self.__login.main_loop()
                if botones["jugar"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    self.__jugar.main_loop()
                if botones["opciones"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    self.__opciones.main_loop()
                if botones["ranking"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    self.__ranking.main_loop()
                if botones["salir"].checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
