from abc import ABC, abstractmethod


class FormacionStartegy(ABC):
    def __init__(self) -> None:
        self._matriz = [
            [0, 0, 0, 0, 0, 0, 0],  # arquero#
            [0, 0, 0, 0, 0, 0, 0],  # defensa#
            [0, 0, 0, 0, 0, 0, 0],  # mediocampo#
            [0, 0, 0, 0, 0, 0, 0],
        ]  # delanteros#

    @abstractmethod
    def formar(self, nro_equipo):
        pass

    def mostrar_formacion(self):
        print("Formación en el campo:")
        for fila in self._matriz:
            print(fila)

    "Sacar esto"


class Formacion442(FormacionStartegy):
    def formar(self, nro_equipo):
        # arquero#
        self._matriz[0][3] = nro_equipo
        # defensas#
        self._matriz[1][0] = nro_equipo
        self._matriz[1][2] = nro_equipo
        self._matriz[1][4] = nro_equipo
        self._matriz[1][6] = nro_equipo
        # mediocampistas#
        self._matriz[2][0] = nro_equipo
        self._matriz[2][2] = nro_equipo
        self._matriz[2][4] = nro_equipo
        self._matriz[2][6] = nro_equipo
        # delanteros#
        self._matriz[3][2] = nro_equipo
        self._matriz[3][4] = nro_equipo
        return self._matriz


class Formacion433(FormacionStartegy):
    def formar(self, nro_equipo):
        # arquero#
        self._matriz[0][3] = nro_equipo
        # defensas#
        self._matriz[1][0] = nro_equipo
        self._matriz[1][2] = nro_equipo
        self._matriz[1][4] = nro_equipo
        self._matriz[1][6] = nro_equipo
        # mediocmapistas#
        self._matriz[2][1] = nro_equipo
        self._matriz[2][3] = nro_equipo
        self._matriz[2][5] = nro_equipo
        # delanteros#
        self._matriz[3][1] = nro_equipo
        self._matriz[3][3] = nro_equipo
        self._matriz[3][5] = nro_equipo
        return self._matriz


class Equipo:
    def __init__(self, jugadores, nro_equipo, formacion=Formacion433):
        self._jugadores = jugadores
        self.__formacion = formacion
        self.__nro_equipo = nro_equipo
        self.__equipo = self.establecer_formacion(self.__nro_equipo)

    @property
    def equipo(self):
        return self.__equipo

    @property
    def nro_equipo(self):
        return self.__nro_equipo

    def get_jugadores(self):
        return self._jugadores

    def get_formacion(self, formacion):
        self.__formacion = formacion
        self.__equipo = self.establecer_formacion(self.nro_equipo)

    @property
    def formacion(self):
        return self.__formacion

    def establecer_formacion(self, nro_equipo):
        formacion = self.__formacion().formar(nro_equipo)
        return formacion

    def imprimir_jugadores(self):
        print("Formación en el campo:")
        for fila in self.__equipo:
            print(fila)


jugadores = [3, 3, 3, 3, 3, 3, 3, 3]
a = Equipo(jugadores, 1)
a.imprimir_jugadores()
