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

    def get_matriz_cancha(self):
        return self._cancha
    
    def mostrar_cancha(self):
        for i in self._cancha:
            print(i)
    
    def mapear_cancha(self, formacion1, formacion2):
    # equipo 1 (jugador 1)
        self._cancha[0] = [str(jugador) if jugador else '0' for jugador in formacion1[0]]
        self._cancha[1] = [str(jugador) if jugador else '0' for jugador in formacion1[1]]
        self._cancha[3] = [str(jugador) if jugador else '0' for jugador in formacion1[2]]
        self._cancha[5] = [str(jugador) if jugador else '0' for jugador in formacion1[3]]
    # equipo 2 (jugador 2)
        self._cancha[7] = [str(jugador) if jugador else '0' for jugador in formacion2[0]]
        self._cancha[6] = [str(jugador) if jugador else '0' for jugador in formacion2[1]]
        self._cancha[4] = [str(jugador) if jugador else '0' for jugador in formacion2[2]]
        self._cancha[2] = [str(jugador) if jugador else '0' for jugador in formacion2[3]]
