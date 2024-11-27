import gif_pygame
import time
import pygame
import random
from settings import *

from .VentanaView import VentanaView


class CanchaView(VentanaView):
    def __init__(self, pantalla, nombre_equipo):
        super().__init__(pantalla)
        self.__nombre_equipo = nombre_equipo
        self.__renderizaciones = {}
        self.__estadio = camp_nou
        self.__estadio_cancha = barcelona
        self.__acciones = {}
        self.__pase_seleccionado = False
        self.__cantidad_pases = 0
        self.__equipo = 1
        self.__accion = None
        self.__accion_anterior = None  # esto creo que se saca
        self.__numero_random_seleccionado = False
        self.__gif_actual = "corriendo"
        self.__posicion_pelota = None
        self.__lista_jugadores = None
        self.__posicion_pelota = None
        self.__nro_jugada_global = 0
        self.__nroJugada = 0
        self.__gif_terminado = True
        self.__gif_anterior = None
        self.__goles = []
        self.__accion_cpu = None
        self.__nroJugada_cpu = 0

    def mostrar(self, tiempo):
        self._botones = {}
        pygame.display.set_caption("GAMEPLAY")
        self._pantalla.fill(NEGRO)
        self._pantalla.blit(self.__estadio, (0, 0))
        CIRCULO = pygame.image.load(CIRCULONEGRO)
        CIRCULO = pygame.transform.scale(CIRCULO, (50, 50))
        self._pantalla.blit(CIRCULO, (ANCHO * 0.92, ALTO * 0.12))
        self._pantalla.blit(CIRCULO, (ANCHO * 0.77, ALTO * 0.12))
        RECTANGULO = pygame.image.load(RECTANGULO_NEGRO)
        RECATANGULO = pygame.transform.scale(RECTANGULO, (600, 400))
        self._pantalla.blit(RECATANGULO, (ANCHO * 0.228, ALTO * 0.01))
        TIEMPO = get_fuente(50).render(f"      {tiempo}", True, NEGRO)
        self._pantalla.blit(boton_negro3, (ANCHO * 0.575, ALTO * 0.57))
        self._pantalla.blit(boton_negro4, (ANCHO * 0.575, ALTO * 0.77))
        score = self.__renderizaciones["score"]
        self._pantalla.blit(TIEMPO, (int(ANCHO * 0.81), int(ALTO * 0.04)))
        self._pantalla.blit(score, (int(ANCHO * 0.7), int(ALTO * 0.001)))
        self._pantalla.blit(
            self.__estadio_cancha, (int(ANCHO * 0.01), int(ALTO * 0.01))
        )
        equipo = self.__ajustar_texto(f"{self.__nombre_equipo}", FUENTE, 85, BLANCO)
        self._pantalla.blit(equipo, (int(ANCHO * 0.75), int(ALTO * 0.102)))
        cpu = get_fuente(35).render("CPU", True, BLANCO)
        self._pantalla.blit(cpu, (int(ANCHO * 0.93), int(ALTO * 0.105)))
        self.mostrar_jugadores()
        self.mostrar_pelota()
        self.mostrar_goles()

        self.texto_jugadas()

        self.renderizar_gif()
        # pygame.display.update()

        # print(self.__posicion_pelota)

        if self.__pase_seleccionado:
            if self.__cantidad_pases >= 1:
                PASE1 = self._mostrar_boton(
                    boton_negro2,
                    (ANCHO * 0.3, ALTO * 0.65),
                    "PASE1",
                    get_fuente(50),
                    BLANCO,
                    "Green",
                )
                atributos_carta = self.__atributos_carta[0]
                CAMISETA = atributos_carta["CAMISETA"]
                DOR = atributos_carta["DORSAL"]
                NOMBRE_JUGADOR = atributos_carta["NOMBRE_JUGADOR"]
                CARTA_IMAGEN = atributos_carta["CARTA"]
                PASE = atributos_carta["PASE"]
                self._pantalla.blit(CARTA_IMAGEN, (int(ANCHO * 0.2), int(ALTO * 0.8)))
                self._pantalla.blit(PASE, (int(ANCHO * 0.228), int(ALTO * 0.82)))
                self._pantalla.blit(
                    NOMBRE_JUGADOR, (int(ANCHO * 0.22), int(ALTO * 0.86))
                )
                self._pantalla.blit(CAMISETA, (int(ANCHO * 0.225), int(ALTO * 0.89)))
                self._pantalla.blit(DOR, (int(ANCHO * 0.24), int(ALTO * 0.935)))
                self._botones["pase1"] = PASE1
            if self.__cantidad_pases >= 2:
                PASE2 = self._mostrar_boton(
                    boton_negro2,
                    (ANCHO * 0.5, ALTO * 0.65),
                    "PASE2",
                    get_fuente(50),
                    BLANCO,
                    "Green",
                )
                atributos_carta = self.__atributos_carta[1]
                CAMISETA = atributos_carta["CAMISETA"]
                DOR = atributos_carta["DORSAL"]
                NOMBRE_JUGADOR = atributos_carta["NOMBRE_JUGADOR"]
                CARTA_IMAGEN = atributos_carta["CARTA"]
                PASE = atributos_carta["PASE"]
                self._pantalla.blit(CARTA_IMAGEN, (int(ANCHO * 0.3), int(ALTO * 0.8)))
                self._pantalla.blit(PASE, (int(ANCHO * 0.328), int(ALTO * 0.82)))
                self._pantalla.blit(
                    NOMBRE_JUGADOR, (int(ANCHO * 0.32), int(ALTO * 0.86))
                )
                self._pantalla.blit(CAMISETA, (int(ANCHO * 0.325), int(ALTO * 0.89)))
                self._pantalla.blit(DOR, (int(ANCHO * 0.34), int(ALTO * 0.935)))
                self._botones["pase2"] = PASE2
            if self.__cantidad_pases >= 3:
                PASE3 = self._mostrar_boton(
                    boton_negro2,
                    (ANCHO * 0.3, ALTO * 0.75),
                    "PASE3",
                    get_fuente(50),
                    BLANCO,
                    "Green",
                )
                atributos_carta = self.__atributos_carta[2]
                CAMISETA = atributos_carta["CAMISETA"]
                DOR = atributos_carta["DORSAL"]
                NOMBRE_JUGADOR = atributos_carta["NOMBRE_JUGADOR"]
                CARTA_IMAGEN = atributos_carta["CARTA"]
                PASE = atributos_carta["PASE"]
                self._pantalla.blit(CARTA_IMAGEN, (int(ANCHO * 0.4), int(ALTO * 0.8)))
                self._pantalla.blit(PASE, (int(ANCHO * 0.428), int(ALTO * 0.82)))
                NOMBRE_JUGADOR, (int(ANCHO * 0.42), int(ALTO * 0.86))
                self._pantalla.blit(CAMISETA, (int(ANCHO * 0.425), int(ALTO * 0.89)))
                self._pantalla.blit(DOR, (int(ANCHO * 0.44), int(ALTO * 0.935)))
                self._botones["pase3"] = PASE3
            if self.__cantidad_pases >= 4:
                PASE4 = self._mostrar_boton(
                    boton_negro2,
                    (ANCHO * 0.5, ALTO * 0.75),
                    "PASE4",
                    get_fuente(50),
                    BLANCO,
                    "Green",
                )
                atributos_carta = self.__atributos_carta[3]
                CAMISETA = atributos_carta["CAMISETA"]
                DOR = atributos_carta["DORSAL"]
                NOMBRE_JUGADOR = atributos_carta["NOMBRE_JUGADOR"]
                CARTA_IMAGEN = atributos_carta["CARTA"]
                PASE = atributos_carta["PASE"]
                self._pantalla.blit(CARTA_IMAGEN, (int(ANCHO * 0.5), int(ALTO * 0.8)))
                self._pantalla.blit(PASE, (int(ANCHO * 0.528), int(ALTO * 0.82)))
                self._pantalla.blit(
                    NOMBRE_JUGADOR, (int(ANCHO * 0.52), int(ALTO * 0.86))
                )
                self._pantalla.blit(CAMISETA, (int(ANCHO * 0.525), int(ALTO * 0.89)))
                self._pantalla.blit(DOR, (int(ANCHO * 0.54), int(ALTO * 0.935)))

                self._botones["pase4"] = PASE4
            # self._botones[]
            # if self.__pase:
            #     pase = self.__acciones["pase_concretado"]
            #     self._pantalla.blit(pase, (int(ANCHO * 0.8), int(ALTO * 0.7)))
            # else:
            #     pase = self.__acciones["pase_errado"]
            #     self._pantalla.blit(pase, (int(ANCHO * 0.8), int(ALTO * 0.7)))

        # if self.__pase_seleccionado:
        PASE = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.65),
            "PASE",
            get_fuente(50),
            BLANCO,
            "Green",
        )

        TIRO = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.75),
            "TIRO",
            get_fuente(50),
            BLANCO if self.__equipo == 1 else NEGRO,
            "Green" if self.__equipo == 1 else NEGRO,
        )

        GAMBETA = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.85),
            "GAMBETA",
            get_fuente(50),
            BLANCO if self.__equipo == 1 else NEGRO,
            "Green" if self.__equipo == 1 else NEGRO,
        )

        INTERCEPTAR = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.95),
            "INTERCEPTAR",
            get_fuente(50),
            BLANCO if self.__equipo == 2 else NEGRO,
            "Green" if self.__equipo == 2 else NEGRO,
        )
        self._botones["interceptar"] = INTERCEPTAR
        self._botones["gambeta"] = GAMBETA
        self._botones["tiro"] = TIRO
        self._botones["pase"] = PASE

    def renderizar_gif(self):
        gif = self.__renderizaciones[self.__gif_actual][
            0 if self.__gif_actual == "corriendo" else self.__numero_random_seleccionado
        ]
        gif.render(self._pantalla, (int(ANCHO * 0.232), int(ALTO * 0.018)))

        if gif.ended:
            self.__gif_terminado = True
            gif.reset()
            print(self.__gif_actual, "GIFFF ACTUAL")
            print(self.__gif_anterior, "GIFFF ANTERIOR")
            if self.__gif_actual != self.__gif_anterior:
                self.cambiar_gif()
        else:
            self.__gif_terminado = False

    def cambiar_gif(self):
        if self.__gif_actual != "corriendo":
            self.__gif_actual = "corriendo"
        elif self.__accion is not None:  # and self.__accion_anterior != self.__accion:
            if self.__gif_actual != "corriendo":
                self.__gif_anterior = self.__gif_actual
                self.__accion_anterior = self.__gif_actual
            self.__gif_actual = self.__accion
            print(self.__gif_actual, "actual")
            print(self.__gif_anterior, "anterior")
            self.__numero_random_seleccionado = random.randint(
                0, int(len(self.__renderizaciones[self.__gif_actual]) - 1)
            )

    def mostrar_mensaje(self, mensaje, y):
        fuente = get_fuente(75)
        texto_render = fuente.render(mensaje, True, "White")
        self._pantalla.blit(
            texto_render, (ANCHO / 2 - texto_render.get_width() / 2, y + 300)
        )
        pygame.display.flip()

    def mostrar_jugadores(self):
        jugador = pygame.image.load(EQUIPO_US)
        jugador_punto = pygame.transform.scale(jugador, (10, 10))
        jugador_cpu = pygame.image.load(EQUIPO_CPU)
        punto_cpu = pygame.transform.scale(jugador_cpu, (10, 10))
        jugadores_usuario = [0, 1, 3, 5]
        jugadores_cpu = [2, 4, 6, 7]
        for coordenada, tipo in self.__lista_jugadores.items():
            x, y = tipo
            if coordenada[0] in jugadores_usuario:
                self._pantalla.blit(jugador_punto, (x, y))
            elif coordenada[0] in jugadores_cpu:
                self._pantalla.blit(punto_cpu, (x, y))

    def mostrar_pelota(self):
        pelota = pygame.image.load(PELOTA)
        pelota = pygame.transform.scale(pelota, (10, 10))
        self._pantalla.blit(pelota, self.__posicion_pelota)

    def set_lista_jugadores(self, jugadores):
        self.__lista_jugadores = jugadores

    def set_estadio(self, estadio):
        self.__estadio = estadio

    def setear_estadio_cancha(self):
        if self.__estadio == camp_nou:
            self.__estadio_cancha = barcelona
        elif self.__estadio == bernabeu:
            self.__estadio_cancha = madrid
        elif self.__estadio == old_traford:
            self.__estadio_cancha = manchester
        elif self.__estadio == monumental:
            self.__estadio_cancha = nuñez
        elif self.__estadio == bombonera:
            self.__estadio_cancha = boca
        elif self.__estadio == azteca:
            self.__estadio_cancha = mexico
        elif self.__estadio == malasia:
            self.__estadio_cancha = malasya

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

    def renderizar_acciones(self):
        acciones = {
            "pase_valido": self.__ajustar_texto(
                "                               Buen Pase \n    -- Has hacertado el pase :) --",
                FUENTE,
                400,
                VERDE,
            ),
            "pase_invalido": self.__ajustar_texto(
                "                                Mal Pase \n       -- Has errado el pase :) --",
                FUENTE,
                400,
                ROJO,
            ),
            "tiro_al_arco": self.__ajustar_texto(
                "\n        CHUTASTEEEEEEEEEE!", FUENTE, 350, BLANCO
            ),
            "tiro_fallado": self.__ajustar_texto(
                "                          Erraste el tiro\n-- La tiraste a la segunda bandeja --\n                        BURROOOOOOOO!!!",
                FUENTE,
                450,
                ROJO,
            ),
            "atajado": self.__ajustar_texto(
                "                       ATAJADA RIVAL\n-- QUE PARADON DEL ARQUERO!! --",
                FUENTE,
                435,
                ROJO,
            ),
            "gol": self.__ajustar_texto(
                "               Acertaste el tiro\n   -- Gooooooolazooooo --",
                FUENTE,
                450,
                VERDE,
            ),
            "interseccion_valida": self.__ajustar_texto(
                "                 Interseccion exitosa \n-- Le quitaste el balon al rival! --",
                FUENTE,
                400,
                VERDE,
            ),
            "interseccion_fallida": self.__ajustar_texto(
                "                   Interseccion fallida \n -- No le quitaste el balon al rival :( --",
                FUENTE,
                435,
                ROJO,
            ),
            "gambeta_exitosa": self.__ajustar_texto(
                "                       Gambeta exitosa \n      -- Buena gambeta chaval! -- \n                         ankara messi",
                FUENTE,
                380,
                VERDE,
            ),
            "gambeta_fallida": self.__ajustar_texto(
                "                       Gambeta fallida \n      -- Mala gambeta chaval! -- \n                  no ankara messi :'(",
                FUENTE,
                380,
                ROJO,
            ),
            "pase_a_interceptar": self.__ajustar_texto(
                "                        Pase del rival \n-- Aqui va el balon companiero! --",
                FUENTE,
                450,
                VERDE,
            ),
            "gol_cpu": self.__ajustar_texto(
                "        El rival disparo al arco\n   -- Gooooooolazooooo --",
                FUENTE,
                400,
                VERDE,
            ),
            "atajado_cpu": self.__ajustar_texto(
                "                El rival disparo al arco\n-- QUE PARADON DEL ARQUERO!! --\n          TU ARQUERO PARA TODAS",
                FUENTE,
                400,
                VERDE,
            ),
            "tiro_fallado_cpu": self.__ajustar_texto(
                "               El rival disparo al arco\n      -- El rival la tiro a saturno --\n                       BURROOOOOOOO!!!",
                FUENTE,
                400,
                ROJO,
            ),
        }
        self.__acciones = acciones

    def renderizar(self):
        score = pygame.image.load(SCORE)
        score = pygame.transform.scale(score, (400, 200))
        CORRIENDO_1 = gif_pygame.load(CORRIENDO, loops=0)
        PASE_GIF = gif_pygame.load(PASE, loops=0)
        PASE2_GIF = gif_pygame.load(PASE2, loops=0)

        CUADRADO_TEXTO = pygame.image.load(RECTANGULO_NEGRO)
        CUADRADO_TEXTO = pygame.transform.scale(CUADRADO_TEXTO, (450, 250))

        TIRO_GIF = gif_pygame.load(TIRO, loops=0)
        TIRO2_GIF = gif_pygame.load(TIRO2, loops=0)
        TIRO_LEJANO_GIF = gif_pygame.load(TIRO_LEJANO, loops=0)
        TIRO_FALLADO_GIF = gif_pygame.load(TIRO_FALLADO, loops=0)

        GOL_GIF = gif_pygame.load(GOL, loops=0)
        GOL2_GIF = gif_pygame.load(GOL2, loops=0)
        GOL3_GIF = gif_pygame.load(GOL3, loops=0)

        GAMBETA_GIF = gif_pygame.load(GAMBETA, loops=0)
        GAMBETA2_GIF = gif_pygame.load(GAMBETA2, loops=0)
        GAMBETA3_GIF = gif_pygame.load(GAMBETA3, loops=0)
        GAMBETA_FALLIDA_GIF = gif_pygame.load(GAMBETA_FALLIDA, loops=0)

        INTERCEPCION_PASE_GIF = gif_pygame.load(INTERCEPCION_PASE, loops=0)
        INTERCEPCION_PASE2_GIF = gif_pygame.load(INTERCEPCION_PASE2, loops=0)
        INTERCEPCION_PASE3_GIF = gif_pygame.load(INTERCEPCION_PASE3, loops=0)
        INTERCEPCION_FALLIDA_GIF = gif_pygame.load(INTERCEPCION_FALLIDA, loops=0)
        INTERCEPCION_FALLIDA2_GIF = gif_pygame.load(INTERCEPCION_FALLIDA2, loops=0)

        ATAJADA_GIF = gif_pygame.load(ATAJADA, loops=0)
        ATAJADA2_GIF = gif_pygame.load(ATAJADA2, loops=0)

        COMIENZA_PARTIDO_GIF = gif_pygame.load(COMIENZA_PARTIDO, loops=0)
        COMIENZA_PARTIDO2_GIF = gif_pygame.load(COMIENZA_PARTIDO2, loops=0)

        SAQUE_MEDIO_GIF = gif_pygame.load(SAQUE_MEDIO, loops=0)

        FIN_PARTIDO_GIF = gif_pygame.load(FIN_PARTIDO, loops=0)

        gifs = {
            "pase_valido": [PASE_GIF, PASE2_GIF],
            "pase_invalido": [
                INTERCEPCION_PASE_GIF,
                INTERCEPCION_PASE2_GIF,
                INTERCEPCION_PASE3_GIF,
            ],
            "tiro_al_arco": [TIRO_GIF, TIRO2_GIF, TIRO_LEJANO_GIF],
            "tiro_fallado": [TIRO_FALLADO_GIF, TIRO_LEJANO_GIF],
            "gol": [GOL_GIF, GOL2_GIF, GOL3_GIF],
            "gambeta_exitosa": [GAMBETA_GIF, GAMBETA2_GIF, GAMBETA3_GIF],
            "gambeta_fallida": [GAMBETA_FALLIDA_GIF, GAMBETA_FALLIDA_GIF],
            "interseccion_valida": [
                INTERCEPCION_PASE_GIF,
                INTERCEPCION_PASE2_GIF,
                INTERCEPCION_PASE3_GIF,
            ],
            "interseccion_fallida": [
                INTERCEPCION_FALLIDA_GIF,
                INTERCEPCION_FALLIDA2_GIF,
            ],
            "atajado": [ATAJADA_GIF, ATAJADA2_GIF],
            "corriendo": [CORRIENDO_1],
            "score": score,
            "comienza": [COMIENZA_PARTIDO_GIF, COMIENZA_PARTIDO2_GIF],
            "saque": [SAQUE_MEDIO_GIF, SAQUE_MEDIO_GIF],
            "fin": [FIN_PARTIDO_GIF, FIN_PARTIDO_GIF],
        }
        "AGREGAR MAS GIFS"

        self.__renderizaciones = gifs

    def set_pase(self, pase):
        self.__pase = pase

    def set_pase_seleccionado(self, cantidad_pases):
        self.__pase_seleccionado = True
        self.__cantidad_pases = cantidad_pases

    def set_posicion_pelota(self, posicion):
        self.__posicion_pelota = posicion

    def deseleccionar_pase(self):
        self.__pase_seleccionado = False

    def renderizar_carta(self, jugadores):
        self.__atributos_carta = []
        CARTA_IMAGEN = pygame.image.load(IMAGEN_CARTA)
        CARTA_IMAGEN = pygame.transform.scale(CARTA_IMAGEN, (120, 140))
        CAMISETA = pygame.image.load(DORSAL)
        CAMISETA = pygame.transform.scale(CAMISETA, (60, 60))
        i = 0
        for jugador in jugadores:
            i += 1
            estadisticas = {
                "PASE": self.__ajustar_texto(f"PASE {i}", FUENTE, 50, VERDE_CLARO),
                "CAMISETA": CAMISETA,
                "DORSAL": self.__ajustar_texto(
                    f"{jugador.get_dorsal()}", FUENTE, 30, BLANCO
                ),
                "NOMBRE_JUGADOR": self.__ajustar_texto(
                    jugador.get_nombre(), FUENTE, 65, BLANCO
                ),
                "CARTA": CARTA_IMAGEN,
            }
            self.__atributos_carta.append(estadisticas)

    def cambiar_equipo(self, equipo):
        self.__equipo = equipo

    def set_accion(self, accion):
        self.__accion_anterior = self.__accion
        self.__accion = accion
        # self.__gif_actual = accion
        # self.__gif_terminado = False

    def set_nroJugada(self):
        self.__nroJugada += 1

    def set_goles(self, goles):
        self.__goles = goles

    def mostrar_goles(self):
        CIRCULO = pygame.image.load(CIRCULONEGRO)
        CIRCULO = pygame.transform.scale(CIRCULO, (50, 50))
        self._pantalla.blit(CIRCULO, (ANCHO * 0.92, ALTO * 0.11))
        self._pantalla.blit(CIRCULO, (ANCHO * 0.77, ALTO * 0.11))
        COLOR1 = BLANCO
        COLOR2 = BLANCO
        if self.__goles[0] > self.__goles[1]:
            COLOR1 = VERDE_CLARO
            COLOR2 = ROJO
        elif self.__goles[0] < self.__goles[1]:
            COLOR1 = ROJO
            COLOR2 = VERDE_CLARO
        gol_equipo = get_fuente(50).render(f"{self.__goles[0]}", True, COLOR1)
        self._pantalla.blit(gol_equipo, (int(ANCHO * 0.785), int(ALTO * 0.13)))
        gol_rival = get_fuente(50).render(f"{self.__goles[1]}", True, COLOR2)
        self._pantalla.blit(gol_rival, (int(ANCHO * 0.935), int(ALTO * 0.13)))

    def set_goles(self, goles):
        self.__goles = goles

    def mostrar_goles(self):
        COLOR1 = BLANCO
        COLOR2 = BLANCO
        if self.__goles[0] > self.__goles[1]:
            COLOR1 = VERDE_CLARO
            COLOR2 = ROJO
        elif self.__goles[0] < self.__goles[1]:
            COLOR1 = ROJO
            COLOR2 = VERDE_CLARO
        gol_equipo = get_fuente(50).render(f"{self.__goles[0]}", True, COLOR1)
        self._pantalla.blit(gol_equipo, (int(ANCHO * 0.785), int(ALTO * 0.142)))
        gol_rival = get_fuente(50).render(f"{self.__goles[1]}", True, COLOR2)
        self._pantalla.blit(gol_rival, (int(ANCHO * 0.935), int(ALTO * 0.142)))

    def get_gif_terminado(self):
        if self.__gif_actual == "corriendo":
            return True
        return self.__gif_terminado

    def inicio_partido(self):
        self.__gif_actual = "corriendo"
        self.__accion = None

    def set_accion_cpu(self, accion):
        self.__accion_cpu = accion

    def texto_jugadas(self):
        if self.__nro_jugada_global > 0:
            texto_jugada = get_fuente(50).render(
                f"Jugada Nro {self.__nroJugada}", True, BLANCO
            )
            self._pantalla.blit(texto_jugada, (int(ANCHO * 0.72), int(ALTO * 0.615)))
        if self.__nro_jugada_global > 1 and self.__accion_cpu is not None:
            texto_jugada = get_fuente(50).render(
                f"Jugada Nro {self.__nroJugada_cpu}", True, BLANCO
            )
            self._pantalla.blit(texto_jugada, (int(ANCHO * 0.72), int(ALTO * 0.815)))

        if self.__accion_cpu is not None:
            texto = self.__acciones[self.__accion_cpu]
            self._pantalla.blit(texto, (int(ANCHO * 0.63), int(ALTO * 0.87)))

        if self.__accion is not None:
            texto = self.__acciones[self.__accion]
            self._pantalla.blit(texto, (int(ANCHO * 0.63), int(ALTO * 0.67)))

    def set_nroJugada_cpu(self):
        self.__nroJugada_cpu += 1

    def ultima_jugada(self, equipo):
        self.__nro_jugada_global += 1
        if equipo == 1:
            self.__nroJugada = self.__nro_jugada_global
        else:
            self.__nroJugada_cpu = self.__nro_jugada_global
