import random

class Acciones:
    def __init__(self, dificultad):
        self._dificultad = dificultad
        self._bonificacion_de_gambeta=False
    
    def set_valor_bonificacion(self,valor:bool):
        self._bonificacion_de_gambeta=valor
    
    def valor_bonificacion(self, metodo_atributo, jugador, atributo):
        posicion = jugador.get_posicion()[0]
        if metodo_atributo == 'get_pase' and posicion == 'DEFENSA':
            atributo *= 1.15 # 15% más de pase para defensas 
        elif metodo_atributo == 'get_pase' and posicion == 'MEDIOCAMPISTA':
            atributo *= 1.10 # 10% más de pase para mediocampistas 
        elif metodo_atributo == 'get_disparo' and posicion == 'MEDIOCAMPISTA':
            atributo *= 1.10 # 10% más de tiro para mediocampistas 
        elif metodo_atributo == 'get_disparo' and posicion == 'DELANTERO':
            atributo *= 1.15 # 15% más de tiro para delanteros
        return atributo

    "VERIFICAR SI BONIFICACION VUELVE A FALSE"

    def calcular_efectividad(self, jugador, equipo, metodo_atributo, descripcion):
        print(f'GAMBETA ACTIVA --> {self._bonificacion_de_gambeta}')
        
        atributo = int(getattr(jugador, metodo_atributo)())
        print(f'jugador', jugador)
        probabilidad = random.randint(0, self._dificultad.get_probabilidad() if equipo == 1 else 100)
        print('EQUIPO ACTUAL PROBABILIDAD--> ', equipo)
        print('probabilidad de 0 a ', self._dificultad.get_probabilidad() if equipo == 1 else 100)
        

        if self._bonificacion_de_gambeta:
            atributo = self.valor_bonificacion(metodo_atributo, jugador, atributo)

        if metodo_atributo == 'get_disparo':
            if jugador.get_posicion()[0] == 'ARQUERO':
                atributo = atributo * 0.2
            if jugador.get_posicion()[0] == 'DEFENSA':
                atributo = atributo * 0.4            
            if jugador.get_posicion()[0] == 'MEDIOCAMPISTA':
                atributo = atributo * 0.5        
        print(f"Probabilidad de {descripcion} correcta: ", str(int(atributo*100)/(self._dificultad.get_probabilidad() if equipo == 1 else 100)) + '%')
        print(f'{probabilidad} vs {atributo}')
        return probabilidad <= atributo
        "Si no funciona sacar getattr"

    def calcular_efectividad_pase(self, jugador, equipo):
        return self.calcular_efectividad(jugador, equipo, 'get_pase', 'pase')

    def calcular_efectividad_tiro(self, jugador,equipo):
        return self.calcular_efectividad(jugador,equipo, 'get_disparo', 'tiro')

    def calcular_efectividad_intercepcion(self, jugador, equipo):
        return self.calcular_efectividad(jugador,equipo, 'get_defensa', 'intercepción')

    def calcular_efectividad_atajar(self, jugador,equipo):
        return self.calcular_efectividad(jugador,equipo, 'get_handling', 'atajar')
    
    def calcular_efectividad_gambeta(self, jugador,equipo):
            return self.calcular_efectividad(jugador,equipo, 'get_gambeta', 'gambeta')


'COSAS PARA IMPLEMENTAR'
'- INTEGRAR LA VELOCIDADD, FISICO Y LA DEFENSA PARA LA INTERCEPCION'
'- INTEGRAR LA GAMBETA PARA QUE TE HABILITE TIRAR UN PASE SI O SI (EL ENEMIGO NO PUEDE INTERCEPTAR)'
'- INTEGRAR LA VELOCIDAD AL TIRO'

