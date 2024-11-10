from AbmCarta import AbmCarta
from AbmEquipo import AbmEquipo
from Equipo import Equipo

########## ABM CARTA ##########

abmC = AbmCarta()
jugador = abmC.get_por_id(41)
print(jugador)
# abm.close()

########## ABM EQUIPO ##########

# Creación de equipo
equipo2 = Equipo(200, "equipo2", 2)

# abm equipo
abmE = AbmEquipo()

# Agregar equipo a la BDD
# abmE.insertar(equipo2)

# Devuelve el equipo por id
equipo = abmE.get_por_id(200)
print(equipo.get_id_equipo())  # imprimo su id

# Devuelve todos los equipos
equipos = abmE.get_all()
for equipo in equipos:  # imprimo todos sus ids
    print(equipo.get_id_equipo())

# Actualizar equipo en la BDD
equipo2_actualizado = Equipo(
    200, "equipo2.0", 2
)  # el mismo id pero le cambio el nombre
abmE.actualizar(equipo2_actualizado)

# Borrado lógico de equipo en la BDD
# abmE.borrar(200)
