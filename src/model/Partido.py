from EquipoLogico import Equipo
from collections import deque

# from formacion import *
from Cancha import Cancha


class Partido:
    def __init__(self, jugador1):
        self._jugador1 = jugador1
        self._jugador2 = Equipo("CPU FC", 2)
        self._partido_en_curso = True
        self._cronometro = None
        self._cancha = Cancha(self._jugador1, self._jugador2)
        self._equipo_con_posesion = None  # EQUIPO 1 O EQUIPO 2
        self._posicion_pelota = None
        # self._dificultad=dificultad# para empezar a programar

    def _jugador_con_pelota(self):
        jugador = self._cancha.get_diccionario_equipo1().get(
            self._posicion_pelota, None
        )
        if jugador is None:
            jugador = self._cancha.get_diccionario_equipo2().get(
                self._posicion_pelota, None
            )
        return jugador

    "BUSCA EN LOS DICCIONARIOS QUE JUGADOR TIENE LA PELOTA, SI NO ESTA EN EL DICCIONARIO DEVUELVE NONE"

    def puntos_cercanos(self):
        matriz = self._cancha.get_matriz_cancha()

        filas = len(matriz)
        columnas = len(matriz[0])
        visitado = [[False for _ in range(columnas)] for _ in range(filas)]
        if self._equipo_con_posesion == 1:
            movimientos = [
                (1, 0),  # Abajo
                (0, -1),  # Izquierda
                (0, 1),  # Derecha
            ]
        else:
            movimientos = [
                (-1, 0),  # Arriba
                (0, -1),  # Izquierda
                (0, 1),  # Derecha
            ]

        "La idea es buscar pases para avanzar hacia el arco del enemigo"
        "Como es una matriz vertical, el equipo 1 avanza hacia abajo y el equipo 2 hacia arriba"

        fila_inicio, columna_inicio = self._posicion_pelota
        cola = deque([(fila_inicio, columna_inicio, 0)])  # (fila, columna, distancia)
        visitado[fila_inicio][columna_inicio] = True

        aliados_cercanos = []
        enemigos_cercanos = []

        while cola:
            fila_actual, columna_actual, distancia = cola.popleft()

            # Verificar si encontramos un 1
            if (
                matriz[fila_actual][columna_actual] == self._equipo_con_posesion
                and distancia != 0
            ):
                aliados_cercanos.append(((fila_actual, columna_actual), distancia))
                if len(aliados_cercanos) > 4:
                    aliados_cercanos.sort(key=lambda x: x[1])
                    aliados_cercanos.pop()
            elif (
                matriz[fila_actual][columna_actual] != self._equipo_con_posesion
                and matriz[fila_actual][columna_actual] != 0
            ):
                enemigos_cercanos.append(((fila_actual, columna_actual), distancia))
                if len(enemigos_cercanos) > 4:
                    enemigos_cercanos.sort(key=lambda x: x[1])
                    enemigos_cercanos.pop()

            # Explorar los vecinos
            for movimiento in movimientos:
                nueva_fila = fila_actual + movimiento[0]
                nueva_columna = columna_actual + movimiento[1]

                if (
                    0 <= nueva_fila < filas
                    and 0 <= nueva_columna < columnas
                    and not visitado[nueva_fila][nueva_columna]
                ):
                    visitado[nueva_fila][nueva_columna] = True
                    cola.append((nueva_fila, nueva_columna, distancia + 1))
        return aliados_cercanos, enemigos_cercanos

    "SE PUEDE MODIFICAR PARA QUE TIRE DIRECTAMENTE LOS ALIADOS Y ENEMIGOS MAS CERCANOS"
    "NOTA SEPARAR LA FUNCION EN DOS, UNA QUE BUSQUE ALIADOS Y OTRA QUE BUSQUE ENEMIGOS"
    "ASI BUSCAR EL ENEMIGO MAS CERCANO AL JUGADOR QUE SE LE HACE EL PASE, NO AL QUE TIENE LA PELOTA ACTUAL"
    "ADEMAS DE HACER MAS LEGIBLE EL CODIGO"


e = Equipo("leo", 1)
p = Partido(e)
p._cancha.mostrar_cancha()
print()

p._posicion_pelota = (0, 3)
p._equipo_con_posesion = 1
aliados, enemigos = p.puntos_cercanos()
print("aliados: ", aliados)
print()
print("enemigos: ", enemigos)


# print("posibles pases: \n")
# p._posicion_pelota = (7, 3)
# p._equipo_con_posesion = 2
# print(p.jugadores_cercanos(2))
# print()
# print("posibles interceptores: \n")
# print(p.jugadores_cercanos(1))
