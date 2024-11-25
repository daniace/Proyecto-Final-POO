from model.ModeloUsuario import ModeloUsuarios
from view.ABMUsuarioView import VistaABMUsuarios


class ControladorABMUsuarios:
    def __init__(self):
        self.modelo = ModeloUsuarios()
        self.vista = VistaABMUsuarios()

        # Conectar callbacks
        self.vista.conectar_eliminar_usuario(self.eliminar_usuario)
        self.vista.conectar_alta_usuario(self.alta_usuario)
        self.vista.conectar_modificar_usuario(self.modificar_usuario)

        # Cargar usuarios
        self.cargar_usuarios()

    def cargar_usuarios(self):
        """Carga los usuarios en la vista."""
        usuarios = self.modelo.obtener_usuarios()
        self.vista.cargar_usuarios(usuarios)

    def alta_usuario(self, nombre, password, admin, score):
        """Agrega un nuevo usuario."""
        self.modelo.insertar_usuario(nombre, password, admin, score)
        self.cargar_usuarios()

    def modificar_usuario(self, id_usuario, nombre, password, admin, score):
        """Modifica un usuario existente."""
        self.modelo.actualizar_usuario(id_usuario, nombre, password, admin, score)
        self.cargar_usuarios()

    def eliminar_usuario(self, id_usuario):
        """Elimina un usuario."""
        self.modelo.eliminar_usuario(id_usuario)
        self.cargar_usuarios()

    def iniciar(self):
        """Inicia la vista."""
        self.vista.iniciar()

    def cerrar(self):
        self.vista.cerrar()


if __name__ == "__main__":
    controlador = ControladorABMUsuarios()
    controlador.iniciar()
