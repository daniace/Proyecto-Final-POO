import customtkinter as ctk


class LoginAdmin:
    def __init__(self):
        # Configuración inicial de customtkinter
        ctk.set_appearance_mode("System")  # Modos: "System", "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

        # Ventana principal
        self.root = ctk.CTk()
        self.root.title("Iniciar Sesión")
        self.root.resizable(False, False)
        self.centrar_ventana()
        self.visible = False

        # Títulos y campos
        self.label_titulo = ctk.CTkLabel(
            self.root, text="Iniciar Sesión", font=("Arial", 20)
        )
        self.label_titulo.pack(pady=10)

        self.entry_username = ctk.CTkEntry(
            self.root, placeholder_text="Nombre de usuario"
        )
        self.entry_username.pack(pady=10, padx=50)

        self.entry_password = ctk.CTkEntry(
            self.root, placeholder_text="Contraseña", show="*"
        )
        self.entry_password.pack(pady=10, padx=50)

        # Botón de login
        self.btn_login = ctk.CTkButton(self.root, text="Iniciar Sesión")
        self.btn_login.pack(pady=20)

        self.btn_cerrar = ctk.CTkButton(self.root, text="Cerrar", command=self.cerrar)
        self.btn_cerrar.pack(pady=10)

        # Etiqueta para mostrar resultados
        self.lbl_resultado = ctk.CTkLabel(self.root, text="")
        self.lbl_resultado.pack(pady=10)

    def centrar_ventana(self):
        """Centra la ventana en la pantalla."""
        ancho_ventana = 250  # Ancho de la ventana
        alto_ventana = 300  # Alto de la ventana

        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Calcular la posición centrada
        pos_x = int((ancho_pantalla - ancho_ventana) / 2)
        pos_y = int((alto_pantalla - alto_ventana) / 2)

        # Establecer la geometría de la ventana
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    def obtener_credenciales(self):
        """Devuelve el nombre de usuario y contraseña ingresados."""
        return self.entry_username.get(), self.entry_password.get()

    def mostrar_resultado(self, mensaje):
        """Actualiza la etiqueta de resultados con un mensaje."""
        self.lbl_resultado.configure(text=mensaje)

    def conectar_boton_login(self, callback):
        """Conecta el botón de login a un evento o función."""
        self.btn_login.configure(command=callback)

    def iniciar(self):
        """Inicia el bucle principal de la ventana."""
        self.visible = True
        self.root.mainloop()

    def cerrar(self):
        """Cierra la ventana de la vista."""
        self.visible = False
        self.root.destroy()
