import sys
import pygame as pg
from controller.MenuViewControlador import MenuController

if __name__ == "__main__":
    menu_principal = MenuController()
    menu_principal.main_loop()
