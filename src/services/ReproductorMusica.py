import pygame

from src.settings import SONIDO_FONDO


class ReproductorMusica:
    def __init__(self):
        self.__musica = pygame.mixer.music

    def reproducir_soundtrack(self):
        """Reproduce el soundtrack del juego en bucle."""
        pygame.mixer.init()
        self.__musica.load(SONIDO_FONDO)
        self.__musica.play(-1)

    def reanudar_soundtrack(self):
        """Reanuda el soundtrack del juego."""
        self.__musica.unpause()

    def pausar_soundtrack(self):
        """Pausa el soundtrack del juego."""
        self.__musica.pause()
