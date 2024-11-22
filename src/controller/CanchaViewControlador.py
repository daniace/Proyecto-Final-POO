import sys

import pygame

from .Controlador import Controlador
from settings import *
from view.CanchaView import CanchaView


class CanchaController(Controlador):
    def __init__(self, pantalla):
        super().__init__()
        self._view = CanchaView(pantalla)

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.JugarViewControlador import JugarController

        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0].checkForInput(mouse_pos):
                    menu_jugar = JugarController()
                    menu_jugar.main_loop()
