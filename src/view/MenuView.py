import pygame
from .Boton import Boton
from settings import *
from .VentanaView import VentanaView


class MenuView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def mostrar(self):
        # Fondo de pantalla
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
            pygame.font.Font(EMOJIS),
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
            boton_surface,
            (ANCHO * 0.5, ALTO * 0.5 + 270),
            "SALIR",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )
        for boton in [
            BOTON_LOGIN,
            BOTON_JUGAR,
            BOTON_OPCIONES,
            BOTON_RANKING,
            BOTON_SALIR,
        ]:
            self._botones.append(boton)
