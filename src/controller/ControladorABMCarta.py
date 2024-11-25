# controlador_abm_cartas.py
from model.ModeloCarta import ModeloCartas
from view.ABMCartaView import VistaABMCartas


class ControladorABMCartas:
    def __init__(self):
        self.modelo = ModeloCartas()
        self.vista = VistaABMCartas()

        # Conectar eventos de la vista a métodos del controlador
        self.vista.conectar_alta_carta(self.alta_carta)
        self.vista.conectar_modificar_carta(self.modificar_carta)
        self.vista.conectar_eliminar_carta(self.eliminar_carta)
        self.vista.conectar_alta_arquero(self.alta_arquero)
        self.vista.conectar_modificar_arquero(self.modificar_arquero)

    def iniciar(self):
        """Inicia la vista."""
        self.actualizar_tabla()
        self.vista.iniciar()

    def cerrar(self):
        """Cierra la vista."""
        self.vista.cerrar()

    def actualizar_tabla(self):
        """Actualiza los datos de la tabla."""
        cartas = self.modelo.obtener_cartas()
        self.vista.cargar_cartas(cartas)

    def alta_carta(self, *datos):
        """Llama al modelo para insertar una nueva carta."""
        self.modelo.insertar_carta(*datos)
        self.actualizar_tabla()

    def alta_arquero(self, *datos):
        """Llama al modelo para insertar un nuevo arquero."""
        self.modelo.insertar_arquero(*datos)
        self.actualizar_tabla()

    def modificar_carta(self, id_carta, *datos):
        """Llama al modelo para modificar una carta existente."""
        self.modelo.actualizar_carta(id_carta, *datos)
        self.actualizar_tabla()

    def modificar_arquero(self, id_carta, *datos):
        """Llama al modelo para modificar un arquero existente."""
        self.modelo.actualizar_arquero(id_carta, *datos)
        self.actualizar_tabla()

    def eliminar_carta(self, id_carta):
        """Llama al modelo para eliminar (deshabilitar) una carta."""
        self.modelo.eliminar_carta(id_carta)
        self.actualizar_tabla()


if __name__ == "__main__":
    controlador = ControladorABMCartas()
    controlador.iniciar()
