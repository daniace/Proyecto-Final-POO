class Usuario:  # Clase que representa a un usuario del juego o un administrador
    def __init__(
        self,
        id_usuario=None,
        nombre_usuario: str = "",
        password: str = "",
        admin: int = 0,
        baja_usuario: int = 0,
        score: int = 0,
    ) -> None:
        self.__id_usuario: int = id_usuario
        self.__nombre_usuario: str = nombre_usuario
        self.__password: str = password
        self.__admin: int = admin
        self.__baja_usuario: int = baja_usuario
        self.__score: int = score

    def get_id(self):
        return self.__id_usuario

    def get_nombre(self):
        return self.__nombre_usuario

    def set_nombre(self, nombre):
        self.__nombre_usuario = nombre

    def get_password(self):
        return self.__password

    def get_admin(self):
        return self.__admin

    def get_baja_usuario(self):
        return self.__baja_usuario

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def __str__(self) -> str:
        return f"ID: {self.__id_usuario}, Nombre: {self.__nombre_usuario}, Password: {self.__password}, Admin: {self.__admin}, Baja: {self.__baja_usuario}, Score: {self.__score}"
