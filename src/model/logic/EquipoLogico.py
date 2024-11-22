import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # se agerego para que pueda leer la clase carta xd
from database.AbmCarta import AbmCarta
from .formacion import *
import random


class EquipoLogico:
    def __init__(self, nombre_equipo, nro_equipo):
        self.__nombre_equipo = nombre_equipo
        self._nro_equipo = nro_equipo  # NRO_EQUIPO TIENE 1 O 2
        self._formacion = Formacion433()  # Tipo FORMACION A utilizar #433 DEFAULT
        self._jugadores = self.generar_equipo_random()  # LISTA JUGADORES
        self._distribucion = self.establecer_distribucion()  # MATRIZ DE JUGADORES

    def mostrar_listaj(self):
        for jugador in self._jugadores:
            print(jugador.get_nombre())

    def get_nombre(self):
        return self.__nombre_equipo

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

    def set_formacion(self, formacion):
        self._formacion = formacion
        self._distribucion = self.establecer_distribucion()

    def establecer_distribucion(self):
        return self._formacion.formar(self._nro_equipo)

    "revisar si funciona correctamente, sino pasar valor a una variabloe y devolverla"
    "Se encarga de establecer la distribucion de los jugadores en la cancha"

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
        "Debe devolver unicamente la lista de jugadores"
        return cartas

    def nuevo_equipo(self):
        self._jugadores = self.generar_equipo_random()

    "es necesario tener dos funciones para generar un nuevo equipo? nuevo_equipo deveria retornar la lista de jugadores?"

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


"Una vez funcione todo lo logico eliminar las funciones de imprimir y mostrar"
