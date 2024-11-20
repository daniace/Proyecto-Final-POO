import sqlite3

import pygame
from pgu import gui


class ABMUsuarios:
    def __init__(self):
        # Inicialización de Pygame
        pygame.init()

        # Configuración de la ventana
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("ABM de Usuarios")

        # Creación de la aplicación de GUI
        self.app = gui.App()

        # Definición de la ventana principal
        self.main_window = gui.Container(width=800, height=600)

        # Creación de widgets con separación adecuada
        self.lista_usuarios = gui.List(width=750, height=200)
        self.entry_nombre = gui.Input(value="", size=20)
        self.entry_email = gui.Input(value="", size=30)
        self.entry_telefono = gui.Input(value="", size=15)
        self.entry_id = gui.Input(value="", size=10)
        self.btn_agregar = gui.Button("Agregar", action=self.agregar_usuario)
        self.btn_eliminar = gui.Button("Eliminar", action=self.eliminar_usuario)
        self.btn_modificar = gui.Button("Modificar", action=self.modificar_usuario)
        self.btn_actualizar = gui.Button(
            "Actualizar", action=self.actualizar_lista_usuarios
        )

        # Añadir widgets a la ventana principal con márgenes para evitar colisiones
        self.main_window.add(gui.Label("ID Usuario (para eliminar/modificar):"), 10, 10)
        self.main_window.add(self.entry_id, 200, 10)
        self.main_window.add(gui.Label("Nombre Usuario:"), 10, 40)
        self.main_window.add(self.entry_nombre, 200, 40)
        self.main_window.add(gui.Label("Email:"), 10, 70)
        self.main_window.add(self.entry_email, 200, 70)
        self.main_window.add(gui.Label("Teléfono:"), 10, 100)
        self.main_window.add(self.entry_telefono, 200, 100)
        self.main_window.add(self.btn_agregar, 10, 130)
        self.main_window.add(self.btn_eliminar, 100, 130)
        self.main_window.add(self.btn_modificar, 200, 130)
        self.main_window.add(self.btn_actualizar, 300, 130)
        self.main_window.add(gui.Label("Usuarios:"), 10, 170)
        self.main_window.add(self.lista_usuarios, 10, 200)

        # Inicialización de la lista de usuarios
        self.actualizar_lista_usuarios()

        # Configuración de la aplicación
        self.app.init(self.main_window)
        self.running = True

    def obtener_usuarios(self):
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email, telefono FROM usuarios")
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios

    def actualizar_lista_usuarios(self, btn=None):
        self.lista_usuarios.clear()
        usuarios = self.obtener_usuarios()
        for usuario in usuarios:
            self.lista_usuarios.add(
                gui.Label(f"{usuario[0]} - {usuario[1]} - {usuario[2]} - {usuario[3]}")
            )

    def agregar_usuario(self, btn=None):
        nombre = self.entry_nombre.value
        email = self.entry_email.value
        telefono = self.entry_telefono.value
        if nombre and email and telefono:
            conn = sqlite3.connect("usuarios.db")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, email, telefono) VALUES (?, ?, ?)",
                (nombre, email, telefono),
            )
            conn.commit()
            conn.close()
            self.actualizar_lista_usuarios()

    def eliminar_usuario(self, btn=None):
        id_usuario = self.entry_id.value
        if id_usuario:
            conn = sqlite3.connect("usuarios.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
            conn.commit()
            conn.close()
            self.actualizar_lista_usuarios()

    def modificar_usuario(self, btn=None):
        id_usuario = self.entry_id.value
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()

        # Actualizar nombre si no está vacío
        nombre = self.entry_nombre.value
        if nombre:
            cursor.execute(
                "UPDATE usuarios SET nombre = ? WHERE id = ?", (nombre, id_usuario)
            )

        # Actualizar email si no está vacío
        email = self.entry_email.value
        if email:
            cursor.execute(
                "UPDATE usuarios SET email = ? WHERE id = ?", (email, id_usuario)
            )

        # Actualizar teléfono si no está vacío
        telefono = self.entry_telefono.value
        if telefono:
            cursor.execute(
                "UPDATE usuarios SET telefono = ? WHERE id = ?", (telefono, id_usuario)
            )

        conn.commit()
        conn.close()
        self.actualizar_lista_usuarios()

    def run(self):
        # Bucle principal de Pygame
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                # Procesar los eventos de PGU
                self.app.event(event)

                # Obtener la posición del ratón
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.btn_agregar.rect.collidepoint(pos):
                        self.agregar_usuario()
                    elif self.btn_eliminar.rect.collidepoint(pos):
                        self.eliminar_usuario()
                    elif self.btn_modificar.rect.collidepoint(pos):
                        self.modificar_usuario()
                    elif self.btn_actualizar.rect.collidepoint(pos):
                        self.sactualizar_lista_usuarios()

            self.screen.fill((255, 255, 255))
            self.app.paint(self.screen)
            pygame.display.flip()

        pygame.quit()


# Crear una instancia del sistema de ABM de usuarios y ejecutarlo
if __name__ == "__main__":
    abm_usuarios = ABMUsuarios()
    abm_usuarios.run()
