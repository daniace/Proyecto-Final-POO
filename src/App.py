# Example file showing a basic pygame "game loop"
# from cgitb import text

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Héroes Del Balón")
scene_bg = pygame.image.load("src/assets/images/scene.jpg")
scene_bg = pygame.transform.scale(scene_bg, (1280, 720))
texto = pygame.font.Font("src/assets/font/Pixeltype.ttf", 72)
clock = pygame.time.Clock()

# Fuentes
font = pygame.font.Font(None, 36)
# Colores
WHITE = (255, 255, 255)
BUTTON_COLOR = (200, 200, 170)
BUTTON_HOVER_COLOR = (180, 180, 150)
# Función para dibujar botones
def draw_button(text, x, y, w, h, color, hover_color):
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, w, h)
    
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, button_rect)
    else:
        pygame.draw.rect(screen, color, button_rect)
    
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + w / 2, y + h / 2))
    screen.blit(text_surface, text_rect)
    
    return button_rect

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
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
    screen.blit(scene_bg, (0, 0))
        # Dibujar botones   #WIDTH = 1280; HEIGHT = 720
    play_button = draw_button("JUGAR", 1280 // 2 - 100, 720 // 2 - 130, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
    options_button = draw_button("OPCIONES", 1280 // 2 - 100, 720 // 2 - 17, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
    quit_button = draw_button("SALIR", 1280 // 2 - 100, 720 // 2 + 90, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)

    # Centrar texto
    text_surface = texto.render("Heroes Del Balon", True, (255, 255, 255))
    text_rect = text_surface.get_rect(midtop=(screen.get_width() / 2, 20))
    screen.blit(text_surface, text_rect)
    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
