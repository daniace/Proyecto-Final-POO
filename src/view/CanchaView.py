import gif_pygame
import pygame

from settings import *

from .VentanaView import VentanaView


class CanchaView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def mostrar(self):
        self._botones = {}
        pygame.display.set_caption("GAMEPLAY")
        self._pantalla.fill(NEGRO)
        # self._pantalla.blit(marcador, (int(ANCHO * 0.76), int(ALTO * 0.01)))
        # self._pantalla.blit(marcador, (int(ANCHO * 0.2), int(ALTO * 0.55)))
        self._pantalla.blit(BG_CANCHA_OFICIAL, (int(ANCHO * 0.01), int(ALTO * 0.01)))
        TIEMPO = get_fuente(50).render("TIEMPO", True, BLANCO)
        self._pantalla.blit(TIEMPO, (int(ANCHO * 0.84), int(ALTO * 0.05)))
        ATAJADA_GIF.render(self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05)))
        ATAJADA_GIF.pause()
    

        CANCHA_ATRAS = self._mostrar_boton(
            boton_rojo_cuadrado,
            (ANCHO * 0.035, ALTO * 0.065),
            "🔙",
            pygame.font.Font(EMOJIS, 75),
            BLANCO,
            ROJO,
        )

        PASE = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.65),
            "PASE",
            get_fuente(50),
            BLANCO,
            "Green",
        )

        TIRO = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.75),
            "TIRO",
            get_fuente(50),
            BLANCO,
            "Green",
        )

        GAMBETA = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.85),
            "GAMBETA",
            get_fuente(50),
            BLANCO,
            "Green",
        )

        INTERCEPTAR = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.95),
            "INTERCEPTAR",
            get_fuente(50),
            BLANCO,
            "Green",
        )

        self._botones["interceptar"] = INTERCEPTAR
        self._botones["gambeta"] = GAMBETA
        self._botones["tiro"] = TIRO
        self._botones["pase"] = PASE
        self._botones["atras"] = CANCHA_ATRAS
        
    def mostrar_mensaje(self, mensaje, y):
        fuente = get_fuente(75)
        texto_render = fuente.render(mensaje, True, "White")
        self._pantalla.blit(texto_render, (ANCHO / 2 - texto_render.get_width() / 2, y + 300))
        pygame.display.flip()


    