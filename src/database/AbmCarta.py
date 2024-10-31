from DaoInterfaz import DaoInterfaz
from Singleton import Database


class AbmCarta(DaoInterfaz):
    def __init__(self):
        self.__database = (
            Database()
        )  # Aca se hace la conexion a la base de datos mediante singleton

    def get_por_id(self, id):  # obtiene una carta por su id
        self.__database.query("SELECT * FROM cartas WHERE id = ?", (id,))
        return self.__database.fetchone()

    def get_all(self):  # obtiene todas las cartas
        self.__database.query("SELECT * FROM cartas")
        return self.__database.fetchall()

    def insertar(self, objeto):  # inserta una nueva carta
        self.__database.query(
            "INSERT INTO carta (short_name,team_jersey_number,player_positions,club_name,nationality,overall,pace,shooting,passing,dribbling,defending,physical) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                objeto.get_nombre(),
                objeto.get_dorsal(),
                objeto.get_posicion(),
                objeto.get_club(),
                objeto.get_nacionalidad(),
                objeto.get_quimica(),
                objeto.get_velocidad(),
                objeto.get_disparo(),
                objeto.get_pase(),
                objeto.get_gambeta(),
                objeto.get_defensa(),
                objeto.get_fisico(),
            ),
        )
        self.__database.commit()

    def actualizar(self, objeto):  # actualiza las estadisticas de una carta
        self.__database.query(
            "UPDATE INTO carta SET overall=?, pace=?, shooting=?,passing=?,dribbling=?,physical=? WHERE sofifa_id=?",
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
        self.__database.commit()

    def borrar(self, id):  # Borrado logico de una carta
        self.__database.query(
            "UPDATE FROM cartas SET deshabilitado = 1 WHERE id = ?", (id,)
        )
        self.__database.commit()

    def cerrar(self):
        self.__database.close()
