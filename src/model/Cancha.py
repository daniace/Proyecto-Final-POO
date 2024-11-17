from EquipoLogico import EquipoLogico


class Cancha:
    def __init__(self, equipo1, equipo2) -> None:
        self._equipo1 = equipo1
        self._equipo2 = equipo2
        self._cancha = [[0 for _ in range(8)] for _ in range(8)]
        self._diccionario_equipo1 = None
        self._diccionario_equipo2 = None
        self.mapear_cancha()

    def get_matriz_cancha(self):
        return self._cancha

    def mostrar_cancha(self):
        for i in self._cancha:
            print(i)

    def get_diccionario_equipo1(self):
        return self._diccionario_equipo1

    def get_diccionario_equipo2(self):
        return self._diccionario_equipo2

    def mapear_cancha(self):
        # equipo 1 (jugador 1)
        self._cancha[0] = self._equipo1.get_distribucion()[0]
        self._cancha[1] = self._equipo1.get_distribucion()[1]
        self._cancha[3] = self._equipo1.get_distribucion()[2]
        self._cancha[5] = self._equipo1.get_distribucion()[3]
        # equipo 2 (jugador 2)
        self._cancha[7] = self._equipo2.get_distribucion()[0]
        self._cancha[6] = self._equipo2.get_distribucion()[1]
        self._cancha[4] = self._equipo2.get_distribucion()[2]
        self._cancha[2] = self._equipo2.get_distribucion()[3]
        "Te devuelve como deben ir en la cancha"
        self.obtener_diccionario_jugadores()  # una vez se setean los equipos, se debe generar el diccionario

    def obtener_diccionario_jugadores(self):
        self._diccionario_equipo1 = {}
        self._diccionario_equipo2 = {}
        jugador_index = 0
        jugador_index2 = 0
        equipo1 = self._equipo1.get_jugadores()
        equipo2 = self._equipo2.get_jugadores()[::-1]

        for i in range(len(self._cancha)):
            for j in range(len(self._cancha[i])):
                if (
                    self._cancha[i][j] == self._equipo1.get_nro_equipo()
                ):  # NRO_EQUIPO TIENE 1 O 2
                    self._diccionario_equipo1[(i, j)] = equipo1[jugador_index]
                    jugador_index += 1
                if self._cancha[i][j] == self._equipo2.get_nro_equipo():
                    self._diccionario_equipo2[(i, j)] = equipo2[jugador_index2]
                    jugador_index2 += 1
        # return diccionario_jugadores_equipo1, diccionario_jugadores_equipo2

    def mostrar_diccionario(self):
        print("DICCIONARIO EQUIPO 1")
        for clave, valor in self._diccionario_equipo1.items():
            print(f"{clave}: {valor}")

        print("Diccionario EQUIPO 2")
        for clave, valor in self._diccionario_equipo2.items():
            print(f"{clave} : {valor}")


# if __name__ == "__main__":
#     e1 = EquipoLogico("equipo1", 1)
#     e2 = EquipoLogico("equipo2", 2)
#     c = Cancha(e1, e2)
#     c.mostrar_cancha()
#     # c.mostrar_diccionario()
