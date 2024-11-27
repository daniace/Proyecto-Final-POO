import gif_pygame
import pygame
import random
from settings import *

from .VentanaView import VentanaView


class CanchaView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.__renderizaciones = {}
        self.__estadio = camp_nou
        self.__estadio_cancha = barcelona
        self.__acciones = {}
        self.__pase_seleccionado = False
        self.__cantidad_pases = 0
        self.__equipo = 1
        self.__accion = None
        self.__nombre_gif = "corriendo"
        self.__numero_random_seleccionado = False
        self.__gif_actual = None

    def mostrar(self, tiempo):
        self._botones = {}
        pygame.display.set_caption("GAMEPLAY")
        self._pantalla.fill(NEGRO)
        self._pantalla.blit(self.__estadio, (0, 0))
        TIEMPO = get_fuente(50).render(f"      {tiempo}", True, NEGRO)
        score = self.__renderizaciones["score"]
        self._pantalla.blit(TIEMPO, (int(ANCHO * 0.81), int(ALTO * 0.04)))
        self._pantalla.blit(score, (int(ANCHO * 0.7), int(ALTO * 0.001)))
        self._pantalla.blit(
            self.__estadio_cancha, (int(ANCHO * 0.01), int(ALTO * 0.01))
        )
        equipo = get_fuente(35).render("Equipo 1", True, BLANCO)
        self._pantalla.blit(equipo, (int(ANCHO * 0.76), int(ALTO * 0.105)))
        cpu = get_fuente(35).render("Equipo 2", True, BLANCO)
        self._pantalla.blit(cpu, (int(ANCHO * 0.91), int(ALTO * 0.105)))

        # if self.__accion is not None:
        #     texto = self.__acciones[self.__accion]
            
            
            
        #     if self.__gif is not None:  #esto creo que se saca, siempre hay gif creo
        #         if not self.__numero_random_seleccionado:
        #             self.__numero_random_seleccionado = True
        #             self.__num = random.randint(0, len(self.__renderizaciones[self.__gif]) - 1)
        #             self.__gif_actual = self.__renderizaciones[self.__gif][self.__num if not self.__gif == 'corriendo' else 0]
                
        #         self.__gif_actual.render(
        #         self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05))
        #         )
        #         if self.__gif_actual.ended:
        #             self.__gif = 'corriendo'
        #             if self.__gif != self.__accion:
        #                 self.__gif = self.__accion
        #                 self.__numero_random_seleccionado = False
                    
                    
        #             # self.__gif = None
        


        #     self._pantalla.blit(texto, (int(ANCHO * 0.25), int(ALTO * 0.05)))
            
        if self.__accion is not None:
            texto = self.__acciones[self.__accion]
            self._pantalla.blit(texto, (int(ANCHO * 0.25), int(ALTO * 0.05)))

            self.renderizar_gif()
        # pygame.display.update()



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
                self._pantalla.blit(
                    NOMBRE_JUGADOR, (int(ANCHO * 0.42), int(ALTO * 0.86))
                )
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
            gif = self.__renderizaciones[self.__gif_actual][0 if self.__gif_actual == 'corriendo' else self.__numero_random_seleccionado]
            gif.render(self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05)))

            if gif.ended:
                self.cambiar_gif()

    def cambiar_gif(self):
        if self.__gif_actual != "corriendo":
            self.__gif_actual = "corriendo"
        elif self.__accion is not None:
            self.__gif_actual = self.__accion
            self.__accion = None
            self.__numero_random_seleccionado = random.randint(0, len(self.__renderizaciones[self.__gif]) - 1)

    def mostrar_mensaje(self, mensaje, y):
        fuente = get_fuente(75)
        texto_render = fuente.render(mensaje, True, "White")
        self._pantalla.blit(
            texto_render, (ANCHO / 2 - texto_render.get_width() / 2, y + 300)
        )
        pygame.display.flip()

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
        tamaño = 42  # Tamaño inicial
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
            "pase_valido": self.__ajustar_texto("Pase exitoso", FUENTE, 250, NEGRO),
            "pase_invalido": self.__ajustar_texto("Pase fallido", FUENTE, 250, NEGRO),
            "tiro_al_arco": self.__ajustar_texto("Tiro al arco", FUENTE, 250, NEGRO),
            "tiro_fallado": self.__ajustar_texto("Tiro fallido", FUENTE, 250, NEGRO),
            "atajado": self.__ajustar_texto("Tiro atajado", FUENTE, 250, NEGRO),
            "gol": self.__ajustar_texto("Gooooooolazoooo", FUENTE, 250, NEGRO),
            "interseccion_valida": self.__ajustar_texto(
            "Intercepcion exitosa", FUENTE, 250, NEGRO
            ),
            "interseccion_fallida": self.__ajustar_texto(
            "Intercepcion fallida", FUENTE, 250, NEGRO
            ),
            "gambeta_exitosa": self.__ajustar_texto(
            "Gambeta exitosa", FUENTE, 250, NEGRO
            ),
            "gambeta_fallida": self.__ajustar_texto(
            "Gambeta fallida", FUENTE, 250, NEGRO
            ),
        }
        self.__acciones = acciones

    def renderizar(self):
        score = pygame.image.load(SCORE)
        score = pygame.transform.scale(score, (400, 200))
        CORRIENDO_1 = gif_pygame.load(CORRIENDO, loops=0)
        PASE_GIF = gif_pygame.load(PASE, loops=0)
        PASE2_GIF = gif_pygame.load(PASE2, loops=0)


        TIRO_GIF = gif_pygame.load(TIRO, loops=0)
        TIRO_LEJANO_GIF = gif_pygame.load(TIRO_LEJANO, loops=0)

        
        GAMBETA_GIF = gif_pygame.load(GAMBETA, loops=0)
        GAMBETA2_GIF = gif_pygame.load(GAMBETA2, loops=0)
        GAMBETA3_GIF = gif_pygame.load(GAMBETA3, loops=0)
        GAMBETA4_GIF = gif_pygame.load(GAMBETA4, loops=0)

        INTERCEPCION_PASE_GIF = gif_pygame.load(INTERCEPCION_PASE, loops=0)
        INTERCEPCION_PASE2_GIF = gif_pygame.load(INTERCEPCION_PASE2, loops=0)
        INTERCEPCION_PASE3_GIF = gif_pygame.load(INTERCEPCION_PASE3, loops=0)

        ATAJADA_GIF = gif_pygame.load(ATAJADA, loops=0)
        ATAJADA2_GIF = gif_pygame.load(ATAJADA2, loops=0)
        
        gifs = {'pase_valido': [PASE_GIF, PASE2_GIF],
                'pase_invalido': [INTERCEPCION_PASE_GIF, INTERCEPCION_PASE2_GIF, INTERCEPCION_PASE3_GIF],
                'tiro_al_arco': [TIRO_GIF, TIRO_LEJANO_GIF],
                'tiro_fallado': [TIRO_GIF, TIRO_LEJANO_GIF],
                'gol': [TIRO_GIF, TIRO_LEJANO_GIF],
                'gambeta_exitosa': [GAMBETA_GIF, GAMBETA2_GIF, GAMBETA3_GIF, GAMBETA4_GIF],
                'gambeta_fallida': [GAMBETA_GIF, GAMBETA2_GIF, GAMBETA3_GIF, GAMBETA4_GIF],
                'interseccion_valida': [INTERCEPCION_PASE_GIF, INTERCEPCION_PASE2_GIF, INTERCEPCION_PASE3_GIF],
                'interseccion_fallida': [INTERCEPCION_PASE_GIF, INTERCEPCION_PASE2_GIF, INTERCEPCION_PASE3_GIF],
                'atajado': [ATAJADA_GIF, ATAJADA2_GIF],
                'corriendo': [CORRIENDO_1],
                'score': score
        }
        'AGREGAR MAS GIFS'
        
        self.__renderizaciones = gifs

    def set_pase(self, pase):
        self.__pase = pase

    def set_pase_seleccionado(self, cantidad_pases):
        self.__pase_seleccionado = True
        self.__cantidad_pases = cantidad_pases

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
        self.__accion = accion
        self.__gif_actual = accion
