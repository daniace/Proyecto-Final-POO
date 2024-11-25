class Equipo:
    def __init__(
        self,
        id_equipo=None,
        nombre_equipo=None,
        id_usuario=None,
        baja_equipo=None,
        id_carta1=None,
        id_carta2=None,
        id_carta3=None,
        id_carta4=None,
        id_carta5=None,
        id_carta6=None,
        id_carta7=None,
        id_carta8=None,
        id_carta9=None,
        id_carta10=None,
        id_carta11=None,
    ):
        self.__id_equipo: int = id_equipo
        self.__nombre_equipo: str = nombre_equipo
        self.__id_usuario: int = id_usuario
        self.__baja_equipo = baja_equipo
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

    def set_nombre(self, nombre_equipo):
        self.__nombre_equipo = nombre_equipo

    def set_cartas(self, cartas):
        for carta in cartas:
            print(carta)
        self.__id_carta1 = cartas[0].get_id()
        self.__id_carta2 = cartas[1].get_id()
        self.__id_carta3 = cartas[2].get_id()
        self.__id_carta4 = cartas[3].get_id()
        self.__id_carta5 = cartas[4].get_id()
        self.__id_carta6 = cartas[5].get_id()
        self.__id_carta7 = cartas[6].get_id()
        self.__id_carta8 = cartas[7].get_id()
        self.__id_carta9 = cartas[8].get_id()
        self.__id_carta10 = cartas[9].get_id()
        self.__id_carta11 = cartas[10].get_id()

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def __str__(self) -> str:
        return f"ID: {self.__id_equipo}, Nombre: {self.__nombre_equipo}, ID Usuario: {self.__id_usuario}, Baja: {self.__baja_equipo}"
