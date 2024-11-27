import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # se agerego para que pueda leer la clase carta
from database.AbmCarta import AbmCarta
from .formacion import *
import random


class EquipoLogico:
    def __init__(self, nombre_equipo, es_cpu=False):
        self.__nombre_equipo = nombre_equipo
        self._nro_equipo = 1 if not es_cpu else 2  # NRO_EQUIPO TIENE 1 O 2
        self._formacion = Formacion433()  # Tipo FORMACION A utilizar #433 DEFAULT
        self._jugadores = self.generar_equipo_random()  # LISTA JUGADORES
        self._distribucion = self.establecer_distribucion()  # MATRIZ DE JUGADORES

    def get_nombre(self):
        return str(self.__nombre_equipo)

    def get_nro_equipo(self):
        return self._nro_equipo

    def get_distribucion(self):
        return self._distribucion

    def get_jugadores(self):
        lista_jugadores = self._jugadores
        return lista_jugadores

    @property
    def formacion(self):
        return self._formacion

    def set_nombre(self, nombre_equipo):
        self.__nombre_equipo = nombre_equipo

    def set_formacion(self, formacion):
        self._formacion = formacion
        self._distribucion = self.establecer_distribucion()

    def establecer_distribucion(self):
        return self._formacion.formar(self._nro_equipo)

    def generar_equipo_random(self):
        self.__generador = AbmCarta()
        cartas = []
        porteros = self.__generador.get_porteros()
        defensores = self.__generador.get_defensores()
        mediocampistas = self.__generador.get_mediocampistas()
        delanteros = self.__generador.get_delanteros()

        cartas += random.sample(porteros, self._formacion.cantidad_arqueros())
        cartas += random.sample(defensores, self._formacion.cantidad_dfc())
        cartas += random.sample(mediocampistas, self._formacion.cantidad_mc())
        cartas += random.sample(delanteros, self._formacion.cantidad_dc())

        self.__generador.close()
        return cartas

    def nuevo_equipo(self):
        self._jugadores = self.generar_equipo_random()


    def mostrar_plantilla_lista(self):
        for i in self._jugadores:
            print(i)

    def mostrar_plantilla_matriz(self):
        print(
            "formacion: ",
            self._formacion.cantidad_dfc(),
            "-",
            self._formacion.cantidad_mc(),
            "-",
            self._formacion.cantidad_dc(),
        )
        self._formacion.mostrar_formacion()

