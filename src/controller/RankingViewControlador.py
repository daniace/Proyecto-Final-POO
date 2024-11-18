import sys

import pygame

from settings import *
from view.RankingView import RankingView


class RankingController:
    def __init__(self):
        self.__vista = RankingView(pygame.display.set_mode((ANCHO, ALTO)))

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self.__vista.get_botones()
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

    def main_loop(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            # Mostrar el menú
            self.__vista.mostrar_ranking()

            # Manejar eventos
            eventos = pygame.event.get()
            self.manejar_eventos(eventos, mouse_pos)

            clock.tick(60)
            pygame.display.update()
