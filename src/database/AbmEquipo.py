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
            "SELECT * FROM equipo WHERE baja_equipo = 0"
        )
        if resultado is None:
            print("No se encontraron equipos")
        else:
            for equipo in equipos:
                objeto = Equipo()
