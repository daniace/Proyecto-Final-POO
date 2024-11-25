import sys

import pygame

from settings import *
from view.VentanaView import VentanaView  # la Ventana padre

from abc import ABC, abstractmethod


class Controlador(ABC):
    def __init__(self):
        self._view = None
        self.boton_actual = None    

    @abstractmethod
    def manejar_eventos(self, eventos, mouse_pos):
        pass
    
    def cambiar_boton_actual (self):
        botones = self._view.get_botones()
        for boton_texto, boton in botones.items():
                    if boton.seleccionado:
                        self.boton_actual = boton
    

    def main_loop(self):
        while True:
            if self._view.get_visibilidad():
                mouse_pos = pygame.mouse.get_pos()
                self._view.mostrar()  # Mostrar el menú
                eventos = pygame.event.get()  # Manejar eventos
                self.manejar_eventos(eventos, mouse_pos)

                if self.boton_actual is not None:
                        self.boton_actual.changeColor()
                        self.boton_actual.update(self._view._pantalla)
                        
                clock.tick(60)
                pygame.display.update()
