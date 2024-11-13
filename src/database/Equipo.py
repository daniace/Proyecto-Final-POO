from database.AbmCarta import AbmCarta
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # se agerego para que pueda leer la clase carta xd
from controller.formacion import *
import random


class Equipo:
    def __init__(self, id_equipo, nombre_equipo, id_usuario):
        self.__id_equipo: int = id_equipo
        self.__nombre_equipo: str = nombre_equipo
        self.__id_usuario: int = id_usuario
        self.__baja_equipo = 0
        self._plantilla_equipo = self._generar_equipo_random()
        self._formacion = Formacion433(
            self._plantilla_equipo
        )  # se genera como predeterminado#

    def get_id_equipo(self):
        return self.__id_equipo

    def get_nombre(self):
        return self.__nombre_equipo

    def get_id_usuario(self):
        return self.__id_usuario

    def get_baja_equipo(self):
        return self.__baja_equipo

    def _generar_equipo_random(self):
        self.__generador = AbmCarta()
        cartas = []
        porteros = self.__generador.get_porteros()
        defensores = self.__generador.get_defensores()
        mediocampistas = self.__generador.get_mediocampistas()
        delanteros = self.__generador.get_delanteros()

        for i in range(0, 1):
            cartas.append(random.choice(porteros))

        for i in range(0, 4):
            cartas.append(random.choice(defensores))

        for i in range(0, 3):
            cartas.append(random.choice(mediocampistas))

        for i in range(0, 3):
            cartas.append(random.choice(delanteros))

        self.__generador.close()

        return cartas

    def mostrar_plantilla_lista(self):
        for i in self._plantilla_equipo:
            print(i)

    def mostrar_plantilla_matriz(self):
        print("formacion: ", self._formacion.get_formacion())
        self._formacion.formar()
        self._formacion.mostrar_formacion()


# us=Equipo(2,'hola fc',1)
# us.mostrar_plantilla_lista()
# us.mostrar_plantilla_matriz()
