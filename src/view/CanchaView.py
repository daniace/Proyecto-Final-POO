import gif_pygame
import pygame

from settings import *

from .VentanaView import VentanaView


class CanchaView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.__renderizaciones = {}
        self.__estadio = camp_nou
        self.__estadio_cancha = barcelona

    def mostrar(self):
        self._botones = {}
        pygame.display.set_caption("GAMEPLAY")
        self._pantalla.fill(NEGRO)
        # self._pantalla.blit(marcador, (int(ANCHO * 0.76), int(ALTO * 0.01)))
        # self._pantalla.blit(marcador, (int(ANCHO * 0.2), int(ALTO * 0.55)))
        estadio = self.__estadio_cancha
        self._pantalla.blit(estadio, (int(ANCHO * 0.01), int(ALTO * 0.01)))
        TIEMPO = get_fuente(50).render("TIEMPO", True, BLANCO)
        self._pantalla.blit(TIEMPO, (int(ANCHO * 0.84), int(ALTO * 0.05)))
        # ATAJADA_GIF = gif_pygame.load(ATAJADA)
        # gif_superficie = gif_pygame.GIFPygame(ATAJADA_GIF)
        # self._pantalla.blit(
        #     gif_superficie.blit_ready(), (int(ANCHO * 0.25), int(ALTO * 0.05))
        # )
        # # ATAJADA_GIF.render(gif_superficie, (int(ANCHO * 0.25), int(ALTO * 0.05)))
        # if self.__pase:
        #     PASE_GIF = gif_pygame.load(PASE)
        #     PASE_GIF.render(self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05)))

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

    def mostrar_mensaje(self, mensaje, y):
        fuente = get_fuente(75)
        texto_render = fuente.render(mensaje, True, "White")
        self._pantalla.blit(
            texto_render, (ANCHO / 2 - texto_render.get_width() / 2, y + 300)
        )
        pygame.display.flip()

    def set_estadio(self, estadio):
        self.__estadio = estadio

    def setear_estadio_cancha(self):
        if self.__estadio == camp_nou:
            self.__estadio_cancha = barcelona
        elif self.__estadio == bernabeu:
            self.__estadio_cancha = madrid
        elif self.__estadio == old_traford:
            self.__estadio_cancha = manchester
        elif self.__estadio == monumental:
            self.__estadio_cancha = nuñez
        elif self.__estadio == bombonera:
            self.__estadio_cancha = boca
        elif self.__estadio == azteca:
            self.__estadio_cancha = mexico
        elif self.__estadio == malasia:
            self.__estadio_cancha = malasya

    def renderizar(self):
        PASE_GIF = gif_pygame.load(PASE)
        PASE2_GIF = gif_pygame.load(PASE2)

        TIRO_GIF = gif_pygame.load(TIRO)
        TIRO_LEJANO_GIF = gif_pygame.load(TIRO_LEJANO)

        GAMBETA_GIF = gif_pygame.load(GAMBETA)
        GAMBETA2_GIF = gif_pygame.load(GAMBETA2)
        GAMBETA3_GIF = gif_pygame.load(GAMBETA3)
        GAMBETA4_GIF = gif_pygame.load(GAMBETA4)

        INTERCEPCION_PASE_GIF = gif_pygame.load(INTERCEPCION_PASE)
        INTERCEPCION_PASE2_GIF = gif_pygame.load(INTERCEPCION_PASE2)
        INTERCEPCION_PASE3_GIF = gif_pygame.load(INTERCEPCION_PASE3)

        ATAJADA_GIF = gif_pygame.load(ATAJADA)
        ATAJADA2_GIF = gif_pygame.load(ATAJADA2)

        gifs = {
            "pase": PASE_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "pase2": PASE2_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "tiro": TIRO_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "tiro_lejano": TIRO_LEJANO_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "gambeta": GAMBETA_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "gambeta2": GAMBETA2_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "gambeta3": GAMBETA3_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "gambeta4": GAMBETA4_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "intercepcion_pase": INTERCEPCION_PASE_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "intercepcion_pase2": INTERCEPCION_PASE2_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "intercepcion_pase3": INTERCEPCION_PASE3_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "atajada": ATAJADA_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
            "atajada2": ATAJADA2_GIF.render(
                self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
            ),
        }
        self.__renderizaciones = gifs
