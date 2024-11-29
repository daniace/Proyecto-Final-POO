import pygame

from settings import *
from .VentanaView import VentanaView


class MenuView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def mostrar(self):
        self._botones = {}
        # Fondo de pantalla
        pygame.display.set_caption("HEROES DEL BALON")
        self._pantalla.blit(BG, (0, 0))

        # Título del menú
        MENU_TEXTO = get_fuente(120).render("HEROES DEL BALON", True, "White")
        MENU_RECT = MENU_TEXTO.get_rect(center=(int(ANCHO * 0.5), 180))
        self._pantalla.blit(MENU_TEXTO, MENU_RECT)

        # Botones
        BOTON_LOGIN = self._mostrar_boton(
            boton_cuadrado,
            (ANCHO * 0.1, ALTO * 0.1),
            "👤",
            pygame.font.Font(EMOJIS, 50),
            BLANCO,
            NEGRO,
        )
        BOTON_JUGAR = self._mostrar_boton(
            boton_surface,
            (ANCHO * 0.5, ALTO * 0.5),
            "JUGAR",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )
        BOTON_OPCIONES = self._mostrar_boton(
            boton_surface,
            (ANCHO * 0.5, ALTO * 0.5 + 180),
            "OPCIONES",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )
        BOTON_RANKING = self._mostrar_boton(
            boton_surface,
            (ANCHO * 0.5, ALTO * 0.5 + 90),
            "RANKING",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )
        BOTON_SALIR = self._mostrar_boton(
            boton_rojo2,
            (ANCHO * 0.5, ALTO * 0.5 + 270),
            "SALIR",
            get_fuente(75),
            BLANCO,
            ROJO,
        )
        BOTON_MIEMBROS = self._mostrar_boton(
            boton_cuadrado,
            (ANCHO * 0.95, ALTO * 0.93),
            "👥",
            pygame.font.Font(EMOJIS, 50),
            BLANCO,
            NEGRO,
        )
        self._botones["miembros"] = BOTON_MIEMBROS
        self._botones["login"] = BOTON_LOGIN
        self._botones["jugar"] = BOTON_JUGAR
        self._botones["opciones"] = BOTON_OPCIONES
        self._botones["ranking"] = BOTON_RANKING
        self._botones["salir"] = BOTON_SALIR
