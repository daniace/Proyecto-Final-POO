import sqlite3

import pygame
from pgu import gui


class SistemaLogin:
    def __init__(self):
        # Inicialización de Pygame
        pygame.init()

        # Configuración de la ventana
        self.screen = pygame.display.set_mode((320, 240))
        pygame.display.set_caption("Sistema de Login")

        # Creación de la aplicación de GUI
        self.app = gui.App()

        # Definición de la ventana principal
        self.main_window = gui.Container(width=320, height=240)

        # Creación de widgets con separación adecuada
        self.entry_username = gui.Input(value="", size=20)
        self.entry_password = gui.Input(value="", size=20, password=True)
        self.btn_login = gui.Button("Login", action=self.validate_login)
        self.lbl_result = gui.Label("")

        # Añadir widgets a la ventana principal con márgenes para evitar colisiones
        self.main_window.add(gui.Label("Nombre de Usuario:"), 10, 10)
        self.main_window.add(self.entry_username, 10, 40)
        self.main_window.add(gui.Label("Contraseña:"), 10, 80)
        self.main_window.add(self.entry_password, 10, 110)
        self.main_window.add(self.btn_login, 100, 150)
        self.main_window.add(self.lbl_result, 10, 190)

        # Configuración de la aplicación
        self.app.init(self.main_window)
        self.running = True

    def mostrar_mensaje(self, mensaje, cerrar=False):
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
        btn_cerrar.style.font = pygame.font.Font(
            None, 20
        )  # Tamaño de la fuente del botón

        def cerrar_popup(btn):
            popup.close()
            if cerrar:
                self.running = False

        btn_cerrar.connect(gui.CLICK, cerrar_popup, btn_cerrar)

        content.tr()
        content.td(btn_cerrar, align=1)

        # Personalización del popup
        popup = gui.Dialog(gui.Label("Mensaje"), content)
        popup.style.bgcolor = (255, 255, 255)  # Color de fondo del popup
        popup.style.border = 1  # Borde del popup
        popup.open()

    def validate_login(self, btn):
        username = self.entry_username.value
        password = self.entry_password.value

        # Conexión a la base de datos
        conn = sqlite3.connect("src\model\database\heroesdelbalon.db")
        cursor = conn.cursor()

        # Consulta para verificar usuario y contraseña
        cursor.execute(
            "SELECT * FROM usuario WHERE nombre_usuario = ? AND password = ?",
            (username, password),
        )
        user = cursor.fetchone()

        # Validar el resultado de la consulta
        if user:
            self.lbl_result.value = "Login exitoso"
            self.mostrar_mensaje("Inicio de sesión exitoso", cerrar=True)
        else:
            self.lbl_result.value = "Login fallido"
            self.mostrar_mensaje("Inicio de sesión fallido")

        # Cierre de la conexión
        conn.close()

    def run(self):
        # Bucle principal de Pygame
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                # Procesar los eventos de PGU
                self.app.event(event)

                # Verificar si el botón izquierdo del ratón está presionado y en el botón de login
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.btn_login.rect.collidepoint(pos):
                        self.validate_login(
                            self.btn_login
                        )  # Conectar el botón con la función de validación

            self.screen.fill((255, 255, 255))
            self.app.paint(self.screen)
            pygame.display.flip()

        pygame.quit()


# Crear una instancia del sistema de login y ejecutarlo
if __name__ == "__main__":
    sistema_login = SistemaLogin()
    sistema_login.run()
