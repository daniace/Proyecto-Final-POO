import customtkinter as ctk

from view.ABMView import centrar_ventana


class LoginAdmin(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Configuración inicial de customtkinter
        ctk.set_appearance_mode("System")  # Modos: "System", "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"
        # Ventana principal
        self.title("Iniciar Sesión")
        self.resizable(False, False)

        # Títulos y campos
        self.__label_titulo = ctk.CTkLabel(
            self, text="Iniciar Sesión", font=("Arial", 20)
        )
        self.__label_titulo.pack(pady=10)

        self.__entry_username = ctk.CTkEntry(self, placeholder_text="Nombre de usuario")
        self.__entry_username.pack(pady=10, padx=50)

        self.__entry_password = ctk.CTkEntry(
            self, placeholder_text="Contraseña", show="*"
        )
        self.__entry_password.pack(pady=10, padx=50)

        # Botón de login
        self.__btn_login = ctk.CTkButton(self, text="Iniciar Sesión")
        self.__btn_login.pack(pady=20)

        self.__btn_cerrar = ctk.CTkButton(self, text="Cerrar", command=self.destroy)
        self.__btn_cerrar.pack(pady=10)

        # Etiqueta para mostrar resultados
        self.__lbl_resultado = ctk.CTkLabel(self, text="")
        self.__lbl_resultado.pack(pady=10)

    def _obtener_credenciales(self):
        """Devuelve el nombre de usuario y contraseña ingresados."""
        return self.__entry_username.get(), self.__entry_password.get()

    def _mostrar_resultado(self, mensaje):
        """Actualiza la etiqueta de resultados con un mensaje."""
        self.__lbl_resultado.configure(text=mensaje)

    def _conectar_boton_login(self, callback):
        """Conecta el botón de login a un evento o función."""
        self.__btn_login.configure(command=callback)

    def iniciar(self):
        """Inicia la vista."""
        centrar_ventana(self, 300, 300)
        self.mainloop()
