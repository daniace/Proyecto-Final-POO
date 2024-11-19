import random

class Acciones:
    def __init__(self, dificultad):
        self._dificultad = dificultad

    def calcular_efectividad(self, jugador, metodo_atributo, descripcion):
        atributo = int(getattr(jugador, metodo_atributo)())
        probabilidad = random.randint(0, self._dificultad.get_probabilidad())
        if metodo_atributo == 'get_disparo':

            if jugador.get_posicion()[0] == 'ARQUERO':
                print('HOALAAA')
                atributo = atributo * 0.2
            if jugador.get_posicion()[0] == 'DEFENSA':
                atributo = atributo * 0.4            
            if jugador.get_posicion()[0] == 'MEDIOCAMPISTA':
                atributo = atributo * 0.5
        print(f"Probabilidad de {descripcion} correcta: ", str(int((atributo * 100)/self._dificultad.get_probabilidad())))
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


'COSAS PARA IMPLEMENTAR'
'- INTEGRAR LA VELOCIDADD, FISICO Y LA DEFENSA PARA LA INTERCEPCION'
'- INTEGRAR LA GAMBETA PARA QUE TE HABILITE TIRAR UN PASE SI O SI (EL ENEMIGO NO PUEDE INTERCEPTAR)'
'- INTEGRAR LA VELOCIDAD AL TIRO'

