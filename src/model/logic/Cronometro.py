import threading
import time


class Cronometro(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__duracion_del_partido=120 #cantidad de segundos equivalentes a 2 minutos#
        self.__contador=0 #inicializa el cronometro en 0#
        self.daemon=True #declaramos el hilo caomo daemon lo que permite que se ejecute en 2 plano, y que cuando se termine el programa muera el hilo#
        self._evento_partido_terminado=threading.Event() #se activa un evento cuando termina el tiempo#
        
    def run(self) -> None:
        
        while self.__contador<self.__duracion_del_partido:
            time.sleep(1)
            self.__contador+=1
        
        self._evento_partido_terminado.set() #cuando se acaba el tiempo, dispara el evento al progarama en el que se ejecuta#
