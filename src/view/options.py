import sys

import pygame

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
radio_borde = 5

# Cargar imagen de fondo
background_image = pygame.image.load(r"src\assets\images\options.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Fuentes
font = pygame.font.Font(None, 36)


# Función para dibujar botones
def draw_button(text, x, y, w, h, color, hover_color):
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, w, h)

    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, button_rect, border_radius=radio_borde)
    else:
        pygame.draw.rect(screen, color, button_rect, border_radius=radio_borde)

    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + w / 2, y + h / 2))
    screen.blit(text_surface, text_rect)

    return button_rect


# Main loop
running = True
while running:
    screen.blit(background_image, (0, 0))  # Dibujar imagen de fondo

    # Dibujar botones
    volver_button = draw_button(
        "Volver",
        WIDTH // 2 - 350,
        HEIGHT // 2 - 250,
        100,
        40,
        BUTTON_COLOR,
        BUTTON_HOVER_COLOR,
    )
    play_button = draw_button(
        "Dificultad",
        WIDTH // 2 - 300,
        HEIGHT // 2 - 130,
        130,
        40,
        BUTTON_COLOR,
        BUTTON_HOVER_COLOR,
    )
    options_button = draw_button(
        "Sonido",
        WIDTH // 2 - 300,
        HEIGHT // 2 - 17,
        130,
        40,
        BUTTON_COLOR,
        BUTTON_HOVER_COLOR,
    )
    quit_button = draw_button(
        "Controles",
        WIDTH // 2 - 300,
        HEIGHT // 2 + 90,
        130,
        40,
        BUTTON_COLOR,
        BUTTON_HOVER_COLOR,
    )
    facil_button = draw_button(
        "Facil",
        WIDTH // 2 - 150,
        HEIGHT // 2 - 130,
        100,
        40,
        BUTTON_COLOR,
        BUTTON_HOVER_COLOR,
    )
    normal_button = draw_button(
        "Normal",
        WIDTH // 2 - 20,
        HEIGHT // 2 - 130,
        100,
        40,
        BUTTON_COLOR,
        BUTTON_HOVER_COLOR,
    )
    dificil_button = draw_button(
        "Dificil",
        WIDTH // 2 + 105,
        HEIGHT // 2 - 130,
        100,
        40,
        BUTTON_COLOR,
        BUTTON_HOVER_COLOR,
    )
    sonido_on_button = draw_button(
        "Encendido",
        WIDTH // 2 - 90,
        HEIGHT // 2 - 17,
        130,
        40,
        BUTTON_COLOR,
        BUTTON_HOVER_COLOR,
    )
    sonido_off_button = draw_button(
        "apagado",
        WIDTH // 2 + 60,
        HEIGHT // 2 - 17,
        130,
        40,
        BUTTON_COLOR,
        BUTTON_HOVER_COLOR,
    )

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
