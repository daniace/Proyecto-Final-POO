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

    def reset(self):
        for i in range(len(self._matriz)):  # Recorre las filas
            for j in range(len(self._matriz[i])):  # Recorre las columnas de cada fila
                self._matriz[i][j] = 0

    def mostrar_formacion(self):
        print("Formación en el campo:")
        for fila in self._matriz:
            print(fila)

    def cantidad_arqueros(self):
        return 1

    def cantidad_dfc(self):
        pass

    def cantidad_mc(self):
        pass

    def cantidad_dc(self):
        pass


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

    def cantidad_dfc(self):
        return 4

    def cantidad_mc(self):
        return 4

    def cantidad_dc(self):
        return 2


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

    def cantidad_dfc(self):
        return 4

    def cantidad_mc(self):
        return 3

    def cantidad_dc(self):
        return 3


class Formacion352(FormacionStartegy):
    def formar(self, nro_equipo):
        # arquero#
        self._matriz[0][3] = nro_equipo
        # defensas#
        self._matriz[1][1] = nro_equipo
        self._matriz[1][3] = nro_equipo
        self._matriz[1][5] = nro_equipo
        # mediocmapistas#
        self._matriz[2][0] = nro_equipo
        self._matriz[2][2] = nro_equipo
        self._matriz[2][3] = nro_equipo
        self._matriz[2][4] = nro_equipo
        self._matriz[2][6] = nro_equipo
        # delanteros#
        self._matriz[3][2] = nro_equipo
        self._matriz[3][4] = nro_equipo

        return self._matriz

    def cantidad_dfc(self):
        return 3

    def cantidad_mc(self):
        return 5

    def cantidad_dc(self):
        return 2


"NOTA: nro_equipo debe ser un numero para ingresar en la matriz del equipo para diferenciarlos"
"Se puede implementar con el id del equipo pero no se que tan bueno sea"
# "matriz = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [1, 0, 1, 0, 1, 0, 1],
#     [0, 0, 2, 0, 2, 0, 0],
#     [1, 0, 1, 0, 1, 0, 1],
#     [2, 0, 2, 0, 2, 0, 2],
#     [0, 0, 1, 0, 1, 0, 0],
#     [2, 0, 2, 0, 2, 0, 2],
#     [0, 0, 0, 2, 0, 0, 0],
# ]"
"Quedando asi, siendo 1 y 2 los equipos"
