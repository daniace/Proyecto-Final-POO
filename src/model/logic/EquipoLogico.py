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
        self.__id_usuario = random.randint(1000, 999999)
        self.__nombre_equipo = nombre_equipo
        self.__nro_equipo = 1 if not es_cpu else 2  # NRO_EQUIPO TIENE 1 O 2
        self.__formacion = Formacion433()  # Tipo FORMACION A utilizar #433 DEFAULT
        self.__jugadores = self.__generar_equipo_random()  # LISTA JUGADORES
        self.__distribucion = self.establecer_distribucion()  # MATRIZ DE JUGADORES

    def get_nombre(self):
        return str(self.__nombre_equipo)

    def get_nro_equipo(self):
        return self.__nro_equipo

    def get_distribucion(self):
        return self.__distribucion

    def get_jugadores(self):
        lista_jugadores = self.__jugadores
        return lista_jugadores

    @property
    def formacion(self):
        return self.__formacion

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def get_id_usuario(self):
        return self.__id_usuario

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def get_id_usuario(self):
        return self.__id_usuario

    def set_nombre(self, nombre_equipo):
        self.__nombre_equipo = nombre_equipo

    def set_formacion(self, formacion):
        self.__formacion = formacion
        self.__distribucion = self.establecer_distribucion()

    def establecer_distribucion(self):
        return self.__formacion.formar(self.__nro_equipo)

    def __generar_equipo_random(self):
        self.__generador = AbmCarta()
        cartas = []
        porteros = self.__generador.get_porteros()
        defensores = self.__generador.get_defensores()
        mediocampistas = self.__generador.get_mediocampistas()
        delanteros = self.__generador.get_delanteros()

        cartas += random.sample(porteros, self.__formacion.cantidad_arqueros())
        cartas += random.sample(defensores, self.__formacion.cantidad_dfc())
        cartas += random.sample(mediocampistas, self.__formacion.cantidad_mc())
        cartas += random.sample(delanteros, self.__formacion.cantidad_dc())

        self.__generador.close()
        return cartas

    def nuevo_equipo(self):
        self.__jugadores = self.__generar_equipo_random()

    def mostrar_plantilla_lista(self):
        for i in self.__jugadores:
            print(i)

    def mostrar_plantilla_matriz(self):
        print(
            "formacion: ",
            self.__formacion.cantidad_dfc(),
            "-",
            self.__formacion.cantidad_mc(),
            "-",
            self.__formacion.cantidad_dc(),
        )
        self.__formacion.mostrar_formacion()
