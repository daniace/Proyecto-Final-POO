import pygame

from settings import *
from .VentanaView import VentanaView


class LoginView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def mostrar(self):
        self._botones = {}
        pygame.display.set_caption("LOGIN")
        # Fondo de pantalla
        self._pantalla.blit(BG, (0, 0))

        # Tabla
        IMAGEN_TABLA = pygame.image.load("src/assets/images/tabla.png")
        IMAGEN_TABLA = pygame.transform.scale(IMAGEN_TABLA, (650, 340))
        self._pantalla.blit(IMAGEN_TABLA, (int(ANCHO * 0.25), int(ALTO * 0.3)))

        # Botones
        LOGIN = self._mostrar_boton(
            boton_surface,
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 90)),
            "LOGIN",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )

        LOGIN_ATRAS = self._mostrar_boton(
            boton_rojo_cuadrado,
            (ANCHO * 0.045, ALTO * 0.09),
            "🔙",
            pygame.font.Font(EMOJIS, 75),
            BLANCO,
            ROJO,
        )

        self._botones["login"] = LOGIN
        self._botones["atras"] = LOGIN_ATRAS

    def mostrar_texto_usuario(self, texto_usuario):
        superficie_texto = get_fuente(50).render(texto_usuario, True, NEGRO)
        self._pantalla.blit(superficie_texto, (int(ANCHO * 0.4), int(ALTO * 0.5)))
