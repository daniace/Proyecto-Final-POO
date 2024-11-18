import sys

import pygame

from .Controlador import Controlador
from settings import *
from view.LoginView import LoginView


class LoginController(Controlador):
    def __init__(self):
        self._view = LoginView(pygame.display.set_mode((ANCHO, ALTO)))

    def manejar_eventos(self, eventos, mouse_pos):
        botones = 
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