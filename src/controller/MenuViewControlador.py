import sys

import pygame

from settings import *
from view.MenuView import MenuView
from .RankingViewControlador import RankingController


class MenuController:
    def __init__(self):
        self.__menu = MenuView(pygame.display.set_mode((ANCHO, ALTO)))
        self.__ranking = RankingController()

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self.__menu.get_botones()
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
                    self.__menu.opciones()
                if botones[3].checkForInput(mouse_pos):
                    self.__ranking.main_loop()
                if botones[4].checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

    def main_loop(self, booleano=True):
        while booleano:
            mouse_pos = pygame.mouse.get_pos()

            # Mostrar el menú
            self.__menu.mostrar_menu()

            # Manejar eventos
            eventos = pygame.event.get()
            self.manejar_eventos(eventos, mouse_pos)

            clock.tick(60)
            pygame.display.update()
