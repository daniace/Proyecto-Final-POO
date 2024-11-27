import pygame
from view.PantallaCargaView import CargaView
from Controlador import Controlador
from settings import *


class PantallaCargaController(Controlador):
    def __init__(self):
        self._view = CargaView(SCREEN)

    def manejador_eventos(self, eventos, mouse_pos):
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
