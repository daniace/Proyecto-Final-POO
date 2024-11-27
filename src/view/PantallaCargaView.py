import pygame
from .VentanaView import VentanaView
from settings import *
import time


class CargaView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.__mostrar_pantalla = True

    def mostrar(self, progreso):
        pygame.display.set_caption("Pantalla de carga")
        self._pantalla.fill(NEGRO)
        texto = f"Cargando... {progreso}%"
        mensaje = get_fuente(50).render(texto, True, BLANCO)
        self._pantalla.blit(
            mensaje,
            (
                ANCHO // 2 - mensaje.get_width() // 2,
                ALTO // 2 - mensaje.get_height() // 2 - 40,
            ),
        )
        # Barra de carga
        x = ANCHO // 2 - 200  # Posición X de la barra (centrada)
        y = ALTO // 2  # Posición Y de la barra
        largo_barra = 400  # Longitud total de la barra
        alto_barra = 30  # Alto de la barra
        pygame.draw.rect(
            self._pantalla, BLANCO, (x, y, largo_barra, alto_barra), 2
        )  # Borde de la barra
        # Calcular el ancho lleno de la barra según el porcentaje
        ancho_lleno = (largo_barra * progreso) // 100
        pygame.draw.rect(
            self._pantalla, VERDE, (x + 2, y + 2, ancho_lleno, alto_barra - 4)
        )  # Barra verde
        pygame.display.flip()

    # Simula el progreso de carga

    pygame.display.flip()

    def main_loop(self):
        for progreso in range(0, 101, 10):  # Incrementos de 10% en el progreso
            self.mostrar(progreso)
            pygame.time.delay(100)  # Simula tiempo de carga (0.5 segundos por paso)
