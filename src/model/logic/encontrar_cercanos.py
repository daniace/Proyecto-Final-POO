from collections import deque

"MATRIZ DEBERIA SER LA CANCHA DE FUTBOL"


def encontrar_jugadores(matriz, punto_referencia, numero):
    filas = len(matriz)
    columnas = len(matriz[0])
    visitado = [[False for _ in range(columnas)] for _ in range(filas)]
    movimientos = [
        # (-1, 0), para que no evalue para atras
        (1, 0),
        (0, -1),
        (0, 1),
    ]  # Movimientos posibles: arriba, abajo, izquierda, derecha

    fila_inicio, columna_inicio = punto_referencia
    cola = deque([(fila_inicio, columna_inicio, 0)])  # (fila, columna, distancia)
    visitado[fila_inicio][columna_inicio] = True

    puntos_cercanos = []

    while cola:
        fila_actual, columna_actual, distancia = cola.popleft()

        # Verificar si encontramos un 1
        if matriz[fila_actual][columna_actual] == numero:
            puntos_cercanos.append(((fila_actual, columna_actual), distancia))
            if len(puntos_cercanos) > 4:
                puntos_cercanos.sort(key=lambda x: x[1])
                puntos_cercanos.pop()
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
    return puntos_cercanos


# Si no se encuentra un 1 en la matriz
matriz = [
    [0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 0, 2, 0, 2, 0, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [2, 0, 2, 0, 2, 0, 2],
    [0, 0, 1, 0, 1, 0, 0],
    [2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 2, 0, 0, 0],
]

for fila in matriz:
    print(fila)


def invertir_matriz_verticalmente(matriz):
    return matriz[::-1]


"integrar esto para que en el contrataque de la maquina"


# punto_referencia = (3, 0)
# puntos_cercanos = encontrar_jugadores(matriz, punto_referencia, 1)
# for punto, distancia in puntos_cercanos:
#     print(f"El 1 está en la posición {punto} a una distancia de {distancia}")
# print()
# puntos_cercanos = encontrar_jugadores(matriz, punto_referencia, 2)
# for punto, distancia in puntos_cercanos:
#     print(f"El 2 está en la posición {punto} a una distancia de {distancia}")
