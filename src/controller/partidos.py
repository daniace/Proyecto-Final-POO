from Cronometro import Cronometro
from Cancha import Cancha
from database.Equipo import Equipo
import time

class Partido():
    def __init__(self,jugador1:Equipo,jugador2:Equipo) -> None: #jugador 1 y 2 tienen  que ser tipo usuario (al cual se le debe sumar un atributo, que tenga la clase Plantilla, la cual ocupa, las clases cartas y formaciones))#
        self._jugador1=jugador1
        self._jugador2=jugador2
        self._partido_en_curso=True
        self._cronometro=None
        self._cancha=Cancha()
        self._equipo_con_posecion=None
    
    def mapear_cancha(self):
        self._cancha.mapear_cancha(self._jugador1.get_matriz_jugadores(),self._jugador2.get_matriz_jugadores())
        self._cancha.mostrar_cancha()
        
    def jugar_partido(self):
        self._partido_en_curso=True
        
        if self._cronometro is None or not self._cronometro.is_alive():
            self._cronometro=Cronometro()
            self._cronometro.start()
        
        while self._partido_en_curso:
            if self._cronometro._evento_partido_terminado.is_set():
                self._partido_en_curso=False
            else:
                time.sleep(1)
                print("hola") #aca estaria la logica del juego#
        print("fin del partido")
        self._cronometro.join()

equipo1= Equipo(1,"P1",111)
equipo2= Equipo(2,"P2",222)

doparti=Partido(equipo1,equipo2)
doparti.mapear_cancha()
doparti.jugar_partido()