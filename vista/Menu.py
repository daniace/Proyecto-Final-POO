import pygame
import sys
from button import *
# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Héroes del Balón")

# Colores
WHITE = (255, 255, 255)
BUTTON_COLOR = (200, 200, 170)
BUTTON_HOVER_COLOR = (180, 180, 150)

# Cargar imagen de fondo
background_image = pygame.image.load(r"src\assets\images\gutbol.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Fuentes
font = pygame.font.Font(None, 36)

# Función para dibujar botones
# def draw_button(text, x, y, w, h, color, hover_color):
#     mouse_pos = pygame.mouse.get_pos()
#     button_rect = pygame.Rect(x, y, w, h)
    
#     if button_rect.collidepoint(mouse_pos):
#         pygame.draw.rect(screen, hover_color, button_rect)
#     else:
#         pygame.draw.rect(screen, color, button_rect)
    
#     text_surface = font.render(text, True, WHITE)
#     text_rect = text_surface.get_rect(center=(x + w / 2, y + h / 2))
#     screen.blit(text_surface, text_rect)
    
    # return button_rect

# Main loop
running = True
while running:
    screen.blit(background_image, (0, 0))  # Dibujar imagen de fondo
    
    # Dibujar botones
    play_button = draw_button("JUGAR", WIDTH // 2 - 100, HEIGHT // 2 - 130, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
    options_button = draw_button("OPCIONES", WIDTH // 2 - 100, HEIGHT // 2 - 17, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
    quit_button = draw_button("SALIR", WIDTH // 2 - 100, HEIGHT // 2 + 90, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                print("Iniciar el juego")
            elif options_button.collidepoint(event.pos):
                print("Opciones del juego")
            elif quit_button.collidepoint(event.pos):
                running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
