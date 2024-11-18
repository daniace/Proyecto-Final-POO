import random

class Acciones:
    def __init__(self, dificultad):
        self._dificultad = dificultad

    def calcular_efectividad(self, jugador, metodo_atributo, descripcion):
        atributo = int(getattr(jugador, metodo_atributo)())
        print(f"Probabilidad de {descripcion} correcta: ", atributo)
        probabilidad = random.randint(0, self._dificultad.get_probaibilidad())
        return probabilidad <= atributo
        "Si no funciona sacar getattr"

    def calcular_efectividad_pase(self, jugador):
        return self.calcular_efectividad(jugador, 'get_pase', 'pase')

    def calcular_efectividad_tiro(self, jugador):
        return self.calcular_efectividad(jugador, 'get_disparo', 'tiro')

    def calcular_efectividad_intercepcion(self, jugador):
        return self.calcular_efectividad(jugador, 'get_defensa', 'intercepción')

    def calcular_efectividad_atajar(self, jugador):
        return self.calcular_efectividad(jugador, 'get_gk_handling', 'atajar')



