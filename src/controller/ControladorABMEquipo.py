from model.ModeloABMEquipo import ModeloABMEquipo
from view.ABMEquipoView import VistaABMEquipo


class ControladorABMEquipo:
    def __init__(self):
        self.__modelo = ModeloABMEquipo()
        self.__vista = VistaABMEquipo()

        # Conectar callbacks
        self.__vista._conectar_eliminar_equipo(self.__eliminar_equipo)
        self.__vista._conectar_alta_equipo(self.__alta_equipo)
        self.__vista._conectar_modificar_equipo(self.__modificar_equipo)
        self.__vista.protocol("WM_DELETE_WINDOW", self.cerrar)

        # Cargar equipos
        self.__cargar_equipos()

    def get_vista(self):
        """Devuelve la vista."""
        return self.__vista

    def __cargar_equipos(self):
        """Carga los equipos en la vista."""
        equipos = self.__modelo._obtener_equipos()
        self.__vista._cargar_equipos(equipos)

    def __alta_equipo(
        self,
        nombre_equipo,
        carta1,
        carta2,
        carta3,
        carta4,
        carta5,
        carta6,
        carta7,
        carta8,
        carta9,
        carta10,
        carta11,
    ):
        """Agrega un nuevo equipo."""
        self.__modelo._insertar_equipo(
            nombre_equipo,
            carta1,
            carta2,
            carta3,
            carta4,
            carta5,
            carta6,
            carta7,
            carta8,
            carta9,
            carta10,
            carta11,
        )
        self.__cargar_equipos()

    def __modificar_equipo(
        self,
        id_equipo,
        nombre_equipo,
        carta1,
        carta2,
        carta3,
        carta4,
        carta5,
        carta6,
        carta7,
        carta8,
        carta9,
        carta10,
        carta11,
    ):
        """Modifica un equipo existente."""
        self.__modelo._actualizar_equipo(
            id_equipo,
            None,
            nombre_equipo,
            carta1,
            carta2,
            carta3,
            carta4,
            carta5,
            carta6,
            carta7,
            carta8,
            carta9,
            carta10,
            carta11,
        )
        self.__cargar_equipos()

    def __eliminar_equipo(self, id_equipo):
        """Elimina un equipo."""
        self.__modelo._eliminar_equipo(id_equipo)
        self.__cargar_equipos()

    def iniciar(self):
        self.__vista.iniciar()

    def cerrar(self):
        self.__vista.withdraw()

    def focus(self):
        self.__vista.focus()
