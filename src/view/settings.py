import pygame

from database.AbmCarta import AbmCarta
from database.AbmUsuario import AbmUsuario

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
# Fuentes
FUENTE = "src/assets/font/Pixeltype.ttf"
EMOJIS = "src/assets/font/NotoEmoji-Regular.ttf"


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

clock = pygame.time.Clock()

boton_surface = pygame.image.load(IMAGEN_BOTON4)
boton_surface = pygame.transform.scale(boton_surface, (250, 80))

boton_cuadrado = pygame.image.load(IMAGEN_CUADRADO)
boton_cuadrado = pygame.transform.scale(boton_cuadrado, (80, 80))


def get_fuente(tamanio):
    return pygame.font.Font(FUENTE, tamanio)


clock = pygame.time.Clock()

boton_surface = pygame.image.load(IMAGEN_BOTON4)
boton_surface = pygame.transform.scale(boton_surface, (250, 80))

abmcarta = AbmCarta()
defensores = abmcarta.get_defensores()
abmusuario = AbmUsuario()
usuarios = abmusuario.get_all()

POS_MOUSE = pygame.mouse.get_pos()
