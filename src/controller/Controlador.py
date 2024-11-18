import pygame
from view.VentanaView import VentanaView
from abc import ABC, abstractmethod


class Controlador(ABC):

    @abstractmethod
    def manejar_eventos(self, eventos, mouse_pos):
        pass

    @abstractmethod
    def main_loop(self):
        pass
