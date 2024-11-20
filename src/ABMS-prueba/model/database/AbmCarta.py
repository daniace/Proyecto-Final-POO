from model.database.Carta import Carta
from model.database.DaoInterfaz import DaoInterfaz
from model.database.Singleton import Database


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
        if not resultado:
            print(f"No se encontró la carta con el id: {id}")
        else:
            return Carta(
                resultado[0][0],
                resultado[0][1],
                resultado[0][2],
                resultado[0][3],
                resultado[0][4],
                resultado[0][5],
                resultado[0][6],
                resultado[0][7],
                resultado[0][8],
                resultado[0][9],
                resultado[0][10],
                resultado[0][11],
                resultado[0][12],
                resultado[0][13],
                resultado[0][14],
                resultado[0][15],
                resultado[0][16],
                resultado[0][17],
                resultado[0][18],
                resultado[0][19],
            )  # Devuelve el primer elemento de la lista si hay resultados, sino None

    def get_all(self):  # obtiene todas las cartas
        resultado = self.__database.execute_query(
            "SELECT * FROM carta WHERE deshabilitado = 0 LIMIT 50"
        )
        if not resultado:
            print("No se encontraron cartas")
        else:
            listajugadores = []
            for carta in resultado:
                objeto = Carta(
                    carta[0],
                    carta[1],
                    carta[2],
                    carta[3],
                    carta[4],
                    carta[5],
                    carta[6],
                    carta[7],
                    carta[8],
                    carta[9],
                    carta[10],
                    carta[11],
                    carta[12],
                    carta[13],
                    carta[14],
                    carta[15],
                    carta[16],
                    carta[17],
                    carta[18],
                    carta[19],
                )
                listajugadores.append(objeto)
            return listajugadores

    def get_defensores(self):  # obtiene todas las cartas de defensores
        resultado = self.__database.execute_query(
            "SELECT * FROM carta WHERE player_positions LIKE '%CB%' OR player_positions LIKE '%LB%' OR player_positions LIKE '%RB%' OR player_positions LIKE '%LWB%' OR player_positions LIKE '%RWB%' AND deshabilitado = 0 ORDER BY random() LIMIT 10"
        )
        if not resultado:
            print("No se encontraron cartas")
        else:
            listajugadores = []
            for carta in resultado:
                objeto = Carta(
                    carta[0],
                    carta[1],
                    carta[2],
                    carta[3],
                    carta[4],
                    carta[5],
                    carta[6],
                    carta[7],
                    carta[8],
                    carta[9],
                    carta[10],
                    carta[11],
                    carta[12],
                    carta[13],
                    carta[14],
                    carta[15],
                    carta[16],
                    carta[17],
                    carta[18],
                    carta[19],
                )
                listajugadores.append(objeto)
            return listajugadores

    def get_mediocampistas(self):  # obtiene todas las cartas de mediocampistas
        resultado = self.__database.execute_query(
            "SELECT * FROM carta WHERE player_positions LIKE '%CM%' OR player_positions LIKE '%CDM%' OR player_positions LIKE '%CAM%' OR player_positions LIKE '%RM%' OR player_positions LIKE '%LM%' AND deshabilitado = 0 ORDER BY random() LIMIT 10"
        )
        if not resultado:
            print("No se encontraron cartas")
        else:
            listajugadores = []
            for carta in resultado:
                objeto = Carta(
                    carta[0],
                    carta[1],
                    carta[2],
                    carta[3],
                    carta[4],
                    carta[5],
                    carta[6],
                    carta[7],
                    carta[8],
                    carta[9],
                    carta[10],
                    carta[11],
                    carta[12],
                    carta[13],
                    carta[14],
                    carta[15],
                    carta[16],
                    carta[17],
                    carta[18],
                    carta[19],
                )
                listajugadores.append(objeto)
            return listajugadores

    def get_delanteros(self):  # obtiene todas las cartas de delanteros
        resultado = self.__database.execute_query(
            "SELECT * FROM carta WHERE player_positions LIKE '%ST%' OR player_positions LIKE '%CF%' OR player_positions LIKE '%LW%' OR player_positions LIKE '%RW%' AND deshabilitado = 0 ORDER BY random() LIMIT 10"
        )
        if not resultado:
            print("No se encontraron cartas")
        else:
            listajugadores = []
            for carta in resultado:
                objeto = Carta(
                    carta[0],
                    carta[1],
                    carta[2],
                    carta[3],
                    carta[4],
                    carta[5],
                    carta[6],
                    carta[7],
                    carta[8],
                    carta[9],
                    carta[10],
                    carta[11],
                    carta[12],
                    carta[13],
                    carta[14],
                    carta[15],
                    carta[16],
                    carta[17],
                    carta[18],
                    carta[19],
                )
                listajugadores.append(objeto)
            return listajugadores

    def get_porteros(self):  # obtiene todas las cartas de porteros
        resultado = self.__database.execute_query(
            "SELECT * FROM carta WHERE player_positions LIKE '%GK%' AND deshabilitado = 0 ORDER BY random() LIMIT 10"
        )
        if not resultado:
            print("No se encontraron cartas")
        else:
            listajugadores = []
            for carta in resultado:
                objeto = Carta(
                    carta[0],
                    carta[1],
                    carta[2],
                    carta[3],
                    carta[4],
                    carta[5],
                    carta[6],
                    carta[7],
                    carta[8],
                    carta[9],
                    carta[10],
                    carta[11],
                    carta[12],
                    carta[13],
                    carta[14],
                    carta[15],
                    carta[16],
                    carta[17],
                    carta[18],
                    carta[19],
                )
                listajugadores.append(objeto)
            return listajugadores

    def insertar(self, objeto):  # inserta una nueva carta
        self.__database.execute_non_query(
            "INSERT INTO carta (id_carta,short_name,nationality,club_name,overall,player_positions,team_jersey_number,pace,shooting,passing,dribbling,defending,physic) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                objeto.get_id(),
                objeto.get_nombre(),
                objeto.get_nacionalidad(),
                objeto.get_club(),
                objeto.get_valoracion(),
                objeto.get_posicion(),
                objeto.get_posicion_equipo(),
                objeto.get_dorsal(),
                objeto.get_velocidad(),
                objeto.get_disparo(),
                objeto.get_pase(),
                objeto.get_gambeta(),
                objeto.get_defensa(),
                objeto.get_fisico(),
                objeto.get_gk_diving(),
                objeto.get_gk_handling(),
                objeto.get_gk_kicking(),
                objeto.get_gk_reflexes(),
                objeto.get_gk_speed(),
                objeto.get_gk_positioning(),
            ),
        )

    def actualizar(self, objeto):  # actualiza las estadisticas de una carta
        self.__database.execute_non_query(
            "UPDATE carta SET overall = ?,pace = ?,shooting = ?,passing = ?,dribbling = ?,physic = ? WHERE id_carta = ?",
            (
                objeto.get_id(),
                objeto.get_nombre(),
                objeto.get_nacionalidad(),
                objeto.get_club(),
                objeto.get_valoracion(),
                objeto.get_posicion(),
                objeto.get_posicion_equipo(),
                objeto.get_dorsal(),
                objeto.get_velocidad(),
                objeto.get_disparo(),
                objeto.get_pase(),
                objeto.get_gambeta(),
                objeto.get_defensa(),
                objeto.get_fisico(),
                objeto.get_gk_diving(),
                objeto.get_gk_handling(),
                objeto.get_gk_kicking(),
                objeto.get_gk_reflexes(),
                objeto.get_gk_speed(),
                objeto.get_gk_positioning(),
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

    def close(self):
        self.__database.close_connection()
