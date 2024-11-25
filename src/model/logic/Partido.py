from model.logic.EquipoLogico import EquipoLogico
from model.logic.Cancha import Cancha
from model.logic.Cronometro import Cronometro
from model.logic.formacion import *
from model.logic.Dificultades import *
import random
import time
from model.logic.Acciones import Acciones


class Partido:
    def __init__(self, jugador1: EquipoLogico, dificultad: Dificultad, vista): #Le agregue el atributo vista para poder utilizarlo en CanchaViewControlador y mostrar los mensajes
        self._jugador1 = jugador1
        self._jugador2 = EquipoLogico("CPU FC", es_cpu=True)
        self._partido_en_curso = True
        self._cronometro = None
        self._cancha = Cancha(self._jugador1, self._jugador2)
        self._equipo_con_posesion = 1  # EQUIPO 1 O EQUIPO 2
        self._posicion_pelota = (0, 3)  #DONDE ARRANCA EL PARTIDO
        self._acciones = Acciones(dificultad)  # VER SI ESTO QUEDA ASI
        self._dificultad=dificultad
        self._goles = [0,0]
        self._view = vista

    def _jugador_con_pelota(self):
        """Devuelve el jugador en base a la posición actual de la pelota"""
        return self._cancha.get_diccionario().get(self._posicion_pelota, None)

    def _cambio_equipo(self) -> None:
        """Cambia el equipo que tiene la pelota"""
        self._equipo_con_posesion = 1 if self._equipo_con_posesion == 2 else 2

    def mostrar_pases(self, es_cpu: bool = False):
        aliados_cercanos = self._cancha.encontrar_puntos_cercanos(
            self._posicion_pelota, "aliado"
        )

        if es_cpu:
            return random.choice(aliados_cercanos)[0] if aliados_cercanos else None

        if not aliados_cercanos:
            print("No hay jugadores disponibles para recibir el pase.")
            return None

        print(
            "---------------------------------------------------------------------------------------"
        )
        # print("Pases disponibles")
        # self._cancha.imprimir_jugadores(aliados_cercanos)
        self._view.mostrar_mensaje("Pases disponibles:", 100)
        lista_jugadores = [jugador[0] for jugador in aliados_cercanos]
        for i, jugador in enumerate(lista_jugadores):
            self._view.mostrar_mensaje(f"{i+1} - {jugador}", 150 + (i * 40))
        

        decision = self._obtener_decision_usuario(len(aliados_cercanos))
        return aliados_cercanos[decision - 1][0]

    def _obtener_decision_usuario(self, max_opciones: int) -> int:
        while True:
            try:
                decision = int(input("Seleccione un pase: ")) #input("Seleccione un pase: ") #Deberia ingresar un evento
                if 1 <= decision <= max_opciones:
                    return decision
                else:
                    print("Selección no válida... seleccione un pase válido.")
            except ValueError:
                print("Entrada no válida... por favor ingrese un número.")

    def realizar_pase(self, es_cpu: bool = False) -> bool:
        aliado_destino = self.mostrar_pases(es_cpu)
        if not aliado_destino:
            return False

        jugador_con_pelota = self._jugador_con_pelota()
        print(f"Pase de {self._posicion_pelota} a {aliado_destino}.")

        if self._acciones.calcular_efectividad_pase(jugador_con_pelota,self._equipo_con_posesion):
            print("El pase fue exitoso.")
            self._posicion_pelota = aliado_destino
            return True
        else:
            print("El pase fue FALLADO.")
            self._posicion_pelota = self._cancha.encontrar_puntos_cercanos(
                self._posicion_pelota, "enemigo"
            )[0]
            self._cambio_equipo()
            print(
                "Pelota en -->",
                self._posicion_pelota,
                "Equipo Actual -->",
                self._equipo_con_posesion,
            )
            return False

    def realizar_intercepcion(self) -> bool:
        print("INTENTANDO INTERCEPTAR...")
        posicion_enemigo = self._cancha.encontrar_puntos_cercanos(
            self._posicion_pelota, "enemigo"
        )[0]
        print("ENEMIGO A INTERCEPTAR -->", posicion_enemigo)
        print()

        enemigo_cercano = self._cancha.buscar_jugador(posicion_enemigo)
        if self._acciones.calcular_efectividad_intercepcion(enemigo_cercano, 2 if self._equipo_con_posesion == 1 else 1):
            print("SE INTERCEPTO LA PELOTA")
            self._posicion_pelota = posicion_enemigo
            self._cambio_equipo()
            return True
        else:
            print("Intercepción Fallida")
            return False

    def realizar_atajar(self) -> bool:
        """Únicamente ataja cuando el equipo enemigo tira al arco"""
        posicion_arquero = (0, 3) if self._equipo_con_posesion == 2 else (7, 3)
        arquero = self._cancha.buscar_jugador(posicion_arquero)

        self._posicion_pelota = posicion_arquero
        self._cambio_equipo()

        if self._acciones.calcular_efectividad_atajar(arquero, self._equipo_con_posesion):
            print("SE ATAJÓ EL TIRO")
            return True
        else:
            print("NO SE ATAJÓ EL TIRO")
            return False

    def realizar_tiro(self) -> bool:
        jugador_actual = self._cancha.buscar_jugador(self._posicion_pelota)
        if self._acciones.calcular_efectividad_tiro(jugador_actual,self._equipo_con_posesion):
            return True
        else:
            print("Se falló el tiro")
            print("SALE DEL ARCO ENEMIGO")
            self._posicion_pelota = (0, 3) if self._equipo_con_posesion == 2 else (7, 3)
            self._cambio_equipo()
            return False
    
    def realizar_gambeta(self) -> bool:
        jugador_con_pelota = self._jugador_con_pelota() 
        if self._acciones.calcular_efectividad_gambeta(jugador_con_pelota, self._equipo_con_posesion):
            print("¡Gambeta exitosa! El jugador contrario no pudo interceptar la pelota.")
            self._acciones.set_valor_bonificacion(True)
            if self._jugador_con_pelota().get_posicion()[0]=='DEFENSA':
                print("%15 mas de probabilidades de pase correcto")
            if self._jugador_con_pelota().get_posicion()[0]=='MEDIOCAMPISTA':
                print("%10 mas de probabilidades de pase y de tiro correcto")
            if self._jugador_con_pelota().get_posicion()[0]=='DELANTERO':
                print("%15 mas de probabilidades de tiro correcto")
            return True 
        else:
            print("Gambeta fallida. El jugador contrario ha recuperado la pelota.")
            self._cambio_equipo()
            self._posicion_pelota = self._cancha.encontrar_puntos_cercanos( self._posicion_pelota, "enemigo" )[0] 
            return False

    def _jugar_turno_jugador(self) -> None:
        time.sleep(1)
        self.mostrar_cancha_con_pelota()                #despues esto se tiene que borrar#
        print(
            "---------------------------------------------------------------------------------------"
        )
        print(
            "POSICION ACTUAL -->",
            self._posicion_pelota,
            " Equipo Actual -->",
            self._equipo_con_posesion,
        )
        print()
        print(
            f"{self._jugador_con_pelota()} tiene la pelota, ¿qué desea hacer?:\n1 - Pase\n2 - Tiro\n3- Gambeta"
        )
        decision = self._obtener_decision_usuario(3)
        match decision:
            case 1:
                self.realizar_pase()
                self._acciones.set_valor_bonificacion(False)
            case 2:
                print("TIRO DEL JUGADOR 1")
                if self.realizar_tiro():
                    if not self.realizar_atajar():
                        print("\033[1;32m"+"GOOOOL DEL JUGADOR 1!!!"+"\033[0;m")
                        self._goles[0] += 1 
                        print('GOLES -->', 'P1',self._goles[0], '- CPU ',self._goles[1])
                self._acciones.set_valor_bonificacion(False)
            case 3:
                if self._jugador_con_pelota().get_posicion()[0]=='ARQUERO':
                    print("el Aqruero no pude realizar gambeta")
                else: self.realizar_gambeta()

    def _jugar_turno_cpu(self) -> None:
        self.mostrar_cancha_con_pelota()        #despues esto se tiene que borrar#
        print(
            "---------------------------------------------------------------------------------------"
        )
        print(
            f"{self._jugador_con_pelota()} tiene la pelota, CPU está tomando una decisión..."
        )
        time.sleep(2)
        decision = random.choices([1, 2], weights=[0.7, 0.3],k=1)[0]
        match decision:
            case 1:
                print("PASE DE LA CPU")
                if self.realizar_pase(es_cpu=True):
                    print("DESEA INTENTAR INTERCEPTAR?")
                    eleccion = self._obtener_decision_usuario(2)
                    if eleccion == 1:
                        self.realizar_intercepcion()
            case 2:
                print("TIRO DE LA CPU")
                if self.realizar_tiro():
                    if not self.realizar_atajar():
                        print("\033[4;31m"+"GOOOOL DE LA CPU!!!"+"\033[0;m")
                        self._goles[1] += 1 
                        print('GOLES -->', 'P1',self._goles[0], '- CPU ',self._goles[1])

    def _jugar_turno(self) -> None:
        if self._equipo_con_posesion == 1:
            self._jugar_turno_jugador()
        else:
            self._jugar_turno_cpu()

    def mostrar_cancha_con_pelota(self):                #esta funcion despues se tiene que borrar#
        matriz = self._cancha.get_matriz_cancha()

        for i, fila in enumerate(matriz):
            for j, elemento in enumerate(fila):
                if (i, j) == self._posicion_pelota:
                    print(f"{elemento}°", end=' ')
                else:
                    print(elemento, end=' ')
            print()
    
    def _repartir_puntos(self,goles): ##
        dificultades=[Facil,Medio,Dificil]
        for dificultad in dificultades:
            if isinstance(self._dificultad,dificultad):
                print(self._dificultad.get_mensaje())
                if goles[0] > goles[1]:
                    print("\033[1;32m"+f"{self._jugador1.get_nombre()} ha ganado {self._dificultad.get_pts_por_ganar()}"+"\033[0;m")
                elif goles[0] == goles[1]:
                    print ("\033[1;36m"+f"{self._jugador1.get_nombre()} empato con {self._jugador2.get_nombre()}  , suma {self._dificultad.get_pts_por_empatar()}"+"\033[0;m")
                else:
                    print("\033[1:31m"+f"{self._jugador2.get_nombre()} ha ganado!  {self._jugador1.get_nombre()} suma {self._dificultad.get_pts_por_perder()}"+"\033[0;m")

    def jugar_partido(self) -> None:
        self._partido_en_curso = True

        if self._cronometro is None or not self._cronometro.is_alive():
            self._cronometro = Cronometro()
            self._cronometro.start()

        while self._partido_en_curso:
            if self._cronometro._evento_partido_terminado.is_set():
                self._partido_en_curso = False
            else:
                self._jugar_turno()

        self._cronometro.join()
        print("\033[1;31m"+"Fin del partido"+"\033[0;m")
        print('RESULTADO -->', 'P1',self._goles[0], '- CPU ',self._goles[1])
        self._repartir_puntos(self._goles)



# cosas que hacer:
# - implementar la dificultad de las acciones dependiendo de la posicion de la cancha 
# ES DECIR, SI HACE UN PASE UN DEFENSA, DEBERIA SE MAS FACIL QUE SI LO HACE UN DELANTERO
# LO CONTRARIO CON EL TIRO AL ARCO

# -DEVOLVER POSICION MAS GENERALIZADA (EJ: DELANTERO, DEFENSA, ETC)


