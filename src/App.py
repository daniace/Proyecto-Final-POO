import sys

import pygame

from view.Boton import Boton

# pygame setup
pygame.init()
ANCHO = 1280
ALTO = 720
SCREEN = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Héroes Del Balón")
scene_bg = pygame.image.load("src/assets/images/scene.jpg")
BG = pygame.transform.scale(scene_bg, (ANCHO, ALTO))
bg_opciones = pygame.image.load("src/assets/images/options.png")
BG_OPCIONES = pygame.transform.scale(bg_opciones, (ANCHO, ALTO))


def get_font(size):
    return pygame.font.Font("src/assets/font/Pixeltype.ttf", size)


clock = pygame.time.Clock()

# Fuentes
font = pygame.font.Font(None, 36)
# Colores
WHITE = (255, 255, 255)
BUTTON_COLOR = (200, 200, 170)
BUTTON_HOVER_COLOR = (180, 180, 150)


def jugar():
    pygame.display.set_caption("JUGANDO")

    while True:
        JUGAR_POS_MOUSE = pygame.mouse.get_pos()

        SCREEN.fill("black")

        TEXTO_JUGAR = get_font(45).render("VENTANA JUGANDO", True, "White")
        JUGAR_RECT = TEXTO_JUGAR.get_rect(center=(ANCHO // 2, 50))
        SCREEN.blit(TEXTO_JUGAR, JUGAR_RECT)

        JUGAR_ATRAS = Boton(
            image=None,
            pos=(ANCHO // 2 - 100, ALTO // 2 - 130),
            text_input="ATRAS",
            font=get_font(75),
            base_color="White",
            hovering_color="Green",
        )

        JUGAR_ATRAS.changeColor(JUGAR_POS_MOUSE)
        JUGAR_ATRAS.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if JUGAR_ATRAS.checkForInput(JUGAR_POS_MOUSE):
                    menu_principal()

        pygame.display.update()


def opciones():
    while True:
        OPCIONES_POS_MOUSE = pygame.mouse.get_pos()

        SCREEN.blit(BG_OPCIONES, (0, 0))

        TEXTO_OPCIONES = get_font(45).render("VENTANA OPCIONES", True, "Black")
        OPCIONES_RECT = TEXTO_OPCIONES.get_rect(center=(ANCHO // 2, 50))
        SCREEN.blit(TEXTO_OPCIONES, OPCIONES_RECT)

        OPCIONES_DIFICULTAD = Boton(
            image=None,
            pos=(int(ANCHO * 0.15), int(ALTO * 0.3)),
            text_input="DIFICULTAD",
            font=get_font(75),
            base_color="Black",
            hovering_color="White",
        )

        OPCIONES_DIFICULTAD.changeColor(OPCIONES_POS_MOUSE)
        OPCIONES_DIFICULTAD.update(SCREEN)

        FACIL = Boton(
            image=None,
            pos=(int(ANCHO * 0.3), int(ALTO * 0.3)),
            text_input="FACIL",
            font=get_font(75),
            base_color="Black",
            hovering_color="White",
        )

        FACIL.changeColor(OPCIONES_POS_MOUSE)
        FACIL.update(SCREEN)

        NORMAL = Boton(
            image=None,
            pos=(int(ANCHO * 0.45), int(ALTO * 0.3)),
            text_input="NORMAL",
            font=get_font(75),
            base_color="Black",
            hovering_color="White",
        )

        NORMAL.changeColor(OPCIONES_POS_MOUSE)
        NORMAL.update(SCREEN)

        DIFICIL = Boton(
            image=None,
            pos=(int(ANCHO * 0.6), int(ALTO * 0.3)),
            text_input="DIFICIL",
            font=get_font(75),
            base_color="Black",
            hovering_color="White",
        )

        DIFICIL.changeColor(OPCIONES_POS_MOUSE)
        DIFICIL.update(SCREEN)

        OPCIONES_SONIDO = Boton(
            image=None,
            pos=(int(ANCHO * 0.15), int(ALTO * 0.4)),
            text_input="SONIDO",
            font=get_font(75),
            base_color="Black",
            hovering_color="White",
        )

        OPCIONES_SONIDO.changeColor(OPCIONES_POS_MOUSE)
        OPCIONES_SONIDO.update(SCREEN)

        SONIDO_ON = Boton(
            image=None,
            pos=(int(ANCHO * 0.3), int(ALTO * 0.4)),
            text_input="ON",
            font=get_font(75),
            base_color="Black",
            hovering_color="White",
        )

        SONIDO_ON.changeColor(OPCIONES_POS_MOUSE)
        SONIDO_ON.update(SCREEN)

        SONIDO_OFF = Boton(
            image=None,
            pos=(int(ANCHO * 0.45), int(ALTO * 0.4)),
            text_input="OFF",
            font=get_font(75),
            base_color="Black",
            hovering_color="White",
        )

        SONIDO_OFF.changeColor(OPCIONES_POS_MOUSE)
        SONIDO_OFF.update(SCREEN)

        OPCIONES_CONTROLES = Boton(
            image=None,
            pos=(int(ANCHO * 0.15), int(ALTO * 0.5)),
            text_input="CONTROLES",
            font=get_font(75),
            base_color="Black",
            hovering_color="White",
        )

        OPCIONES_CONTROLES.changeColor(OPCIONES_POS_MOUSE)
        OPCIONES_CONTROLES.update(SCREEN)

        OPCIONES_ATRAS = Boton(
            image=None,
            pos=(int(ANCHO * 0.1), int(ALTO * 0.1)),
            text_input="ATRAS",
            font=get_font(75),
            base_color="Black",
            hovering_color="White",
        )

        OPCIONES_ATRAS.changeColor(OPCIONES_POS_MOUSE)
        OPCIONES_ATRAS.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPCIONES_ATRAS.checkForInput(OPCIONES_POS_MOUSE):
                    menu_principal()

        pygame.display.update()


def menu_principal():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXTO = get_font(45).render("MENU PRINCIPAL", True, "White")
        MENU_RECT = MENU_TEXTO.get_rect(center=(int(ANCHO * 0.5), 50))

        BOTON_JUGAR = Boton(
            image=None,
            pos=(int(ANCHO * 0.5), int(ALTO * 0.5)),
            text_input="JUGAR",
            font=get_font(75),
            base_color="White",
            hovering_color="Green",
        )
        BOTON_OPCIONES = Boton(
            image=None,
            pos=(int(ANCHO * 0.5), int(ALTO * 0.5 + 90)),
            text_input="OPCIONES",
            font=get_font(75),
            base_color="White",
            hovering_color="Green",
        )
        BOTON_SALIR = Boton(
            image=None,
            pos=(int(ANCHO * 0.5), int(ALTO * 0.5 + 180)),
            text_input="SALIR",
            font=get_font(75),
            base_color="White",
            hovering_color="Green",
        )

        SCREEN.blit(MENU_TEXTO, MENU_RECT)

        for boton in [BOTON_JUGAR, BOTON_OPCIONES, BOTON_SALIR]:
            boton.changeColor(MENU_MOUSE_POS)
            boton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_JUGAR.checkForInput(MENU_MOUSE_POS):
                    jugar()
                if BOTON_OPCIONES.checkForInput(MENU_MOUSE_POS):
                    opciones()
                if BOTON_SALIR.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


menu_principal()
