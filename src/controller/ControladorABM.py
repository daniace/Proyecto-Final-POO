import hashlib

from model.database.Singleton import Database


class ControllerABM:
    def __init__(self):
        self.db = Database()

    def consistencia_carta(
        self,
        nombre,
        nacionalidad,
        club,
        promedio,
        posicion,
        dorsal,
        stat1,
        stat2,
        stat3,
        stat4,
        stat5,
        stat6,
    ):
        if nombre == "":
            raise ValueError("El nombre de la carta no puede estar vacío")
        if nacionalidad == "":
            raise ValueError("La nacionalidad de la carta no puede estar vacía")
        if club == "":
            raise ValueError("El club de la carta no puede estar vacío")
        if int(promedio) < 0 or int(promedio) > 100:
            raise ValueError("El promedio de la carta debe estar entre 0 y 100")
        if posicion == "":
            raise ValueError("La posición de la carta no puede estar vacía")
        if int(dorsal) < 0 or int(dorsal) > 100:
            raise ValueError("El dorsal de la carta debe estar entre 0 y 100")
        if int(stat1) < 0 or int(stat1) > 100:
            raise ValueError(f"El {stat1} de la carta debe estar entre 0 y 100")
        if int(stat2) < 0 or int(stat2) > 100:
            raise ValueError(f"El {stat2} de la carta debe estar entre 0 y 100")
        if int(stat3) < 0 or int(stat3) > 100:
            raise ValueError(f"El {stat3} de la carta debe estar entre 0 y 100")
        if int(stat4) < 0 or int(stat4) > 100:
            raise ValueError(f"El {stat4} de la carta debe estar entre 0 y 100")
        if int(stat5) < 0 or int(stat5) > 100:
            raise ValueError(f"El {stat5} de la carta debe estar entre 0 y 100")
        if int(stat6) < 0 or int(stat6) > 100:
            raise ValueError(f"El {stat6} de la carta debe estar entre 0 y 100")

    # validar login admin
    def validar_login(self, nombre_usuario, password):
        self.db.connect()
        password = hashlib.sha256(password.encode()).hexdigest()
        if self.db.execute_query(
            "SELECT * FROM usuario WHERE nombre_usuario = ? AND password = ? AND admin = 1",
            (nombre_usuario, password),
        ):
            return True

    # Métodos para Usuario
    def get_usuario(self):
        self.db.connect()
        return self.db.execute_query(
            "SELECT id_usuario, nombre_usuario, password, admin, score FROM usuario WHERE baja_usuario = 0 or baja_usuario is NULL"
        )

    def add_usuario(self, nombre_usuario, password, admin):
        if nombre_usuario == "":
            raise ValueError("El nombre de usuario no puede estar vacío")
        if password != "":
            password = hashlib.sha256(password.encode()).hexdigest()
        self.db.execute_non_query(
            "INSERT INTO usuario (nombre_usuario, password, admin) VALUES (?, ?, ?)",
            (nombre_usuario, password, admin),
        )

    def update_usuario(self, user_id, nombre_usuario, password, admin, score):
        if nombre_usuario == "":
            raise ValueError("El nombre de usuario no puede estar vacío")
        if admin == 1 and password == "":
            raise ValueError("La contraseña no puede estar vacía")
        if admin == 1 and password != "":
            password = hashlib.sha256(password.encode()).hexdigest()
        self.db.execute_non_query(
            "UPDATE usuario SET nombre_usuario = ?, password = ?, admin = ?, score = ? WHERE id_usuario = ?",
            (nombre_usuario, password, admin, score, user_id),
        )

    def delete_usuario(self, user_id):
        self.db.execute_non_query(
            "UPDATE usuario SET baja_usuario = 1 WHERE id_usuario = ?", (user_id,)
        )

    def get_equipos(self):
        return self.db.execute_query("""SELECT
                    e.id_equipo,
                    u.nombre_usuario,
                    e.nombre_equipo,
                    c1.short_name AS carta1,
                    c2.short_name AS carta2,
                    c3.short_name AS carta3,
                    c4.short_name AS carta4,
                    c5.short_name AS carta5,
                    c6.short_name AS carta6,
                    c7.short_name AS carta7,
                    c8.short_name AS carta8,
                    c9.short_name AS carta9,
                    c10.short_name AS carta10,
                    c11.short_name AS carta11
                    FROM equipo AS e
                    INNER JOIN carta AS c1 ON e.id_carta1 = c1.id_carta
                    INNER JOIN carta AS c2 ON e.id_carta2 = c2.id_carta
                    INNER JOIN carta AS c3 ON e.id_carta3 = c3.id_carta
                    INNER JOIN carta AS c4 ON e.id_carta4 = c4.id_carta
                    INNER JOIN carta AS c5 ON e.id_carta5 = c5.id_carta
                    INNER JOIN carta AS c6 ON e.id_carta6 = c6.id_carta
                    INNER JOIN carta AS c7 ON e.id_carta7 = c7.id_carta
                    INNER JOIN carta AS c8 ON e.id_carta8 = c8.id_carta
                    INNER JOIN carta AS c9 ON e.id_carta9 = c9.id_carta
                    INNER JOIN carta AS c10 ON e.id_carta10 = c10.id_carta
                    INNER JOIN carta AS c11 ON e.id_carta11 = c11.id_carta
                    INNER JOIN usuario AS u ON e.id_usuario = u.id_usuario
                    WHERE baja_equipo = 0;""")

    def get_equipo_usuario(self):
        dict_usuarios = {}
        tupla = self.db.execute_query(
            "SELECT DISTINCT id_usuario,nombre_usuario FROM usuario WHERE baja_usuario = 0 AND nombre_usuario IS NOT NULL AND nombre_usuario != ''"
        )
        for id_usuario, nombre_usuario in tupla:
            dict_usuarios[id_usuario] = nombre_usuario
        return dict_usuarios

    def get_equipo_carta(self):
        dict_cartas = {}
        tupla = self.db.execute_query(
            "SELECT DISTINCT id_carta,short_name FROM carta WHERE deshabilitado = 0 AND short_name IS NOT NULL AND short_name != '' ORDER BY RANDOM() LIMIT 25"
        )
        for id_carta, short_name in tupla:
            dict_cartas[id_carta] = short_name
        return dict_cartas

    def add_equipo(
        self,
        nombre_equipo,
        id_usuario,
        id_carta1,
        id_carta2,
        id_carta3,
        id_carta4,
        id_carta5,
        id_carta6,
        id_carta7,
        id_carta8,
        id_carta9,
        id_carta10,
        id_carta11,
    ):
        if nombre_equipo == "":
            raise ValueError("El nombre del equipo no puede estar vacío")

        self.db.execute_non_query(
            "INSERT INTO equipo (nombre_equipo, id_usuario, id_carta1, id_carta2, id_carta3, id_carta4, id_carta5, id_carta6, id_carta7, id_carta8, id_carta9, id_carta10, id_carta11) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                nombre_equipo,
                id_usuario,
                id_carta1,
                id_carta2,
                id_carta3,
                id_carta4,
                id_carta5,
                id_carta6,
                id_carta7,
                id_carta8,
                id_carta9,
                id_carta10,
                id_carta11,
            ),
        )

    def update_equipo(
        self,
        id_equipo,
        nombre_equipo,
        id_usuario,
        id_carta1,
        id_carta2,
        id_carta3,
        id_carta4,
        id_carta5,
        id_carta6,
        id_carta7,
        id_carta8,
        id_carta9,
        id_carta10,
        id_carta11,
    ):
        self.db.execute_non_query(
            "UPDATE equipo SET nombre_equipo = ?, id_usuario = ?, id_carta1 = ?, id_carta2 = ?, id_carta3 = ?, id_carta4 = ?, id_carta5 = ?, id_carta6 = ?, id_carta7 = ?, id_carta8 = ?, id_carta9 = ?, id_carta10 = ?, id_carta11 = ? WHERE id_equipo = ?",
            (
                nombre_equipo,
                id_usuario,
                id_carta1,
                id_carta2,
                id_carta3,
                id_carta4,
                id_carta5,
                id_carta6,
                id_carta7,
                id_carta8,
                id_carta9,
                id_carta10,
                id_carta11,
                id_equipo,
            ),
        )

    def delete_equipo(self, equipo_id):
        self.db.execute_non_query(
            "UPDATE equipo SET baja_equipo = 1 WHERE id_equipo = ?", (equipo_id,)
        )

    # Métodos para Cartas
    def get_cartas(self):
        return self.db.execute_query(
            "SELECT id_carta, short_name, nationality, club_name, overall, player_positions, team_jersey_number, pace, shooting, passing, dribbling, defending, physic, gk_diving, gk_handling, gk_kicking, gk_reflexes, gk_speed, gk_positioning FROM carta WHERE deshabilitado = 0"
        )

    def get_carta_club(self):
        lista_clubes = []
        tupla = self.db.execute_query(
            "SELECT DISTINCT club_name FROM carta WHERE deshabilitado = 0 AND club_name IS NOT NULL"
        )
        for item in tupla:
            for i in item:
                lista_clubes.append(i)
        return lista_clubes

    def get_carta_nacionalidad(self):
        lista_nacionalidades = []
        tupla = self.db.execute_query(
            "SELECT DISTINCT nationality FROM carta WHERE deshabilitado = 0 AND nationality IS NOT NULL"
        )
        for item in tupla:
            for i in item:
                lista_nacionalidades.append(i)
        return lista_nacionalidades

    def add_carta_jugador(
        self,
        nombre: str,
        nacionalidad: str,
        club: str,
        promedio: int,
        posicion: str,
        dorsal: int,
        velocidad: int,
        tiro: int,
        pase: int,
        gambeta: int,
        defensa: int,
        fisico: int,
    ):
        self.consistencia_carta(
            nombre=nombre,
            nacionalidad=nacionalidad,
            club=club,
            promedio=promedio,
            posicion=posicion,
            dorsal=dorsal,
            stat1=velocidad,
            stat2=tiro,
            stat3=pase,
            stat4=gambeta,
            stat5=defensa,
            stat6=fisico,
        )

        self.db.execute_non_query(
            "INSERT INTO carta (short_name, nationality, club_name, overall, player_positions, team_jersey_number, pace, shooting, passing, dribbling, defending, physic) VALUES (?, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                nombre,
                nacionalidad,
                club,
                promedio,
                posicion,
                dorsal,
                velocidad,
                tiro,
                pase,
                gambeta,
                defensa,
                fisico,
            ),
        )

    def add_carta_arquero(
        self,
        nombre: str,
        nacionalidad: str,
        club: str,
        promedio: int,
        dorsal: int,
        diving: int,
        handling: int,
        kicking: int,
        reflexes: int,
        speed: int,
        positioning: int,
    ):
        self.consistencia_carta(
            nombre=nombre,
            nacionalidad=nacionalidad,
            club=club,
            promedio=promedio,
            posicion="",
            dorsal=dorsal,
            stat1=diving,
            stat2=handling,
            stat3=kicking,
            stat4=reflexes,
            stat5=speed,
            stat6=positioning,
        )
        self.db.execute_non_query(
            "INSERT INTO carta (short_name, nationality, club_name, overall, team_jersey_number, gk_diving, gk_handling, gk_kicking, gk_reflexes, gk_speed, gk_positioning, player_positions) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'GK')",
            (
                nombre,
                nacionalidad,
                club,
                promedio,
                dorsal,
                diving,
                handling,
                kicking,
                reflexes,
                speed,
                positioning,
            ),
        )

    def update_carta_jugador(
        self,
        id_carta: int,
        nombre: str,
        nacionalidad: str,
        club: str,
        promedio: int,
        posicion: str,
        dorsal: int,
        velocidad: int,
        tiro: int,
        pase: int,
        gambeta: int,
        defensa: int,
        fisico: int,
    ):
        self.consistencia_carta(
            nombre=nombre,
            nacionalidad=nacionalidad,
            club=club,
            promedio=promedio,
            posicion=posicion,
            dorsal=dorsal,
            stat1=velocidad,
            stat2=tiro,
            stat3=pase,
            stat4=gambeta,
            stat5=defensa,
            stat6=fisico,
        )
        self.db.execute_non_query(
            "UPDATE carta SET short_name = ?, nationality = ?, club_name = ?, overall = ?, player_positions = ?, team_jersey_number = ?, pace = ?, shooting = ?, passing = ?, dribbling = ?, defending = ?, physic = ? WHERE id_carta = ?",
            (
                nombre,
                nacionalidad,
                club,
                promedio,
                posicion,
                dorsal,
                velocidad,
                tiro,
                pase,
                gambeta,
                defensa,
                fisico,
                id_carta,
            ),
        )

    def update_carta_arquero(
        self,
        id_carta: int,
        nombre: str,
        nacionalidad: str,
        club: str,
        promedio: int,
        dorsal: int,
        diving: int,
        handling: int,
        kicking: int,
        reflexes: int,
        speed: int,
        positioning: int,
    ):
        self.consistencia_carta(
            nombre=nombre,
            nacionalidad=nacionalidad,
            club=club,
            promedio=promedio,
            posicion="",
            dorsal=dorsal,
            stat1=diving,
            stat2=handling,
            stat3=kicking,
            stat4=reflexes,
            stat5=speed,
            stat6=positioning,
        )

        self.db.execute_non_query(
            "UPDATE carta SET short_name = ?, nationality = ?, club_name = ?, overall = ?, team_jersey_number = ?, gk_diving = ?, gk_handling = ?, gk_kicking = ?, gk_reflexes = ?, gk_speed = ?, gk_positioning = ? WHERE id_carta = ?",
            (
                nombre,
                nacionalidad,
                club,
                promedio,
                dorsal,
                diving,
                handling,
                kicking,
                reflexes,
                speed,
                positioning,
                id_carta,
            ),
        )

    def delete_carta(self, carta_id):
        self.db.execute_non_query(
            "UPDATE carta SET deshabilitado = 1 WHERE id_carta = ?", (carta_id,)
        )


if __name__ == "__main__":
    controller = ControllerABM()
    dict = controller.get_equipo_carta()
    for key, value in dict.items():
        print(key, value)
