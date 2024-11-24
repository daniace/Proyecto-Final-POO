from model.database.AbmEquipo import AbmEquipo
from model.database.AbmCarta import AbmCarta
from model.database.AbmUsuario import AbmUsuario


class ControladorBD:
    def __init__(self):
        self.__abmEquipo = AbmEquipo()
        self.__abmCarta = AbmCarta()
        self.__usuario = AbmUsuario()

    def get_usuarios_ranking(self):
        self.__generador = AbmUsuario()
        usuarios = self.__generador.get_all()
        self.__generador.close()
        return usuarios
