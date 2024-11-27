from model.logic.Partido import Partido
from model.logic.EquipoLogico import EquipoLogico
from model.logic.Dificultades import *
from model.logic.Cancha import *
e = EquipoLogico('leo')
e2 = EquipoLogico('leo2',es_cpu=True)
FORMACION_USUARIO={
    "4-3-3": {
        "portero": [(133, 92)],
        "defensas": [(111,128), (161,129),(213,142),(55,141)],
        "mediocampistas": [(137,188),(184,198),(88,197)],
        "delanteros": [(185,264),(138,275),(88,262)],
    },
    "4-4-2": {
        "portero": [(133, 92)],
        "defensas": [(103,129), (168,127),(207,142 ),(64,143)],
        "mediocampistas": [(135,174),(204,208),(69,207),(134,254 )],
        "delanteros": [(183,292),(84,295)],
    },
}
FORMACION_CPU={
    "4-3-3": {
        "portero": [(137,320)],
        "defensas": [(159,289),(111,290),(214,273),(55,273)],
        "mediocampistas": [(183,213),(136,221),(90,213)],
        "delanteros": [(178,150),(134,142),(88,151)],
    }}

def relacionar_posiciones(diccionario_1):
        diccionario = diccionario_1
        formacion_usuario = FORMACION_USUARIO["4-3-3"]
        formcion_cpu = FORMACION_CPU["4-3-3"]
        
        diccionario_jugadores = {}
        indice1 = 0
        indice2 = 0
        indice3 = 0
        indice4 = 0
        indice5 = 0
        indice6 = 0
        
        for coordenada in diccionario.keys():
            
            if coordenada[0] == 0:
                diccionario_jugadores[coordenada] = formacion_usuario["portero"][0]
            
            if coordenada[0] == 1:
                diccionario_jugadores[coordenada] = formacion_usuario["defensas"][indice1]
                indice1 +=1
            
            if coordenada[0] == 2:
                diccionario_jugadores[coordenada] = formcion_cpu["delanteros"][indice2]
                indice2 +=1
            
            if coordenada[0] == 3:
                diccionario_jugadores[coordenada] = formacion_usuario["mediocampistas"][indice3]
                indice3 +=1
                
            if coordenada[0] == 4:
                diccionario_jugadores[coordenada] = formcion_cpu["mediocampistas"][indice4]
                indice4 +=1
                
            if coordenada[0] == 5:
                diccionario_jugadores[coordenada] = formacion_usuario["delanteros"][indice5]
                indice5 +=1
                
            if coordenada[0] == 6:
                diccionario_jugadores[coordenada] = formcion_cpu["defensas"][indice6]
                indice6 +=1
                
            if coordenada[0] == 7:
                diccionario_jugadores[coordenada] = formcion_cpu["portero"][0]
        return diccionario_jugadores

cancha = Cancha(e,e2)
cancha.mostrar_cancha()
diccionario = cancha.get_diccionario()
print()
for i,j in diccionario.items():
    print(i,j)

print()
# diccionario = diccionario.keys()
diccionario2 = relacionar_posiciones(diccionario)
for i,j in diccionario2.items():
    print(i,j)

print('pelota en posicion --> ',diccionario2[(0,3)])

# e.mostrar_plantilla_lista()
# p = Partido(e, Facil())
# print(p.get_diccionario())
# p.jugar_partido()