from tkinter import TclError

from controller.ControladorABMCarta import ControladorABMCartas
from controller.ControladorABMEquipo import ControladorABMEquipo
from controller.ControladorABMUsuario import ControladorABMUsuarios
from view.MenuABMView import MenuABM


class ControladorMenuABM:
    def __init__(self):
        self.__vista = MenuABM()
        self.__vista._conectar_abm_usuarios(self.__abrir_abm_usuarios)
        self.__vista._conectar_abm_equipos(self.__abrir_abm_equipos)
        self.__vista._conectar_abm_cartas(self.__abrir_abm_cartas)
        self.__ventana_abm_usuarios = None
        self.__ventana_abm_equipo = None
        self.__ventana_abm_carta = None

    def __abrir_abm_cartas(self):
        if (
            self.__ventana_abm_carta is None
            or not self.__ventana_abm_carta.get_vista().winfo_exists()
        ):
            self.__ventana_abm_carta = ControladorABMCartas()
            self.__ventana_abm_carta.iniciar()
        else:
            try:
                if self.__ventana_abm_carta.get_vista().winfo_exists():
                    self.__ventana_abm_carta.focus()
                else:
                    self.__ventana_abm_carta = ControladorABMCartas()
                    self.__ventana_abm_carta.iniciar()
            except TclError:
                self.__ventana_abm_carta = ControladorABMCartas()
                self.__ventana_abm_carta.iniciar()

    def __abrir_abm_equipos(self):
        if (
            self.__ventana_abm_equipo is None
            or not self.__ventana_abm_equipo.get_vista().winfo_exists()
        ):
            self.__ventana_abm_equipo = ControladorABMEquipo()
            self.__ventana_abm_equipo.iniciar()
        else:
            self.__ventana_abm_equipo.focus()

    def __abrir_abm_usuarios(self):
        if (
            self.__ventana_abm_usuarios is None
            or not self.__ventana_abm_usuarios.get_vista().winfo_exists()
        ):
            self.__ventana_abm_usuarios = ControladorABMUsuarios()
            self.__ventana_abm_usuarios.iniciar()
        else:
            self.__ventana_abm_usuarios.focus()

    def run(self):
        self.__vista.iniciar()

    def close(self):
        self.__vista.destroy()
