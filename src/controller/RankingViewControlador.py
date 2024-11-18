import sys

import pygame

from .Controlador import Controlador
from settings import *
from view.RankingView import RankingView


class RankingController(Controlador):
    def __init__(self):
        super().__init__()

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0].checkForInput(RANKING_POS_MOUSE):
                    pass
                    # usuarios_actualizado = abmusuario.get_all()
                    # actualizar_ranking(usuarios_actualizado)
                if botones[1].checkForInput(RANKING_POS_MOUSE):
                    pass
                    # menu_principal()
