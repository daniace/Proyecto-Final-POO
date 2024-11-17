from EquipoLogico import EquipoLogico
from collections import deque
from Cancha import Cancha
from Cronometro import Cronometro
from Dificultades import *
import random
import time

class Partido:
    def __init__(self, jugador1:EquipoLogico,dificultad:Dificultad):
        self._jugador1 = jugador1
        self._jugador2 = EquipoLogico("CPU FC", 2)
        self._partido_en_curso = True
        self._cronometro = None
        self._cancha = Cancha(self._jugador1, self._jugador2)
        self._equipo_con_posesion = 1  # EQUIPO 1 O EQUIPO 2
        self._posicion_pelota = (0,3)
        self._dificultad=dificultad

    def _jugador_con_pelota(self):
        jugador = self._cancha.get_diccionario_equipo1().get(self._posicion_pelota, None)
        if jugador is None:
            jugador = self._cancha.get_diccionario_equipo2().get(self._posicion_pelota, None)
        return jugador

    def imprimir_jugadores(self,lista_jugadores):
        for i,j in lista_jugadores:
            print(str(i),self._cancha.get_diccionario_equipo1().get(i,"sorry brodel, no esta"), "esta a una distancia de ", j)

    def puntos_cercanos(self):
        print("entra a puntos cercanos")
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

        fila_inicio, columna_inicio = self._posicion_pelota
        cola = deque([(fila_inicio, columna_inicio, 0)])  # (fila, columna, distancia)
        visitado[fila_inicio][columna_inicio] = True

        aliados_cercanos = []
        enemigos_cercanos = []

        while cola:
            fila_actual, columna_actual, distancia = cola.popleft()

            if matriz[fila_actual][columna_actual] == self._equipo_con_posesion and distancia != 0:
                aliados_cercanos.append(((fila_actual, columna_actual), distancia))
                if len(aliados_cercanos) > 4:
                    aliados_cercanos.sort(key=lambda x: x[1])
                    aliados_cercanos.pop()
            elif matriz[fila_actual][columna_actual] != self._equipo_con_posesion and matriz[fila_actual][columna_actual] != 0:
                enemigos_cercanos.append(((fila_actual, columna_actual), distancia))
                if len(enemigos_cercanos) > 4:
                    enemigos_cercanos.sort(key=lambda x: x[1])
                    enemigos_cercanos.pop()

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

    def _calcular_efectividad_pase(self, jugador_origen):
        atributo_pase = int(jugador_origen.get_pase())
        print("probabilidad de pase correcto: ",atributo_pase)# Obtener el atributo de pase del jugador
        probabilidad = random.randint(0, self._dificultad.get_probaibilidad())
        return probabilidad <= atributo_pase

    def realizar_pase(self):
        print("entra a realizar pase")
        aliados_cercanos, _ = self.puntos_cercanos()
        if not aliados_cercanos:
            print("No hay jugadores disponibles para recibir el pase.")
            return
        
        self.imprimir_jugadores(aliados_cercanos)
        decision=(int(input("\nseleccione opcion de pase : ")))
        
        while decision > len(aliados_cercanos) or decision == 0:
            decision= int(input(("\n selccion no valida... selccione un pase")))
        aliado_destino = aliados_cercanos[decision-1][0]# seleciona al jugador que uno eligio
        
        jugador_con_pelota = self._jugador_con_pelota()
        
        if not jugador_con_pelota:
            print("No se encontró al jugador con la pelota.")
            return

        print(f"Pase de {self._posicion_pelota} a {aliado_destino}.")
        
        if self._calcular_efectividad_pase(jugador_con_pelota):
            print("El pase fue exitoso.")
            self._posicion_pelota = aliado_destino
        else:
            print("El pase fue interceptado.")
            self._posicion_pelota = aliado_destino  # Actualiza la posición para la recuperación
            self.perder_posesion()

    def perder_posesion(self):
        _, enemigos_cercanos = self.puntos_cercanos()
        if not enemigos_cercanos:
            print("No hay jugadores enemigos cercanos para recuperar la pelota.")
            return

        enemigo_mas_cercano = enemigos_cercanos[0][0]  # Elige el enemigo más cercano
        print(f"La pelota es recuperada por el jugador en la posición {enemigo_mas_cercano}.")
        self._posicion_pelota = enemigo_mas_cercano
        self._equipo_con_posesion = 1 if self._equipo_con_posesion == 2 else 2
    
    def jugar_partido(self):
        
        self._partido_en_curso = True

        if self._cronometro is None or not self._cronometro.is_alive():
            self._cronometro = Cronometro()
            self._cronometro.start()

        while self._partido_en_curso:
            if self._cronometro._evento_partido_terminado.is_set():
                self._partido_en_curso = False
            else:
                if self._equipo_con_posesion == 1:
                    time.sleep(1)
                    print(f"{self._jugador_con_pelota()} tiene la pelota, ¿qué desea hacer?:\n 1 - Pase ")
                    decision = int(input("Seleccione alguna opción...  "))
                    match decision:
                        case 1:
                            self.realizar_pase()
                else:
                    print(f"{self._jugador_con_pelota()} tiene la pelota, CPU está tomando una decisión...")
                    self.realizar_pase()

        print("Fin del partido")
        self._cronometro.join()



# Ejemplo de uso
e = EquipoLogico("leo", 1)
p = Partido(e)
p._cancha.mostrar_cancha()
print()
p.jugar_partido()

# cosas que hacer:
# metodo patear
# programar IA
# dificultades (facil, medio, dificil)#
