import hashlib

from model.database.Singleton import Database


class ModeloABMUsuarios:
    def __init__(self):
        self.__db = Database()

    def _obtener_usuarios(self):
        """Devuelve una lista de todos los usuarios activos (baja_usuario = 0)."""
        self.__db.connect()
        usuarios = self.__db.execute_query(
            "SELECT id_usuario, nombre_usuario, password, admin, score FROM usuario WHERE baja_usuario = 0"
        )
        self.__db.close_connection()
        return usuarios

    def _insertar_usuario(self, nombre_usuario, password, admin, score):
        """Inserta un nuevo usuario en la tabla usuario."""
        password = hashlib.sha256(password.encode()).hexdigest()
        self.__db.connect()
        self.__db.execute_non_query(
            "INSERT INTO usuario (nombre_usuario, password, admin, baja_usuario, score) VALUES (?, ?, ?, 0, ?)",
            (nombre_usuario, password, admin, score),
        )
        self.__db.close_connection()

    def _actualizar_usuario(self, id_usuario, nombre_usuario, password, admin, score):
        """Actualiza un usuario existente."""
        password = hashlib.sha256(password.encode()).hexdigest()
        self.__db.connect()
        self.__db.execute_non_query(
            "UPDATE usuario SET nombre_usuario = ?, password = ?, admin = ?, score = ? WHERE id_usuario = ?",
            (nombre_usuario, password, admin, score, id_usuario),
        )
        self.__db.close_connection()

    def _eliminar_usuario(self, id_usuario):
        """Marca un usuario como dado de baja (baja_usuario = 1)."""
        self.__db.connect()
        self.__db.execute_non_query(
            "UPDATE usuario SET baja_usuario = 1 WHERE id_usuario = ?", (id_usuario,)
        )
        self.__db.close_connection()


if __name__ == "__main__":
    modelo = ModeloABMUsuarios()
    usuarios = modelo._obtener_usuarios()
    for usuario in usuarios:
        print(
            f"{usuario[0]} - {usuario[1]} - {usuario[2]} - {usuario[3]} - {usuario[4]} - {usuario[5]}"
        )
