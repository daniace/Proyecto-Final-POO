from .Boton import Boton
import pygame


class VentanaView:
    def __init__(self, pantalla):
        self.__pantalla = pantalla  # La pantalla principal
        self.__botones = []

    def mostrar(self):
        pass

    def get_botones(self):
        return self.__botones

    def mostrar_boton(self, imagen, pos, texto, fuente, color_base, hovering_color):
        mouse_pos = pygame.mouse.get_pos()
        boton = Boton(imagen, pos, texto, fuente, color_base, hovering_color)
        boton.changeColor(mouse_pos)
        boton.update(self.__pantalla)
        return boton
