from model.database.Singleton import Database


class ModeloABMEquipo:
    def __init__(self):
        self.__db = Database()

    def _obtener_equipos(self):
        """Devuelve una lista de todos los equipos activos (baja_equipo = 0)."""
        self.__db.connect()
        equipos = self.__db.execute_query(
            """SELECT
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
                    WHERE baja_equipo = 0;"""
        )
        self.__db.close_connection()
        return equipos

    def _insertar_equipo(
        self,
        nombre_equipo,
        carta1,
        carta2,
        carta3,
        carta4,
        carta5,
        carta6,
        carta7,
        carta8,
        carta9,
        carta10,
        carta11,
    ):
        """Inserta un nuevo equipo en la tabla equipo."""
        self.__db.connect()
        self.__db.execute_non_query(
            "INSERT INTO equipo (nombre_equipo, id_carta1, id_carta2, id_carta3, id_carta4, id_carta5, id_carta6, id_carta7, id_carta8, id_carta9, id_carta10, id_carta11, baja_equipo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)",
            (
                nombre_equipo,
                carta1,
                carta2,
                carta3,
                carta4,
                carta5,
                carta6,
                carta7,
                carta8,
                carta9,
                carta10,
                carta11,
            ),
        )
        self.__db.close_connection()

    def _actualizar_equipo(
        self,
        id_equipo,
        id_usuario,
        nombre_equipo,
        carta1,
        carta2,
        carta3,
        carta4,
        carta5,
        carta6,
        carta7,
        carta8,
        carta9,
        carta10,
        carta11,
    ):
        """Actualiza un equipo existente."""
        self.__db.connect()
        self.__db.execute_non_query(
            "UPDATE equipo SET id_usuario = ?, nombre_equipo = ?, id_carta1 = ?, id_carta2 = ?, id_carta3 = ?, id_carta4 = ?, id_carta5 = ?, id_carta6 = ?, id_carta7 = ?, id_carta8 = ?, id_carta9 = ?, id_carta10 = ?, id_carta11 = ? WHERE id_equipo = ?",
            (
                id_usuario,
                nombre_equipo,
                carta1,
                carta2,
                carta3,
                carta4,
                carta5,
                carta6,
                carta7,
                carta8,
                carta9,
                carta10,
                carta11,
                id_equipo,
            ),
        )
        self.__db.close_connection()

    def _eliminar_equipo(self, id_equipo):
        """Marca un equipo como dado de baja (baja_equipo = 1)."""
        self.__db.connect()
        self.__db.execute_non_query(
            "UPDATE equipo SET baja_equipo = 1 WHERE id_equipo = ?", (id_equipo,)
        )
        self.__db.close_connection()
