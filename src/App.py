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
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(scene_bg, (0, 0))
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
