import pygame

from settings import *

from .VentanaView import VentanaView


class LoginEquipoView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.__renderizados = {}

    def mostrar(self):
        self._botones = {}
        tabla_login = self.__renderizados["tabla_login"]
        self._pantalla.blit(tabla_login, (ANCHO * 0.25, ALTO * 0.2))
        texto_usuario = self.__renderizados["texto_usuario"]
        self._pantalla.blit(texto_usuario, (ANCHO * 0.28, ALTO * 0.33))
        flecha_atras = self.__renderizados["flecha_atras"]

        boton_usuario = self._mostrar_boton(
            None,
            (ANCHO * 0.54, ALTO * 0.36),
            "               ",
            get_fuente(60),
            NEGRO,
            NEGRO,
        )
        volver_atras = self._mostrar_boton(
            flecha_atras,
            (ANCHO * 0.29, ALTO * 0.25),
            "  ",
            get_fuente(30),
            BLANCO,
            ROJO,
        )
        self._botones["volver_atras"] = volver_atras
        self._botones["boton_usuario"] = boton_usuario

    def renderizar(self):
        renderizados = {}
        flecha_atras = pygame.image.load(FLECHA_IZQUIERDA)
        flecha_atras = pygame.transform.scale(boton_flecha_izquierda, (50, 50))
        tabla_login = pygame.image.load(TABLA_LOGIN)
        tabla_login = pygame.transform.scale(tabla_login, (600, 200))
        texto_usuario = get_fuente(60).render("USUARIO:", True, NEGRO)
        renderizados = {
            "tabla_login": tabla_login,
            "texto_usuario": texto_usuario,
            "flecha_atras": flecha_atras,
        }
        self.__renderizados = renderizados

    def mostrar_texto_usuario(self, texto_usuario):
        superficie_texto = self.__ajustar_texto(texto_usuario, FUENTE, 300, NEGRO)
        self._pantalla.blit(superficie_texto, (ANCHO * 0.43, ALTO * 0.335))

    def __ajustar_texto(self, texto, fuente, max_ancho, color):
        tamaño = 50  # Tamaño inicial
        while True:
            # llama a la fuente con el tamaño inicial
            fuente_actual = pygame.font.Font(fuente, tamaño)
            # renderiza el texto
            texto_renderizado = fuente_actual.render(texto, True, NEGRO)
            if texto_renderizado.get_width() <= max_ancho:
                # si el texto entra en el ancho maximo lo devuelve
                return get_fuente(tamaño).render(texto, True, color)
            tamaño -= 1
