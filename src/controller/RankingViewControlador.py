import sys

import pygame

from .Controlador import Controlador
from settings import *
from view.RankingView import RankingView


class RankingController(Controlador):
    def __init__(self):
        super().__init__()
        self._view = RankingView(pygame.display.set_mode((ANCHO, ALTO)))

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.MenuViewControlador import MenuController

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
                    menu_principal = MenuController()
                    menu_principal.main_loop()
