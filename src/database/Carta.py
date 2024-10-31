class Carta:
    def __init__(
        self,
        id_carta=None,
        nombre: str = "",
        dorsal: int = 0,
        posicion: str = "",
        club: str = "",
        nacionalidad: str = "",
        velocidad: int = 0,
        disparo: int = 0,
        pase: int = 0,
        gambeta: int = 0,
        defensa: int = 0,
        fisico: int = 0,
    ):
        self.__id_carta: int = id_carta
        self.__nombre: str = nombre
        self.__dorsal: int = dorsal
        self.__posicion: str = posicion
        self.__club: str = club
        self.__nacionalidad: str = nacionalidad
        self.__velocidad: int = velocidad
        self.__disparo: int = disparo
        self.__pase: int = pase
        self.__gambeta: int = gambeta
        self.__defensa: int = defensa
        self.__fisico: int = fisico
        self.__quimica: int = self.valoracion()

    def valoracion(self):
        return int(
            (
                self.__velocidad
                + self.__disparo
                + self.__pase
                + self.__gambeta
                + self.__defensa
                + self.__fisico
            )
            / 6
        )

    def get_nombre(self):
        return self.__nombre

    def get_dorsal(self):
        return self.__dorsal

    def get_posicion(self):
        return self.__posicion

    def get_club(self):
        return self.__club

    def get_nacionalidad(self):
        return self.__nacionalidad

    def get_quimica(self):
        return self.__quimica

    def get_velocidad(self):
        return self.__velocidad

    def get_disparo(self):
        return self.__disparo

    def get_pase(self):
        return self.__pase

    def get_gambeta(self):
        return self.__gambeta

    def get_defensa(self):
        return self.__defensa

    def get_fisico(self):
        return self.__fisico

    def get_id(self):
        return self.__id_carta
