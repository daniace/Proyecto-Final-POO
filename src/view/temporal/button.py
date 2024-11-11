import sys

import pygame

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Héroes del Balón")

# Colores
WHITE = (255, 255, 255)
BUTTON_COLOR = (200, 200, 170)
BUTTON_HOVER_COLOR = (180, 180, 150)


def draw_button(text, x, y, w, h, color, hover_color):
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, w, h)

    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, button_rect)
    else:
        pygame.draw.rect(screen, color, button_rect)

    font = pygame.font.Font(r"src\assets\font\Pixeltype.ttf", 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + w / 2, y + h / 2))
    screen.blit(text_surface, text_rect)

    return button_rect
