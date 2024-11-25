import pygame
import sys
from settings import *
from view.LoginJugarView import LoginJugarView
from .Controlador import Controlador
from model.database.AbmUsuario import AbmUsuario
from model.database.Usuario import Usuario


class LoginJugarViewControlador(Controlador):
    def __init__(self, pantalla, jugar):
        self.__jugar = jugar
        self._view = LoginJugarView(pantalla)
        self.__texto_usuario = ""
        self.__usuarioIngresado = False
        self.__Ingresado = False
        self.__Usuario = Usuario()

    def manejar_eventos(self, eventos, mouse_pos):
        boton = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not self.__Ingresado:
                    self.__usuarioIngresado = True
                    if event.key == pygame.K_BACKSPACE:
                        self.__texto_usuario = self.__texto_usuario[:-1]
                    else:
                        self.__texto_usuario += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton["volver_atras"].checkForInput(mouse_pos):
                    if self.__Ingresado:
                        self._view.ocultar_visibilidad()
                        self.__jugar.main_loop()
                    else:
                        self._view.set_no_ingresado(True)

                if boton["aceptar"].checkForInput(mouse_pos):
                    if self.__usuarioIngresado:
                        abmusuario = AbmUsuario()
                        self.__jugar.set_usuario_ingresado()
                        self.__Usuario.set_nombre(self.__texto_usuario)
                        self.__jugar.set_nombre_usuario(self.__texto_usuario)
                        abmusuario.insertar(self.__Usuario)
                        abmusuario.close()
                        self._view.set_no_ingresado(False)
                        self.__texto_usuario = ""
                        self._view.set_ingresado(True)
                        self.__Ingresado = True
        self._view.mostrar_texto_usuario(self.__texto_usuario)

    def main_loop(self):
        self._view.renderizar()
        super().main_loop()
