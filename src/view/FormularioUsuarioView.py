import customtkinter as ctk

from view.ABMView import centrar_ventana


class FormularioUsuario(ctk.CTkToplevel):
    def __init__(self, vista_padre, modo, datos_usuario=None):
        super().__init__()
        self.__vista_padre = vista_padre
        self.__modo = modo
        self.__datos_usuario = datos_usuario

        # Ventana de formulario
        self.title("Formulario Usuario")
        self.resizable(False, False)

        # Campos
        self.__entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre de usuario")
        self.__entry_nombre.pack(pady=10, padx=10)

        self.__entry_password = ctk.CTkEntry(
            self, placeholder_text="Contraseña", show="*"
        )
        self.__entry_password.pack(pady=10, padx=10)

        self.__entry_admin = ctk.CTkEntry(self, placeholder_text="Admin (0 o 1)")
        self.__entry_admin.pack(pady=10, padx=10)

        self.__entry_score = ctk.CTkEntry(self, placeholder_text="Score")
        self.__entry_score.pack(pady=10, padx=10)

        # Botón de guardar
        self.__btn_guardar = ctk.CTkButton(self, text="Guardar", command=self.__guardar)
        self.__btn_guardar.pack(pady=20)

        # Cargar datos si es modificación
        if self.__modo == "modificar" and self.__datos_usuario:
            print(self.__datos_usuario)
            self.__entry_nombre.insert(0, self.__datos_usuario[1])
            self.__entry_password.insert(0, self.__datos_usuario[2])
            self.__entry_admin.insert(0, self.__datos_usuario[3])
            self.__entry_score.insert(0, self.__datos_usuario[4])

    def __guardar(self):
        """Guarda el usuario."""
        nombre = self.__entry_nombre.get()
        password = self.__entry_password.get()
        admin = self.__entry_admin.get()
        score = self.__entry_score.get()

        if self.__modo == "alta":
            self.__vista_padre._alta_usuario_callback(nombre, password, admin, score)
        elif self.__modo == "modificar":
            id_usuario = self.__datos_usuario[0]
            self.__vista_padre._modificar_usuario_callback(
                id_usuario, nombre, password, admin, score
            )
        self.withdraw()

    def iniciar(self):
        """Inicia el formulario."""
        centrar_ventana(self, 250, 300)
        self.grab_set()
        self.deiconify()
