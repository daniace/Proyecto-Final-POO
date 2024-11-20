import sqlite3

import pygame
from pgu import gui

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ABM de Usuarios")

# Creación de la aplicación de GUI
app = gui.App()

# Definición de la ventana principal
main_window = gui.Container(width=800, height=600)


# Función para obtener usuarios de la base de datos
def obtener_usuarios():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, email, telefono FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios


# Función para actualizar la lista de usuarios en la interfaz
def actualizar_lista_usuarios():
    lista_usuarios.clear()
    usuarios = obtener_usuarios()
    for usuario in usuarios:
        lista_usuarios.add(
            gui.Label(f"{usuario[0]} - {usuario[1]} - {usuario[2]} - {usuario[3]}")
        )


# Función para agregar un usuario
def agregar_usuario(btn=None):
    nombre = entry_nombre.value
    email = entry_email.value
    telefono = entry_telefono.value
    if nombre and email and telefono:
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, telefono) VALUES (?, ?, ?)",
            (nombre, email, telefono),
        )
        conn.commit()
        conn.close()
        actualizar_lista_usuarios()


# Función para eliminar un usuario
def eliminar_usuario(btn=None):
    id_usuario = entry_id.value
    if id_usuario:
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        conn.commit()
        conn.close()
        actualizar_lista_usuarios()


# Función para modificar un usuario
def modificar_usuario(btn=None):
    id_usuario = entry_id.value
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # Actualizar nombre si no está vacío
    nombre = entry_nombre.value
    if nombre:
        cursor.execute(
            "UPDATE usuarios SET nombre = ? WHERE id = ?", (nombre, id_usuario)
        )

    # Actualizar email si no está vacío
    email = entry_email.value
    if email:
        cursor.execute(
            "UPDATE usuarios SET email = ? WHERE id = ?", (email, id_usuario)
        )

    # Actualizar teléfono si no está vacío
    telefono = entry_telefono.value
    if telefono:
        cursor.execute(
            "UPDATE usuarios SET telefono = ? WHERE id = ?", (telefono, id_usuario)
        )

    conn.commit()
    conn.close()
    actualizar_lista_usuarios()


# Creación de widgets con separación adecuada
lista_usuarios = gui.List(width=750, height=200)

entry_nombre = gui.Input(value="", size=20)
entry_email = gui.Input(value="", size=30)
entry_telefono = gui.Input(value="", size=15)
entry_id = gui.Input(value="", size=10)
btn_agregar = gui.Button("Agregar", action=agregar_usuario)
btn_eliminar = gui.Button("Eliminar", action=eliminar_usuario)
btn_modificar = gui.Button("Modificar", action=modificar_usuario)
btn_actualizar = gui.Button("Actualizar", action=actualizar_lista_usuarios)

# Añadir widgets a la ventana principal
main_window.add(gui.Label("ID Usuario (para eliminar/modificar):"), 10, 10)
main_window.add(entry_id, 200, 10)
main_window.add(gui.Label("Nombre Usuario:"), 10, 40)
main_window.add(entry_nombre, 200, 40)
main_window.add(gui.Label("Email:"), 10, 70)
main_window.add(entry_email, 200, 70)
main_window.add(gui.Label("Teléfono:"), 10, 100)
main_window.add(entry_telefono, 200, 100)
main_window.add(btn_agregar, 10, 130)
main_window.add(btn_eliminar, 100, 130)
main_window.add(btn_modificar, 200, 130)
main_window.add(btn_actualizar, 300, 130)
main_window.add(gui.Label("Usuarios:"), 10, 170)
main_window.add(lista_usuarios, 10, 200)

# Inicialización de la lista de usuarios
actualizar_lista_usuarios()

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

        # Obtener la posición del ratón
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_agregar.rect.collidepoint(pos):
                agregar_usuario()
            elif btn_eliminar.rect.collidepoint(pos):
                eliminar_usuario()
            elif btn_modificar.rect.collidepoint(pos):
                modificar_usuario()
            elif btn_actualizar.rect.collidepoint(pos):
                actualizar_lista_usuarios()

    screen.fill((255, 255, 255))
    app.paint(screen)
    pygame.display.flip()

pygame.quit()
