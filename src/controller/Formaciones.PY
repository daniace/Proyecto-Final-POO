from abc import ABC, abstractmethod


class Formacion_Strategy (ABC):
    
    @abstractmethod
    def formacion (self, equipo): #aca se asignan tambien los atacantes y defensores
        pass
    
class Formacion_442 (Formacion_Strategy):
    
    def formacion (self, equipo):
         matriz = [[0,      equipo, 0, equipo, 0,   0,    0, 0],
                   [0,      equipo, 0, equipo, 0, equipo, 0, 0],
                   [equipo,   0,    0,   0,    0,   0,    0, 0],
                   [0,      equipo, 0, equipo, 0, equipo, 0, 0],
                   [0,      equipo, 0, equipo, 0,   0,    0, 0]
        ]
         return matriz
        #Aca se asignan las posiciones de los jugadores en la formacion 442
        #siendo 0 vacio, 1 equipo jugador y 2 equipo maquina

class Formacion_433 (Formacion_Strategy):
    
    def formacion (self, equipo):
        matriz = [[0,    equipo, 0,   0,    0,   0,    0, 0],
                  [0,    equipo, 0, equipo, 0, equipo, 0, 0],
                  [equipo, 0,    0, equipo, 0, equipo, 0, 0],
                  [0,    equipo, 0, equipo, 0, equipo, 0, 0],
                  [0,    equipo, 0,   0,    0,   0,    0, 0]
        ] 
        return matriz
    
class Formacion_352 (Formacion_Strategy):
    
    def formacion (self, equipo):
        matriz = [[0,        0,    0, equipo,    0,   0,    0, 0],
                  [0,      equipo, 0, equipo,    0, equipo, 0, 0],
                  [equipo, equipo, 0, equipo,    0,   0,    0, 0],
                  [0,      equipo, 0, equipo,    0, equipo, 0, 0],
                  [0,        0,    0, equipo,    0,   0,    0, 0]
        ]
        return matriz
    
    

class Plantilla:
    def __init__(self, equipo, jugadores ,formacion = Formacion_442):
        self.__equipo = equipo # si es 1 es el equipo del jugador, si es 2 es el equipo de la ma
        self.__jugadores = jugadores # lista de jugadores
        self.__formacion =  formacion #Se podria utilizar el patron strategy? para asignar directamente la formacion establecida
        #aca se asignaria la formacion a utilizar

    def set_formacion(self, formacion):
        self.__formacion = formacion
    
    def get_formacion(self):
        return self.__formacion.formacion(self.__equipo)
   
    def obtener_diccionario_jugadores(self, matriz, jugadores):
        diccionario_jugadores = {}
        jugador_index = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == 1:
                    diccionario_jugadores[(i, j)] = jugadores[jugador_index]
                    jugador_index += 1
        return diccionario_jugadores
    # requiere que se introduzca una lista de jugadores en el orden en que se encuentran en la matriz
    #devuelve diccionario de relacionando la posicion de la formacion con cada jugdor
    # adaptarlo para la maquina
    
def reflejar_matriz(matriz): 
    return [fila[::-1] for fila in matriz]
#VER DONDE METER ESTA FUNCION PARA REFLEJAR LA MATRIZ DE LA MAQUINA

# Ejemplo de uso
matriz_original = [
    [1, 1, 0, 1, 0, 0, 2, 0],
    [0, 1, 2, 1, 2, 1, 2, 0],
    [1, 0, 2, 0, 2, 0, 0, 2],
    [0, 1, 2, 1, 2, 1, 2, 0],
    [0, 1, 0, 1, 0, 0, 2, 0]
]

matriz_reflejada = reflejar_matriz(matriz_original)
print("Matriz Original:")
for fila in matriz_original:
    print(fila)

print("\nMatriz Reflejada:")
for fila in matriz_reflejada:
    print(fila)   
print()

jugadores  = ["Jugador1", "Jugador2", "Jugador3", "Jugador4", "Jugador5", "Jugador6", "Jugador7", "Jugador8"]
plantilla = Plantilla(1, jugadores, Formacion_352())
# print(plantilla.get_formacion())
print("FORMACION 352")
for fila in plantilla.get_formacion():
    print(fila)
print()
print("FORMACION 442")
plantilla.set_formacion(Formacion_442())
for fila in plantilla.get_formacion():
    print(fila)
print()
print("FORMACION 433")
plantilla.set_formacion(Formacion_433())
for fila in plantilla.get_formacion():
    print(fila)