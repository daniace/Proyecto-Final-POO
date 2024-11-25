import customtkinter as ctk


class FormularioUsuario:
    def __init__(self, vista_padre, modo, datos_usuario=None):
        self.vista_padre = vista_padre
        self.modo = modo
        self.datos_usuario = datos_usuario

        # Ventana de formulario
        self.root = ctk.CTkToplevel()
        self.root.title("Formulario Usuario")
        self.root.resizable(False, False)
        self.centrar_ventana()

        # Campos
        self.entry_nombre = ctk.CTkEntry(
            self.root, placeholder_text="Nombre de usuario"
        )
        self.entry_nombre.pack(pady=10, padx=10)

        self.entry_password = ctk.CTkEntry(
            self.root, placeholder_text="Contraseña", show="*"
        )
        self.entry_password.pack(pady=10, padx=10)

        self.entry_admin = ctk.CTkEntry(self.root, placeholder_text="Admin (0 o 1)")
        self.entry_admin.pack(pady=10, padx=10)

        self.entry_score = ctk.CTkEntry(self.root, placeholder_text="Score")
        self.entry_score.pack(pady=10, padx=10)

        # Botón de guardar
        self.btn_guardar = ctk.CTkButton(
            self.root, text="Guardar", command=self.guardar
        )
        self.btn_guardar.pack(pady=20)

        # Cargar datos si es modificación
        if self.modo == "modificar" and self.datos_usuario:
            self.entry_nombre.insert(0, self.datos_usuario[1])
            self.entry_password.insert(0, self.datos_usuario[2])
            self.entry_admin.insert(0, self.datos_usuario[3])
            self.entry_score.insert(0, self.datos_usuario[5])

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

    def guardar(self):
        """Guarda el usuario."""
        nombre = self.entry_nombre.get()
        password = self.entry_password.get()
        admin = self.entry_admin.get()
        score = self.entry_score.get()

        if self.modo == "alta":
            self.vista_padre.alta_usuario_callback(nombre, password, admin, score)
        elif self.modo == "modificar":
            id_usuario = self.datos_usuario[0]
            self.vista_padre.modificar_usuario_callback(
                id_usuario, nombre, password, admin, score
            )
        self.root.destroy()

    def iniciar(self):
        """Inicia el formulario."""
        self.root.grab_set()
        self.root.mainloop()
