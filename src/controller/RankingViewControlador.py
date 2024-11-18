import sys

import pygame

from .Controlador import Controlador
from settings import *
from view.RankingView import RankingView
from .MenuViewControlador import MenuController


class RankingController(Controlador):
    def __init__(self):
        self._view = RankingView(pygame.display.set_mode((ANCHO, ALTO)))
        self._menu = MenuController()

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0].checkForInput(mouse_pos):
                    pass
                # usuarios_actualizado = abmusuario.get_all()
                # actualizar_ranking(usuarios_actualizado)
                if botones[1].checkForInput(mouse_pos):
                    self._menu.main_loop()  # menú principal
