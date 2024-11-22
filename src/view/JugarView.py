import pygame

from settings import *

from .VentanaView import VentanaView


class JugarView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.__estadio = camp_nou

    def mostrar(self):
        self._botones = {}
        pygame.display.set_caption("JUGANDO")
        self._pantalla.fill(NEGRO)

        COLOR_FONDO = (120, 120, 120)
        TEXTO_ESTADIO = get_fuente(60).render("ESTADIO", True, BLANCO)
        ESTADIO_RECT = TEXTO_ESTADIO.get_rect(
            center=(int(ANCHO * 0.12), int(ALTO * 0.92))
        )
        margen = 20
        fondo_rect = ESTADIO_RECT.inflate(margen, margen)

        self.__dibujar_estadio()
        self._pantalla.blit(imagen_messi_copa, (int(ANCHO * 0.63), int(ALTO * 0.03)))
        pygame.draw.rect(self._pantalla, COLOR_FONDO, fondo_rect, border_radius=20)
        self._pantalla.blit(TEXTO_ESTADIO, ESTADIO_RECT)

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
        CAMBIAR_ESTADIO_ATRAS = self._mostrar_boton(
            boton_flecha_izquierda,
            (ANCHO * 0.027, ALTO * 0.92),
            "  ",
            get_fuente(30),
            BLANCO,
            ROJO,
        )

        CAMBIAR_ESTADIO_ADELANTE = self._mostrar_boton(
            boton_flecha_derecha,
            (ANCHO * 0.213, ALTO * 0.92),
            "  ",
            get_fuente(30),
            BLANCO,
            ROJO,
        )

        self._botones["atras"] = JUGAR_ATRAS
        self._botones["comienza"] = JUGAR_COMIENZA
        self._botones["dado"] = DADO
        self._botones["cambiar_formacion_atras"] = CAMBIAR_FORMACION_ATRAS
        self._botones["cambiar_formacion_adelante"] = CAMBIAR_FORMACION_ADELANTE
        self._botones["cambiar_estadio_atras"] = CAMBIAR_ESTADIO_ATRAS
        self._botones["cambiar_estadio_adelante"] = CAMBIAR_ESTADIO_ADELANTE

    def dibujar_formaciones(self, SCREEN, formaciones, formacion_actual, equipo):
        CARTA_IMAGEN = pygame.image.load(IMAGEN_CARTA)
        CARTA_IMAGEN = pygame.transform.scale(CARTA_IMAGEN, (80, 120))
        for jugador in equipo:
            print(jugador.get_nombre())
        for posicion in POSICIONES:
            for cordenadas, jugador in zip(
                formaciones[formacion_actual][posicion], equipo
            ):
                x = int(ANCHO * cordenadas[0])
                y = int(ALTO * cordenadas[1])

                NOMBRE_JUGADOR = self.__ajustar_texto(
                    jugador.get_nombre(), FUENTE, 70, jugador
                )
                SCREEN.blit(CARTA_IMAGEN, (x, y))
                SCREEN.blit(NOMBRE_JUGADOR, (x + 8.5, y + 90))

    def texto_formacion(self, formacion_actual):
        COLOR_FONDO = (120, 120, 120)
        TEXTO_FORMACION = get_fuente(75).render(
            f"FORMACION {formacion_actual}", True, "White"
        )
        FORMACION_RECT = TEXTO_FORMACION.get_rect(
            center=(int(ANCHO * 0.5), int(ALTO * 0.08))
        )
        margen = 8
        fondo_rect = FORMACION_RECT.inflate(margen * 3, margen * 2)
        pygame.draw.rect(self._pantalla, COLOR_FONDO, fondo_rect, border_radius=20)
        self._pantalla.blit(TEXTO_FORMACION, FORMACION_RECT)

    def __ajustar_texto(self, texto, fuente, max_ancho, jugador):
        tamaño = 20
        while True:
            fuente_actual = pygame.font.Font(fuente, tamaño)
            texto_renderizado = fuente_actual.render(texto, True, NEGRO)
            if texto_renderizado.get_width() <= max_ancho:
                return get_fuente(tamaño).render(jugador.get_nombre(), True, NEGRO)
            tamaño -= 1

    def __dibujar_estadio(self):
        self._pantalla.blit(self.__estadio, (0, 0))

    def cambiar_estadio(self, estadio):
        self.__estadio = estadio

    def get_estadio(self):
        return self.__estadio
