class Carta:
    def __init__(
        self,
        id_carta,
        nombre,
        dorsal,
        posicion,
        club,
        nacionalidad,
        velocidad,
        disparo,
        pase,
        gambeta,
        defensa,
        fisico,
    ):
        self.__id_carta = id_carta
        self.__nombre = nombre
        self.__dorsal = dorsal
        self.__posicion = posicion
        self.__club = club
        self.__nacionalidad = nacionalidad
        self.__velocidad = velocidad
        self.__disparo = disparo
        self.__pase = pase
        self.__gambeta = gambeta
        self.__defensa = defensa
        self.__fisico = fisico
        self.__quimica = self.valoracion()

    def valoracion(self):
        return (
            self.__velocidad
            + self.__disparo
            + self.__pase
            + self.__gambeta
            + self.__defensa
            + self.__fisico
        ) / 6

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
