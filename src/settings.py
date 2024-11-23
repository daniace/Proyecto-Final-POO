import gif_pygame
import pygame

from model.database.AbmCarta import AbmCarta
from model.database.AbmUsuario import AbmUsuario
from model.database.Usuario import Usuario

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
FORMACION_PREDETERMINADA = "4-3-3"
POSICIONES = [
    "portero",
    "defensas",
    "mediocampistas",
    "delanteros",
]  # asi de esta forma es la correcta
FORMACIONES = {
    "4-3-3": {
        "portero": [(0.45, 0.79)],
        "defensas": [(0.30, 0.56), (0.40, 0.58), (0.50, 0.58), (0.60, 0.56)],
        "mediocampistas": [(0.35, 0.34), (0.45, 0.36), (0.55, 0.34)],
        "delanteros": [(0.35, 0.13), (0.45, 0.11), (0.55, 0.13)],  # tupla: (ancho,alto)
    },
    "4-4-2": {
        "portero": [(0.45, 0.79)],
        "defensas": [(0.30, 0.56), (0.40, 0.58), (0.50, 0.58), (0.60, 0.56)],
        "mediocampistas": [(0.31, 0.33), (0.40, 0.36), (0.50, 0.36), (0.59, 0.33)],
        "delanteros": [(0.40, 0.12), (0.50, 0.12)],
    },
}

# Recursos
IMAGEN_FONDO = "src/assets/images/scene.jpg"
IMAGEN_FORMACION = "src/assets/images/formacion.jpg"
IMAGEN_FONDO_OPCIONES = "src/assets/images/options.png"
IMAGEN_BOTON1 = "src/assets/images/boton.png"
IMAGEN_BOTON2 = "src/assets/images/boton2.png"
IMAGEN_BOTON3 = "src/assets/images/boton3.png"
IMAGEN_BOTON4 = "src/assets/images/boton4.png"
IMAGEN_CARTA = "src/assets/images/carta1.png"
IMAGEN_CANCHA = "src/assets/images/cancha.png"
CAMP_NOU = "src/assets/images/campnou.png"
MONUMENTAL = "src/assets/images/monumental.png"
BOMBONERA = "src/assets/images/bombonera.png"
BERNABEU = "src/assets/images/bernabeu.png"
IMAGEN_ESTADIO = "src/assets/images/estadio.jpg"
IMAGEN_TABLA = "src/assets/images/tabla.png"
IMAGEN_CUADRADO = "src/assets/images/boton_cuadrado.png"
IMAGEN_BOTON5 = "src/assets/images/boton5.png"
IMAGEN_RANKING = "src/assets/images/ranking.jpg"
IMAGEN_DADO = "src/assets/images/dado_1.png"
HOME = "src/assets/images/Home.png"
IMAGEN_BOTON6 = "src/assets/images/boton6.png"
IMAGEN_BOTON7 = "src/assets/images/boton7.png"
BOTON_NEGRO = "src/assets/images/BotonNegro.png"
RECTANGULO_NEGRO = "src/assets/images/RectanguloNegro.png"
MESSI = "src/assets/images/messi.png"
MESSI_COPA = "src/assets/images/messi_copa.png"
D10S = "src/assets/images/d10s.png"
DIBU = "src/assets/images/dibu.png"
DORSAL = "src/assets/images/dorsal.png"
# Fuentes
FUENTE = "src/assets/font/Pixeltype.ttf"
EMOJIS = "src/assets/font/NotoEmoji-Regular.ttf"
IMAGEN_CANCHA_OFICIAL = "src/assets/images/canchita.png"
FLECHA_IZQUIERDA = "src/assets/images/flechaIzquierda.png"
FLECHA_DERECHA = "src/assets/images/flechaDerecha.png"
OLD_TRAFORD = "src/assets/images/oldtraford.png"
MALASIA = "src/assets/images/malasia.png"
AZTECA = "src/assets/images/azteca.png"
# GIFS
ATAJADA = "src/assets/images/atajada.gif"
ATAJADA_GIF = gif_pygame.load(ATAJADA)
pygame.font.init()

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
BG_CANCHA_OFICIAL = pygame.transform.scale(bg_cancha_oficial, (250, 400))
bg_estadio = pygame.image.load(IMAGEN_ESTADIO)
BG_ESTADIO = pygame.transform.scale(bg_estadio, TAMANIO_PANTALLA)
clock = pygame.time.Clock()

##ESTADIOS##
azteca = pygame.image.load(AZTECA)
azteca = pygame.transform.scale(azteca, TAMANIO_PANTALLA)

malasia = pygame.image.load(MALASIA)
malasia = pygame.transform.scale(malasia, TAMANIO_PANTALLA)

old_traford = pygame.image.load(OLD_TRAFORD)
old_traford = pygame.transform.scale(old_traford, TAMANIO_PANTALLA)

camp_nou = pygame.image.load(CAMP_NOU)
camp_nou = pygame.transform.scale(camp_nou, TAMANIO_PANTALLA)

monumental = pygame.image.load(MONUMENTAL)
monumental = pygame.transform.scale(monumental, TAMANIO_PANTALLA)

bernabeu = pygame.image.load(BERNABEU)
bernabeu = pygame.transform.scale(bernabeu, TAMANIO_PANTALLA)

bombonera = pygame.image.load(BOMBONERA)
bombonera = pygame.transform.scale(bombonera, TAMANIO_PANTALLA)
##ESTADIOS##

dorsal = pygame.image.load(DORSAL)
dorsal = pygame.transform.scale(dorsal, (35, 35))

imagen_messi = pygame.image.load(MESSI)
imagen_messi = pygame.transform.scale(imagen_messi, (350, 350))

imagen_messi_copa = pygame.image.load(MESSI_COPA)
imagen_messi_copa = pygame.transform.scale(imagen_messi_copa, (650, 350))

imagen_d10s = pygame.image.load(D10S)
imagen_d10s = pygame.transform.scale(imagen_d10s, (280, 280))

imagen_dibu = pygame.image.load(DIBU)
imagen_dibu = pygame.transform.scale(imagen_dibu, (350, 350))

boton_surface = pygame.image.load(IMAGEN_BOTON4)
boton_surface = pygame.transform.scale(boton_surface, (250, 80))

boton_flecha_izquierda = pygame.image.load(FLECHA_IZQUIERDA)
boton_flecha_izquierda = pygame.transform.scale(boton_flecha_izquierda, (65, 65))

boton_flecha_derecha = pygame.image.load(FLECHA_DERECHA)
boton_flecha_derecha = pygame.transform.scale(boton_flecha_derecha, (65, 65))


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

boton_negro = pygame.image.load(BOTON_NEGRO)
boton_negro = pygame.transform.scale(boton_negro, (250, 100))
boton_negro2 = pygame.transform.scale(boton_negro, (250, 80))

marcador = pygame.image.load(RECTANGULO_NEGRO)
marcador = pygame.transform.scale(marcador, (300, 400))


def get_fuente(tamanio):
    return pygame.font.Font(FUENTE, tamanio)


clock = pygame.time.Clock()


abmcarta = AbmCarta()
defensores = abmcarta.get_defensores()
abmusuario = AbmUsuario()
usuarios = abmusuario.get_all()
usuario = Usuario()

POS_MOUSE = pygame.mouse.get_pos()
