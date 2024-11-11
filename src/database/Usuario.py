class Usuario:  # Clase que representa a un usuario del juego o un administrador
    def __init__(
        self,
        idUsuario=None,
        nombreUsuario: str = "",
        password: str = "",
        admin: int = 0,
        bajaUsuario: int = 0,
    ) -> None:
        self.__idUsuario: int = idUsuario
        self.__nombreUsuario: str = nombreUsuario
        self.__password: str = password
        self.__admin: int = admin
        self.__bajaUsuario: int = bajaUsuario

    def get_id(self):
        return self.__idUsuario

    def get_nombre(self):
        return self.__nombreUsuario

    def set_nombre(self, nombre):
        self.__nombreUsuario = nombre

    def get_password(self):
        return self.__password

    def get_admin(self):
        return self.__admin

    def get_bajaUsuario(self):
        return self.__bajaUsuario

    def __str__(self) -> str:
        return f"ID: {self.__idUsuario}, Nombre: {self.__nombreUsuario}, Password: {self.__password}, Admin: {self.__admin}, Baja: {self.__bajaUsuario}"
