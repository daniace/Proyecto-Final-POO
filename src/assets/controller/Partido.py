import random
"IDEAS PARA LA PARTE DE ZONAS, MAPA Y MOVIMIENTO"

# class Zona:
#     def __init__(self, nombre, dificultad_pase, dificultad_tiro):
#         self.nombre = nombre
#         self.dificultad_pase = dificultad_pase
#         self.dificultad_tiro = dificultad_tiro 
#         "Esto esta bueno, si es que cada jugador puede hacer todas las acciones"
#
#     def calcular_exito(self,habilidad_jugador, dificultad_zona):
#         # Porcentaje de éxito en función de la habilidad y la dificultad de la zona
#         chance_exito = habilidad_jugador - dificultad_zona
#         return random.randint(0, 100) < chance_exito

#     def mover_jugador(self,jugador, zona_actual, zona_destino):
#         # Calcular si el jugador puede moverse a la zona destino
#         exito = self.calcular_exito(jugador.habilidad_pase, zona_actual.dificultad_pase)
#         if exito:
#             return zona_destino
#         else:
#             return zona_actual  # Se mantiene en la zona actual si falla
#         "SE MUEVE DE UNA ZONA A OTRA, NO POR COORDENADAS"

class Mapa:
    def __init__(self):
        self.zonas = [Zona("Defensa", 30, 0), Zona("Mediocampo", 20, 10), Zona("Ataque", 10, 30)]
        self.posicion_balon = self.zonas[1]  # Iniciar en mediocampo
#Los valores de zona es de otra clase Zona, que tenia como parametros probabilidad de pase, y probabilidad de tiro


    def mover_balon(self, zona_destino):
        if zona_destino in self.zonas:
            self.posicion_balon = zona_destino #unicamente mente mueve el balon de zona a otra :v
            
            
class Zona:
    def __init__(self, nombre, posiciones):
        self.nombre = nombre
        self.posiciones = posiciones  # Posiciones ocupadas en la zona 
        "Tupla"

    def agregar_jugador(self, jugador, posicion):
        self.posiciones[posicion] = jugador


class Evento:
    def __init__(self, tipo, jugador, exito):
        self.tipo = tipo
        self.jugador = jugador
        self.exito = exito

    def ejecutar(self):
        if self.exito:
            print(f"{self.jugador.nombre} ha tenido éxito en {self.tipo}")
        else:
            print(f"{self.jugador.nombre} ha fallado en {self.tipo}")
    'innecesario'

class Jugador:
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo
        self.posicion = None # Posición actual del jugador


def turno(jugador, mapa, accion):
    resultado = accion(jugador, mapa.posicion_balon)
    mapa.mover_balon(resultado)

def obtener_jugadores_adyacentes(zona, posicion_actual):
    "SE PODRIA AGREGAR UNA CONDICION QUE SE ELIJA PASE LARGO O CORTO y verifique los jugadores en base a eso"
    x, y = posicion_actual
    posiciones_adyacentes = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    jugadores_cercanos = {}

    for pos in posiciones_adyacentes:
        if pos in zona.posiciones and zona.posiciones[pos] is not None:
            jugadores_cercanos[pos] = zona.posiciones[pos]
    
    return jugadores_cercanos



def obtener_receptores_disponibles(zona, jugador_con_balon):
    jugadores_cercanos = obtener_jugadores_adyacentes(zona, jugador_con_balon.posicion)
    return {pos: jugador for pos, jugador in jugadores_cercanos.items() if jugador.equipo == jugador_con_balon.equipo}


def elegir_receptor(jugadores_disponibles, estrategia="cercano"):
    if estrategia == "cercano":
        return min(jugadores_disponibles.items(), key=lambda item: abs(item[0][0]) + abs(item[0][1]))
    # Aquí podrías agregar más estrategias



class Zonas:
    def __init__(self, nombre, ancho, alto):
        self.nombre = nombre  # Nombre de la zona (por ejemplo, "Mediocampo")
        self.ancho = ancho  # Ancho del campo (número de columnas)
        self.alto = alto    # Alto del campo (número de filas)
        self.campo = {}  # Diccionario para almacenar jugadores por coordenadas

    def agregar_jugador(self, jugador, x, y):
        """Agrega un jugador a la zona en las coordenadas (x, y)."""
        if self.es_posicion_valida(x, y):
            self.campo[(x, y)] = jugador
        else:
            print(f"Posición ({x}, {y}) fuera de los límites de la zona.")

    def quitar_jugador(self, x, y):
        """Quita un jugador de una posición específica."""
        if (x, y) in self.campo:
            del self.campo[(x, y)]
        else:
            print(f"No hay jugador en la posición ({x}, {y}).")

    def es_posicion_valida(self, x, y):
        """Verifica si una posición (x, y) es válida dentro de las dimensiones de la zona."""
        return 0 <= x < self.ancho and 0 <= y < self.alto

    def obtener_jugadores_adyacentes(self, x, y):
        """Devuelve un diccionario de jugadores adyacentes a la posición (x, y)."""
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha
        jugadores_adyacentes = {}

        for dx, dy in direcciones:
            nueva_x, nueva_y = x + dx, y + dy
            if self.es_posicion_valida(nueva_x, nueva_y) and (nueva_x, nueva_y) in self.campo:
                jugadores_adyacentes[(nueva_x, nueva_y)] = self.campo[(nueva_x, nueva_y)]
        
        return jugadores_adyacentes

defensa = Zonas("Defensa", 5, 3)
defensa.agregar_jugador("P1", 0, 0)
defensa.agregar_jugador("P2", 1, 0)
defensa.agregar_jugador("P3", 2, 0)
defensa.agregar_jugador("P4", 0, 1)
print(defensa.obtener_jugadores_adyacentes(0,0))