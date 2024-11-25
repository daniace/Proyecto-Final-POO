import pygame
from pgu import gui

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((320, 240))
pygame.display.set_caption("Sistema de Login")

# Creación de la aplicación de GUI
app = gui.App()

# Definición de la ventana principal
main_window = gui.Container(width=320, height=240)


# Función de validación de usuario
def validate_login(btn):
    username = entry_username.value
    password = entry_password.value
    if username == "user" and password == "pass":
        lbl_result.value = "Login exitoso"
    else:
        lbl_result.value = "Login fallido"


# Creación de widgets con separación adecuada
entry_username = gui.Input(value="", size=20)
entry_password = gui.Input(value="", size=20, password=True)
btn_login = gui.Button("Login", action=validate_login)
lbl_result = gui.Label("")

# Añadir widgets a la ventana principal con márgenes para evitar colisiones
main_window.add(gui.Label("Nombre de Usuario:"), 10, 10)
main_window.add(entry_username, 10, 40)
main_window.add(gui.Label("Contraseña:"), 10, 80)
main_window.add(entry_password, 10, 110)
main_window.add(btn_login, 100, 150)
main_window.add(lbl_result, 10, 190)

# Configuración de la aplicación
app.init(main_window)

# Bucle principal de Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        app.event(event)
    screen.fill((255, 255, 255))
    app.paint(screen)
    pygame.display.flip()

pygame.quit()
