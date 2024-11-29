import pygame
import gif_pygame  # Importa la biblioteca gif_pygame

# Inicializa Pygame
pygame.init()

# Configura la ventana
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Reproduciendo un GIF con gif_pygame")

# Carga el GIF animado

gif = gif_pygame.load(
    "src/assets/images/gifs/7ae3c7ad104a968dc735871c0bf17608.gif", loops=1
)

# Variables de control
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass

    # Limpia la pantalla
    screen.fill((0, 0, 0))

    # Dibuja el GIF en la posición deseada
    gif.render(screen, (50, 50))  # Cambia las coordenadas según lo necesites

    # Actualiza la pantalla
    pygame.display.flip()

pygame.quit()
