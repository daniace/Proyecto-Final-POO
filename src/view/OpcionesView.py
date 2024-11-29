import pygame

from settings import *

from .Boton import Boton
from .VentanaView import VentanaView


class OpcionesView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.__dificultad = "medio"
        self.__sonido = "on"

    def mostrar(self):
        if self._visible:
            self._botones = {}
            self._pantalla.blit(BG_OPCIONES, (0, 0))
            pygame.display.set_caption("OPCIONES")

            TEXTO_OPCIONES = get_fuente(100).render("OPCIONES", True, "Black")
            OPCIONES_RECT = TEXTO_OPCIONES.get_rect(center=(ANCHO // 2, 50))
            self._pantalla.blit(TEXTO_OPCIONES, OPCIONES_RECT)

            self._pantalla.blit(boton_negro_grande, (ANCHO * 0.025, ALTO * 0.534))
            TEXTO_CONTROLES = get_fuente(65).render("CONTROLES:", True, "White")
            CONTROLES_RECT = TEXTO_CONTROLES.get_rect(
                center=(int(ANCHO * 0.15), int(ALTO * 0.62))
            )
            self._pantalla.blit(TEXTO_CONTROLES, CONTROLES_RECT)

            self._pantalla.blit(boton_negro_grande, (ANCHO * 0.025, ALTO * 0.22))
            TEXTO_DIFICULTAD = get_fuente(60).render("DIFICULTAD:", True, "White")
            CONTROLES_RECT = TEXTO_DIFICULTAD.get_rect(
                center=(int(ANCHO * 0.15), int(ALTO * 0.3))
            )
            self._pantalla.blit(TEXTO_DIFICULTAD, CONTROLES_RECT)

            self._pantalla.blit(boton_negro_grande, (ANCHO * 0.025, ALTO * 0.37))
            TEXTO_SONIDO = get_fuente(65).render("SONIDO:", True, "White")
            CONTROLES_RECT = TEXTO_SONIDO.get_rect(
                center=(int(ANCHO * 0.15), int(ALTO * 0.45))
            )
            self._pantalla.blit(TEXTO_SONIDO, CONTROLES_RECT)

            control1_img = pygame.image.load("src/assets/images/control1.png")
            control1_img = pygame.transform.scale(control1_img, (200, 100))

            control2_img = pygame.image.load("src/assets/images/control2.png")
            control2_img = pygame.transform.scale(control2_img, (300, 300))

            self._pantalla.blit(control1_img, (int(ANCHO * 0.38), int(ALTO * 0.58)))
            self._pantalla.blit(control2_img, (int(ANCHO * 0.59), int(ALTO * 0.42)))

            FACIL = self._mostrar_boton(
                boton_verde,
                (int(ANCHO * 0.4), int(ALTO * 0.3)),
                "FACIL",
                get_fuente(75),
                VERDE_FUERTE if self.__dificultad == "facil" else "White",
                "Green",
            )
            NORMAL = self._mostrar_boton(
                boton_amarillo,
                (int(ANCHO * 0.6), int(ALTO * 0.3)),
                "NORMAL",
                get_fuente(75),
                AMARILLO_FUERTE if self.__dificultad == "medio" else "White",
                "Yellow",
            )

            DIFICIL = self._mostrar_boton(
                boton_rojo,
                (int(ANCHO * 0.8), int(ALTO * 0.3)),
                "DIFICIL",
                get_fuente(75),
                ROJO_CLARO if self.__dificultad == "dificil" else "White",
                ROJO,
            )

            SONIDO_ON = self._mostrar_boton(
                boton_negro,
                (int(ANCHO * 0.50), int(ALTO * 0.44)),
                "ON",
                get_fuente(75),
                VERDE if self.__sonido == "on" else "White",
                "Green",
            )

            SONIDO_OFF = self._mostrar_boton(
                boton_negro,
                (int(ANCHO * 0.70), int(ALTO * 0.44)),
                "OFF",
                get_fuente(75),
                ROJO if self.__sonido == "off" else "White",
                "Red",
            )

            OPCIONES_ATRAS = self._mostrar_boton(
                boton_rojo_cuadrado,
                (int(ANCHO * 0.95), int(ALTO * 0.9)),
                "🔙",
                pygame.font.Font(EMOJIS, 75),
                "White",
                "Red",
            )

            self._botones["facil"] = FACIL
            self._botones["normal"] = NORMAL
            self._botones["dificil"] = DIFICIL
            self._botones["sonido_on"] = SONIDO_ON
            self._botones["sonido_off"] = SONIDO_OFF
            self._botones["atras"] = OPCIONES_ATRAS

    def set_dificultad(self, dificultad):
        self.__dificultad = dificultad

    def set_sonido(self, sonido):
        self.__sonido = sonido
