# from database.AbmCarta import AbmCarta
# from database.AbmEquipo import AbmEquipo
# from database.Equipo import Equipo
from Usuario import Usuario
from AbmUsuario import AbmUsuario

########## ABM CARTA ##########

# abmC = AbmCarta()
# jugador = abmC.get_por_id(41)
# print(jugador, type(jugador))
# abm.close()

########## ABM EQUIPO ##########

# # Creación de equipo
# equipo2 = Equipo(200, "equipo2", 2)

# # abm equipo
# abmE = AbmEquipo()

# # Agregar equipo a la BDD
# # abmE.insertar(equipo2)

# # Devuelve el equipo por id
# equipo = abmE.get_por_id(200)
# print(equipo.get_id_equipo())  # imprimo su id

# # Devuelve todos los equipos
# equipos = abmE.get_all()
# for equipo in equipos:  # imprimo todos sus ids
#     print(equipo.get_id_equipo())

# # Actualizar equipo en la BDD
# equipo2_actualizado = Equipo(
#     200, "equipo2.0", 2
# )  # el mismo id pero le cambio el nombre
# abmE.actualizar(equipo2_actualizado)

# # Borrado lógico de equipo en la BDD
# # abmE.borrar(200)

########## ABM USUARIO ##########

usuario = Usuario(None, "user")
abmU = AbmUsuario()
abmU.insertar(usuario)
