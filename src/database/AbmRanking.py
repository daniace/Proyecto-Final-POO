from DaoInterfaz import DaoInterfaz
from Singleton import Database
from Ranking import Ranking


class AbmRanking(DaoInterfaz):
    def __init__(self):
        self.__database = Database()
        self.__database.connect

    def get_por_id(self, id):
        resultado = self.__database.execute_query(
            "SELECT * FROM ranking WHERE id_usuario ?",
            (id),  # Devuelve también los usuarios dados de baja
        )
        if not resultado:
            print(f"No hay score para el usuario: {id}")
        else:
            return Ranking(
                resultado[0][0], resultado[0][1]
            )  # Retorna 1 usuario y su score
    
    def get_all(self):
        usuarios = []
        resultado =