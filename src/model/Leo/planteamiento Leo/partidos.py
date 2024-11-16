# from Cronometro import Cronometro
from Cancha import Cancha
from formacion import Equipo, Formacion442
import time


class Partido:
    def __init__(self, jugador1, jugador2, equipo1, equipo2) -> None:
        self._jugador1 = jugador1
        self._jugador2 = jugador2
        self._partido_en_curso = True
        self._cronometro = None
        self._cancha = Cancha(
            equipo1.equipo, equipo2.equipo
        )  # ingresa directamente equipo con la formacion ya asignada

    def mapear_cancha(self):
        pass

    def jugar_partido(self):
        self._partido_en_curso = True

        if self._cronometro is None or not self._cronometro.is_alive():
            # self._cronometro = Cronometro()
            self._cronometro.start()

        while self._partido_en_curso:
            if self._cronometro._evento_partido_terminado.is_set():
                self._partido_en_curso = False
            else:
                time.sleep(1)
                print("hola")  # aca estaria la logica del juego#
        print("fin del partido")
        self._cronometro.join()


jugadores = [11, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 11 seria arquero
jugadores2 = [22, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]  # 22 seria arquero

equipo1 = Equipo(jugadores, 1)  # Si no se le pone nada se le asigan la posicion 433
equipo2 = Equipo(jugadores2, 2, Formacion442)


matr = Cancha(equipo1.equipo, equipo2.equipo)
matr.agregar_equipos()

matr.mostrar_cancha()


"asignar los equipos en cancha directamente o en partido?"
"hacer diccionario de las posiciones de los jugadores para los jugadores"
