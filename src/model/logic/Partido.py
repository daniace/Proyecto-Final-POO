from EquipoLogico import EquipoLogico
from Cancha import Cancha
from Cronometro import Cronometro
from Dificultades import *
import random
import time
from Acciones import Acciones

class Partido:
    def __init__(self, jugador1:EquipoLogico,dificultad:Dificultad):
        self._jugador1 = jugador1
        self._jugador2 = EquipoLogico("CPU FC", 2)
        self._partido_en_curso = True
        self._cronometro = None
        self._cancha = Cancha(self._jugador1, self._jugador2)
        self._equipo_con_posesion = 1  # EQUIPO 1 O EQUIPO 2
        self._posicion_pelota = (0,3)
        self._acciones = Acciones(dificultad) #VER SI ESTO QUEDA ASI

    def _jugador_con_pelota(self):
        return self._cancha.get_diccionario().get(self._posicion_pelota, None)
    "DEVUELVE EL JUGADOR EN BASE A LA POSICION ACTUAL DE LA PELOTA"
    
    def _cambio_equipo(self):
        "CAMBIA EL EQUIPO QUE TIENE LA PELOTA"
        self._equipo_con_posesion = 1 if self._equipo_con_posesion == 2 else 2

    def mostrar_pases(self, es_cpu=False):
        aliados_cercanos = self._cancha.encontrar_puntos_cercanos(self._posicion_pelota, 'aliado')
        
        if es_cpu:
            return aliados_cercanos[random.randint(0, len(aliados_cercanos)-1)][0]
        
        if not aliados_cercanos:
            print("No hay jugadores disponibles para recibir el pase.")
            return
        print("---------------------------------------------------------------------------------------")
        print("Pases disponibles")
        self._cancha.imprimir_jugadores(aliados_cercanos)
        print()
        decision=(int(input("\nSeleccione opcion de pase : ")))
        
        while decision > len(aliados_cercanos) or decision == 0 or decision < 0:
            decision= int(input(("\n selccion no valida... selccione un pase")))
        return aliados_cercanos[decision-1][0]# seleciona al jugador que uno eligio

    def realizar_pase(self, es_cpu=False):
        
        aliado_destino = self.mostrar_pases(es_cpu)
        jugador_con_pelota = self._jugador_con_pelota()
        
        print(f"Pase de {self._posicion_pelota} a {aliado_destino}.")
        
        if self._acciones.calcular_efectividad_pase(jugador_con_pelota):
                print("El pase fue exitoso.")
                self._posicion_pelota = aliado_destino
                return True
        else:
            print("El pase fue FALLADO.")
            self._posicion_pelota = self._cancha.encontrar_puntos_cercanos(self._posicion_pelota, 'enemigo') [0]# Actualiza la posición para la recuperación
            self._cambio_equipo()
            print('Pelota en -->',self._posicion_pelota, 'Equipo Actual --> ', self._equipo_con_posesion)
            return False

    'se cambia el equipo con la pelota en la intercepcion y se vuelve a cambiar si se intercepta'
    'se deberia comprobar la intercepcion cada vez que se hace un pase'
    def realizar_intercepcion (self):
        print('INTENTANDO INTERCEPTAR...')
        posicion_enemigo = self._cancha.encontrar_puntos_cercanos(self._posicion_pelota, 'enemigo') [0]
        # self._cancha.imprimir_jugadores(posicion_enemigo)
        print('ENEMIGO A INTERCEPTAR -->',posicion_enemigo)
        print()
        enemigo_cercano = self._cancha.buscar_jugador(posicion_enemigo)

        "ENEMIGO CERCANO DEBE SER UNO SOLO Y AGREGAR FUNCION QUE DEVUELVA QUE ENEMIGO ES"
        if self._acciones.calcular_efectividad_intercepcion (enemigo_cercano):
            print('SE INTERCEPTO LA PELOTA')
            self._posicion_pelota = posicion_enemigo
            self._cambio_equipo() #Se cambia el equipo que tiene la pelota
            return True
        else:
            print("Intercepcion Fallida")
            return False

    def realizar_atajar(self):
        "UNICAMENTE ATAJA CUANDO EL EQUIPO ENEMIGO TIRA AL ARCO"
        posicion_arquero = (0,3) if self._equipo_con_posesion == 2 else (7,3)
        arquero = self._cancha.buscar_jugador(posicion_arquero)
                
        self._posicion_pelota = posicion_arquero
        self._cambio_equipo()
        "Siempre que se tire al arco sale del arco"
        
        if self._acciones.calcular_efectividad_atajar(arquero):
            print("SE ATAJÓ EL TIRO")
            return True
        else:
            print('NO SE ATAJÓ EL TIRO')
            return False    
        
        
    def realizar_tiro(self):
        jugador_actual = self._cancha.buscar_jugador(self._posicion_pelota)

        
        if self._acciones.calcular_efectividad_tiro(jugador_actual):
            return True
        else:
            print("Se fallo el tiro")
            print('SALE DEL ARCO ENEMIGO')
            self._posicion_pelota = (0,3) if self._equipo_con_posesion == 2 else (7,3)
            self._cambio_equipo()
            return False
        
        
        
        
    def jugar_partido(self):
        
        self._partido_en_curso = True

        if self._cronometro is None or not self._cronometro.is_alive():
            self._cronometro = Cronometro()
            self._cronometro.start()

        while self._partido_en_curso:
            if self._cronometro._evento_partido_terminado.is_set():
                self._partido_en_curso = False
            else:
                if self._equipo_con_posesion == 1:
                    time.sleep(2)
                    print("---------------------------------------------------------------------------------------")
                    print("POSICION ACTUAL -->",self._posicion_pelota, ' Equipo Actual --> ', self._equipo_con_posesion)
                    print()
                    print(f"{self._jugador_con_pelota()} tiene la pelota, ¿qué desea hacer?:\n1 - Pase\n2 - Tiro")
                    decision = int(input("Seleccione alguna opción...  "))
                    match decision:
                        case 1:
                            self.realizar_pase()
                        case 2:
                            print('TIRO DEL JUGADOR 1')
                            if self.realizar_tiro():
                                if not self.realizar_atajar():
                                    print('GOOOOL DEL JUGADOR 1!!!')
                                    self._partido_en_curso = False
                        
                else:
                    print("---------------------------------------------------------------------------------------")
                    print(f"{self._jugador_con_pelota()} tiene la pelota, CPU está tomando una decisión...")
                    time.sleep(2)
                    decision = random.choice([1, 2])  # La CPU elige una acción al azar
                    match decision:
                        case 1:
                            print('PASE DE LA CPU')
                            if self.realizar_pase(es_cpu=True):
                                print('DESEA INTENTAR INTERCEPTAR?')
                                eleccion = int(input('1 SI\n2 - NO\n'))
                                if eleccion == 1:
                                    self.realizar_intercepcion()
                                else:
                                    pass
                                    
                        case 2:
                            print('TIRO DE LA CPU')
                            if self.realizar_tiro():
                                if not self.realizar_atajar():
                                    print('GOOOOL DE LA CPU!!!')
                                    self._partido_en_curso = False

        print("Fin del partido")
        self._cronometro.join()



# Ejemplo de uso
e = EquipoLogico("leo", 1)
p = Partido(e,Facil())
p._cancha.mostrar_cancha()

# print(p._cancha.buscar_jugador((7,3)))
# print()
# # print(p._equipo_con_posesion)
# for i in range(10):
#     print('-----------------------------------------------------------------------')
#     print('POSICION ACTUAL -->',p._posicion_pelota, ' Equipo Actual --> ', p._equipo_con_posesion)
#     print('PASE---')
#     if p.realizar_pase():
#         p.realizar_intercepcion()

p.jugar_partido()
'PRUEBEN ANASHE'
'SIMULACION DE PARTIDO'

# cosas que hacer:
# metodo patear
# programar IA
# dificultades (facil, medio, dificil)#

'HABILITAR LA INTERCEPCION CUANDO LO TIENE LA MAQUINA'
'SEPARAR PARA QUE QUEDE MAS LEGIBLE'