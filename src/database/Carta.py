import random


class Carta:
    def __init__(
        self,
        id_carta=None,
        nombre: str = "",
        nacionalidad: str = "",
        club: str = "",
        valoracion: int = 0,
        posicion: str = "",
        posicion_equipo: str = "",
        dorsal: int = 0,
        velocidad: int = 0,
        disparo: int = 0,
        pase: int = 0,
        gambeta: int = 0,
        defensa: int = 0,
        fisico: int = 0,
        gk_diving: int = 0,
        gk_handling: int = 0,
        gk_kicking: int = 0,
        gk_reflexes: int = 0,
        gk_speed: int = 0,
        gk_positioning: int = 0,
    ):
        self.__id_carta: int = id_carta
        self.__nombre: str = nombre
        self.__nacionalidad: str = nacionalidad
        self.__club: str = club
        self.__valoracion: int = valoracion
        self.__posicion: str = posicion
        self.__posicion_equipo: str = posicion_equipo
        self.__dorsal: int = dorsal
        self.__velocidad: int = velocidad
        self.__disparo: int = disparo
        self.__pase: int = pase
        self.__gambeta: int = gambeta
        self.__defensa: int = defensa
        self.__fisico: int = fisico
        self.__gk_diving: int = gk_diving
        self.__gk_handling: int = gk_handling
        self.__gk_kicking: int = gk_kicking
        self.__gk_reflexes: int = gk_reflexes
        self.__gk_speed: int = gk_speed
        self.__gk_positioning: int = gk_positioning
        self.__tenencia = False

    def get_nombre(self):
        return self.__nombre

    def get_dorsal(self):
        return self.__dorsal

    def get_posicion(self):
        return self.__posicion

    def get_posicion_equipo(self):
        return self.__posicion_equipo

    def get_club(self):
        return self.__club

    def get_nacionalidad(self):
        return self.__nacionalidad

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

    def get_gk_diving(self):
        return self.__gk_diving

    def get_gk_handling(self):
        return self.__gk_handling

    def get_gk_kicking(self):
        return self.__gk_kicking

    def get_gk_reflexes(self):
        return self.__gk_reflexes

    def get_gk_speed(self):
        return self.__gk_speed

    def get_gk_positioning(self):
        return self.__gk_positioning

    def get_tenencia(self):
        return self.__tenencia

    def get_valoracion(self):
        return self.__valoracion

    def get_id(self):
        return self.__id_carta

    def set_tenencia(self):
        if not self.__tenencia:
            self.__tenencia = True
        else:
            self.__tenencia = False

    def __str__(self) -> str:
        if self.__posicion == "GK":
            return f"{self.__nombre} ({self.__club}) - {self.__posicion} - {self.__valoracion} - {self.__gk_diving} - {self.__gk_handling} - {self.__gk_kicking} - {self.__gk_reflexes} - {self.__gk_speed} - {self.__gk_positioning}"
        else:
            return f"{self.__nombre} ({self.__club}) - {self.__posicion} - {self.__valoracion} - {self.__velocidad} - {self.__disparo} - {self.__pase} - {self.__gambeta} - {self.__defensa} - {self.__fisico}"


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
