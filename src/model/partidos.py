from Cronometro import Cronometro
from Cancha import Cancha
from database.Equipo import Equipo
import time

class Partido:
    def __init__(self, jugador1: Equipo, jugador2: Equipo) -> None:
        self._jugador1 = jugador1
        self._jugador2 = jugador2
        self._partido_en_curso = True
        self._cronometro = None
        self._cancha = Cancha()
        self._equipo_con_posecion = None
        self._jugador_con_pelota = None

    def mapear_cancha(self):
        self._cancha.mapear_cancha(self._jugador1.get_matriz_jugadores(), self._jugador2.get_matriz_jugadores())
        self._cancha.mostrar_cancha()

    def _mostrar_opciones_pase(self):
        if self._jugador_con_pelota is None:
            print("No hay ningún jugador en posesión del balón.")
            return []

        # Convertir el jugador a string para comparación
        jugador_con_pelota_str = str(self._jugador_con_pelota)

        # Encontrar la posición del jugador con el balón en la matriz
        posicion_actual = None
        for i, linea in enumerate(self._cancha.get_matriz_cancha()):
            print(f"Revisando línea {i}: {linea}")
            if jugador_con_pelota_str in linea:
                posicion_actual = (i, linea.index(jugador_con_pelota_str))
                break

        if posicion_actual is None:
            print("No se pudo determinar la posición del jugador con el balón.")
            return []

        print(f"Posición del jugador con el balón: {posicion_actual}")

        x, y = posicion_actual
        posibles_receptores = []

        # Lógica de pase basada en la posición en la cancha
        lineas_a_revisar = []
        if x == 0:  # Arquero
            lineas_a_revisar = [1]
        elif x == 1:  # Defensa
            lineas_a_revisar = [0, 1, 3]
        elif x == 3:  # Mediocampo
            lineas_a_revisar = [1, 3, 5]
        elif x == 5:  # Delantero
            lineas_a_revisar = [3, 5]

        # Revisar las líneas específicas
        for nx in lineas_a_revisar:
            for ny in range(len(self._cancha.get_matriz_cancha()[nx])):
                jugador = self._cancha.get_matriz_cancha()[nx][ny]
                print(f"Revisando posición ({nx}, {ny}): {jugador}")

                # Verificación mejorada para asegurarse de que el jugador pertenece al equipo en posesión
                jugador_objeto = None
                for fila in self._equipo_con_posecion.get_matriz_jugadores():
                    for j in fila:
                        if str(j) == jugador:
                            jugador_objeto = j
                            break

                if jugador != '0' and jugador != jugador_con_pelota_str and jugador_objeto:
                    posibles_receptores.append(jugador_objeto)

        if not posibles_receptores:
            print("No hay jugadores disponibles para recibir el pase.")
            return []

        print(f"Jugadores disponibles para recibir el pase de {self._jugador_con_pelota}:")
        for i, jugador in enumerate(posibles_receptores):
            print(f"{i + 1}. {jugador}")
        return posibles_receptores

    def pase(self):
        posibles_receptores = self._mostrar_opciones_pase()
        if not posibles_receptores:
            print("No hay jugadores disponibles para recibir el pase.")
            return

        while True:
            try:
                seleccion = int(input("Selecciona el número del jugador al que quieres pasar el balón: ")) - 1
                if 0 <= seleccion < len(posibles_receptores):
                    jugador_destino = posibles_receptores[seleccion]
                    break
                else:
                    print("Selección no válida. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número.")

        print(f"{self._jugador_con_pelota} pasa el balón a {jugador_destino}.")
        self._jugador_con_pelota = jugador_destino  # Actualizar el jugador en posesión del balón

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
                time.sleep(1)
                print(f"{self._jugador_con_pelota} tiene la pelota, ¿qué desea hacer?:\n 1 - Pase ")
                desicion = int(input("Seleccione alguna opción...  "))
                match desicion:
                    case 1:
                        self.pase()  # Aquí estaría la lógica del juego

        print("Fin del partido")
        self._cronometro.join()

equipo1 = Equipo(1, "P1", 111)
equipo2 = Equipo(2, "P2", 222)

doparti = Partido(equipo1, equipo2)
doparti.mapear_cancha()
doparti.jugar_partido()

