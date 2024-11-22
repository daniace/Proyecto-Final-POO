import sys

import pygame

from .Controlador import Controlador
from settings import *
from view.LoginView import LoginView


class LoginController(Controlador):
    def __init__(self):
        super().__init__()
        self._view = LoginView(pygame.display.set_mode((ANCHO, ALTO)))

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        from controller.MenuViewControlador import MenuController

        for event in eventos:
            from controller.MenuViewControlador import MenuController

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    texto_usuario = texto_usuario[:-1]
                else:
                    texto_usuario += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0].checkForInput(mouse_pos):
                    menu_principal = MenuController()
                    menu_principal.main_loop()
                if botones[1].checkForInput(mouse_pos):
                    usuario.set_nombre(texto_usuario)
                    abmusuario.insertar(usuario)
        pygame.display.flip()
        clock.tick(60)
