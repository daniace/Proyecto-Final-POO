from DaoInterfaz import DaoInterfaz
from Singleton import Database
from Equipo import Equipo


class AbmEquipo(DaoInterfaz):
    def __init__(self):
        self.__database = Database()
        self.__database.connect

    def get_por_id(self, id):
        resultado = self.__database.execute_query(
            "SELECT * FROM equipo WHERE id_equipo = ? AND baja_equipo = 0", (id)
        )
        if not resultado:
            print(f"No se encontró el equipo con el id: {id}")
        else:
            return resultado[0]

    def get_all(self):
        equipos = []
        resultado = self.__database.execute_non_query(
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

    def insertar(self, objeto):
        self.__database.execute_non_query(
            "INSERT INTO equipo (idEquipo, nombreEquipo, idUsuario) VALUES (?,?,?)",
            (objeto.get_idEquipo(), objeto.get_nombre(), objeto.get_idUsuario()),
        )

    def actualizar(self, objeto):
        self.__database.execute_non_query(
            "UPDATE equipo SET nombreEquipo = ?, bajaEquipo = ? WHERE idEquipo = ?",
            (objeto.get_nombre(), objeto.get_bajaEquipo(), objeto.get_idEquipo()),
        )

    def borrar(self, id):
        self.__database.execute_non_query(
            "UPDATE equipo SET bajaEquipo = 1 WHERE idEquipo = ? AND bajaEquipo = 0",
            (id),
        )
