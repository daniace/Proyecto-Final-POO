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
    formacion_usuario = FORMACION_USUARIO["4-3-3"]
    formacion_cpu = FORMACION_CPU["4-3-3"]

    posiciones = {
        0: ("portero", formacion_usuario),
        1: ("defensas", formacion_usuario),
        2: ("delanteros", formacion_cpu),
        3: ("mediocampistas", formacion_usuario),
        4: ("mediocampistas", formacion_cpu),
        5: ("delanteros", formacion_usuario),
        6: ("defensas", formacion_cpu),
        7: ("portero", formacion_cpu)
    }

    indices = {i: 0 for i in range(8)}
    diccionario_jugadores = {}

    for coordenada in diccionario_1.keys():
        tipo, formacion = posiciones[coordenada[0]]
        diccionario_jugadores[coordenada] = formacion[tipo][indices[coordenada[0]]]
        indices[coordenada[0]] += 1

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