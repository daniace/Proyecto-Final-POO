from abc import ABC, abstractmethod
from .Boton import Boton
import pygame


class VentanaView(ABC):
    def __init__(self, pantalla):
        self._pantalla = pantalla  # La pantalla principal
        self._botones = []

    @abstractmethod
    def mostrar(self):
        pass

    def get_botones(self):
        return self._botones

    def mostrar_boton(self, imagen, pos, texto, fuente, color_base, hovering_color):
        mouse_pos = pygame.mouse.get_pos()
        boton = Boton(imagen, pos, texto, fuente, color_base, hovering_color)
        boton.changeColor(mouse_pos)
        boton.update(self._pantalla)
        return boton
