class Equipo:
    def __init__(self, idEquipo, nombreEquipo, idUsuario, bajaEquipo: int = 0):
        self.__idEquipo: int = idEquipo
        self.__nombreEquipo: str = nombreEquipo
        self.__idUsuario: int = idUsuario
        self.__bajaEquipo = bajaEquipo

    def get_idEquipo(self):
        return self.__idEquipo

    def get_nombre(self):
        return self.__nombreEquipo

    def get_idUsuario(self):
        return self.__idUsuario

    def get_bajaEquipo(self):
        return self.__bajaEquipo

    def equipo_random(self):
        "Esto va aca o en otra clase?"
        pass
