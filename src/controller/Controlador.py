import sys

import pygame

from settings import *
from view.VentanaView import VentanaView  # la Ventana padre

from abc import ABC, abstractmethod


class Controlador(ABC):
    def __init__(self):
        self._view = None

    @abstractmethod
    def manejar_eventos(self, eventos, mouse_pos):
        pass

    def main_loop(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self._view.mostrar()  # Mostrar el menú
            eventos = pygame.event.get()  # Manejar eventos
            self.manejar_eventos(eventos, mouse_pos)
            clock.tick(60)
            pygame.display.update()
