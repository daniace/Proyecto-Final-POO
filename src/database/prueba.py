from AbmCarta import AbmCarta
from AbmEquipo import AbmEquipo
from Equipo import Equipo

##### ABM CARTA #####

abmC = AbmCarta()
jugador = abmC.get_por_id(41)
print(jugador)
# abm.close()

##### ABM EQUIPO #####

# Creación de equipo
equipo = Equipo(123, "equipo1", 1)
# abm equipo
abmE = AbmEquipo()
# Agregar equipo a la BDD
equipo = abmE.insertar(equipo)
