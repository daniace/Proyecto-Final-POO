import sys

import pygame

from .Controlador import Controlador
from settings import *
from view.OpcionesView import OpcionesView


class OpcionesController(Controlador):
    def __init__(self):
        self._view = OpcionesView(pygame.display.set_mode((ANCHO, ALTO)))

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0].checkForInput(mouse_pos):
                    pygame.mixer.music.set_volume(0.5)
                if botones[1].checkForInput(mouse_pos):
                    pygame.mixer.music.set_volume(0)
                if botones[2].checkForInput(mouse_pos):
                    menu_principal()
                if botones[3].checkForInput(mouse_pos):
                    pass
                    # dificultadd.dificil()
                if botones[4].checkForInput(mouse_pos):
                    pass
                    # dificultadd.facil()
        clock.tick(60)
        pygame.display.update()
