from DaoInterfaz import DaoInterfaz
from Singleton import Database


class AbmJugador(DaoInterfaz):
    def __init__(self) -> None:
        self.__database = Database()

    def get_por_id(self, id: int) -> tuple:
        self.__database.query("SELECT * FROM jugadores WHERE id_usuario = ?", (id,))
        return self.__database.fetchone()

    def get_all(self):
        self.__database.query("SELECT * FROM jugadores")
        return self.__database.fetchall()

    def insertar(self, objeto):
        self.__database.query(
            "INSERT INTO jugadores (nombre_usuario, password, admin, baja_usuario) VALUES (?,?,?,?)",
            (
                objeto.get_nombre(),
                objeto.get_password(),
                objeto.get_admin(),
                objeto.get_bajaUsuario(),
            ),
        )
        self.__database.commit()

    def actualizar(self, objeto):
        self.__database.query(
            "UPDATE jugadores SET nombre_usuario = ?, password = ?, admin = ?, baja_usuario = ? WHERE id_usuario = ?",
            (
                objeto.get_nombre(),
                objeto.get_password(),
                objeto.get_admin(),
                objeto.get_bajaUsuario(),
                objeto.get_id(),
            ),
        )
        self.__database.commit()

    def borrar(self, id):
        self.__database.query(
            "UPDATE FROM jugadores SET baja_usuario = 1 WHERE id_usuario = ?", (id,)
        )
