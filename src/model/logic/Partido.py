from EquipoLogico import EquipoLogico
from Cancha import Cancha
from Cronometro import Cronometro
from formacion import *
from Dificultades import *
import random
import time
from Acciones import Acciones


class Partido:
    def __init__(self, jugador1: EquipoLogico, dificultad: Dificultad):
        self._jugador1 = jugador1
        self._jugador2 = EquipoLogico("CPU FC", 2)
        self._partido_en_curso = True
        self._cronometro = None
        self._cancha = Cancha(self._jugador1, self._jugador2)
        self._equipo_con_posesion = 1  # EQUIPO 1 O EQUIPO 2
        self._posicion_pelota = (0, 3)
        self._acciones = Acciones(dificultad)  # VER SI ESTO QUEDA ASI
        self._goles = [0,0]

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
        print("Pases disponibles")
        self._cancha.imprimir_jugadores(aliados_cercanos)
        print()

        decision = self._obtener_decision_usuario(len(aliados_cercanos))
        return aliados_cercanos[decision - 1][0]

    def _obtener_decision_usuario(self, max_opciones: int) -> int:
        while True:
            try:
                decision = int(input("\nSeleccione opción de pase: "))
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

        if self._acciones.calcular_efectividad_pase(jugador_con_pelota):
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
        if self._acciones.calcular_efectividad_intercepcion(enemigo_cercano):
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

        if self._acciones.calcular_efectividad_atajar(arquero):
            print("SE ATAJÓ EL TIRO")
            return True
        else:
            print("NO SE ATAJÓ EL TIRO")
            return False

    def realizar_tiro(self) -> bool:
        jugador_actual = self._cancha.buscar_jugador(self._posicion_pelota)

        if self._acciones.calcular_efectividad_tiro(jugador_actual):
            return True
        else:
            print("Se falló el tiro")
            print("SALE DEL ARCO ENEMIGO")
            self._posicion_pelota = (0, 3) if self._equipo_con_posesion == 2 else (7, 3)
            self._cambio_equipo()
            return False

    def _jugar_turno_jugador(self) -> None:
        time.sleep(2)
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
            f"{self._jugador_con_pelota()} tiene la pelota, ¿qué desea hacer?:\n1 - Pase\n2 - Tiro"
        )
        decision = self._obtener_decision_usuario(2)
        match decision:
            case 1:
                self.realizar_pase()
            case 2:
                print("TIRO DEL JUGADOR 1")
                if self.realizar_tiro():
                    if not self.realizar_atajar():
                        print("GOOOOL DEL JUGADOR 1!!!")
                        self._goles[0] += 1 
                        print('GOLES -->', 'P1',self._goles[0], '- CPU ',self._goles[1])

    def _jugar_turno_cpu(self) -> None:
        self.mostrar_cancha_con_pelota()        #despues esto se tiene que borrar#
        print(
            "---------------------------------------------------------------------------------------"
        )
        print(
            f"{self._jugador_con_pelota()} tiene la pelota, CPU está tomando una decisión..."
        )
        time.sleep(2)
        decision = random.choice([1, 2])
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
                        print("GOOOOL DE LA CPU!!!")
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

        print("Fin del partido")
        print('RESULTADO -->', 'P1',self._goles[0], '- CPU ',self._goles[1])
        self._cronometro.join()


# Ejemplo de uso
e = EquipoLogico("leo", 1)
e.set_formacion(Formacion352())
e.nuevo_equipo()
p = Partido(e, Medio())
p._cancha.mostrar_cancha()
p.jugar_partido()


# cosas que hacer:
# - implementar la dificultad de las acciones dependiendo de la posicion de la cancha 
# ES DECIR, SI HACE UN PASE UN DEFENSA, DEBERIA SE MAS FACIL QUE SI LO HACE UN DELANTERO
# LO CONTRARIO CON EL TIRO AL ARCO

# -DEVOLVER POSICION MAS GENERALIZADA (EJ: DELANTERO, DEFENSA, ETC)


