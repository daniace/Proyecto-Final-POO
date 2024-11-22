import pygame

from settings import *

from .Boton import Boton
from .VentanaView import VentanaView


class OpcionesView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def mostrar(self):
        self._botones = {}
        self._pantalla.blit(BG_OPCIONES, (0, 0))

        TEXTO_OPCIONES = get_fuente(100).render("OPCIONES", True, "Black")
        OPCIONES_RECT = TEXTO_OPCIONES.get_rect(center=(ANCHO // 2, 50))
        self._pantalla.blit(TEXTO_OPCIONES, OPCIONES_RECT)

        COLOR_FONDO = (40, 40, 40)
        TEXTO_CONTROLES = get_fuente(75).render("CONTROLES:", True, "White")
        CONTROLES_RECT = TEXTO_CONTROLES.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.62))
        )
        margen = 10
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(self._pantalla, COLOR_FONDO, fondo_rect, border_radius=15)
        self._pantalla.blit(TEXTO_CONTROLES, CONTROLES_RECT)

        COLOR_FONDO = (40, 40, 40)
        TEXTO_DIFICULTAD = get_fuente(75).render("DIFICULTAD:", True, "White")
        CONTROLES_RECT = TEXTO_DIFICULTAD.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.3))
        )
        margen = 10
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(self._pantalla, COLOR_FONDO, fondo_rect, border_radius=15)
        self._pantalla.blit(TEXTO_DIFICULTAD, CONTROLES_RECT)

        COLOR_FONDO = (40, 40, 40)
        TEXTO_SONIDO = get_fuente(75).render("SONIDO:", True, "White")
        CONTROLES_RECT = TEXTO_SONIDO.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.45))
        )
        margen = 10
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(self._pantalla, COLOR_FONDO, fondo_rect, border_radius=15)
        self._pantalla.blit(TEXTO_SONIDO, CONTROLES_RECT)

        control1_img = pygame.image.load("src/assets/images/control1.png")
        control1_img = pygame.transform.scale(control1_img, (300, 300))

        control2_img = pygame.image.load("src/assets/images/control2.png")
        control2_img = pygame.transform.scale(control2_img, (300, 300))

        self._pantalla.blit(control1_img, (int(ANCHO * 0.38), int(ALTO * 0.42)))
        self._pantalla.blit(control2_img, (int(ANCHO * 0.59), int(ALTO * 0.42)))

        FACIL = self._mostrar_boton(
            boton_verde,
            (int(ANCHO * 0.4), int(ALTO * 0.3)),
            "FACIL",
            get_fuente(75),
            "White",
            "Green",
        )

        NORMAL = self._mostrar_boton(
            boton_amarillo,
            (int(ANCHO * 0.6), int(ALTO * 0.3)),
            "NORMAL",
            get_fuente(75),
            "White",
            "Yellow",
        )

        DIFICIL = self._mostrar_boton(
            boton_rojo,
            (int(ANCHO * 0.8), int(ALTO * 0.3)),
            "DIFICIL",
            get_fuente(75),
            BLANCO,
            ROJO,
        )

        SONIDO_ON = self._mostrar_boton(
            boton_negro,
            (int(ANCHO * 0.50), int(ALTO * 0.44)),
            "ON",
            get_fuente(75),
            "White",
            "Green",
        )

        SONIDO_OFF = self._mostrar_boton(
            boton_negro,
            (int(ANCHO * 0.70), int(ALTO * 0.44)),
            "OFF",
            get_fuente(75),
            "White",
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
