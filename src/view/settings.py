import pygame

from database.AbmCarta import AbmCarta
from database.AbmUsuario import AbmUsuario
from database.Usuario import Usuario

# Configuracion de la pantalla
ANCHO = 1280
ALTO = 720
TAMANIO_PANTALLA = (ANCHO, ALTO)
FULLSCREEN = False
SCREEN = pygame.display.set_mode(TAMANIO_PANTALLA)
clock = pygame.time.Clock()

# Colores en RGB
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
COLOR_FONDO = NEGRO

# Configuracion del juego
FPS = 60

# Recursos
IMAGEN_FONDO = "src/assets/images/scene.jpg"
IMAGEN_FORMACION = "src/assets/images/formacion.jpg"
IMAGEN_FONDO_OPCIONES = "src/assets/images/options.png"
IMAGEN_BOTON1 = "src/assets/images/boton.png"
IMAGEN_BOTON2 = "src/assets/images/boton2.png"
IMAGEN_BOTON3 = "src/assets/images/boton3.png"
IMAGEN_BOTON4 = "src/assets/images/boton4.png"
IMAGEN_CARTA = "src/assets/images/carta.png"
IMAGEN_CANCHA = "src/assets/images/cancha.png"
IMAGEN_TABLA = "src/assets/images/tabla.png"
IMAGEN_CUADRADO = "src/assets/images/boton_cuadrado.png"
IMAGEN_BOTON5 = "src/assets/images/boton5.png"
IMAGEN_RANKING = "src/assets/images/ranking.jpg"
IMAGEN_DADO = "src/assets/images/dado_1.png"
HOME = "src/assets/images/Home.png"
IMAGEN_BOTON6 = "src/assets/images/boton6.png"
IMAGEN_BOTON7 = "src/assets/images/boton7.png"
# Fuentes
FUENTE = "src/assets/font/Pixeltype.ttf"
EMOJIS = "src/assets/font/NotoEmoji-Regular.ttf"
IMAGEN_CANCHA_OFICIAL = "src/assets/images/canchita.png"


def get_fuente(tamanio):
    return pygame.font.Font(FUENTE, tamanio)


# Sonidos
SONIDO_FONDO = "src/assets/audio/soundtrack.wav"
SONIDO_PELE = "src/assets/audio/reypele.wav"

scene_bg = pygame.image.load(IMAGEN_FONDO)
BG = pygame.transform.scale(scene_bg, TAMANIO_PANTALLA)
bg_opciones = pygame.image.load(IMAGEN_FONDO_OPCIONES)
BG_OPCIONES = pygame.transform.scale(bg_opciones, TAMANIO_PANTALLA)
bg_jugar = pygame.image.load(IMAGEN_FONDO)
BG_JUGAR = pygame.transform.scale(bg_jugar, TAMANIO_PANTALLA)
bg_formacion = pygame.image.load(IMAGEN_FORMACION)
BG_FORMACION = pygame.transform.scale(bg_formacion, TAMANIO_PANTALLA)
bg_ranking = pygame.image.load(IMAGEN_RANKING)
BG_RANKING = pygame.transform.scale(bg_ranking, TAMANIO_PANTALLA)
bg_cancha_oficial = pygame.image.load(IMAGEN_CANCHA_OFICIAL)
BG_CANCHA_OFICIAL = pygame.transform.scale(bg_cancha_oficial, (ANCHO, ALTO // 1.3))
clock = pygame.time.Clock()

boton_surface = pygame.image.load(IMAGEN_BOTON4)
boton_surface = pygame.transform.scale(boton_surface, (250, 80))

boton_cuadrado = pygame.image.load(IMAGEN_CUADRADO)
boton_cuadrado = pygame.transform.scale(boton_cuadrado, (75, 75))

boton_home = pygame.image.load(HOME)
boton_home = pygame.transform.scale(boton_home, (70, 70))

boton_rojo = pygame.image.load(IMAGEN_BOTON5)
boton_rojo = pygame.transform.scale(boton_rojo, (250, 80))

boton_rojo_cuadrado = pygame.image.load(IMAGEN_BOTON5)
boton_rojo_cuadrado = pygame.transform.scale(boton_rojo_cuadrado, (75, 75))

boton_verde = pygame.image.load(IMAGEN_BOTON6)
boton_verde = pygame.transform.scale(boton_verde, (250, 80))

boton_verde_cuadrado = pygame.image.load(IMAGEN_BOTON6)
boton_verde_cuadrado = pygame.transform.scale(boton_verde_cuadrado, (75, 75))

boton_amarillo = pygame.image.load(IMAGEN_BOTON7)
boton_amarillo = pygame.transform.scale(boton_amarillo, (250, 80))

boton_dado = pygame.image.load(IMAGEN_DADO)
boton_dado = pygame.transform.scale(boton_dado, (95, 95))


def get_fuente(tamanio):
    return pygame.font.Font(FUENTE, tamanio)


clock = pygame.time.Clock()


abmcarta = AbmCarta()
defensores = abmcarta.get_defensores()
abmusuario = AbmUsuario()
usuarios = abmusuario.get_all()
usuario = Usuario()

POS_MOUSE = pygame.mouse.get_pos()

# Dificultad


class dificultad:
    def __init__(self, facil=70, normal=50, dificil=30):
        self._facil = facil
        self._normal = normal
        self._dificil = dificil

    def dificil(self):
        self._facil -= 10
        self._dificil -= 10

    def facil(self):
        self._facil += 10
        self._dificil += 10
