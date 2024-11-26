# controlador_abm_cartas.py
from model.ModeloABMCarta import ModeloABMCartas
from view.ABMCartaView import VistaABMCartas


class ControladorABMCartas:
    def __init__(self):
        self.__modelo = ModeloABMCartas()
        self.__vista = VistaABMCartas()

        # Conectar eventos de la vista a métodos del controlador
        self.__vista._conectar_alta_carta(self.__alta_carta)
        self.__vista._conectar_modificar_carta(self.__modificar_carta)
        self.__vista._conectar_eliminar_carta(self.__eliminar_carta)
        self.__vista._conectar_alta_arquero(self.__alta_arquero)
        self.__vista._conectar_modificar_arquero(self.__modificar_arquero)
        self.__vista.protocol("WM_DELETE_WINDOW", self.cerrar)

    def get_vista(self):
        """Devuelve la vista."""
        return self.__vista

    def iniciar(self):
        """Inicia la vista."""
        self.__actualizar_tabla()
        self.__vista.iniciar()

    def cerrar(self):
        """Cierra la vista."""
        self.__vista.withdraw()
        self.__vista = None

    def __actualizar_tabla(self):
        """Actualiza los datos de la tabla."""
        cartas = self.__modelo._obtener_cartas()
        self.__vista._cargar_cartas(cartas)

    def __alta_carta(self, *datos):
        """Llama al modelo para insertar una nueva carta."""
        self.__modelo._insertar_carta(*datos)
        self.__actualizar_tabla()

    def __alta_arquero(self, *datos):
        """Llama al modelo para insertar un nuevo arquero."""
        self.__modelo._insertar_arquero(*datos)
        self.__actualizar_tabla()

    def __modificar_carta(self, id_carta, *datos):
        """Llama al modelo para modificar una carta existente."""
        self.__modelo._actualizar_carta(id_carta, *datos)
        self.__actualizar_tabla()

    def __modificar_arquero(self, id_carta, *datos):
        """Llama al modelo para modificar un arquero existente."""
        self.__modelo._actualizar_arquero(id_carta, *datos)
        self.__actualizar_tabla()

    def __eliminar_carta(self, id_carta):
        """Llama al modelo para eliminar (deshabilitar) una carta."""
        self.__modelo._eliminar_carta(id_carta)
        self.__actualizar_tabla()

    def focus(self):
        """Trae la vista al frente."""
        self.__vista.focus()


if __name__ == "__main__":
    controlador = ControladorABMCartas()
    controlador.iniciar()
