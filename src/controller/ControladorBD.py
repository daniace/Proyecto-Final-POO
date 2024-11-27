from model.database.AbmCarta import AbmCarta
from model.database.AbmEquipo import AbmEquipo
from model.database.AbmUsuario import AbmUsuario


class ControladorBD:
    def get_usuarios_ranking(self):
        self.__generador = AbmUsuario()
        usuarios = self.__generador.get_all()  # Trae una lista de Usuarios
        self.__generador.close()
        return usuarios

    def get_usuarios(self, nombre):
        self.__generador = AbmUsuario()
        usuario = self.__generador.get_por_usuario(nombre)  # Trae una lista de Usuarios
        self.__generador.close()
        return usuario
