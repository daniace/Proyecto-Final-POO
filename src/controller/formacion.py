from abc import ABC ,abstractmethod
from typing import List
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #se agerego para que pueda leer la clase carta xd
from database.Carta import Carta

class FormacionStartegy(ABC):
    def __init__(self) -> None: 
        self._equipo: List[Carta]=[]
        self._matriz=[[0,0,0,0,0,0,0],#arquero#
                      [0,0,0,0,0,0,0],#defensa#
                      [0,0,0,0,0,0,0],#mediocampo#
                      [0,0,0,0,0,0,0]]#delanteros#
    
    def set_equipo(self,equipo:List[Carta]):
        self._equipo=equipo

    @abstractmethod
    def formar(self):
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
    
    def cantidad_arqueros(self):
        return 1
    
    def cantidad_dfc(self):
        pass
    def cantidad_mc(self):
        pass
    def cantidad_dc(self):
        pass
    def get_matriz(self):
        return self._matriz

class Formacion442(FormacionStartegy):
    
        
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
    
    def cantidad_dfc(self):
        return 4
    
    def cantidad_mc(self):
        return 4
    
    def cantidad_dc(self):
        return 2


class Formacion433(FormacionStartegy):
    
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
    
    def cantidad_dfc(self):
        return 4
    
    def cantidad_mc(self):
        return 3
    
    def cantidad_dc(self):
        return 3

class Formacion352(FormacionStartegy):
    
    def formar(self):
        #arquero#
        self._matriz[0][3]=self._equipo[0]
        #defensas#
        self._matriz[1][2]=self._equipo[1]
        self._matriz[1][4]=self._equipo[2]
        self._matriz[1][6]=self._equipo[3]
        #mediocmapistas#
        self._matriz[2][0]=self._equipo[4]
        self._matriz[2][2]=self._equipo[5]
        self._matriz[2][3]=self._equipo[6]
        self._matriz[2][4]=self._equipo[7]
        self._matriz[2][6]=self._equipo[8]
        #delanteros#
        self._matriz[3][2]=self._equipo[9]
        self._matriz[3][4]=self._equipo[10]
        
        return self._matriz
    
    def cantidad_dfc(self):
        return 3
    
    def cantidad_mc(self):
        return 5
    
    def cantidad_dc(self):
        return 2
