from Singleton import Database


class AbmCarta:
    def __init__(self):
        self.database = Database()

    def agregar_jugador(
        self,
        nombre_corto,
        dorsal,
        posicion,
        equipo,
        nacionalidad,
        quimica,
        velocidad,
        disparo,
        pase,
        gambeta,
        defensa,
        fisico,
    ):
        query = "INSERT INTO carta(short_name,team_jersey_number,team_positions,club_name,nationality,overall,pace,shooting,passing,dribbling,defending,physical) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
        self.database.query(
            query,
            (
                nombre_corto,
                dorsal,
                posicion,
                equipo,
                nacionalidad,
                quimica,
                velocidad,
                disparo,
                pase,
                gambeta,
                defensa,
                fisico,
            ),
        )
        self.database.commit()

    def obtener_jugadores(self):
        query = "SELECT * FROM carta"
        self.database.query(query)
        return self.database.fetchall()
