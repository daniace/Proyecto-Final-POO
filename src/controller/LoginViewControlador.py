import sys

import pygame

from settings import *
from view.LoginView import LoginView
from model.database.AbmUsuario import AbmUsuario
from .Controlador import Controlador
from model.database.Usuario import Usuario


class LoginController(Controlador):
    def __init__(self):
        super().__init__()
        self._view = LoginView(SCREEN)
        self.__texto_usuario = ""
        self.__Usuarios = Usuario()

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        from controller.MenuViewControlador import MenuController

        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.__texto_usuario = self.__texto_usuario[:-1]
                else:
                    self.__texto_usuario += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["atras"].checkForInput(mouse_pos):
                    menu_principal = MenuController()
                    menu_principal.main_loop()
                if botones["login"].checkForInput(mouse_pos):
                    abmusuario = AbmUsuario()
                    self.__Usuarios.set_nombre(self.__texto_usuario)
                    self.__jugar.set_nombre_usuario(self.__texto_usuario)
                    abmusuario.insertar(self.__Usuarios)
                    abmusuario.close()
        self._view.mostrar_texto_usuario(self.__texto_usuario)
        pygame.display.flip()
        clock.tick(60)
