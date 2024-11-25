from controller.MenuViewControlador import MenuController
from controller.ReproductorMusica import ReproductorMusica

if __name__ == "__main__":
    # musica = ReproductorMusica()
    # musica.reproducir_soundtrack()
    # PONER LA MUSICA CUANDO ESTE EL JUEGO
    menu_principal = MenuController()
    menu_principal.main_loop()
