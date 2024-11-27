import pygame

pygame.init()

# Configuración inicial
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simulación de input() sin bloqueo")
font = pygame.font.Font(None, 36)

# Estado del programa
esperando_input = False
input_value = None
mensaje = "Esperando un número..."


# Función para iniciar la espera de input
def iniciar_espera():
    global esperando_input, mensaje
    esperando_input = True
    mensaje = "Haz clic en un botón para ingresar un número."


# Función que recibe el número del botón
def recibir_input(numero):
    global esperando_input, input_value, mensaje
    if esperando_input:  # Solo procesa si estamos esperando un input
        input_value = numero
        esperando_input = False
        mensaje = f"Número recibido: {numero}"


# Clase botón
class Button:
    def __init__(self, x, y, w, h, text, callback, args=()):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.args = args

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 200, 100), self.rect)
        text_surface = font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback(*self.args)


# Crear botones
buttons = [
    Button(50, 50, 100, 50, "1", recibir_input, (1,)),
    Button(50, 120, 100, 50, "2", recibir_input, (2,)),
    Button(50, 190, 100, 50, "3", recibir_input, (3,)),
]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons:
            button.handle_event(event)

    # Dibujar en pantalla
    screen.fill((255, 255, 255))

    # Dibujar botones
    for button in buttons:
        button.draw(screen)

    # Mostrar mensaje en pantalla
    text_surface = font.render(mensaje, True, (0, 0, 0))
    screen.blit(text_surface, (50, 10))

    pygame.display.flip()

    # Controlar el flujo de la lógica
    if not esperando_input:
        iniciar_espera()  # Activa la espera de input solo una vez

pygame.quit()


import pygame

pygame.init()

# Configuración inicial
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simulación de input() sin bloqueo")
font = pygame.font.Font(None, 36)

# Estado del programa
esperando_input = False
input_value = None
mensaje = "Esperando un número..."


# Función para iniciar la espera de input
def iniciar_espera():
    global esperando_input, mensaje
    esperando_input = True
    mensaje = "Haz clic en un botón para ingresar un número."


# Función que recibe el número del botón
def recibir_input(numero):
    global esperando_input, input_value, mensaje
    if esperando_input:  # Solo procesa si estamos esperando un input
        input_value = numero
        esperando_input = False
        mensaje = f"Número recibido: {numero}"


# Clase botón
class Button:
    def __init__(self, x, y, w, h, text, callback, args=()):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.args = args

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 200, 100), self.rect)
        text_surface = font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback(*self.args)


# Crear botones
buttons = [
    Button(50, 50, 100, 50, "1", recibir_input, (1,)),
    Button(50, 120, 100, 50, "2", recibir_input, (2,)),
    Button(50, 190, 100, 50, "3", recibir_input, (3,)),
]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons:
            button.handle_event(event)

    # Dibujar en pantalla
    screen.fill((255, 255, 255))

    # Dibujar botones
    for button in buttons:
        button.draw(screen)

    # Mostrar mensaje en pantalla
    text_surface = font.render(mensaje, True, (0, 0, 0))
    screen.blit(text_surface, (50, 10))

    pygame.display.flip()

    # Controlar el flujo de la lógica
    if not esperando_input:
        iniciar_espera()  # Activa la espera de input solo una vez

pygame.quit()
