from abc import ABC, abstractmethod

import pygame

from .Boton import Boton


class VentanaView(ABC):
    def __init__(self, pantalla):
        self._pantalla = pantalla  # La pantalla principal
        self._botones = {}
        self._visible = True

    @abstractmethod
    def mostrar(self):
        pass

    def get_botones(self):
        return self._botones

    def _mostrar_boton(
        self, imagen, pos, texto, fuente, color_base, hovering_color, solo_flechas=False
    ):
        boton = Boton(imagen, pos, texto, fuente, color_base, hovering_color)
        if not solo_flechas:
            mouse_pos = pygame.mouse.get_pos()
            boton.changeColor(mouse_pos)
        boton.update(self._pantalla)
        return boton

    def mostrar_visibilidad(self):
        self._visible = True

    def ocultar_visibilidad(self):
        self._visible = False

    def get_visibilidad(self):
        return self._visible

    def renderizar(self):
        pass
