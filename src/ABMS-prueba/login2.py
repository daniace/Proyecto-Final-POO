import sqlite3

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


# Función para mostrar una ventana emergente personalizada
def mostrar_mensaje(mensaje, cerrar=False):
    content = gui.Table()
    content.tr()

    # Personalización del mensaje
    mensaje_label = gui.Label(mensaje)
    mensaje_label.style.color = (255, 0, 0)  # Color del texto rojo
    mensaje_label.style.font = pygame.font.Font(None, 24)  # Tamaño de la fuente
    content.td(mensaje_label)

    # Crear el botón de cerrar con personalización
    btn_cerrar = gui.Button("Cerrar")
    btn_cerrar.style.color = (0, 0, 255)  # Color del texto del botón
    btn_cerrar.style.bgcolor = (192, 192, 192)  # Color de fondo del botón
    btn_cerrar.style.font = pygame.font.Font(None, 20)  # Tamaño de la fuente del botón

    def cerrar_popup(btn):
        popup.close()
        if cerrar:
            global running
            running = False

    btn_cerrar.connect(gui.CLICK, cerrar_popup, btn_cerrar)

    content.tr()
    content.td(btn_cerrar, align=1)

    # Personalización del popup
    popup = gui.Dialog(gui.Label("Mensaje"), content)
    popup.style.bgcolor = (255, 255, 255)  # Color de fondo del popup
    popup.style.border = 1  # Borde del popup
    popup.open()


# Función de validación de usuario
def validate_login(btn):
    username = entry_username.value
    password = entry_password.value

    # Conexión a la base de datos
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # Consulta para verificar usuario y contraseña
    cursor.execute(
        "SELECT * FROM usuarios WHERE nombre = ? AND password = ?", (username, password)
    )
    user = cursor.fetchone()

    # Validar el resultado de la consulta
    if user:
        lbl_result.value = "Login exitoso"
        mostrar_mensaje("Inicio de sesión exitoso", cerrar=True)
    else:
        lbl_result.value = "Login fallido"
        mostrar_mensaje("Inicio de sesión fallido")

    # Cierre de la conexión
    conn.close()


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
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        # Procesar los eventos de PGU
        app.event(event)

        # Verificar si el botón izquierdo del ratón está presionado y en el botón de login
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if btn_login.rect.collidepoint(pos):
                validate_login(
                    btn_login
                )  # Conectar el botón con la función de validación

    screen.fill((255, 255, 255))
    app.paint(screen)
    pygame.display.flip()

pygame.quit()
