from DaoInterfaz import DaoInterfaz
from Singleton import Database


class AbmJugador(DaoInterfaz):
    def __init__(self) -> None:
        self.__database = Database()
        self.__database.connect()

    def get_por_id(self, id: int) -> tuple:
        resultado = self.__database.execute_query(
            "SELECT * FROM usuario WHERE id_usuario = ? AND baja_usuario = 0", (id,)
        )
        return (
            resultado[0]
            if resultado
            else print(f"No se encontro el usuario con ese id: {id}")
        )  # Devuelve el primer elemento de la lista si hay resultados, sino None

    def get_all(self):
        return self.__database.execute_query(
            "SELECT * FROM usuario WHERE baja_usuario = 0"
        )

    def insertar(self, objeto):
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

    def actualizar(self, objeto):
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

    def borrar(self, id):
        self.__database.execute_non_query(
            "UPDATE usuario SET baja_usuario = 1 WHERE id_usuario = ? AND baja_usuario = 0",
            (id,),
        )
