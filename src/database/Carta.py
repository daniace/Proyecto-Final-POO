import random


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
        self._posicion: str = posicion
        self.__club: str = club
        self.__nacionalidad: str = nacionalidad
        self.__velocidad: int = velocidad
        self.__disparo: int = disparo
        self.__pase: int = pase
        self.__gambeta: int = gambeta
        self.__defensa: int = defensa
        self.__fisico: int = fisico
        self.__valoracion: int = self.valoracion()
        self.__tenencia = False

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

    def set_tenencia(self):
        if not self.__tenencia:
            self.__tenencia = True
        else:
            self.__tenencia = False

    def __str__(self) -> str:
        return f"{self.__id_carta} - {self.__nombre}"


class Delantero(Carta):
    def get_posicion(self):
        return "Delantero"

    def tirar_arco(self):
        "Esta funcion tira al arco"
        if random.randint(1, 100) < self.__disparo:
            return True
        else:
            return False

    def hacer_regate(self):
        "Esta funcion hace una gambeta"
        if random.randint(1, 100) < self.__gambeta:
            return True
        else:
            return False


class Mediocampista(Carta):
    def get_posicion(self):
        return "Mediocampista"

    def hacer_pase(self):
        "ESTA FUNCION HACE UN PASE"
        if random.randint(1, 100) < self.__pase:
            return True
        else:
            return False

    def interceptar(self):
        "Esta funcion intercepta un pase"
        if random.randint(1, 100) < self.__defensa:
            return True
        else:
            return False


class Defensor(Carta):
    def get_posicion(self):
        return "Defensor"

    def interceptar(self):
        "Esta funcion intercepta un pase"
        if random.randint(1, 100) < self.__defensa:
            return True
        else:
            return False

    def hacer_tackle(self):
        "Esta funcion intercepta un pase"
        if random.randint(1, 100) < self.__defensa:
            return True
        else:
            return False


class Portero(Carta):
    def get_posicion(self):
        return "Portero"

    def atajar(self):
        "Esta funcion ataja un tiro"
        if random.randint(1, 100) < self.__defensa:
            return True
        else:
            return False


"Es la mejor forma o hay otra forma mejor?"
"SEPARAR ESTO EN DISTINTAS CLASES "
