class Equipo:
    def __init__(
        self,
        id_equipo,
        nombre_equipo,
        id_usuario,
        id_carta1,
        id_carta2,
        id_carta3,
        id_carta4,
        id_carta5,
        id_carta6,
        id_carta7,
        id_carta8,
        id_carta9,
        id_carta10,
        id_carta11,
    ):
        self.__id_equipo: int = id_equipo
        self.__nombre_equipo: str = nombre_equipo
        self.__id_usuario: int = id_usuario
        self.__baja_equipo = 0
        self.__id_carta1 = id_carta1
        self.__id_carta2 = id_carta2
        self.__id_carta3 = id_carta3
        self.__id_carta4 = id_carta4
        self.__id_carta5 = id_carta5
        self.__id_carta6 = id_carta6
        self.__id_carta7 = id_carta7
        self.__id_carta8 = id_carta8
        self.__id_carta9 = id_carta9
        self.__id_carta10 = id_carta10
        self.__id_carta11 = id_carta11

    def get_id_equipo(self):
        return self.__id_equipo

    def get_nombre(self):
        return self.__nombre_equipo

    def get_id_usuario(self):
        return self.__id_usuario

    def get_baja_equipo(self):
        return self.__baja_equipo

    def get_id_carta1(self):
        return self.__id_carta1

    def get_id_carta2(self):
        return self.__id_carta2

    def get_id_carta3(self):
        return self.__id_carta3

    def get_id_carta4(self):
        return self.__id_carta4

    def get_id_carta5(self):
        return self.__id_carta5

    def get_id_carta6(self):
        return self.__id_carta6

    def get_id_carta7(self):
        return self.__id_carta7

    def get_id_carta8(self):
        return self.__id_carta8

    def get_id_carta9(self):
        return self.__id_carta9

    def get_id_carta10(self):
        return self.__id_carta10

    def get_id_carta11(self):
        return self.__id_carta11
