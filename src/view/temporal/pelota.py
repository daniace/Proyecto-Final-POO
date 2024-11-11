import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento de una Pelota")

# Colores
COLOR_FONDO = (0, 0, 0)
COLOR_PELOTA = (255, 0, 0)

# Configuración de la pelota
radio_pelota = 30
pos_x, pos_y = ANCHO // 2, ALTO // 2  # Posición inicial
vel_x, vel_y = 5, 5  # Velocidad de la pelota en cada eje

# Bucle principal
reloj = pygame.time.Clock()
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover la pelota
    pos_x += vel_x
    pos_y += vel_y

    # Rebotar en los bordes
    if pos_x - radio_pelota <= 0 or pos_x + radio_pelota >= ANCHO:
        vel_x = -vel_x
    if pos_y - radio_pelota <= 0 or pos_y + radio_pelota >= ALTO:
        vel_y = -vel_y

    # Dibujar en la pantalla
    pantalla.fill(COLOR_FONDO)  # Limpiar la pantalla
    pygame.draw.circle(pantalla, COLOR_PELOTA, (pos_x, pos_y), radio_pelota)  # Dibujar la pelota

    pygame.display.flip()  # Actualizar la pantalla
    reloj.tick(60)  # Limitar a 60 FPS
