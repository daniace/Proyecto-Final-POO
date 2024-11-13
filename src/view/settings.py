# Configuracion de la pantalla
ANCHO = 1280
ALTO = 720
TAMANIO_PANTALLA = (ANCHO, ALTO)
FULLSCREEN = False

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
#
IMAGEN_BOTON5 = "src/assets/images/boton5.png"
IMAGEN_RANKING = "src/assets/images/ranking.jpg"
# Fuentes
FUENTE = "src/assets/font/Pixeltype.ttf"


def get_fuente(tamanio):
    return pygame.font.Font(FUENTE, tamanio)


# Sonidos
SONIDO_FONDO = "src/assets/audio/soundtrack.wav"
SONIDO_PELE = "src/assets/audio/reypele.wav"
