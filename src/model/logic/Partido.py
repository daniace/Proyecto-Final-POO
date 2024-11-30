import random
import time

from controller.ReproductorMusica import ReproductorMusica
from model.logic.Acciones import Acciones
from model.logic.Cancha import Cancha
from model.logic.Cronometro import Cronometro
from model.logic.Dificultades import *
from model.logic.EquipoLogico import EquipoLogico
from model.logic.formacion import *


class Partido:
    def __init__(
        self, jugador1: EquipoLogico, dificultad, vista
    ):  # Le agregue el atributo vista para poder utilizarlo en CanchaViewControlador y mostrar los mensajes
        self._jugador1 = jugador1
        self._jugador2 = EquipoLogico("CPU FC", es_cpu=True)
        self._partido_en_curso = True
        self._cronometro = None
        self._cancha = Cancha(self._jugador1, self._jugador2)
        self._equipo_con_posesion = 1  # EQUIPO 1 O EQUIPO 2
        self._posicion_pelota = (0, 3)  # DONDE ARRANCA EL PARTIDO
        self._acciones = Acciones(dificultad)  # VER SI ESTO QUEDA ASI
        self._dificultad = dificultad
        self._goles = [0, 0]
        self._view = vista
        self.__accion_cpu = None
        self.__reproductor_musica = ReproductorMusica()

    def get_diccionario(self):
        return self._cancha.get_diccionario()

    def _jugador_con_pelota(self):
        """Devuelve el jugador en base a la posición actual de la pelota"""
        return self._cancha.get_diccionario().get(self._posicion_pelota, None)

    def _cambio_equipo(self) -> None:
        """Cambia el equipo que tiene la pelota"""
        self._equipo_con_posesion = 1 if self._equipo_con_posesion == 2 else 2

    def imprimir_jugadores(self, lista_jugadores):
        lista = []
        diccionario = self._cancha.get_diccionario()
        for i, j in lista_jugadores:
            lista.append(diccionario.get(i, None))
        return lista

    def get_equipo_con_posesion(self) -> int:
        return self._equipo_con_posesion

    def get_posicion_pelota(self) -> tuple:
        return self._posicion_pelota

    def mostrar_pases(self, es_cpu: bool = False):
        aliados_cercanos = self._cancha.encontrar_puntos_cercanos(
            self._posicion_pelota, "aliado"
        )

        if es_cpu:
            return random.choice(aliados_cercanos)[0] if aliados_cercanos else None

        if not aliados_cercanos:
            return None
        return aliados_cercanos

    def realizar_pase(self, aliado_destino, es_cpu: bool = False) -> bool:
        if not aliado_destino:
            return False

        jugador_con_pelota = self._jugador_con_pelota()
        if self._acciones.calcular_efectividad_pase(
            jugador_con_pelota, self._equipo_con_posesion
        ):
            self._acciones.set_valor_bonificacion(False)
            self._posicion_pelota = aliado_destino
            return True
        else:
            self._posicion_pelota = self._cancha.encontrar_puntos_cercanos(
                self._posicion_pelota, "enemigo"
            )[0]
            self._cambio_equipo()
            self._acciones.set_valor_bonificacion(False)
            return False

    def realizar_intercepcion(self) -> bool:
        posicion_enemigo = self._cancha.encontrar_puntos_cercanos(
            self._posicion_pelota, "enemigo"
        )[0]

        enemigo_cercano = self._cancha.buscar_jugador(posicion_enemigo)
        if self._acciones.calcular_efectividad_intercepcion(
            enemigo_cercano, 2 if self._equipo_con_posesion == 1 else 1
        ):
            self._posicion_pelota = posicion_enemigo
            self._cambio_equipo()
            return "interseccion_valida"
        else:
            return "interseccion_fallida"

    def realizar_atajar(self) -> bool:
        """Únicamente ataja cuando el equipo enemigo tira al arco"""
        posicion_arquero = (0, 3) if self._equipo_con_posesion == 2 else (7, 3)
        arquero = self._cancha.buscar_jugador(posicion_arquero)

        self._posicion_pelota = posicion_arquero
        self._cambio_equipo()

        if self._acciones.calcular_efectividad_atajar(
            arquero, self._equipo_con_posesion
        ):
            return True
        else:
            return False

    def realizar_tiro(self) -> bool:
        jugador_actual = self._cancha.buscar_jugador(self._posicion_pelota)
        if self._acciones.calcular_efectividad_tiro(
            jugador_actual, self._equipo_con_posesion
        ):
            self._acciones.set_valor_bonificacion(False)
            self.__reproductor_musica.cargar_musica(r"src\assets\audio\gool.wav")
            self.__reproductor_musica.reproducir(1)
            return True
        else:
            self._posicion_pelota = (0, 3) if self._equipo_con_posesion == 2 else (7, 3)
            self._cambio_equipo()
            self._acciones.set_valor_bonificacion(False)
            return False

    def realizar_gambeta(self) -> bool:
        jugador_con_pelota = self._jugador_con_pelota()
        if self._acciones.calcular_efectividad_gambeta(
            jugador_con_pelota, self._equipo_con_posesion
        ):
            print(
                "¡Gambeta exitosa! El jugador contrario no pudo interceptar la pelota."
            )
            self._acciones.set_valor_bonificacion(True)
            if self._jugador_con_pelota().get_posicion()[0] == "DEFENSA":
                print("%15 mas de probabilidades de pase correcto")
            if self._jugador_con_pelota().get_posicion()[0] == "MEDIOCAMPISTA":
                print("%10 mas de probabilidades de pase y de tiro correcto")
            if self._jugador_con_pelota().get_posicion()[0] == "DELANTERO":
                print("%15 mas de probabilidades de tiro correcto")
            return True
        else:
            print("Gambeta fallida. El jugador contrario ha recuperado la pelota.")
            self._cambio_equipo()
            self._posicion_pelota = self._cancha.encontrar_puntos_cercanos(
                self._posicion_pelota, "enemigo"
            )[0]
            return False

    def jugar_turno_jugador(self, decision, aliado_pase=None) -> None:
        match decision:
            case 1:
                if self.realizar_pase(aliado_pase):
                    return "pase_valido"
                else:
                    return "pase_invalido"
            case 2:
                if self.realizar_tiro():
                    if not self.realizar_atajar():
                        print("\033[1;32m" + "GOOOOL DEL JUGADOR 1!!!" + "\033[0;m")
                        self._goles[0] += 1
                        print(
                            "GOLES -->", "P1", self._goles[0], "- CPU ", self._goles[1]
                        )
                        return "gol"
                    else:
                        return "atajado"
                else:
                    return "tiro_fallado"
            case 3:
                if self._jugador_con_pelota().get_posicion()[0] == "ARQUERO":
                    return "gambeta_fallida"
                else:
                    if self.realizar_gambeta():
                        return "gambeta_exitosa"
                    else:
                        return "gambeta_fallida"

    def _jugar_turno_cpu(self) -> None:
        pesos = {}
        pesos["ARQUERO"] = [1, 0]
        pesos["DEFENSOR"] = [0.8, 0.2]
        pesos["MEDIOCAMPISTA"] = [0.7, 0.3]
        pesos["DELANTERO"] = [0, 1]

        jugador_cpu = self._jugador_con_pelota().get_posicion()[0]
        print(type(jugador_cpu))
        decision = random.choices([1, 2], weights=pesos.get(jugador_cpu), k=1)[0]
        # if self._posicion_pelota
        match decision:
            case 1:
                pase_cpu = self.mostrar_pases(es_cpu=True)
                if self.realizar_pase(pase_cpu):
                    self.__accion_cpu = "pase_a_interceptar"
                    return True
            case 2:
                if self.realizar_tiro():
                    if not self.realizar_atajar():
                        self.__accion_cpu = "gol_cpu"
                        print("\033[4;31m" + "GOOOOL DE LA CPU!!!" + "\033[0;m")
                        self._goles[1] += 1
                        print(
                            "GOLES -->", "P1", self._goles[0], "- CPU ", self._goles[1]
                        )
                    else:
                        self.__accion_cpu = "atajado_cpu"
                else:
                    self.__accion_cpu = "tiro_fallado_cpu"

    def mostrar_cancha_con_pelota(self):
        matriz = self._cancha.get_matriz_cancha()

        for i, fila in enumerate(matriz):
            for j, elemento in enumerate(fila):
                if (i, j) == self._posicion_pelota:
                    print(f"{elemento}°", end=" ")
                else:
                    print(elemento, end=" ")
            print()

    def mostrar_resultado(self):
        print("\033[1;31m" + "Fin del partido" + "\033[0;m")
        print("RESULTADO -->", "P1", self._goles[0], "- CPU ", self._goles[1])
        return self._repartir_puntos(self._goles)

    def _repartir_puntos(self, goles):  ##
        dificultades = [Facil, Medio, Dificil]
        for dificultad in dificultades:
            if isinstance(self._dificultad, dificultad):
                print(self._dificultad.get_mensaje())
                if goles[0] > goles[1]:
                    print(
                        "\033[1;32m"
                        + f"{self._jugador1.get_nombre()} ha ganado {self._dificultad.get_pts_por_ganar()}"
                        + "\033[0;m"
                    )
                    return self._dificultad.get_pts_por_ganar()
                elif goles[0] == goles[1]:
                    print(
                        "\033[1;36m"
                        + f"{self._jugador1.get_nombre()} empato con {self._jugador2.get_nombre()}  , suma {self._dificultad.get_pts_por_empatar()}"
                        + "\033[0;m"
                    )
                    return self._dificultad.get_pts_por_empatar()
                else:
                    print(
                        "\033[1:31m"
                        + f"{self._jugador2.get_nombre()} ha ganado!  {self._jugador1.get_nombre()} suma {self._dificultad.get_pts_por_perder()}"
                        + "\033[0;m"
                    )
                    return self._dificultad.get_pts_por_perder()

    def get_goles(self):
        return self._goles

    def get_accion_cpu(self):
        return self.__accion_cpu
