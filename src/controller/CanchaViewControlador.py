import sys

import pygame

from settings import *
from view.CanchaView import CanchaView
from model.logic.Partido import Partido
from model.logic.Dificultades import *
from model.logic.EquipoLogico import EquipoLogico
from .Controlador import Controlador


class CanchaController(Controlador):
    def __init__(self, pantalla,dificultad:Dificultad,jugador:EquipoLogico):
        super().__init__()
        self._view = CanchaView(pantalla)
        self._dificultad=dificultad
        self._jugador=jugador
        self._partido=Partido(jugador,dificultad)

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.JugarViewControlador import JugarController

        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["atras"].checkForInput(mouse_pos):
                    menu_jugar = JugarController(self._dificultad)
                    menu_jugar.main_loop()
