import random


class jugador:
    def __init__(self, nombre, posicion, nro_equipo, pase) -> None:
        self.nombre = nombre
        self.posicion = posicion
        self.nro_equipo = nro_equipo
        self.pase = pase
        self.tiene_lapelota = False

    def hacer_pase(self):
        "ESTA FUNCION HACE UN PASE"
        if random.randint(1, 100) < self.__pase:
            return True
        else:
            return False


class Partido:
    def pase(self, jugador1, jugador2, maquina):
        if jugador1.hacer_pase() and not maquina.interceptar():
            jugador2.tiene_lapelota = True
            jugador1.tiene_lapelota = False
        else:
            maquina.tiene_lapelota = True
            jugador1.tiene_lapelota = False
        # la maquina agarra la pelota
