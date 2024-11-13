import sys

import pygame

from .Boton import *
from .settings import *

# pygame setup
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load(SONIDO_FONDO)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


def jugar():
    pygame.display.set_caption("JUGANDO")

    while True:
        JUGAR_POS_MOUSE = pygame.mouse.get_pos()
        SCREEN.fill(NEGRO)
        OFFSET = 40
        TEXTO_JUGAR = get_fuente(45).render("VENTANA JUGANDO", True, "White")
        JUGAR_RECT = TEXTO_JUGAR.get_rect(center=(ANCHO // 2, 50))
        SCREEN.blit(TEXTO_JUGAR, JUGAR_RECT)

        CANCHA_IMAGEN = pygame.image.load(IMAGEN_CANCHA)
        CANCHA_IMAGEN = pygame.transform.scale(CANCHA_IMAGEN, (ANCHO // 2, ALTO))
        SCREEN.blit(CANCHA_IMAGEN, (int(ANCHO * 0.25), 0))

        # Formacion 4-3-3
        CARTA_IMAGEN = pygame.image.load(IMAGEN_CARTA)
        CARTA_IMAGEN = pygame.transform.scale(CARTA_IMAGEN, (80, 120))
        DELANTERO1_RECT = CARTA_IMAGEN.get_rect(
            center=(int(ANCHO * 0.4), int(ALTO * 0.3))
        )
        DELANTERO2_RECT = CARTA_IMAGEN.get_rect(
            center=(int(ANCHO * 0.5), int(ALTO * 0.3))
        )
        DELANTERO3_RECT = CARTA_IMAGEN.get_rect(
            center=(int(ANCHO * 0.6), int(ALTO * 0.3))
        )
        MEDIOCAMPISTA1_RECT = CARTA_IMAGEN.get_rect(
            center=(int(ANCHO * 0.4), int(ALTO * 0.5))
        )
        MEDIOCAMPISTA2_RECT = CARTA_IMAGEN.get_rect(
            center=(int(ANCHO * 0.5), int(ALTO * 0.5))
        )
        MEDIOCAMPISTA3_RECT = CARTA_IMAGEN.get_rect(
            center=(int(ANCHO * 0.6), int(ALTO * 0.5))
        )
        DEFENSA1_RECT = CARTA_IMAGEN.get_rect(
            center=(int(ANCHO * 0.35), int(ALTO * 0.7))
        )
        DEFENSA2_RECT = CARTA_IMAGEN.get_rect(
            center=(int(ANCHO * 0.45), int(ALTO * 0.7))
        )
        DEFENSA3_RECT = CARTA_IMAGEN.get_rect(
            center=(int(ANCHO * 0.55), int(ALTO * 0.7))
        )
        DEFENSA4_RECT = CARTA_IMAGEN.get_rect(
            center=(int(ANCHO * 0.65), int(ALTO * 0.7))
        )
        PORTERO_RECT = CARTA_IMAGEN.get_rect(center=(int(ANCHO * 0.5), int(ALTO * 0.9)))
        NOMBRE_JUGADOR = get_fuente(20).render(defensores[0].get_str(), True, NEGRO)
        NOMBRE_DELANTERO1 = NOMBRE_JUGADOR.get_rect(center=DELANTERO1_RECT.center)
        NOMBRE_DELANTERO2 = NOMBRE_JUGADOR.get_rect(center=DELANTERO2_RECT.center)
        NOMBRE_DELANTERO3 = NOMBRE_JUGADOR.get_rect(center=DELANTERO3_RECT.center)
        NOMBRE_MEDIOCAMPISTA1 = NOMBRE_JUGADOR.get_rect(
            center=MEDIOCAMPISTA1_RECT.center
        )
        NOMBRE_MEDIOCAMPISTA2 = NOMBRE_JUGADOR.get_rect(
            center=MEDIOCAMPISTA2_RECT.center
        )
        NOMBRE_MEDIOCAMPISTA3 = NOMBRE_JUGADOR.get_rect(
            center=MEDIOCAMPISTA3_RECT.center
        )
        NOMBRE_DEFENSA1 = NOMBRE_JUGADOR.get_rect(center=DEFENSA1_RECT.center)
        NOMBRE_DEFENSA2 = NOMBRE_JUGADOR.get_rect(center=DEFENSA2_RECT.center)
        NOMBRE_DEFENSA3 = NOMBRE_JUGADOR.get_rect(center=DEFENSA3_RECT.center)
        NOMBRE_DEFENSA4 = NOMBRE_JUGADOR.get_rect(center=DEFENSA4_RECT.center)
        NOMBRE_PORTERO = NOMBRE_JUGADOR.get_rect(center=PORTERO_RECT.center)

        # Delanteros
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.4) - OFFSET, int(ALTO * 0.2)))
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.5) - OFFSET, int(ALTO * 0.2)))
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.6) - OFFSET, int(ALTO * 0.2)))
        # Mediocampistas
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.4) - OFFSET, int(ALTO * 0.4)))
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.5) - OFFSET, int(ALTO * 0.4)))
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.6) - OFFSET, int(ALTO * 0.4)))
        # Defensores
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.35) - OFFSET, int(ALTO * 0.6)))
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.45) - OFFSET, int(ALTO * 0.6)))
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.55) - OFFSET, int(ALTO * 0.6)))
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.65) - OFFSET, int(ALTO * 0.6)))
        # Portero
        SCREEN.blit(CARTA_IMAGEN, (int(ANCHO * 0.5) - OFFSET, int(ALTO * 0.8)))

        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_DELANTERO1)
        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_DELANTERO2)
        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_DELANTERO3)
        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_MEDIOCAMPISTA1)
        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_MEDIOCAMPISTA2)
        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_MEDIOCAMPISTA3)
        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_DEFENSA1)
        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_DEFENSA2)
        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_DEFENSA3)
        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_DEFENSA4)
        SCREEN.blit(NOMBRE_JUGADOR, NOMBRE_PORTERO)

        JUGAR_ATRAS = Boton(
            boton_surface,
            (ANCHO * 0.88, ALTO * 0.9),
            "ATRAS",
            get_fuente(75),
            "White",
            "Green",
        )
        JUGAR_ATRAS.changeColor(JUGAR_POS_MOUSE)
        JUGAR_ATRAS.update(SCREEN)
        # ------------
        COLOR_FONDO = (128, 128, 128)
        TEXTO_FORMACION = get_fuente(75).render("FORMACION 4-3-3", True, "White")
        FORMACION_RECT = TEXTO_FORMACION.get_rect(
            center=(int(ANCHO * 0.5), int(ALTO * 0.1))
        )
        margen = 20
        fondo_rect = FORMACION_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
        SCREEN.blit(TEXTO_FORMACION, FORMACION_RECT)
        # ------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # ESTE FOR SE TENDRA QUE IMPLEMENTAR EN EL CONTROLADOR
                # Y ACA SOLO LLAMAMOS A LA VARIABLE/FUNCION DE DICHO CONTROLADOR Y SUS PARAMETROS
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
        COLOR_FONDO = (128, 128, 128)
        TEXTO_CONTROLES = get_fuente(75).render("CONTROLES:", True, "White")
        CONTROLES_RECT = TEXTO_CONTROLES.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.6))
        )
        margen = 20
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
        SCREEN.blit(TEXTO_CONTROLES, CONTROLES_RECT)

        #
        # TEXTO_CONTROLES = get_fuente(75).render("CONTROLES", True, "White")
        # CONTROLES_RECT = TEXTO_CONTROLES.get_rect(
        #    center=(int(ANCHO * 0.15), int(ALTO * 0.6))
        # )
        # SCREEN.blit(TEXTO_CONTROLES, CONTROLES_RECT)

        COLOR_FONDO = (128, 128, 128)
        TEXTO_DIFICULTAD = get_fuente(75).render("DIFICULTAD:", True, "White")
        CONTROLES_RECT = TEXTO_DIFICULTAD.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.3))
        )
        margen = 20
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
        SCREEN.blit(TEXTO_DIFICULTAD, CONTROLES_RECT)

        # TEXTO_DIFICULTAD = get_fuente(75).render("DIFICULTAD", True, "White")
        # DIFICULTAD_RECT = TEXTO_DIFICULTAD.get_rect(
        #    center=(int(ANCHO * 0.15), int(ALTO * 0.3))
        # )
        # SCREEN.blit(TEXTO_DIFICULTAD, DIFICULTAD_RECT)

        COLOR_FONDO = (128, 128, 128)
        TEXTO_SONIDO = get_fuente(75).render("SONIDO:", True, "White")
        CONTROLES_RECT = TEXTO_SONIDO.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.45))
        )
        margen = 20
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
        SCREEN.blit(TEXTO_SONIDO, CONTROLES_RECT)

        # TEXTO_SONIDO = get_fuente(75).render("SONIDO", True, "White")
        # SONIDO_RECT = TEXTO_SONIDO.get_rect(
        #    center=(int(ANCHO * 0.15), int(ALTO * 0.45))
        # )
        # SCREEN.blit(TEXTO_SONIDO, SONIDO_RECT)

        control1_img = pygame.image.load("src/assets/images/control1.png")
        control1_img = pygame.transform.scale(control1_img, (300, 300))

        control2_img = pygame.image.load("src/assets/images/control2.png")
        control2_img = pygame.transform.scale(control2_img, (300, 300))

        SCREEN.blit(control1_img, (int(ANCHO * 0.3), int(ALTO * 0.4)))
        SCREEN.blit(control2_img, (int(ANCHO * 0.54), int(ALTO * 0.4)))

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

        # JUGAR_ATRAS = Boton(
        #    boton_surface,
        #    (int(ANCHO * 4.7), int(ALTO * 3.2)),
        #    "ATRAS",
        #    get_fuente(75),
        #    "Black",
        #    "White",
        # )
        # RANKING_ATRAS = Boton(
        #    boton_surface,
        #    (int(ANCHO * 0.5), int(ALTO * 0.9)),
        #    "ATRAS",
        #    get_fuente(75),
        #    "Black",
        #    "White",
        # )

        for boton in [
            FACIL,
            NORMAL,
            DIFICIL,
            SONIDO_ON,
            SONIDO_OFF,
            OPCIONES_ATRAS,
            # JUGAR_ATRAS,
            # RANKING_ATRAS
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
                # if JUGAR_ATRAS.checkForInput(OPCIONES_POS_MOUSE):
                #    menu_principal()
                # if RANKING_ATRAS.checkForInput(OPCIONES_POS_MOUSE):
                #    menu_principal()

        clock.tick(60)
        pygame.display.update()


def ranking():
    while True:
        SCREEN.fill("black")

        SCREEN.blit(BG_RANKING, (0, 0))
        RANKING_POS_MOUSE = pygame.mouse.get_pos()

        IMAGEN_RANKING_USUARIOS = pygame.image.load(IMAGEN_TABLA)
        IMAGEN_RANKING_USUARIOS = pygame.transform.scale(
            IMAGEN_RANKING_USUARIOS, (ANCHO // 3, ALTO - 100)
        )
        SCREEN.blit(IMAGEN_RANKING_USUARIOS, (int(ANCHO * 0.35), int(ALTO * 0.1)))

        for i, usuario in enumerate(usuarios):
            texto = f"{i + 1}. {usuario.get_nombre()} - {usuario.get_score()}"
            texto_usuario = get_fuente(72).render(texto, True, NEGRO)
            SCREEN.blit(texto_usuario, (ANCHO // 2 - 120, 170 + i * 50))

        TEXTO_TABLA = get_fuente(50).render("USUARIO - PUNTUACION", True, NEGRO)
        TEXTO_TABLA_RECT = TEXTO_TABLA.get_rect(
            center=(int(ANCHO * 0.52), int(ALTO * 0.2))
        )
        SCREEN.blit(TEXTO_TABLA, TEXTO_TABLA_RECT)

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

        BOTON_LOGIN = Boton(
            boton_cuadrado,
            (int(ANCHO * 0.1), int(ALTO * 0.1)),
            "👤",
            pygame.font.Font(EMOJIS, 50),
            BLANCO,
            NEGRO,
        )

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

        for boton in [
            BOTON_JUGAR,
            BOTON_OPCIONES,
            BOTON_RANKING,
            BOTON_SALIR,
            BOTON_LOGIN,
        ]:
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
