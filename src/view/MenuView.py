import pygame
from .Boton import Boton
from settings import *


class MenuView:
    def __init__(self, pantalla):
        self.__pantalla = pantalla  # La pantalla principal donde se dibuja el menú
        self.__botones = []

    def mostrar_menu(self):
        # Fondo de pantalla
        self.__pantalla.blit(BG, (0, 0))

        # Título del menú
        MENU_TEXTO = get_fuente(120).render("HEROES DEL BALON", True, "White")
        MENU_RECT = MENU_TEXTO.get_rect(center=(int(ANCHO * 0.5), 180))
        self.__pantalla.blit(MENU_TEXTO, MENU_RECT)

        # Botones
        BOTON_LOGIN = self.mostrar_boton(
            boton_cuadrado,
            (ANCHO * 0.1, ALTO * 0.1),
            "👤",
            pygame.font.Font(EMOJIS),
            BLANCO,
            NEGRO,
        )
        BOTON_JUGAR = self.mostrar_boton(
            boton_surface,
            (ANCHO * 0.5, ALTO * 0.5),
            "JUGAR",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )
        BOTON_OPCIONES = self.mostrar_boton(
            boton_surface,
            (ANCHO * 0.5, ALTO * 0.5 + 180),
            "OPCIONES",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )
        BOTON_RANKING = self.mostrar_boton(
            boton_surface,
            (ANCHO * 0.5, ALTO * 0.5 + 90),
            "RANKING",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )
        BOTON_SALIR = self.mostrar_boton(
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
            self.__botones.append(boton)

    def get_botones(self):
        return self.__botones

    def mostrar_boton(self, imagen, pos, texto, fuente, color_base, hovering_color):
        mouse_pos = pygame.mouse.get_pos()
        boton = Boton(imagen, pos, texto, fuente, color_base, hovering_color)
        boton.changeColor(mouse_pos)
        boton.update(self.__pantalla)
        return boton
