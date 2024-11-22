import pygame

from settings import *

from .VentanaView import VentanaView


class CanchaView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def mostrar(self):
        self._botones = {}
        self._pantalla.fill(NEGRO)
        self._pantalla.blit(BG_CANCHA_OFICIAL, (0, 0))
        CANCHA_ATRAS = self._mostrar_boton(
            boton_rojo_cuadrado,
            (ANCHO * 0.035, ALTO * 0.065),
            "🔙",
            pygame.font.Font(EMOJIS, 75),
            BLANCO,
            ROJO,
        )
        self._botones["atras"] = CANCHA_ATRAS
