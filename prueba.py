import pygame

pygame.init()

# Crear una ventana redimensionable
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Ventana redimensionable")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar cambios en el tamaño de la ventana
        if event.type == pygame.VIDEORESIZE:
            nuevo_ancho, nuevo_alto = event.size
            screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
            print(f"Nueva resolución: {new_width}x{new_height}")

    screen.fill((100, 150, 200))
    pygame.display.flip()

pygame.quit()
