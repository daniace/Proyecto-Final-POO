import sys

import pygame

from .settings import *
from .boton import *

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode(TAMANIO_PANTALLA)
clock = pygame.time.Clock()
pygame.display.set_caption("Héroes Del Balón")
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
pygame.mixer.init()
pygame.mixer.music.load(SONIDO_FONDO)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


def get_fuente(tamanio):
    return pygame.font.Font(FUENTE, tamanio)


clock = pygame.time.Clock()

boton_surface = pygame.image.load(IMAGEN_BOTON4)
boton_surface = pygame.transform.scale(boton_surface, (250, 80))


def jugar():
    pygame.display.set_caption("JUGANDO")

    while True:
        JUGAR_POS_MOUSE = pygame.mouse.get_pos()
        SCREEN.blit(BG_FORMACION, (0, 0))
        # SCREEN.fill("black")

        TEXTO_JUGAR = get_fuente(45).render("VENTANA JUGANDO", True, "White")
        JUGAR_RECT = TEXTO_JUGAR.get_rect(center=(ANCHO // 2, 50))
        SCREEN.blit(TEXTO_JUGAR, JUGAR_RECT)

        JUGAR_ATRAS = Boton(
            boton_surface,
            (ANCHO * 0.88 , ALTO * 0.9),
            "ATRAS",
            get_fuente(75),
            "White",
            "Green",
        )
        JUGAR_ATRAS.changeColor(JUGAR_POS_MOUSE)
        JUGAR_ATRAS.update(SCREEN)
        # ------------
        JUGAR_FORMACION = Boton(
            None,
            (ANCHO // 4.7 - 100, ALTO // 3.2 - 130),
            "FORMACIONES:",
            get_fuente(75),
            "White",
            "Green",
        )
        JUGAR_FORMACION.changeColor(JUGAR_POS_MOUSE)
        JUGAR_FORMACION.update(SCREEN)
        # ------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() #ESTE FOR SE TENDRA QUE IMPLEMENTAR EN EL CONTROLADOR
                #Y ACA SOLO LLAMAMOS A LA VARIABLE/FUNCION DE DICHO CONTROLADOR Y SUS PARAMETROS
            if event.type == pygame.MOUSEBUTTONDOWN:
                if JUGAR_ATRAS.checkForInput(JUGAR_POS_MOUSE):
                    menu_principal()
        clock.tick(60)
        pygame.display.update()


def opciones():
    while True:
        OPCIONES_POS_MOUSE = pygame.mouse.get_pos()

        SCREEN.blit(BG_OPCIONES, (0, 0))

        TEXTO_OPCIONES = get_fuente(100).render("OPCIONES", True, "Black")
        OPCIONES_RECT = TEXTO_OPCIONES.get_rect(center=(ANCHO // 2, 50))
        SCREEN.blit(TEXTO_OPCIONES, OPCIONES_RECT)
        
        #
        COLOR_FONDO = (128,128,128)
        TEXTO_CONTROLES = get_fuente(75).render("CONTROLES:", True, "White")
        CONTROLES_RECT = TEXTO_CONTROLES.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.6))
        )
        margen = 20  
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
        SCREEN.blit(TEXTO_CONTROLES, CONTROLES_RECT)

        #
        #TEXTO_CONTROLES = get_fuente(75).render("CONTROLES", True, "White")
        #CONTROLES_RECT = TEXTO_CONTROLES.get_rect(
        #    center=(int(ANCHO * 0.15), int(ALTO * 0.6))
        #)
        #SCREEN.blit(TEXTO_CONTROLES, CONTROLES_RECT)
        
        COLOR_FONDO = (128,128,128)
        TEXTO_DIFICULTAD = get_fuente(75).render("DIFICULTAD:", True, "White")
        CONTROLES_RECT = TEXTO_DIFICULTAD.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.3))
        )
        margen = 20  
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
        SCREEN.blit(TEXTO_DIFICULTAD, CONTROLES_RECT)
        
        #TEXTO_DIFICULTAD = get_fuente(75).render("DIFICULTAD", True, "White")
        #DIFICULTAD_RECT = TEXTO_DIFICULTAD.get_rect(
        #    center=(int(ANCHO * 0.15), int(ALTO * 0.3))
        #)
        #SCREEN.blit(TEXTO_DIFICULTAD, DIFICULTAD_RECT)

        COLOR_FONDO = (128, 128, 128)  
        TEXTO_SONIDO = get_fuente(75).render("SONIDO:", True, "White")
        CONTROLES_RECT = TEXTO_SONIDO.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.45))
        )
        margen = 20  
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
        SCREEN.blit(TEXTO_SONIDO, CONTROLES_RECT)
        
        #TEXTO_SONIDO = get_fuente(75).render("SONIDO", True, "White")
        #SONIDO_RECT = TEXTO_SONIDO.get_rect(
        #    center=(int(ANCHO * 0.15), int(ALTO * 0.45))
        #)
        #SCREEN.blit(TEXTO_SONIDO, SONIDO_RECT)

        control1_img = pygame.image.load("src/assets/images/control1.png")
        control1_img = pygame.transform.scale(control1_img, (300, 300))

        control2_img = pygame.image.load("src/assets/images/control2.png")
        control2_img = pygame.transform.scale(control2_img, (300, 300))

        SCREEN.blit(control1_img, (int(ANCHO * 0.3), int(ALTO * 0.4)))
        SCREEN.blit(control2_img, (int(ANCHO * 0.54), int(ALTO * 0.44)))

        FACIL = Boton(
            boton_surface,
            (int(ANCHO * 0.4), int(ALTO * 0.3)),
            "FACIL",
            get_fuente(75),
            "Black",
            "White",
        )
        
        NORMAL = Boton(
            boton_surface,
            (int(ANCHO * 0.6), int(ALTO * 0.3)),
            "NORMAL",
            get_fuente(75),
            "Black",
            "White",
        )

        DIFICIL = Boton(
            boton_surface,
            (int(ANCHO * 0.8), int(ALTO * 0.3)),
            "DIFICIL",
            get_fuente(75),
            "Black",
            "White",
        )

        SONIDO_ON = Boton(
            boton_surface,
            (int(ANCHO * 0.4), int(ALTO * 0.45)),
            "ON",
            get_fuente(75),
            "Black",
            "White",
        )

        SONIDO_OFF = Boton(
            boton_surface,
            (int(ANCHO * 0.6), int(ALTO * 0.45)),
            "OFF",
            get_fuente(75),
            "Black",
            "White",
        )

        OPCIONES_ATRAS = Boton(
            boton_surface,
            (int(ANCHO * 0.88), int(ALTO * 0.9)),
            "ATRAS",
            get_fuente(75),
            "Black",
            "White",
        )
        
        #JUGAR_ATRAS = Boton(
        #    boton_surface,
        #    (int(ANCHO * 4.7), int(ALTO * 3.2)),
        #    "ATRAS",
        #    get_fuente(75),
        #    "Black",
        #    "White",
        #)
        #RANKING_ATRAS = Boton(
        #    boton_surface,
        #    (int(ANCHO * 0.5), int(ALTO * 0.9)),
        #    "ATRAS",
        #    get_fuente(75),
        #    "Black",
        #    "White",
        #)

        for boton in [
            FACIL,
            NORMAL,
            DIFICIL,
            SONIDO_ON,
            SONIDO_OFF,
            OPCIONES_ATRAS,
            #JUGAR_ATRAS,
            #RANKING_ATRAS
        ]:
            boton.changeColor(OPCIONES_POS_MOUSE)
            boton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SONIDO_ON.checkForInput(OPCIONES_POS_MOUSE):
                    pygame.mixer.music.set_volume(0.5)
                if SONIDO_OFF.checkForInput(OPCIONES_POS_MOUSE):
                    pygame.mixer.music.set_volume(0)
                if OPCIONES_ATRAS.checkForInput(OPCIONES_POS_MOUSE):
                    menu_principal()
                #if JUGAR_ATRAS.checkForInput(OPCIONES_POS_MOUSE):
                #    menu_principal()
                #if RANKING_ATRAS.checkForInput(OPCIONES_POS_MOUSE):
                #    menu_principal()

        clock.tick(60)
        pygame.display.update()


def ranking():
    while True:
        SCREEN.fill("black")

        TEXTO_RANKING = get_fuente(45).render("VENTANA RANKING", True, "White")
        RANKING_RECT = TEXTO_RANKING.get_rect(center=(ANCHO // 2, 50))
        SCREEN.blit(TEXTO_RANKING, RANKING_RECT)
        SCREEN.blit(BG_RANKING, (0, 0))
        RANKING_POS_MOUSE = pygame.mouse.get_pos()

        RANKING_ATRAS = Boton(
            boton_surface,
            (ANCHO * 0.88, ALTO * 0.9),
            "ATRAS",
            get_fuente(75),
            "white",
            "Green",
        )

        RANKING_ATRAS.changeColor(RANKING_POS_MOUSE)
        RANKING_ATRAS.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RANKING_ATRAS.checkForInput(RANKING_POS_MOUSE):
                    menu_principal()
        clock.tick(60)
        pygame.display.update()


def menu_principal():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXTO = get_fuente(120).render("HEROES DEL BALON", True, "White")
        MENU_RECT = MENU_TEXTO.get_rect(center=(int(ANCHO * 0.5), 180))

        BOTON_JUGAR = Boton(
            boton_surface,
            (int(ANCHO * 0.5), int(ALTO * 0.5)),
            "JUGAR",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )
        BOTON_OPCIONES = Boton(
            boton_surface,
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 90)),
            "OPCIONES",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )

        BOTON_RANKING = Boton(
            boton_surface,
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 180)),
            "RANKING",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )

        BOTON_SALIR = Boton(
            boton_surface,
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 270)),
            "SALIR",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )

        SCREEN.blit(MENU_TEXTO, MENU_RECT)

        for boton in [BOTON_JUGAR, BOTON_OPCIONES, BOTON_RANKING, BOTON_SALIR]:
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
                if BOTON_RANKING.checkForInput(MENU_MOUSE_POS):
                    ranking()
                if BOTON_SALIR.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        clock.tick(60)
        pygame.display.update()


menu_principal()
