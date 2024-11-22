import pygame

from settings import *

from .Boton import Boton
from .VentanaView import VentanaView


class RankingView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def mostrar(self):
        self._botones = {}
        self._pantalla.blit(BG, (0, 0))
        self._pantalla.fill("black")
        # RANKING_POS_MOUSE = pygame.mouse.get_pos()

        IMAGEN_RANKING_USUARIOS = pygame.image.load(IMAGEN_TABLA)
        IMAGEN_RANKING_USUARIOS = pygame.transform.scale(
            IMAGEN_RANKING_USUARIOS, (ANCHO // 3, ALTO - 100)
        )
        self._pantalla.blit(
            IMAGEN_RANKING_USUARIOS, (int(ANCHO * 0.35), int(ALTO * 0.1))
        )

        RANKING_ACTUALIZAR = self._mostrar_boton(
            boton_cuadrado,
            (ANCHO * 0.73, ALTO * 0.9),
            "🔄",
            pygame.font.FontType(EMOJIS, 50),
            BLANCO,
            VERDE,
        )
        RANKING_ATRAS = self._mostrar_boton(
            boton_rojo,
            (ANCHO * 0.88, ALTO * 0.9),
            "ATRAS",
            get_fuente(75),
            BLANCO,
            ROJO,
        )

        self._botones["atras"] = RANKING_ATRAS
        self._botones["actualizar"] = RANKING_ACTUALIZAR
