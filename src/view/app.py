import sys

import pygame

from Boton import *
from settings import *

# pygame setup
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load(SONIDO_FONDO)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# dificultadd = dificultad()


def dibujar_formaciones(SCREEN, formaciones, formacion_actual):
    CARTA_IMAGEN = pygame.image.load(IMAGEN_CARTA)
    CARTA_IMAGEN = pygame.transform.scale(CARTA_IMAGEN, (80, 120))

    for posicion in POSICIONES:
        for cordenadas in formaciones[formacion_actual][posicion]:
            x = int(ANCHO * cordenadas[0])
            y = int(ALTO * cordenadas[1])
            SCREEN.blit(CARTA_IMAGEN, (x, y))


def texto_formacion(formacion_actual):
    COLOR_FONDO = (128, 128, 128)
    TEXTO_FORMACION = get_fuente(75).render(
        f"FORMACION {formacion_actual}", True, "White"
    )
    FORMACION_RECT = TEXTO_FORMACION.get_rect(
        center=(int(ANCHO * 0.5), int(ALTO * 0.08))
    )
    margen = 9
    fondo_rect = FORMACION_RECT.inflate(margen * 2, margen * 2)
    pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
    SCREEN.blit(TEXTO_FORMACION, FORMACION_RECT)


def jugar():
    comienza_partida = False
    formacion_actual = FORMACION_PREDETERMINADA
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
        dibujar_formaciones(SCREEN, FORMACIONES, formacion_actual)
        texto_formacion(formacion_actual)

        #  -------------
        # ------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DADO.checkForInput(JUGAR_POS_MOUSE):
                    comienza_partida = True
                elif comienza_partida:
                    if JUGAR_COMIENZA.checkForInput(JUGAR_POS_MOUSE):
                        cancha()
                elif JUGAR_ATRAS.checkForInput(JUGAR_POS_MOUSE):
                    menu_principal()
                elif CAMBIAR_FORMACION_ATRAS.checkForInput(
                    JUGAR_POS_MOUSE
                ) or CAMBIAR_FORMACION_ADELANTE.checkForInput(JUGAR_POS_MOUSE):
                    if formacion_actual == "4-4-2":
                        formacion_actual = "4-3-3"
                        texto_formacion(formacion_actual)
                    else:
                        formacion_actual = "4-4-2"
                        texto_formacion(formacion_actual)

        clock.tick(FPS)
        pygame.display.update()


def cancha():
    while True:
        SCREEN.fill(NEGRO)
        SCREEN.blit(BG_CANCHA_OFICIAL, (0, 0))

        CANCHA_ATRAS = Boton(
            boton_rojo_cuadrado,
            (ANCHO * 0.035, ALTO * 0.065),
            "🔙",
            pygame.font.Font(EMOJIS, 75),
            BLANCO,
            ROJO,
        )
        CANCHA_ATRAS.changeColor(pygame.mouse.get_pos())
        CANCHA_ATRAS.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CANCHA_ATRAS.checkForInput(pygame.mouse.get_pos()):
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
        COLOR_FONDO = (40, 40, 40)
        TEXTO_CONTROLES = get_fuente(75).render("CONTROLES:", True, "White")
        CONTROLES_RECT = TEXTO_CONTROLES.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.62))
        )
        margen = 10
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
        SCREEN.blit(TEXTO_CONTROLES, CONTROLES_RECT)

        COLOR_FONDO = (40, 40, 40)
        TEXTO_DIFICULTAD = get_fuente(75).render("DIFICULTAD:", True, "White")
        CONTROLES_RECT = TEXTO_DIFICULTAD.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.3))
        )
        margen = 10
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
        SCREEN.blit(TEXTO_DIFICULTAD, CONTROLES_RECT)

        COLOR_FONDO = (40, 40, 40)
        TEXTO_SONIDO = get_fuente(75).render("SONIDO:", True, "White")
        CONTROLES_RECT = TEXTO_SONIDO.get_rect(
            center=(int(ANCHO * 0.15), int(ALTO * 0.45))
        )
        margen = 10
        fondo_rect = CONTROLES_RECT.inflate(margen * 2, margen * 2)
        pygame.draw.rect(SCREEN, COLOR_FONDO, fondo_rect, border_radius=15)
        SCREEN.blit(TEXTO_SONIDO, CONTROLES_RECT)

        control1_img = pygame.image.load("src/assets/images/control1.png")
        control1_img = pygame.transform.scale(control1_img, (300, 300))

        control2_img = pygame.image.load("src/assets/images/control2.png")
        control2_img = pygame.transform.scale(control2_img, (300, 300))

        SCREEN.blit(control1_img, (int(ANCHO * 0.38), int(ALTO * 0.42)))
        SCREEN.blit(control2_img, (int(ANCHO * 0.59), int(ALTO * 0.42)))

        FACIL = Boton(
            boton_verde,
            (int(ANCHO * 0.4), int(ALTO * 0.3)),
            "FACIL",
            get_fuente(75),
            "White",
            "Green",
        )

        NORMAL = Boton(
            boton_amarillo,
            (int(ANCHO * 0.6), int(ALTO * 0.3)),
            "NORMAL",
            get_fuente(75),
            "White",
            "Yellow",
        )

        DIFICIL = Boton(
            boton_rojo,
            (int(ANCHO * 0.8), int(ALTO * 0.3)),
            "DIFICIL",
            get_fuente(75),
            BLANCO,
            ROJO,
        )

        SONIDO_ON = Boton(
            boton_negro,
            (int(ANCHO * 0.50), int(ALTO * 0.44)),
            "ON",
            get_fuente(75),
            "White",
            "Green",
        )

        SONIDO_OFF = Boton(
            boton_negro,
            (int(ANCHO * 0.70), int(ALTO * 0.44)),
            "OFF",
            get_fuente(75),
            "White",
            "Red",
        )

        OPCIONES_ATRAS = Boton(
            boton_rojo_cuadrado,
            (int(ANCHO * 0.95), int(ALTO * 0.9)),
            "🔙",
            pygame.font.Font(EMOJIS, 75),
            "White",
            "Red",
        )

        for boton in [FACIL, NORMAL, DIFICIL, SONIDO_ON, SONIDO_OFF, OPCIONES_ATRAS]:
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
                if DIFICIL.checkForInput(OPCIONES_POS_MOUSE):
                    pass
                    # dificultadd.dificil()
                if FACIL.checkForInput(OPCIONES_POS_MOUSE):
                    pass
                    # dificultadd.facil()
        clock.tick(60)
        pygame.display.update()


def actualizar_ranking(usuarios):
    for i, usuario in enumerate(usuarios):
        texto = f"{i + 1}. {usuario.get_nombre()} - {usuario.get_score()}"
        texto_usuario = get_fuente(72).render(texto, True, NEGRO)
        SCREEN.blit(texto_usuario, (ANCHO // 2 - 120, 170 + i * 50))
    TEXTO_TABLA = get_fuente(50).render("USUARIO - PUNTUACION", True, NEGRO)
    TEXTO_TABLA_RECT = TEXTO_TABLA.get_rect(center=(int(ANCHO * 0.52), int(ALTO * 0.2)))
    SCREEN.blit(TEXTO_TABLA, TEXTO_TABLA_RECT)


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
        actualizar_ranking(usuarios)

        RANKING_ACTUALIZAR = Boton(
            boton_cuadrado,
            (ANCHO * 0.73, ALTO * 0.9),
            "🔄",
            pygame.font.FontType(EMOJIS, 50),
            BLANCO,
            VERDE,
        )

        RANKING_ACTUALIZAR.changeColor(RANKING_POS_MOUSE)
        RANKING_ACTUALIZAR.update(SCREEN)

        RANKING_ATRAS = Boton(
            boton_rojo,
            (ANCHO * 0.88, ALTO * 0.9),
            "ATRAS",
            get_fuente(75),
            BLANCO,
            ROJO,
        )

        RANKING_ATRAS.changeColor(RANKING_POS_MOUSE)
        RANKING_ATRAS.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RANKING_ACTUALIZAR.checkForInput(RANKING_POS_MOUSE):
                    usuarios_actualizado = abmusuario.get_all()
                    actualizar_ranking(usuarios_actualizado)
                if RANKING_ATRAS.checkForInput(RANKING_POS_MOUSE):
                    menu_principal()
        clock.tick(60)
        pygame.display.update()


def mostrar_boton(
    self, texto, posicion, fuente, tamanio_fuente, mouse_pos, boton_rojo=False
):
    if fuente is None:
        fuente = get_fuente(tamanio_fuente)
    boton = Boton(
        boton_rojo if boton_rojo else boton_surface,
        posicion,
        texto,
        pygame.font.Font(EMOJIS, tamanio_fuente) if texto == "👤" else fuente,
        BLANCO,
        NEGRO,
    )
    boton.changeColor(mouse_pos)
    boton.update(self.pantalla)


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
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 180)),
            "OPCIONES",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )

        BOTON_RANKING = Boton(
            boton_surface,
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 90)),
            "RANKING",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )

        BOTON_SALIR = Boton(
            boton_rojo,
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 270)),
            "SALIR",
            get_fuente(75),
            BLANCO,
            ROJO,
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
                if BOTON_LOGIN.checkForInput(MENU_MOUSE_POS):
                    login()
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


def login():
    texto_usuario = ""
    while True:
        SCREEN.blit(BG, (0, 0))
        IMAGEN_TABLA = pygame.image.load("src/assets/images/tabla.png")
        IMAGEN_TABLA = pygame.transform.scale(IMAGEN_TABLA, (650, 340))
        SCREEN.blit(IMAGEN_TABLA, (int(ANCHO * 0.25), int(ALTO * 0.3)))

        LOGIN = Boton(
            boton_surface,
            (int(ANCHO * 0.5), int(ALTO * 0.5 + 90)),
            "LOGIN",
            get_fuente(75),
            BLANCO,
            NEGRO,
        )

        LOGIN_ATRAS = Boton(
            boton_rojo_cuadrado,
            (ANCHO * 0.045, ALTO * 0.09),
            "🔙",
            pygame.font.Font(EMOJIS, 75),
            BLANCO,
            ROJO,
        )

        for boton in [LOGIN, LOGIN_ATRAS]:
            boton.changeColor(pygame.mouse.get_pos())
            boton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    texto_usuario = texto_usuario[:-1]
                else:
                    texto_usuario += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LOGIN_ATRAS.checkForInput(pygame.mouse.get_pos()):
                    menu_principal()
                if LOGIN.checkForInput(pygame.mouse.get_pos()):
                    usuario.set_nombre(texto_usuario)
                    abmusuario.insertar(usuario)
                    menu_principal()
        superficie_texto = get_fuente(50).render(texto_usuario, True, NEGRO)
        SCREEN.blit(superficie_texto, (int(ANCHO * 0.4), int(ALTO * 0.5)))
        pygame.display.flip()
        clock.tick(60)
