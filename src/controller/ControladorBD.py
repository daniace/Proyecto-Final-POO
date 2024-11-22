from model.database.AbmEquipo import AbmEquipo
from model.database.AbmCarta import AbmCarta
from model.database.AbmUsuario import AbmUsuario


class ControladorBD:
    def __init__(self):
        self.__abmEquipo = AbmEquipo()
        self.__abmCarta = AbmCarta()
        self.__usuario = AbmUsuario()

    def get_usuarios_ranking(self):
        usuarios = self.__usuario.get_all()
        return usuarios
