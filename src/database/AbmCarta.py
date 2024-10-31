from DaoInterfaz import DaoInterfaz
from Singleton import Database


class AbmCarta(DaoInterfaz):
    def __init__(self):
        self.__database = (
            Database()
        )  # Aca se hace la conexion a la base de datos mediante singleton
        self.__database.connect()

    def get_por_id(self, id):  # obtiene una carta por su id
        resultado = self.__database.execute_query(
            "SELECT * FROM carta WHERE id_carta = ? AND deshabilitado = 0", (id,)
        )
        return (
            resultado[0]
            if resultado
            else print(f"No se encontro la carta con ese id: {id}")
        )  # Devuelve el primer elemento de la lista si hay resultados, sino None

    def get_all(self):  # obtiene todas las cartas
        self.__database.execute_query("SELECT * FROM carta WHERE deshabilitado = 0")

    def insertar(self, objeto):  # inserta una nueva carta
        self.__database.execute_non_query(
            "INSERT INTO carta (id_carta,short_name,nationality,club_name,overall,player_positions,team_jersey_number,pace,shooting,passing,dribbling,defending,physic) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                objeto.get_id(),
                objeto.get_nombre(),
                objeto.get_nacionalidad(),
                objeto.get_club(),
                objeto.get_quimica(),
                objeto.get_posicion(),
                objeto.get_dorsal(),
                objeto.get_velocidad(),
                objeto.get_disparo(),
                objeto.get_pase(),
                objeto.get_gambeta(),
                objeto.get_defensa(),
                objeto.get_fisico(),
            ),
        )

    def actualizar(self, objeto):  # actualiza las estadisticas de una carta
        self.__database.execute_non_query(
            "UPDATE carta SET overall = ?,pace = ?,shooting = ?,passing = ?,dribbling = ?,physic = ? WHERE id_carta = ?",
            (
                objeto.get_quimica(),
                objeto.get_velocidad(),
                objeto.get_disparo(),
                objeto.get_pase(),
                objeto.get_gambeta(),
                objeto.get_defensa(),
                objeto.get_fisico(),
                objeto.get_id(),
            ),
        )

    def borrar(self, id):  # Borrado logico de una carta
        self.__database.execute_non_query(
            "UPDATE carta SET deshabilitado = 1 WHERE id_carta = ? AND deshabilitado = 0",
            (id,),
        )

    def alta(self, id):
        self.__database.execute_non_query(
            "UPDATE carta SET deshabilitado = 0 WHERE id_carta = ? AND deshabilitado = 1",
            (id,),
        )
