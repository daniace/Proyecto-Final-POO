from abc import ABC ,abstractmethod
from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #se agerego para que pueda leer la clase carta xd
from database.Carta import Carta

class FormacionStartegy(ABC):
    def __init__(self,equipo:List[Carta]) -> None: 
        self._formacion=''
        self._equipo: List[Carta]=equipo    
        self._matriz=[[0,0,0,0,0,0,0],#arquero#
                      [0,0,0,0,0,0,0],#defensa#
                      [0,0,0,0,0,0,0],#mediocampo#
                      [0,0,0,0,0,0,0]]#delanteros#

    
    def get_formacion(self):
        return self._formacion

    @abstractmethod
    def formar(self, equipo):
        pass
    
    def reset(self):
        for i in range(len(self._matriz)):           # Recorre las filas
            for j in range(len(self._matriz[i])):    # Recorre las columnas de cada fila
                self._matriz[i][j] = 0   
    
    def mostrar_formacion(self):
        print("Formación en el campo:")
        for fila in self._matriz:
            fila_str= [str(jugador) if jugador != 0 else "              " for jugador in fila]
            print(fila_str,"\n")

class Formacion442(FormacionStartegy):
    
    def __init__(self, equipo: List[Carta]) -> None:
        super().__init__(equipo)
        self._formacion='4-4-2'
        
    def formar(self):
        #arquero#
        self._matriz[0][3]=self._equipo[0]
        #defensas#
        self._matriz[1][0]=self._equipo[1]
        self._matriz[1][2]=self._equipo[2]
        self._matriz[1][4]=self._equipo[3]
        self._matriz[1][6]=self._equipo[4]
        #mediocampistas#
        self._matriz[2][0]=self._equipo[5]
        self._matriz[2][2]=self._equipo[6]
        self._matriz[2][4]=self._equipo[7]
        self._matriz[2][6]=self._equipo[8]
        #delanteros#
        self._matriz[3][2]=self._equipo[9]
        self._matriz[3][4]=self._equipo[10]
        return self._matriz


class Formacion433(FormacionStartegy):
    
    def __init__(self, equipo: List[Carta]) -> None:
        super().__init__(equipo)
        self._formacion='4-3-3'
        
    def formar(self):
        #arquero#
        self._matriz[0][3]=self._equipo[0]
        #defensas#
        self._matriz[1][0]=self._equipo[1]
        self._matriz[1][2]=self._equipo[2]
        self._matriz[1][4]=self._equipo[3]
        self._matriz[1][6]=self._equipo[4]
        #mediocmapistas#
        self._matriz[2][1]=self._equipo[5]
        self._matriz[2][3]=self._equipo[6]
        self._matriz[2][5]=self._equipo[7]
        #delanteros#
        self._matriz[3][1]=self._equipo[8]
        self._matriz[3][3]=self._equipo[9]
        self._matriz[3][5]=self._equipo[10]
        return self._matriz

# team = [1,2,3,4,5,6,7,8,9,10,11]
# formacion=Formacion442(team)
# formacion.formar()
# formacion.mostrar_formacion()
# print()
# formacio2=Formacion433(team)
# formacio2.formar()
# formacio2.mostrar_formacion()
# formacio2.reset()
# formacio2.mostrar_formacion()