import pygame

from settings import ALTO, ANCHO, get_fuente

from .VentanaView import VentanaView


class GameOverView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def mostrar(self):
        self._botones = {}
        self._pantalla.fill("Black")
        pygame.display.set_caption("GAME OVER")
        texto = get_fuente(200).render("GAME OVER", True, "White")
        rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
        self._pantalla.blit(texto, rect)

        JUGAR_DE_NUEVO = self._mostrar_boton(
            None,
            (ANCHO * 0.2, ALTO * 0.9),
            "JUGAR",
            get_fuente(75),
            "White",
            "Green",
        )

        MENU_PRINCIPAL = self._mostrar_boton(
            None,
            (ANCHO * 0.5, ALTO * 0.9),
            "MENU",
            get_fuente(75),
            "White",
            "Blue",
        )

        SALIR = self._mostrar_boton(
            None,
            (ANCHO * 0.8, ALTO * 0.9),
            "SALIR",
            get_fuente(75),
            "White",
            "Red",
        )

        self._botones["jugar_de_nuevo"] = JUGAR_DE_NUEVO
        self._botones["menu_principal"] = MENU_PRINCIPAL
        self._botones["salir"] = SALIR
