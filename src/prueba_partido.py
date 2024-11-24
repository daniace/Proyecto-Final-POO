from model.logic.Partido import Partido
from model.logic.EquipoLogico import EquipoLogico
from model.logic.Dificultades import *

e = EquipoLogico('leo')
e.mostrar_plantilla_lista()
p = Partido(e, Facil())
p.jugar_partido()