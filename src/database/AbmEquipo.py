from DaoInterfaz import DaoInterfaz
from Equipo import Equipo
from Singleton import Database


class AbmEquipo(DaoInterfaz):
    def __init__(self):
        self.__database = Database()
        self.__database.connect

    def get_por_id(self, id):  # FUNCIONA
        resultado = self.__database.execute_query(
            "SELECT * FROM equipo WHERE id_equipo = ? AND baja_equipo = 0", (id)
        )
        if not resultado:
            print(f"No se encontró el equipo con el id: {id}")
        else:
            return Equipo(
                resultado[0][0], resultado[0][1], resultado[0][2]
            )  # Retorna el equipo con sus 3 atributos

    def get_all(self):  # FUNCIONA
        equipos = []
        resultado = self.__database.execute_query(
            "SELECT * FROM equipo WHERE baja_equipo = 0"  # esta query devuelve en resultado una lista de los equipos
        )
        if resultado is None:
            print("No se encontraron equipos")
        else:
            for equipo in resultado:
                objeto = Equipo(
                    equipo[0], equipo[1], equipo[2]
                )  # creo un objeto Equipo para cada índice de la lista, con sus parámetros: 0, 1, 2
                equipos.append(objeto)
            return equipos

    def insertar(self, objeto):  # FUNCIONA
        self.__database.execute_non_query(
            "INSERT INTO equipo (id_equipo, id_usuario, nombre_equipo, id_carta1, id_carta2, id_carta3, id_carta4, id_carta6, id_carta7_, id_carta8, id_carta9, id_carta10, id_carta11) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (objeto.get_id_equipo(), objeto.get_nombre(), objeto.get_id_usuario()),
        )

    def actualizar(self, objeto):  # FUNCIONA
        self.__database.execute_non_query(
            "UPDATE equipo SET nombre_equipo = ?, baja_equipo = ? WHERE id_equipo = ?",
            (objeto.get_nombre(), objeto.get_baja_equipo(), objeto.get_id_equipo()),
        )

    def borrar(self, id):  # FUNCIONA
        self.__database.execute_non_query(
            "UPDATE equipo SET baja_equipo = 1 WHERE id_equipo = ? AND baja_equipo = 0",
            (id),
        )
