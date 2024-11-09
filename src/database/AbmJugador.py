from DaoInterfaz import DaoInterfaz
from Singleton import Database
from Jugador import Jugador


class AbmJugador(DaoInterfaz):
    def __init__(self) -> None:
        self.__database = Database()
        self.__database.connect()

    def get_por_id(self, id: int) -> tuple:  # ESTO ANDA
        resultado = self.__database.execute_query(
            "SELECT * FROM usuario WHERE id_usuario = ? AND baja_usuario = 0",
            (id,),  # Devuelve una lista de tuplas
        )
        if (
            not resultado
        ):  # Si no se encontro la id o esta dado de baja, devuelve una lista vacia(Aunque solo busques un usuario) y se imprime un mensaje.
            print(f"No se encontró el usuario con el id: {id}, o está dado de baja")
        else:
            return Jugador(
                resultado[0][0],
                resultado[0][1],
                resultado[0][2],
                resultado[0][3],
                resultado[0][4],
            )

    def get_all(self):  # ESTO ANDA
        jugadores = []
        resultado = self.__database.execute_query(
            "SELECT * FROM usuario WHERE baja_usuario = 0"
        )
        if (
            resultado is None
        ):  # Si no se encontro la id, devuelve None y se imprime un mensaje.
            print("No se encontraron usuarios")
        else:
            for jugador in resultado:
                objeto = Jugador(
                    jugador[0], jugador[1], jugador[2], jugador[3], jugador[4]
                )
                jugadores.append(objeto)
            return jugadores

    def insertar(self, objeto):  # ESTO ANDA
        self.__database.execute_non_query(
            "INSERT INTO usuario (id_usuario, nombre_usuario, password, admin, baja_usuario) VALUES (?,?,?,?,?)",
            (
                objeto.get_id(),
                objeto.get_nombre(),
                objeto.get_password(),
                objeto.get_admin(),
                objeto.get_bajaUsuario(),
            ),
        )

    def actualizar(self, objeto):  # ESTO ANDA
        self.__database.execute_non_query(
            "UPDATE usuario SET nombre_usuario = ?, password = ?, admin = ?, baja_usuario = ? WHERE id_usuario = ?",
            (
                objeto.get_nombre(),
                objeto.get_password(),
                objeto.get_admin(),
                objeto.get_bajaUsuario(),
                objeto.get_id(),
            ),
        )

    def borrar(self, id):  # ESTO ANDA
        self.__database.execute_non_query(
            "UPDATE usuario SET baja_usuario = 1 WHERE id_usuario = ? AND baja_usuario = 0",
            (id,),
        )

    def close(self):  # ESTO ANDA
        self.__database.close_connection()
