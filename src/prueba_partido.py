from model.logic.Partido import Partido
from model.logic.EquipoLogico import EquipoLogico
from model.logic.Dificultades import *
from model.logic.Cancha import *
e = EquipoLogico('leo')
e2 = EquipoLogico('leo2',es_cpu=True)

cancha = Cancha(e,e2)
cancha.mostrar_cancha()
diccionario = cancha.get_diccionario()
print()
for i,j in diccionario.items():
    print(i,j)

    ((0,0),jugador)
    ()[0][0]
# e.mostrar_plantilla_lista()
# p = Partido(e, Facil())
# print(p.get_diccionario())
# p.jugar_partido()