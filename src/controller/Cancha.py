from formacion import *
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) 
from database.Equipo import Equipo

class Cancha:
    def __init__(self) -> None:
        self._cancha=[[0,0,0,0,0,0,0],#arquero jugador#
                      [0,0,0,0,0,0,0],#defensa jugador#
                      [0,0,0,0,0,0,0],#delantero cpu#
                      [0,0,0,0,0,0,0],#mediocampo jugardor#
                      [0,0,0,0,0,0,0],#mediocampo cpu
                      [0,0,0,0,0,0,0],#delatero jugador#
                      [0,0,0,0,0,0,0],#defensa cpu
                      [0,0,0,0,0,0,0]]#arquero cpu

    def mostrar_cancha(self):
        for i in self._cancha:
            print(i)

    def mapear_cancha(self,formacion,formacion2):
        #equipo 1#
        self._cancha[0] = [str(jugador) if jugador else '              ' for jugador in formacion[0]]
        self._cancha[1] = [str(jugador) if jugador else '              ' for jugador in formacion[1]]
        self._cancha[3] = [str(jugador) if jugador else '              ' for jugador in formacion[2]]
        self._cancha[5] = [str(jugador) if jugador else '              ' for jugador in formacion[3]]
        #equipo 2#
        self._cancha[7] = [str(jugador) if jugador else '              ' for jugador in formacion2[0]]
        self._cancha[6] = [str(jugador) if jugador else '              ' for jugador in formacion2[1]]
        self._cancha[4] = [str(jugador) if jugador else '              ' for jugador in formacion2[2]]
        self._cancha[2] = [str(jugador) if jugador else '              ' for jugador in formacion2[3]]


# cancha=Cancha()
# jug1=Equipo(1,"P1",111)
# jug2=Equipo(2,"P2",222)
# jug2.set_formacion(Formacion352())
# jug1.set_formacion(Formacion442())
# print("plantilla jugador 1")
# jug1.mostrar_plantilla_lista()
# jug1.mostrar_plantilla_matriz()
# print("plantilla jugador 2")
# jug2.mostrar_plantilla_lista()
# jug2.mostrar_plantilla_matriz()

# cancha.mapear_cancha(jug1.get_matriz_jugadores(),jug2.get_matriz_jugadores())
# print ("\n jugadores en cancha:\n")
# cancha.mostrar_cancha()