class Equipo:
    def __init__(self, id_equipo, nombre_equipo, id_usuario):
        self.__id_equipo: int = id_equipo
        self.__nombre_equipo: str = nombre_equipo
        self.__id_usuario: int = id_usuario
        self.__baja_equipo = 0

    def get_id_equipo(self):
        return self.__id_equipo

    def get_nombre(self):
        return self.__nombre_equipo

    def get_id_usuario(self):
        return self.__id_usuario

    def get_baja_equipo(self):
        return self.__baja_equipo

    def equipo_random(self):
        "Esto va aca o en otra clase?"
        pass
