
#Esto es una simple guia temporal para la demostracion del juego Heroes del Balón 

import random
import time
import threading

# Clase Jugador
class Jugador:
    def __init__(self, nombre, habilidad, velocidad, resistencia):
        self.nombre = nombre
        self.habilidad = habilidad
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.puntos = 0

    def __str__(self):
        return f"{self.nombre} (Habilidad: {self.habilidad}, Velocidad: {self.velocidad}, Resistencia: {self.resistencia})"

# Clase Equipo
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def __str__(self):
        return f"{self.nombre} ({len(self.jugadores)} jugadores)"

# Clase Partido
class Partido:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.marcador = [0, 0]
        self.minuto = 0
        self.tiempo_partido = 90

    def jugar(self):
        # Crear un hilo para el cronómetro
        def cronometro():
            for _ in range(self.tiempo_partido):
                #print(f"Tiempo restante: {self.tiempo_partido - self.minuto} minutos")
                time.sleep(1)
                self.minuto += 1

        # Crear un hilo para el partido
        def partido():
            while self.minuto < self.tiempo_partido:
                print(f"\nMinuto {self.minuto}:")
                print(f"Marcador: {self.equipo1.nombre} {self.marcador[0]} - {self.marcador[1]} {self.equipo2.nombre}")

                # Seleccionar un jugador al azar de cada equipo
                jugador1 = random.choice(self.equipo1.jugadores)
                jugador2 = random.choice(self.equipo2.jugadores)

                print(f"\nJugador 1: {jugador1.nombre} (Habilidad: {jugador1.habilidad}, Velocidad: {jugador1.velocidad}, Resistencia: {jugador1.resistencia})")
                print(f"Jugador 2: {jugador2.nombre} (Habilidad: {jugador2.habilidad}, Velocidad: {jugador2.velocidad}, Resistencia: {jugador2.resistencia})")

                # Tomar decisiones
                print("\n¿Qué deseas hacer?")
                print("1. Patear el balón")
                print("2. Correr con el balón")
                print("3. Pase corto")
                print("4. Pase largo")

                decision = input("Ingresa tu decisión: ")

                if decision == "1":
                    # Patear el balón
                    habilidad1 = jugador1.habilidad + random.randint(-10, 10)
                    habilidad2 = jugador2.habilidad + random.randint(-10, 10)

                    if habilidad1 > habilidad2:
                        self.marcador[0] += 1
                        print(f"{jugador1.nombre} anota un gol para {self.equipo1.nombre}!")
                    else:
                        print(f"{jugador2.nombre} defiende el balón!")

                elif decision == "2":
                    # Correr con el balón
                    velocidad1 = jugador1.velocidad + random.randint(-10, 10)
                    velocidad2 = jugador2.velocidad + random.randint(-10, 10)

                    if velocidad1 > velocidad2:
                        print(f"{jugador1.nombre} supera a {jugador2.nombre}!")
                    else:
                        print(f"{jugador2.nombre} supera a {jugador1.nombre}!")

                elif decision == "3":
                    # Pase corto
                    resistencia1 = jugador1.resistencia + random.randint(-10, 10)
                    resistencia2 = jugador2.resistencia + random.randint(-10, 10)

                    if resistencia1 > resistencia2:
                        print(f"{jugador1.nombre} realiza un pase corto!")
                    else:
                        print(f"{jugador2.nombre} intercepta el pase!")

                elif decision == "4":
                    # Pase largo
                    habilidad1 = jugador1.habilidad + random.randint(-10, 10)
                    habilidad2 = jugador2.habilidad + random.randint(-10, 10)

                    if habilidad1 > habilidad2:
                        print(f"{jugador1.nombre} realiza un pase largo!")
                        
                    else:
                        print(f"{jugador2.nombre} intercepta el pase!")

            # Comprobar si el tiempo ha terminado
                if self.minuto >= self.tiempo_partido:
                    print(f"\nFinal del partido: {self.equipo1.nombre} {self.marcador[0]} - {self.marcador[1]} {self.equipo2.nombre}")
                    break

        # Crear hilos
        hilo_cronometro = threading.Thread(target=cronometro)
        hilo_partido = threading.Thread(target=partido)

        # Iniciar hilos
        hilo_cronometro.start()
        hilo_partido.start()

# Crear jugadores y equipos
jugador1 = Jugador("Lionel Messi", 90, 80, 70)
jugador2 = Jugador("Cristiano Ronaldo", 85, 85, 80)
jugador3 = Jugador("Neymar Jr.", 80, 90, 75)

equipo1 = Equipo("Barcelona")
equipo1.agregar_jugador(jugador1)
equipo1.agregar_jugador(jugador2)

equipo2 = Equipo("Juventus")
equipo2.agregar_jugador(jugador3)

# Jugar partido
partido = Partido(equipo1, equipo2)
partido.jugar()