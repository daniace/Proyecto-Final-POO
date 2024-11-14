import os
import sys
from AbmCarta import AbmCarta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # se agerego para que pueda leer la clase carta xd
from controller.formacion import *
import random


class Equipo:
    def __init__(self, id_equipo, nombre_equipo, id_usuario):
        self.__id_equipo: int = id_equipo
        self.__nombre_equipo: str = nombre_equipo
        self.__id_usuario: int = id_usuario
        self.__baja_equipo = 0
        self._formacion = Formacion433() # se genera como predeterminado#
        self._plantilla_equipo = self._generar_equipo_random()


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

        cartas += random.sample(porteros, self._formacion.cantidad_arqueros())
        cartas += random.sample(defensores, self._formacion.cantidad_dfc())
        cartas += random.sample(mediocampistas, self._formacion.cantidad_mc())
        cartas += random.sample(delanteros, self._formacion.cantidad_dc())

        self.__generador.close()

        return cartas

    def mostrar_plantilla_lista(self):
        for i in self._plantilla_equipo:
            print(i)

    def mostrar_plantilla_matriz(self):
        print("formacion: ",self._formacion.cantidad_dfc(),"-",self._formacion.cantidad_mc(),"-",self._formacion.cantidad_dc())
        self._formacion.set_equipo(self._plantilla_equipo)
        self._formacion.formar()
        self._formacion.mostrar_formacion()
    
    def set_formacion(self, nueva_formacion:FormacionStartegy):
        self._formacion=nueva_formacion
    
    def nuevo_equipo(self):
        self._plantilla_equipo=self._generar_equipo_random()


# us=Equipo(2,'hola fc',1) #inicia con la formacion predeterminada#
# print("plantilla equipo 1:")
# us.mostrar_plantilla_lista()
# us2=Equipo(22,'chau fc',99) #inicia con la fromacion predeterminada#
# us2.set_formacion(Formacion442())#se le setea una nueva fromacion#
# print("plantilla equipo 2:")
# us2.mostrar_plantilla_lista()
# us.nuevo_equipo()
# print("nueva plantilla equipo 1:")
# us.mostrar_plantilla_lista()
