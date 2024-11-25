import hashlib

from model.database.Singleton import Database
from model.database.Usuario import Usuario


class ModeloLogin:
    def __init__(self):
        self.__db = Database()

    def validar_usuario(self, username, password):
        """Valida si las credenciales son correctas."""
        password = hashlib.sha256(password.encode()).hexdigest()
        self.__db.connect()
        usuarios = []
        resultado = self.__db.execute_query(
            "SELECT * FROM usuario WHERE nombre_usuario = ? AND password = ? AND admin = 1",
            (username, password),
        )
        if resultado:
            for usuario in resultado:
                user = Usuario(
                    usuario[0],
                    usuario[1],
                    usuario[2],
                    usuario[3],
                    usuario[4],
                    usuario[5],
                )
                usuarios.append(user)
        self.__db.close_connection()
        for usuario in usuarios:
            if usuario.get_nombre() == username and usuario.get_password() == password:
                return True
        return False


if __name__ == "__main__":
    login = ModeloLogin()
    lpol = login.validar_usuario("admin1", "admin")
    print(lpol)
