import sys
import pygame
from settings import *
from view.CanchaView import CanchaView
from model.logic.Partido import Partido
from model.logic.Dificultades import *
from model.logic.EquipoLogico import EquipoLogico
from .Controlador import Controlador

class CanchaController(Controlador):
    def __init__(self, pantalla, dificultad: Dificultad, jugador: EquipoLogico):
        super().__init__()
        self._view = CanchaView(pantalla)
        self._dificultad = dificultad
        self._jugador = jugador
        self._partido = Partido(jugador, dificultad)
        self._indice_seleccionado = 0
        self.boton_actual = None
        self.boton_mouse = None  
    
    def cambiar_boton_actual (self):
        botones = self._view.get_botones()
        for boton in botones.values():
                if boton.hovering:
                    self.boton_actual = boton
                elif boton.seleccionado:
                    self.boton_actual = boton
    
    
    def main_loop(self):
        while True:
            if self._view.get_visibilidad():
                mouse_pos = pygame.mouse.get_pos()
                self._view.mostrar()  # Mostrar el menú
                eventos = pygame.event.get()  # Manejar eventos
                self.manejar_eventos(eventos, mouse_pos)

                # self.cambiar_boton_actual()
                if self.boton_actual is not None:
                    self.boton_actual.mantener_color()
                    self.boton_actual.update(self._view._pantalla)
                        
                clock.tick(60)
                pygame.display.update()

    def manejar_eventos(self, eventos, mouse_pos):
        from controller.JugarViewControlador import JugarController

        botones = self._view.get_botones()

        for event in eventos:

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["atras"].checkForInput(mouse_pos):
                    self.actualizar_seleccion()
                    menu_jugar = JugarController()
                    menu_jugar.main_loop()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self._indice_seleccionado = (self._indice_seleccionado - 1) % len(botones)
                    self.actualizar_seleccion()
                elif event.key == pygame.K_UP:
                    self._indice_seleccionado = (self._indice_seleccionado + 1) % len(botones)
                    self.actualizar_seleccion()
                elif event.key == pygame.K_RETURN:
                    self.ejecutar_accion()

    def actualizar_seleccion(self):
        botones = self._view.get_botones()
        for indice, (nombre_boton, boton) in enumerate(botones.items()):
            if indice == self._indice_seleccionado:
                boton.seleccionar()
                self.cambiar_boton_actual()
            else:
                boton.deseleccionar()


    def ejecutar_accion(self):
        botones = self._view.get_botones()
        nombre_boton_seleccionado = list(botones.keys())[self._indice_seleccionado]
        
        if nombre_boton_seleccionado == "atras":
            from controller.JugarViewControlador import JugarController
            menu_jugar = JugarController()
            menu_jugar.main_loop()
        elif nombre_boton_seleccionado == "pase":
            print('hizo pasee')
        elif nombre_boton_seleccionado == "tiro":
           print('hizo tiro')
        elif nombre_boton_seleccionado == "gambeta":
            print('hizo gambeta')
        elif nombre_boton_seleccionado == "interceptar":
            print('hizo interceptar')