from formacion import Formacion442, Equipo


class Cancha:
    def __init__(self, equipo1, equipo2) -> None:
        self._cancha = [
            [0, 0, 0, 0, 0, 0, 0],  # arquero jugador#
            [0, 0, 0, 0, 0, 0, 0],  # defensa jugador#
            [0, 0, 0, 0, 0, 0, 0],  # delantero cpu#
            [0, 0, 0, 0, 0, 0, 0],  # mediocampo jugardor#
            [0, 0, 0, 0, 0, 0, 0],  # mediocampo cpu
            [0, 0, 0, 0, 0, 0, 0],  # delatero jugador#
            [0, 0, 0, 0, 0, 0, 0],  # defensa cpu
            [0, 0, 0, 0, 0, 0, 0],
        ]  # arquero cpu
        self._equipo1 = equipo1
        self._equipo2 = equipo2

    def mostrar_cancha(self):
        for i in self._cancha:
            print(i)

    def agregar_equipos(self):
        # Equipo 1
        self._cancha[0] = self._equipo1.equipo[0]
        self._cancha[1] = self._equipo1.equipo[1]
        self._cancha[3] = self._equipo1[2]
        self._cancha[5] = self._equipo1[3]
        # Equipo 2
        self._cancha[7] = self._equipo2[0]
        self._cancha[6] = self._equipo2[1]
        self._cancha[4] = self._equipo2[2]
        self._cancha[2] = self._equipo2[3]

    "Estas dos funciones podrian ir en una sola"

    def diccionario_jugadores(self):
        pass

    def obtener_diccionario_jugadores(self):
        diccionario_jugadores_equipo1 = {}
        diccionario_jugadores_equipo2 = {}
        jugador_index = 0
        jugador_index2 = 0
        for i in range(len(self._cancha)):
            for j in range(len(self._cancha[i])):
                if (
                    self._cancha[i][j] == self._equipo1.nro_equipo
                ):  # NRO_EQUIPO TIENE 1 O 2
                    diccionario_jugadores_equipo1[(i, j)] = self._equipo1.get_jugadores[
                        jugador_index
                    ]
                    jugador_index += 1
                else:
                    diccionario_jugadores_equipo2[(i, j)] = self._equipo2.get_jugadores[
                        jugador_index2
                    ]
                    jugador_index2 += 1
        return diccionario_jugadores_equipo1, diccionario_jugadores_equipo2


"TERMINAR ESTO"

jugadores = [11, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 11 seria arquero
jugadores2 = [22, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]  # 22 seria arquero

equipo1 = Equipo(
    jugadores, 2, Formacion442
)  # Si no se le pone nada se le asigan la posicion 433
equipo2 = Equipo(jugadores2, 1, Formacion442)
matr = Cancha(equipo1, equipo2)
matr.agregar_equipos()
matr.mostrar_cancha()
dic1, dic2 = matr.obtener_diccionario_jugadores()
print(dic1)
print()
print(dic2)
