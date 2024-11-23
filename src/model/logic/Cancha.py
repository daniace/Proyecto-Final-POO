from .EquipoLogico import EquipoLogico
from collections import deque

class Cancha:
    def __init__(self, equipo1, equipo2) -> None:
        self._equipo1 = equipo1
        self._equipo2 = equipo2
        self._cancha = [[0 for _ in range(8)] for _ in range(8)]
        self._diccionario_equipo1 = None
        self._diccionario_equipo2 = None
        self._diccionario_completo = None
        self.mapear_cancha()

    def get_matriz_cancha(self):
        return self._cancha

    def mostrar_cancha(self):
        for i in self._cancha:
            print(i)

    def get_diccionario_equipo1(self):
        return self._diccionario_equipo1

    def get_diccionario_equipo2(self):
        return self._diccionario_equipo2
    
    def get_diccionario(self):
        return self._diccionario_completo

    def mapear_cancha(self):
        # equipo 1 (jugador 1)
        self._cancha[0] = self._equipo1.get_distribucion()[0]
        self._cancha[1] = self._equipo1.get_distribucion()[1]
        self._cancha[3] = self._equipo1.get_distribucion()[2]
        self._cancha[5] = self._equipo1.get_distribucion()[3]
        # equipo 2 (jugador 2)
        self._cancha[7] = self._equipo2.get_distribucion()[0]
        self._cancha[6] = self._equipo2.get_distribucion()[1]
        self._cancha[4] = self._equipo2.get_distribucion()[2]
        self._cancha[2] = self._equipo2.get_distribucion()[3]
        "Te devuelve como deben ir en la cancha"
        self.obtener_diccionario_jugadores()  # una vez se setean los equipos, se debe generar el diccionario

    def obtener_diccionario_jugadores(self):
        # self._diccionario_equipo1 = {}
        # self._diccionario_equipo2 = {}
        self._diccionario_completo = {}
        jugador_index = 0
        jugador_index2 = 0
        equipo1 = self._equipo1.get_jugadores()
        equipo2 = self._equipo2.get_jugadores()[::-1]

        for i in range(len(self._cancha)):
            for j in range(len(self._cancha[i])):
                if (
                    self._cancha[i][j] == self._equipo1.get_nro_equipo()
                ):  # NRO_EQUIPO TIENE 1 O 2
                    # self._diccionario_equipo1[(i, j)] = equipo1[jugador_index]
                    self._diccionario_completo[(i, j)] = equipo1[jugador_index]
                    jugador_index += 1
                if self._cancha[i][j] == self._equipo2.get_nro_equipo():
                    # self._diccionario_equipo2[(i, j)] = equipo2[jugador_index2]
                    self._diccionario_completo[(i, j)] = equipo2[jugador_index2]
                    jugador_index2 += 1
                    
        # return diccionario_jugadores_equipo1, diccionario_jugadores_equipo2

    def mostrar_diccionario(self):
        # print("DICCIONARIO EQUIPO 1")
        # for clave, valor in self._diccionario_equipo1.items():
        #     print(f"{clave}: {valor}")

        # print("Diccionario EQUIPO 2")
        # for clave, valor in self._diccionario_equipo2.items():
        #     print(f"{clave} : {valor}")
        
        print("Diccionario COMPLETO")
        for clave, valor in self._diccionario_completo.items():
            print(f"{clave} : {valor}")
    "No es necesario separarlos en distintos diccionarios, es mas practico tener un solo diccionario con todos los jugadores"

    def imprimir_jugadores(self,lista_jugadores):
        for i,j in lista_jugadores:
            print(">",str(i),self._diccionario_completo.get(i,"sorry brodel, no esta"), "esta a una distancia de ", j)
    
    def buscar_jugador(self, posicion):
        # posicion = jugador
        return self._diccionario_completo.get(posicion, None)
            
    def encontrar_puntos_cercanos(self, posicion, tipo_busqueda):
        filas = len(self._cancha)
        columnas = len(self._cancha[0])
        visitado = [[False for _ in range(columnas)] for _ in range(filas)]
        
        fila_inicio, columna_inicio = posicion
        equipo_con_posesion = self._cancha[fila_inicio][columna_inicio]

        movimientos = [
            (1, 0),  # Abajo
            (0, -1),  # Izquierda
            (0, 1),  # Derecha
            (-1, 0)  # Arriba
        ]
        
        cola = deque([(fila_inicio, columna_inicio, 0)])  # (fila, columna, distancia)
        visitado[fila_inicio][columna_inicio] = True

        puntos_cercanos = []
        while cola:
            fila_actual, columna_actual, distancia = cola.popleft()

            if len(puntos_cercanos) >= 4:
                break

            if tipo_busqueda == "aliado":
                if self._cancha[fila_actual][columna_actual] == equipo_con_posesion and distancia != 0:
                    puntos_cercanos.append(((fila_actual, columna_actual), distancia))
            elif tipo_busqueda == "enemigo":
                
                if len(puntos_cercanos) >= 1:
                    break
                
                if self._cancha[fila_actual][columna_actual] != equipo_con_posesion and self._cancha[fila_actual][columna_actual] != 0:
                    puntos_cercanos.append(((fila_actual, columna_actual), distancia))

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
        
        # Filtrar y ordenar los puntos según el tipo de búsqueda
        if tipo_busqueda == "aliado":
            if equipo_con_posesion == 1:
                # Filtrar para que el equipo 1 avance hacia abajo (mayor fila primero)
                puntos_cercanos = [punto for punto in puntos_cercanos if punto[0][0] >= fila_inicio]
                puntos_cercanos.sort(key=lambda x: (x[1], -x[0][0]))
            else:
                # Filtrar para que el equipo 2 avance hacia arriba (menor fila primero)
                puntos_cercanos = [punto for punto in puntos_cercanos if punto[0][0] <= fila_inicio]
                puntos_cercanos.sort(key=lambda x: (x[1], x[0][0]))
            return puntos_cercanos
        elif tipo_busqueda == "enemigo":
            # Ordenar para que los enemigos más cercanos estén primero
            puntos_cercanos.sort(key=lambda x: x[1])
            return puntos_cercanos [0]
  
    "FUNCION MODIFICADA "
    "NOTA --> Se ingresa una posicion y un TIPO de busqueda"
    "Se retorna una lista de tuplas con los puntos cercanos y la distancia"
    "Si se ingresa 'aliado' busca los aliados mas cercanos, priorizando los que estan mas cerca del arco enemigo"
    "Si se ingresa 'enemigo' busca los enemigos mas cercanos, priorizando los que estan mas cerca del punto ingresado"


"ELIMINAR FUNCIONES DE LOS DICCIONARIOS PARCIALES Y COSAS COMENTADAS QUE NO SE USAN"