import sys
import pygame as pg
from controller.MenuViewControlador import MenuController
from view.MenuView import MenuView
from settings import ANCHO, ALTO

if __name__ == "__main__":
    menu_principal = MenuController()
    menu_principal.main_loop()
