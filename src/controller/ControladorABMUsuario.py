from model.ModeloABMUsuario import ModeloABMUsuarios
from view.ABMUsuarioView import VistaABMUsuarios


class ControladorABMUsuarios:
    def __init__(self):
        self.__modelo = ModeloABMUsuarios()
        self.__vista = VistaABMUsuarios()

        # Conectar callbacks
        self.__vista._conectar_eliminar_usuario(self.__eliminar_usuario)
        self.__vista._conectar_alta_usuario(self.__alta_usuario)
        self.__vista._conectar_modificar_usuario(self.__modificar_usuario)
        self.__vista.protocol("WM_DELETE_WINDOW", self.cerrar)

        # Cargar usuarios
        self.__cargar_usuarios()

    def get_vista(self):
        """Devuelve la vista."""
        return self.__vista

    def __cargar_usuarios(self):
        """Carga los usuarios en la vista."""
        usuarios = self.__modelo._obtener_usuarios()
        self.__vista._cargar_usuarios(usuarios)

    def __alta_usuario(self, nombre, password, admin, score):
        """Agrega un nuevo usuario."""
        self.__modelo._insertar_usuario(nombre, password, admin, score)
        self.__cargar_usuarios()

    def __modificar_usuario(self, id_usuario, nombre, password, admin, score):
        """Modifica un usuario existente."""
        self.__modelo._actualizar_usuario(id_usuario, nombre, password, admin, score)
        self.__cargar_usuarios()

    def __eliminar_usuario(self, id_usuario):
        """Elimina un usuario."""
        self.__modelo._eliminar_usuario(id_usuario)
        self.__cargar_usuarios()

    def iniciar(self):
        """Inicia la vista."""
        self.__vista.iniciar()

    def cerrar(self):
        self.__vista.withdraw()

    def focus(self):
        self.__vista.focus()


if __name__ == "__main__":
    controlador = ControladorABMUsuarios()
    controlador.iniciar()
