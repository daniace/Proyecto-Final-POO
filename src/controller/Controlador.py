import sys

import pygame

from settings import *
from view.VentanaView import VentanaView  # la Ventana padre

from abc import ABC, abstractmethod


class Controlador(ABC):
    def __init__(self):
        self._view = VentanaView(pygame.display.set_mode((ANCHO, ALTO)))

    @abstractmethod
    def manejar_eventos(self, eventos, mouse_pos):
        botones = self.__vista.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                pass

    def main_loop(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            # Mostrar el menú
            self._view.mostrar_menu()

            # Manejar eventos
            eventos = pygame.event.get()
            self.manejar_eventos(eventos, mouse_pos)

            clock.tick(60)
            pygame.display.update()
