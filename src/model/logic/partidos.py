from Cronometro import Cronometro
from Cancha import Cancha
from database.Equipo import Equipo
from database.Carta import Carta
import time
import random


class Partido:
    def __init__(self, jugador1: Equipo) -> None:
        self._jugador1 = jugador1
        self._jugador2 = Equipo(1, "CPU FC", 99)
        self._partido_en_curso = True
        self._cronometro = None
        self._cancha = Cancha(self._jugador1, self._jugador2)
        self._equipo_con_posecion = None
        self._jugador_con_pelota = None
        # self._dificultad=dificultad# para empezar a programar

    def mapear_cancha(self):
        self._cancha.mapear_cancha()
        self._cancha.mostrar_cancha()

    def _encontrar_posicion_jugador(self, jugador):
        for i, linea in enumerate(self._cancha.get_matriz_cancha()):
            if str(jugador) in linea:
                return (i, linea.index(str(jugador)))
        return None

    def _mostrar_opciones_pase(self):
        if not self._jugador_con_pelota:
            print("No hay ningún jugador en posesión del balón.")
            return []

        posicion_actual = self._encontrar_posicion_jugador(self._jugador_con_pelota)
        if not posicion_actual:
            print("No se pudo determinar la posición del jugador con el balón.")
            return []

        x, y = posicion_actual
        posibles_receptores = self._determinar_lineas_a_revisar(x)

        if not posibles_receptores:
            print("No hay jugadores disponibles para recibir el pase.")
            return []

        print(
            f"Jugadores disponibles para recibir el pase de {self._jugador_con_pelota}:"
        )
        for i, jugador in enumerate(posibles_receptores):
            print(f"{i + 1}. {jugador}")
        return posibles_receptores

    def _determinar_lineas_a_revisar(self, x):
        lineas_a_revisar = []
        if x in [0, 7]:  # Arquero
            lineas_a_revisar = [1] if x == 0 else [6]
        elif x in [1, 6]:  # Defensa
            lineas_a_revisar = [0, 1, 3] if x == 1 else [7, 6, 4]
        elif x in [3, 4]:  # Mediocampo
            lineas_a_revisar = [1, 3, 5] if x == 3 else [6, 4, 2]
        elif x in [5, 2]:  # Delantero
            lineas_a_revisar = [3, 5] if x == 5 else [4, 2]

        posibles_receptores = []
        for nx in lineas_a_revisar:
            for ny in range(len(self._cancha.get_matriz_cancha()[nx])):
                jugador = self._cancha.get_matriz_cancha()[nx][ny]
                jugador_objeto = self._obtener_jugador_objeto(jugador)
                if (
                    jugador != "0"
                    and jugador != str(self._jugador_con_pelota)
                    and jugador_objeto
                ):
                    posibles_receptores.append(jugador_objeto)
        return posibles_receptores

    def _obtener_jugador_objeto(self, jugador):
        for fila in self._equipo_con_posecion.get_matriz_jugadores():
            for j in fila:
                if str(j) == jugador:
                    return j
        return None

    def _calcular_efectividad_pase(self, jugador_origen):
        atributo_pase = int(jugador_origen.get_pase())
        probabilidad = random.randint(0, 100)
        print("el atributo pase:", atributo_pase)
        return probabilidad <= atributo_pase

    def _encontrar_jugador_contrario_mas_cercano(self, posicion):
        x, y = posicion
        jugadores_contrarios = []
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self._cancha.get_matriz_cancha()) and 0 <= ny < len(
                self._cancha.get_matriz_cancha()[0]
            ):
                jugador = self._cancha.get_matriz_cancha()[nx][ny]
                if jugador != "0" and jugador not in [
                    str(j)
                    for fila in self._equipo_con_posecion.get_matriz_jugadores()
                    for j in fila
                ]:
                    jugadores_contrarios.append((nx, ny, jugador))
        return jugadores_contrarios[0] if jugadores_contrarios else None

    def pase(self):
        posibles_receptores = self._mostrar_opciones_pase()
        if not posibles_receptores:
            print("No hay jugadores disponibles para recibir el pase.")
            return

        jugador_destino = self._seleccionar_destino(posibles_receptores)
        print(f"{self._jugador_con_pelota} intenta pasar el balón a {jugador_destino}.")
        if self._calcular_efectividad_pase(self._jugador_con_pelota):
            print(
                f"{self._jugador_con_pelota} ha pasado el balón exitosamente a {jugador_destino}."
            )
            self._jugador_con_pelota = jugador_destino
        else:
            print(f"{self._jugador_con_pelota} falló el pase.")
            self._manejar_pase_fallido()

    def _seleccionar_destino(self, posibles_receptores):
        if self._equipo_con_posecion == self._jugador1:
            while True:
                try:
                    seleccion = (
                        int(
                            input(
                                "Selecciona el número del jugador al que quieres pasar el balón: "
                            )
                        )
                        - 1
                    )
                    if 0 <= seleccion < len(posibles_receptores):
                        return posibles_receptores[seleccion]
                    else:
                        print("Selección no válida. Inténtalo de nuevo.")
                except ValueError:
                    print("Entrada no válida. Por favor, introduce un número.")
        else:
            seleccion = random.randint(0, len(posibles_receptores) - 1)
            jugador_destino = posibles_receptores[seleccion]
            print(f"CPU pasa el balón a {jugador_destino}.")
            return jugador_destino

    def _manejar_pase_fallido(self):
        posicion_actual = self._encontrar_posicion_jugador(self._jugador_con_pelota)
        jugador_contrario = self._encontrar_jugador_contrario_mas_cercano(
            posicion_actual
        )
        if jugador_contrario:
            x, y, jugador_mas_cercano = jugador_contrario
            print(f"{jugador_mas_cercano} toma la posesión del balón.")
            self._jugador_con_pelota = jugador_mas_cercano
            self._equipo_con_posecion = (
                self._jugador2
                if self._equipo_con_posecion == self._jugador1
                else self._jugador1
            )

    def jugar_partido(self):
        self._equipo_con_posecion = self._jugador1
        self._jugador_con_pelota = self._jugador1.get_matriz_jugadores()[0][3]

        self._partido_en_curso = True

        if self._cronometro is None or not self._cronometro.is_alive():
            self._cronometro = Cronometro()
            self._cronometro.start()

        while self._partido_en_curso:
            if self._cronometro._evento_partido_terminado.is_set():
                self._partido_en_curso = False
            else:
                if self._equipo_con_posecion == self._jugador1:
                    time.sleep(1)
                    print(
                        f"{self._jugador_con_pelota} tiene la pelota, ¿qué desea hacer?:\n 1 - Pase "
                    )
                    decision = int(input("Seleccione alguna opción...  "))
                    match decision:
                        case 1:
                            self.pase()
                else:
                    print(
                        f"{self._jugador_con_pelota} tiene la pelota, CPU está tomando una decisión..."
                    )
                    self.pase()

        print("Fin del partido")
        self._cronometro.join()


equipo1 = Equipo(1, "P1", 111)

doparti = Partido(equipo1)
doparti.mapear_cancha()
doparti.jugar_partido()
