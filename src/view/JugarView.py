import pygame

from settings import *

from .VentanaView import VentanaView


class JugarView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def mostrar(self):
        self._botones = {}
        pygame.display.set_caption("JUGANDO")
        self._pantalla.fill(NEGRO)

        TEXTO_JUGAR = get_fuente(45).render("VENTANA JUGANDO", True, "White")
        JUGAR_RECT = TEXTO_JUGAR.get_rect(center=(ANCHO // 2, 50))
        self._pantalla.blit(TEXTO_JUGAR, JUGAR_RECT)
        CANCHA_IMAGEN = pygame.image.load(IMAGEN_CANCHA)
        CANCHA_IMAGEN = pygame.transform.scale(CANCHA_IMAGEN, (ANCHO // 2, ALTO))
        self._pantalla.blit(BG_ESTADIO, (0, 0))
        # self._pantalla.blit(imagen_messi, (int(ANCHO * 0.001), int(ALTO * 0.11)))
        self._pantalla.blit(imagen_messi_copa, (int(ANCHO * 0.63), int(ALTO * 0.03)))
        # self._pantalla.blit(imagen_d10s, (int(ANCHO * 0.0001), int(ALTO * 0.3)))
        # self._pantalla.blit(imagen_dibu, (int(ANCHO * 0.001), int(ALTO * 0.55)))
        # BOTONES
        CAMBIAR_FORMACION_ATRAS = self._mostrar_boton(
            boton_flecha_izquierda,
            (ANCHO * 0.31, ALTO * 0.077),
            "  ",
            get_fuente(30),
            BLANCO,
            ROJO,
        )

        CAMBIAR_FORMACION_ADELANTE = self._mostrar_boton(
            boton_flecha_derecha,
            (ANCHO * 0.69, ALTO * 0.077),
            "  ",
            get_fuente(30),
            BLANCO,
            ROJO,
        )

        JUGAR_ATRAS = self._mostrar_boton(
            boton_rojo_cuadrado,
            (ANCHO * 0.045, ALTO * 0.08),
            "🔙",
            pygame.font.Font(EMOJIS, 75),
            BLANCO,
            ROJO,
        )

        JUGAR_COMIENZA = self._mostrar_boton(
            boton_verde,
            (ANCHO * 0.88, ALTO * 0.90),
            "COMIENZA",
            get_fuente(75),
            "White",
            "Green",
        )

        DADO = self._mostrar_boton(
            boton_dado,
            (ANCHO * 0.88, ALTO * 0.6),
            "",
            get_fuente(75),
            "White",
            "Green",
        )

        self._botones["atras"] = JUGAR_ATRAS
        self._botones["comienza"] = JUGAR_COMIENZA
        self._botones["dado"] = DADO
        self._botones["cambiar_formacion_atras"] = CAMBIAR_FORMACION_ATRAS
        self._botones["cambiar_formacion_adelante"] = CAMBIAR_FORMACION_ADELANTE

    def dibujar_formaciones(self, SCREEN, formaciones, formacion_actual):
        CARTA_IMAGEN = pygame.image.load(IMAGEN_CARTA)
        CARTA_IMAGEN = pygame.transform.scale(CARTA_IMAGEN, (80, 120))
        for posicion in POSICIONES:
            for cordenadas in formaciones[formacion_actual][posicion]:
                x = int(ANCHO * cordenadas[0])
                y = int(ALTO * cordenadas[1])
                tamaño = self.ajustar_texto("L.Messi", FUENTE, 60)
                NOMBRE_JUGADOR = get_fuente(tamaño).render("L.Messi", True, NEGRO)
                SCREEN.blit(CARTA_IMAGEN, (x, y))
                SCREEN.blit(NOMBRE_JUGADOR, (x + 8.5, y + 90))

    def texto_formacion(self, formacion_actual):
        COLOR_FONDO = (128, 128, 128)
        TEXTO_FORMACION = get_fuente(75).render(
            f"FORMACION {formacion_actual}", True, "White"
        )
        FORMACION_RECT = TEXTO_FORMACION.get_rect(
            center=(int(ANCHO * 0.5), int(ALTO * 0.08))
        )
        margen = 9
        fondo_rect = FORMACION_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(self._pantalla, COLOR_FONDO, fondo_rect, border_radius=15)
        self._pantalla.blit(TEXTO_FORMACION, FORMACION_RECT)

    def ajustar_texto(self, texto, fuente, max_ancho):
        tamaño = 20
        while True:
            fuente_actual = pygame.font.Font(fuente, tamaño)
            texto_renderizado = fuente_actual.render(texto, True, NEGRO)
            if texto_renderizado.get_width() <= max_ancho:
                return tamaño
            tamaño -= 1
