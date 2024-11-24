import sys

import pygame

from settings import *
from view.CanchaView import CanchaView
from model.logic.Partido import Partido
from model.logic.Dificultades import *
from model.logic.EquipoLogico import EquipoLogico
from .Controlador import Controlador


class CanchaController(Controlador):
    def __init__(self, pantalla,dificultad:Dificultad,jugador:EquipoLogico):
        super().__init__()
        self._view = CanchaView(pantalla)
        self._dificultad=dificultad
        self._jugador=jugador
        self._partido=Partido(jugador,dificultad)
        self._indice_seleccionado = 0
        

    
        
    def manejar_eventos(self, eventos, mouse_pos):
        from controller.JugarViewControlador import JugarController

        botones = self._view.get_botones()
        # print(len(botones))
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["atras"].checkForInput(mouse_pos):
                    menu_jugar = JugarController(self._dificultad)
                    menu_jugar.main_loop()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._indice_seleccionado = (self._indice_seleccionado - 1) % len(botones)
                    self.actualizar_seleccion()
                elif event.key == pygame.K_DOWN:
                    self._indice_seleccionado = (self._indice_seleccionado + 1) % len(botones)
                    self.actualizar_seleccion()
                elif event.key == pygame.K_RETURN:
                    self.ejecutar_accion()

    def actualizar_seleccion(self):
        botones = self._view.get_botones()
        for indice, (nombre_boton, boton) in enumerate(botones.items()):
            if indice == self._indice_seleccionado:
                boton.seleccionar()
                print('boton seleccionado -> ',nombre_boton)
            else:
                boton.deseleccionar()

               

    
    def ejecutar_accion(self):
        botones = self._view.get_botones()
        nombre_boton_seleccionado = list(botones.keys())[self._indice_seleccionado]
        
        if nombre_boton_seleccionado == "atras":
            from controller.JugarViewControlador import JugarController
            menu_jugar = JugarController(self._dificultad)
            menu_jugar.main_loop()
        elif nombre_boton_seleccionado == "pase":
            print('hizo pasee')
        elif nombre_boton_seleccionado == "tiro":
           print('hizo tiro')
        elif nombre_boton_seleccionado == "gambeta":
            print('hizo gambeta')
        elif nombre_boton_seleccionado == "interceptar":
            print('hizo interceptar')
            
    'no se si estos metodos van aca pero para probar'