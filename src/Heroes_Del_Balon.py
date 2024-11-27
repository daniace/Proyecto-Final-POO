from controller.MenuViewControlador import MenuController
from controller.ReproductorMusica import ReproductorMusica
from settings import SONIDO_FONDO

if __name__ == "__main__":
    # reproductor = ReproductorMusica()
    # reproductor.cargar_musica(SONIDO_FONDO)
    # reproductor.reproducir()
    menu_principal = MenuController()
    menu_principal.main_loop()
