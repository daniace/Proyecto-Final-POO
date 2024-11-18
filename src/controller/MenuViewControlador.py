import sys

import pygame

from settings import *
from view.MenuView import MenuView


class MenuController:
    def __init__(self):
        self.__vista = MenuView(pygame.display.set_mode((ANCHO, ALTO)))

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self.__vista.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0].checkForInput(mouse_pos):
                    self.__vista.login()
                if botones[1].checkForInput(mouse_pos):
                    self.__vista.jugar()
                if botones[2].checkForInput(mouse_pos):
                    self.__vista.opciones()
                if botones[3].checkForInput(mouse_pos):
                    self.__vista.ranking()
                if botones[4].checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

    def main_loop(
        self,
    ):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            # Mostrar el menú
            self.__vista.mostrar_menu(mouse_pos)

            # Manejar eventos
            eventos = pygame.event.get()
            self.manejar_eventos(eventos, mouse_pos)

            clock.tick(60)
            pygame.display.update()
