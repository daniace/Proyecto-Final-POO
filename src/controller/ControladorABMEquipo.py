from model.ModeloEquipo import ModeloEquipo
from view.ABMEquipoView import VistaABMEquipo


class ControladorABMEquipo:
    def __init__(self):
        self.modelo = ModeloEquipo()
        self.vista = VistaABMEquipo()

        # Conectar callbacks
        self.vista.conectar_eliminar_equipo(self.eliminar_equipo)
        self.vista.conectar_alta_equipo(self.alta_equipo)
        self.vista.conectar_modificar_equipo(self.modificar_equipo)

        # Cargar equipos
        self.cargar_equipos()

    def cargar_equipos(self):
        """Carga los equipos en la vista."""
        equipos = self.modelo.obtener_equipos()
        self.vista.cargar_equipos(equipos)

    def alta_equipo(self, nombre, password, admin, score):
        """Agrega un nuevo equipo."""
        self.modelo.insertar_equipo(nombre, password, admin, score)
        self.cargar_equipos()

    def modificar_equipo(self, id_equipo, nombre, password, admin, score):
        """Modifica un equipo existente."""
        self.modelo.actualizar_equipo(id_equipo, nombre, password, admin, score)
        self.cargar_equipos()

    def eliminar_equipo(self, id_equipo):
        """Elimina un equipo."""
        self.modelo.eliminar_equipo(id_equipo)
        self.cargar_equipos()

    def iniciar(self):
        self.vista.iniciar()

    def cerrar(self):
        self.vista.cerrar()
