import sys

import pygame

from controller.ReproductorMusica import ReproductorMusica
from model.logic.Dificultades import Facil, Medio, Dificil
from settings import dificultad_actual
from view.OpcionesView import OpcionesView
from settings import *
from .Controlador import Controlador


class OpcionesController(Controlador):
    def __init__(self):
        super().__init__()
        self.__dificultad = dificultad_actual()
        self._view = OpcionesView(SCREEN)
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
                    self.__musica.reanudar()
                    self._view.set_sonido("on")
                    sonido.set_sonido("on")
                if botones["sonido_off"].checkForInput(mouse_pos):
                    self.__musica.pausar()
                    self._view.set_sonido("off")
                    sonido.set_sonido("off")
                if botones["atras"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    menu_principal = MenuController()
                    menu_principal.main_loop()
                if botones["facil"].checkForInput(mouse_pos):
                    self.__dificultad.set_dificultad(Facil())
                    dificultad.set_dificultad(Facil())
                    dificultad.set_dificultad_string("facil")
                    self._view.set_dificultad("facil")
                if botones["normal"].checkForInput(mouse_pos):
                    self.__dificultad.set_dificultad(Medio())
                    dificultad.set_dificultad(Medio())
                    dificultad.set_dificultad_string("medio")
                    self._view.set_dificultad("medio")
                if botones["dificil"].checkForInput(mouse_pos):
                    self.__dificultad.set_dificultad(Dificil())
                    dificultad.set_dificultad(Dificil())
                    dificultad.set_dificultad_string("dificil")
                    self._view.set_dificultad("dificil")
        clock.tick(60)
        pygame.display.update()
