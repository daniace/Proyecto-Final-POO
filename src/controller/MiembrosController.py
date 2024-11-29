from settings import *
from view.MiembrosView import MiembrosView
from .Controlador import Controlador


class MiembrosController(Controlador):
    def __init__(self):
        self._view = MiembrosView(SCREEN)

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["atras"].checkForInput(mouse_pos):
                    from .MenuViewControlador import MenuController

                    menu = MenuController()
                    self._view.ocultar_visibilidad()
                    menu.main_loop()

    def main_loop(self):
        self._view.gif()
        self._view.fotos_integrantes()
        return super().main_loop()
