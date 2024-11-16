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
        self._cancha[3] = self._equipo1.equipo[2]
        self._cancha[5] = self._equipo1.equipo[3]
        # Equipo 2
        self._cancha[7] = self._equipo2.equipo[0]
        self._cancha[6] = self._equipo2.equipo[1]
        self._cancha[4] = self._equipo2.equipo[2]
        self._cancha[2] = self._equipo2.equipo[3]

    "Estas dos funciones podrian ir en una sola"

    def diccionario_jugadores(self):
        pass

    def obtener_diccionario_jugadores(self):
        diccionario_jugadores_equipo1 = {}
        diccionario_jugadores_equipo2 = {}
        jugador_index = 0
        jugador_index2 = 0
        equipo1 = self._equipo1.get_jugadores()
        equipo2 = self._equipo2.get_jugadores()
        for i in range(len(self._cancha)):
            for j in range(len(self._cancha[i])):
                if (
                    self._cancha[i][j] == self._equipo1.nro_equipo
                ):  # NRO_EQUIPO TIENE 1 O 2
                    diccionario_jugadores_equipo1[(i, j)] = equipo1[jugador_index]
                    jugador_index += 1
                if self._cancha[i][j] == self._equipo2.nro_equipo:
                    diccionario_jugadores_equipo2[(i, j)] = equipo2[jugador_index2]
                    jugador_index2 += 1
        return diccionario_jugadores_equipo1, diccionario_jugadores_equipo2


"TERMINAR ESTO"

jugadores = ['Arquero1', 'DFC1', 'DFC1', 'DFC1', 'DFC1', 'MEDIO1', 'MEDIO1', 'MEDIO1', 'MEDIO1', 'DC1', 'DC1']  # 11 seria arquero
jugadores2 = ['GK', 'DFC2', 'DF2', 'DC2', 2, 2, 2, 2, 2, 2, 2][::-1]  # 22 seria arquero

equipo1 = Equipo(
    jugadores, 1, Formacion442
)  # Si no se le pone nada se le asigan la posicion 433
equipo2 = Equipo(jugadores2, 2, Formacion442)
matr = Cancha(equipo1, equipo2)
matr.agregar_equipos()
matr.mostrar_cancha()
dic1, dic2 = matr.obtener_diccionario_jugadores()
print(dic1)
print()
print(dic2)


"SISTEMA DE FORMACIONES - ACCIONES - DISTRIBUCION JUGADORES - DICCIIONARIO DE JUGADORES"
"LISTA DE JUGADORES ORDENADA POR POSICION"
