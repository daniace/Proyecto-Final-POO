import threading
import time

import pygame


class ReproductorMusica:
    def __init__(self, volumen=0.5):
        """
        Inicializa el reproductor de música.
        :param volumen: Volumen inicial (entre 0.0 y 1.0).
        """
        pygame.mixer.init()  # Inicializar el módulo de audio
        self.__volumen = volumen
        self.__musica_actual = None
        self.__reproduciendo = False
        self.__hilo = None

    def cargar_musica(self, ruta):
        """
        Carga un archivo de música.
        :param ruta: Ruta al archivo de música.
        """
        self.__musica_actual = ruta
        pygame.mixer.music.load(ruta)

    def reproducir(self, bucle=-1):
        """
        Reproduce la música en un hilo separado.
        :param bucle: Número de veces que se repetirá la música (-1 para infinito).
        """
        if not self.__musica_actual:
            raise ValueError("No se ha cargado ninguna música.")

        self.__reproduciendo = True

        def __reproducir_musica():
            pygame.mixer.music.set_volume(self.__volumen)
            pygame.mixer.music.play(bucle)
            while self.__reproduciendo:
                time.sleep(0.1)  # Mantiene vivo el hilo

        self.__hilo = threading.Thread(target=__reproducir_musica, daemon=True)
        self.__hilo.start()

    def pausar(self):
        """Pausa la reproducción."""
        pygame.mixer.music.pause()

    def reanudar(self):
        """Reanuda la reproducción."""
        pygame.mixer.music.unpause()

    def detener(self):
        """Detiene la reproducción y el hilo."""
        self.__reproduciendo = False
        pygame.mixer.music.stop()
        if self.__hilo and self.__hilo.is_alive():
            self.__hilo.join(timeout=1)

    def cambiar_volumen(self, volumen):
        """
        Cambia el volumen de la música.
        :param volumen: Nuevo volumen (entre 0.0 y 1.0).
        """
        self.__volumen = volumen
        pygame.mixer.music.set_volume(volumen)

    def es_reproduciendo(self):
        """
        Verifica si la música está reproduciéndose.
        :return: True si está reproduciendo, False en caso contrario.
        """
        return pygame.mixer.music.get_busy()


# Ejemplo de uso
if __name__ == "__main__":
    reproductor = ReproductorMusica()
    reproductor.cargar_musica("musica_de_fondo.mp3")
    reproductor.reproducir()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        reproductor.detener()
