from model.database.Singleton import Database


class ModeloCartas:
    def __init__(self):
        self.__db = Database()

    def obtener_cartas(self):
        """Devuelve todas las cartas activas (deshabilitado = 0)."""
        self.__db.connect()
        cartas = self.__db.execute_query(
            """SELECT id_carta, short_name, nationality, club_name, overall, player_positions, 
                pace, shooting, passing, dribbling, defending, physic, gk_diving,
                gk_handling, gk_kicking, gk_reflexes, gk_speed, gk_positioning
                FROM carta 
                WHERE deshabilitado = 0"""
        )
        self.__db.close_connection()
        return cartas

    def insertar_carta(
        self,
        short_name,
        nationality,
        club_name,
        overall,
        player_positions,
        pace,
        shooting,
        passing,
        dribbling,
        defending,
        physic,
    ):
        """Inserta una nueva carta en la tabla."""
        self.__db.connect()
        self.__db.execute_non_query(
            """INSERT INTO carta 
                (short_name, nationality, club_name, overall, player_positions,
                pace, shooting, passing, dribbling, defending, physic, deshabilitado) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)""",
            (
                short_name,
                nationality,
                club_name,
                overall,
                player_positions,
                pace,
                shooting,
                passing,
                dribbling,
                defending,
                physic,
            ),
        )
        self.__db.close_connection()

    def insertar_arquero(
        self,
        short_name,
        nationality,
        club_name,
        overall,
        gk_diving,
        gk_handling,
        gk_kicking,
        gk_reflexes,
        gk_speed,
        gk_positioning,
    ):
        """Inserta una nueva carta en la tabla."""
        self.__db.connect()
        self.__db.execute_non_query(
            """INSERT INTO carta 
                (short_name, nationality, club_name, overall, player_positions,
                gk_diving, gk_handling, gk_kicking, gk_reflexes, gk_speed, gk_positioning, deshabilitado) 
                VALUES (?, ?, ?, ?, 'GK', ?, ?, ?, ?, ?, ?, 0)""",
            (
                short_name,
                nationality,
                club_name,
                overall,
                gk_diving,
                gk_handling,
                gk_kicking,
                gk_reflexes,
                gk_speed,
                gk_positioning,
            ),
        )
        self.__db.close_connection()

    def actualizar_carta(
        self,
        id_carta,
        short_name,
        nationality,
        club_name,
        overall,
        player_positions,
        pace,
        shooting,
        passing,
        dribbling,
        defending,
        physic,
    ):
        """Actualiza los datos de una carta."""
        self.__db.connect()
        self.__db.execute_non_query(
            """UPDATE carta 
                SET short_name = ?, nationality = ?, club_name = ?, overall = ?,
                player_positions = ?, pace = ?, shooting = ?, passing = ?, 
                dribbling = ?, defending = ?, physic = ? 
                WHERE id_carta = ?""",
            (
                short_name,
                nationality,
                club_name,
                overall,
                player_positions,
                pace,
                shooting,
                passing,
                dribbling,
                defending,
                physic,
                id_carta,
            ),
        )
        self.__db.close_connection()

    def actualizar_arquero(
        self,
        id_carta,
        short_name,
        nationality,
        club_name,
        overall,
        gk_diving,
        gk_handling,
        gk_kicking,
        gk_reflexes,
        gk_speed,
        gk_positioning,
    ):
        """Actualiza los datos de una carta."""
        self.__db.connect()
        self.__db.execute_non_query(
            """UPDATE carta 
                SET short_name = ?, nationality = ?, club_name = ?, overall = ?, 
                gk_diving = ?, gk_handling = ?, gk_kicking = ?, 
                gk_reflexes = ?, gk_speed = ?, gk_positioning = ? 
                WHERE id_carta = ?""",
            (
                short_name,
                nationality,
                club_name,
                overall,
                gk_diving,
                gk_handling,
                gk_kicking,
                gk_reflexes,
                gk_speed,
                gk_positioning,
                id_carta,
            ),
        )
        self.__db.close_connection()

    def eliminar_carta(self, id_carta):
        """Marca una carta como deshabilitada (deshabilitado = 1)."""
        self.__db.connect()
        self.__db.execute_non_query(
            "UPDATE carta SET deshabilitado = 1 WHERE id_carta = ?", (id_carta,)
        )
        self.__db.close_connection()
