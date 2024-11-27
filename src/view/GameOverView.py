import pygame

from settings import ALTO, ANCHO, get_fuente
from model.logic.Partido import Partido
from .VentanaView import VentanaView


class GameOverView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.__puntos = None
        self.__goles = None

    def mostrar(self):
        self._botones = {}
        self._pantalla.fill("Black")
        pygame.display.set_caption("GAME OVER")
        texto = get_fuente(200).render("GAME OVER", True, "White")
        rect = texto.get_rect(center=(ANCHO * 0.5, ALTO * 0.2))
        self._pantalla.blit(texto, rect)
        puntos = get_fuente(80).render(f"puntos Ganados: {self.__puntos}", True, "White")
        self._pantalla.blit(puntos, (ANCHO * 0.33, ALTO * 0.4))
        if self.__goles[0] > self.__goles[1]:
            ganador = get_fuente(80).render("GANASTE", True, "Green")
            self._pantalla.blit(ganador, (ANCHO * 0.425, ALTO * 0.3))
        elif self.__goles[0] < self.__goles[1]:
            perdedor = get_fuente(80).render("PERDISTE", True, "Red")
            self._pantalla.blit(perdedor, (ANCHO * 0.425, ALTO * 0.3))
        else:
            empatador = get_fuente(80).render("EMPATE", True, "Yellow")
            self._pantalla.blit(empatador, (ANCHO * 0.425, ALTO * 0.3))
        goles = get_fuente(80).render(f"resultado  {self.__goles[0]} - {self.__goles[1]}", True, "White")
        self._pantalla.blit(goles, (ANCHO * 0.33, ALTO * 0.5))
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
        
    def mostrar2(self, mensaje):
        self._botones = {}
        self._pantalla.fill("Black")
        pygame.display.set_caption("PUNTOS")
        texto = get_fuente(50).render(mensaje, True, "White")
        rect = texto.get_rect(center=(ANCHO // 4, ALTO // 4))
        self._pantalla.blit(texto, rect)
    
    def set_resultado(self, puntos, goles):
        self.__puntos = puntos
        self.__goles = goles