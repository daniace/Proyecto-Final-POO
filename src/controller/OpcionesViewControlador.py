import sys

import pygame

from controller.ReproductorMusica import ReproductorMusica
from settings import *
from view.OpcionesView import OpcionesView

from .Controlador import Controlador


class OpcionesController(Controlador):
    def __init__(self):
        super().__init__()
        self._view = OpcionesView(pygame.display.set_mode((ANCHO, ALTO)))
        self.__musica = ReproductorMusica()

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.MenuViewControlador import MenuController

        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["sonido_on"].checkForInput(mouse_pos):
                    self.__musica.reanudar_soundtrack()
                if botones["sonido_off"].checkForInput(mouse_pos):
                    self.__musica.pausar_soundtrack()
                if botones["atras"].checkForInput(mouse_pos):
                    menu_principal = MenuController()
                    menu_principal.main_loop()
                if botones["facil"].checkForInput(mouse_pos):
                    pass
                    # dificultadd.dificil()
                if botones["normal"].checkForInput(mouse_pos):
                    pass
                    # dificultadd.facil()
                if botones["dificil"].checkForInput(mouse_pos):
                    pass
        clock.tick(60)
        pygame.display.update()
