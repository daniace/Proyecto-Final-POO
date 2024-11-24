import pygame

from settings import *

from .VentanaView import VentanaView


class JugarView(VentanaView):
    def __init__(self, pantalla, nombre):
        super().__init__(pantalla)
        self.__estadio = camp_nou
        self.__atributos_carta = {}
        self._nuevo_nombre = nombre

    def mostrar(self):
        self._botones = {}
        pygame.display.set_caption("JUGANDO")

        # Dibuja el texto estadio que esta junto a los botones para cambiar los estadios del fondo
        COLOR_FONDO = (120, 120, 120)
        TEXTO_ESTADIO = get_fuente(60).render("ESTADIO", True, BLANCO)
        ESTADIO_RECT = TEXTO_ESTADIO.get_rect(
            center=(int(ANCHO * 0.12), int(ALTO * 0.92))
        )
        margen = 20
        fondo_rect = ESTADIO_RECT.inflate(margen, margen)
        # esto muestra el estadio en el fondo
        self.__dibujar_estadio()
        self._pantalla.blit(
            imagen_messi_copa, (int(ANCHO * 0.63), int(ALTO * 0.03))
        )  # esto muestra al messiArt en pantalla
        pygame.draw.rect(self._pantalla, COLOR_FONDO, fondo_rect, border_radius=20)
        self._pantalla.blit(TEXTO_ESTADIO, ESTADIO_RECT)

        # BOTONES
        CAMBIAR_FORMACION_ATRAS = self._mostrar_boton(
            boton_flecha_izquierda,
            (ANCHO * 0.31, ALTO * 0.055),
            "  ",
            get_fuente(30),
            BLANCO,
            ROJO,
        )

        CAMBIAR_FORMACION_ADELANTE = self._mostrar_boton(
            boton_flecha_derecha,
            (ANCHO * 0.69, ALTO * 0.055),
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
            None,
            (ANCHO * 0.88, ALTO * 0.6),
            "🎲",
            pygame.font.Font(EMOJIS, 75),
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

        NOMBRE_USUARIO = self._mostrar_boton(
            boton_surface,
            (ANCHO * 0.13, ALTO * 0.25),
            "NOMBRE DE USUARIO",
            get_fuente(40),
            BLANCO,
            NEGRO,
        )

        CAMBIO_NOMBRE = self._mostrar_boton(
            boton_surface,
            (ANCHO * 0.13, ALTO * 0.4),
            "NOMBRE DE EQUIPO",
            get_fuente(40),
            BLANCO,
            NEGRO,
        )
        # Guarda los botones como diccionario, recomendacion del profe Luis Luna A.K.A L.L(LA CABRA)
        self._botones["atras"] = JUGAR_ATRAS
        self._botones["comienza"] = JUGAR_COMIENZA
        self._botones["dado"] = DADO
        self._botones["cambiar_formacion_atras"] = CAMBIAR_FORMACION_ATRAS
        self._botones["cambiar_formacion_adelante"] = CAMBIAR_FORMACION_ADELANTE
        self._botones["cambiar_estadio_atras"] = CAMBIAR_ESTADIO_ATRAS
        self._botones["cambiar_estadio_adelante"] = CAMBIAR_ESTADIO_ADELANTE
        self._botones["nombre_equipo"] = CAMBIO_NOMBRE
        self._botones["nombre_usuario"] = NOMBRE_USUARIO

    def dibujar_formaciones(
        self, SCREEN, formaciones, formacion_actual, equipo, dado_apretado
    ):
        if dado_apretado:
            jugadores_asignados = 0  # Contador para asignar jugadores de la lista
            for posicion in POSICIONES:
                # Obtener las coordenadas para la posición actual
                coordenadas = formaciones[formacion_actual][posicion]
                # Si ya se usaron todos los jugadores, romper el bucle
                for cordenadas in coordenadas:
                    if jugadores_asignados >= len(equipo):
                        break
                    # Obtener el jugador correspondiente
                    jugador = equipo[jugadores_asignados]
                    jugadores_asignados += 1  # Avanzar al siguiente jugador
                    # x,y calculan posición en pantalla para la carta, tambien se usa para guiarnos con el texto
                    x = int(ANCHO * cordenadas[0])
                    y = int(ALTO * cordenadas[1])
                    # Utilizo el diccionario de estadisticas que se hizo con la funicon renderizar
                    atributos_carta = self.__atributos_carta[jugador.get_nombre()]
                    PAC = atributos_carta["PAC"]
                    SHO = atributos_carta["SHO"]
                    PAS = atributos_carta["PAS"]
                    DRI = atributos_carta["DRI"]
                    DEF = atributos_carta["DEF"]
                    PHY = atributos_carta["PHY"]
                    DOR = atributos_carta["DORSAL"]
                    OVR = atributos_carta["OVR"]
                    NOMBRE_JUGADOR = atributos_carta["NOMBRE_JUGADOR"]
                    CARTA_IMAGEN = atributos_carta["CARTA"]
                    # Dibujar carta y nombre del jugador
                    SCREEN.blit(CARTA_IMAGEN, (x, y))
                    SCREEN.blit(dorsal, (x + 43, y + 112))
                    SCREEN.blit(PAC, (x + 20, y + 35))
                    SCREEN.blit(SHO, (x + 20, y + 50))
                    SCREEN.blit(PAS, (x + 20, y + 65))
                    SCREEN.blit(DRI, (x + 60.5, y + 35))
                    SCREEN.blit(DEF, (x + 60.5, y + 50))
                    SCREEN.blit(PHY, (x + 60.5, y + 65))
                    SCREEN.blit(NOMBRE_JUGADOR, (x + 30, y + 80))
                    SCREEN.blit(DOR, (x + 55, y + 132))
                    SCREEN.blit(OVR, (x + 46.5, y + 12))

    def texto_formacion(self, formacion_actual):
        COLOR_FONDO = (120, 120, 120)
        TEXTO_FORMACION = get_fuente(75).render(
            f"FORMACION {formacion_actual}", True, "White"
        )
        FORMACION_RECT = TEXTO_FORMACION.get_rect(
            center=(int(ANCHO * 0.5), int(ALTO * 0.055))
        )
        margen = 8
        fondo_rect = FORMACION_RECT.inflate(margen * 3, margen * 2)
        pygame.draw.rect(self._pantalla, COLOR_FONDO, fondo_rect, border_radius=20)
        self._pantalla.blit(TEXTO_FORMACION, FORMACION_RECT)

    def __ajustar_texto(self, texto, fuente, max_ancho, color):
        tamaño = 25  # Tamaño inicial
        while True:
            # llama a la fuente con el tamaño inicial
            fuente_actual = pygame.font.Font(fuente, tamaño)
            # renderiza el texto
            texto_renderizado = fuente_actual.render(texto, True, NEGRO)
            if texto_renderizado.get_width() <= max_ancho:
                # si el texto entra en el ancho maximo lo devuelve
                return get_fuente(tamaño).render(texto, True, color)
            tamaño -= 1

    def __dibujar_estadio(self):
        self._pantalla.blit(self.__estadio, (0, 0))  # Dibujo el estadio en la pantalla

    def cambiar_estadio(self, estadio):
        self.__estadio = estadio  # cambia el estadio, como el main_loop esta escuchando todo el tiempo, la funcion __dibujar_estadio, al cambiarse el estadio se cambia la imagen del fondo

    def get_estadio(self):
        return self.__estadio  # devuelve el estadio

    # Esta funcion es para optimizar el rendimiento, si alguien lee esto y necesita explicacion del porque mejora el rendimiento preguntenme soy BRUNO # la maldita cabra tío soy ANGELO
    def renderizar(self, equipo):
        self.__atributos_carta = {}
        CARTA_IMAGEN = pygame.image.load(IMAGEN_CARTA)
        CARTA_IMAGEN = pygame.transform.scale(CARTA_IMAGEN, (120, 140))
        for jugador in equipo:
            if jugador.get_posicion_arquero() == "GK":
                estadisticas = {
                    "PAC": self.__ajustar_texto(
                        f"DIV {jugador.get_diving()}", FUENTE, 32, BLANCO
                    ),
                    "SHO": self.__ajustar_texto(
                        f"HAN {jugador.get_handling()}", FUENTE, 32, BLANCO
                    ),
                    "PAS": self.__ajustar_texto(
                        f"KIC {jugador.get_kicking()}", FUENTE, 32, BLANCO
                    ),
                    "DRI": self.__ajustar_texto(
                        f"REF {jugador.get_reflexes()}", FUENTE, 32, BLANCO
                    ),
                    "DEF": self.__ajustar_texto(
                        f"SPD {jugador.get_speed()}", FUENTE, 32, BLANCO
                    ),
                    "PHY": self.__ajustar_texto(
                        f"POS {jugador.get_positioning()}", FUENTE, 32, BLANCO
                    ),
                    "DORSAL": self.__ajustar_texto(
                        f"{jugador.get_dorsal()}", FUENTE, 32, BLANCO
                    ),
                    "OVR": self.__ajustar_texto(
                        f"{jugador.get_valoracion()}", FUENTE, 50, VERDE
                    ),
                    "NOMBRE_JUGADOR": self.__ajustar_texto(
                        jugador.get_nombre(), FUENTE, 60, BLANCO
                    ),
                    "CARTA": CARTA_IMAGEN,
                }
            else:
                estadisticas = {
                    "PAC": self.__ajustar_texto(
                        f"PAC {jugador.get_velocidad()}", FUENTE, 32, BLANCO
                    ),
                    "SHO": self.__ajustar_texto(
                        f"SHO {jugador.get_disparo()}", FUENTE, 32, BLANCO
                    ),
                    "PAS": self.__ajustar_texto(
                        f"PAS {jugador.get_pase()}", FUENTE, 32, BLANCO
                    ),
                    "DRI": self.__ajustar_texto(
                        f"DRI {jugador.get_gambeta()}", FUENTE, 32, BLANCO
                    ),
                    "DEF": self.__ajustar_texto(
                        f"DEF {jugador.get_defensa()}", FUENTE, 32, BLANCO
                    ),
                    "PHY": self.__ajustar_texto(
                        f"PHY {jugador.get_fisico()}", FUENTE, 32, BLANCO
                    ),
                    "DORSAL": self.__ajustar_texto(
                        f"{jugador.get_dorsal()}", FUENTE, 32, BLANCO
                    ),
                    "OVR": self.__ajustar_texto(
                        f"{jugador.get_valoracion()}", FUENTE, 50, VERDE
                    ),
                    "NOMBRE_JUGADOR": self.__ajustar_texto(
                        jugador.get_nombre(), FUENTE, 60, BLANCO
                    ),
                    "CARTA": CARTA_IMAGEN,
                }
            self.__atributos_carta[jugador.get_nombre()] = estadisticas
