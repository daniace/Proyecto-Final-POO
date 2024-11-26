import sys

import pygame

from controller.ReproductorMusica import ReproductorMusica
from model.logic.Dificultades import *
from settings import *
from view.OpcionesView import OpcionesView

from .Controlador import Controlador


class OpcionesController(Controlador):
    def __init__(self, dificultad: Dificultad):
        super().__init__()
        self._view = OpcionesView(SCREEN)
        self.__musica = ReproductorMusica()
        self.__dificultad = dificultad

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.MenuViewControlador import MenuController

        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["sonido_on"].checkForInput(mouse_pos):
                    self.__musica.reanudar()
                if botones["sonido_off"].checkForInput(mouse_pos):
                    self.__musica.pausar()
                if botones["atras"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    menu_principal = MenuController(self.__dificultad)
                    menu_principal.main_loop()
                if botones["facil"].checkForInput(mouse_pos):
                    self.__dificultad = Facil()
                    print("instanciado en FACIL")
                if botones["normal"].checkForInput(mouse_pos):
                    self.__dificultad = Medio()
                    print("instanciado en MEDIO")
                if botones["dificil"].checkForInput(mouse_pos):
                    self.__dificultad = Dificil()
                    print("instanciado en Dificil")
        clock.tick(60)
        pygame.display.update()
