import customtkinter as ctk


class FormularioArquero:
    def __init__(self, vista_padre, modo, datos_carta=None):
        self.vista_padre = vista_padre
        self.modo = modo
        self.datos_carta = datos_carta

        # Formulario
        self.root = ctk.CTkToplevel()
        self.root.title("Formulario Carta")
        self.root.resizable(False, False)
        self.centrar_ventana()

        # Campos de entrada
        self.entry_nombre = ctk.CTkEntry(self.root, placeholder_text="Nombre")
        self.entry_nacionalidad = ctk.CTkEntry(
            self.root, placeholder_text="Nacionalidad"
        )
        self.entry_club = ctk.CTkEntry(self.root, placeholder_text="Club")
        self.entry_general = ctk.CTkEntry(self.root, placeholder_text="Overall")
        self.entry_gk_diving = ctk.CTkEntry(self.root, placeholder_text="GK Diving")
        self.entry_gk_handling = ctk.CTkEntry(self.root, placeholder_text="GK Handling")
        self.entry_gk_kicking = ctk.CTkEntry(self.root, placeholder_text="GK Kicking")
        self.entry_gk_reflexes = ctk.CTkEntry(self.root, placeholder_text="GK Reflexes")
        self.entry_gk_speed = ctk.CTkEntry(self.root, placeholder_text="GK Speed")
        self.entry_gk_positioning = ctk.CTkEntry(
            self.root, placeholder_text="GK Positioning"
        )

        # Botón de guardar
        self.btn_guardar = ctk.CTkButton(
            self.root, text="Guardar", command=self.guardar
        )

        # Ubicación de los widgets usando grid
        self.entry_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_nacionalidad.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_club.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_general.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_gk_diving.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_gk_handling.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.entry_gk_kicking.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.entry_gk_reflexes.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.entry_gk_speed.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.entry_gk_positioning.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Coloca el botón debajo de todos los campos
        self.btn_guardar.grid(row=9, column=0, columnspan=2, pady=20)

        # Si estamos en modo "modificar", llenar los campos con los datos existentes
        if self.modo == "modificar" and self.datos_carta:
            self.entry_nombre.insert(0, self.datos_carta[1])
            self.entry_nacionalidad.insert(0, self.datos_carta[2])
            self.entry_club.insert(0, self.datos_carta[3])
            self.entry_general.insert(0, self.datos_carta[4])
            self.entry_gk_diving.insert(0, self.datos_carta[5])
            self.entry_gk_handling.insert(0, self.datos_carta[6])
            self.entry_gk_kicking.insert(0, self.datos_carta[7])
            self.entry_gk_reflexes.insert(0, self.datos_carta[8])
            self.entry_gk_speed.insert(0, self.datos_carta[9])
            self.entry_gk_positioning.insert(0, self.datos_carta[10])

    def centrar_ventana(self):
        """Centra la ventana en la pantalla."""
        ancho_ventana = 350  # Ancho de la ventana
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
        """Llama al callback correspondiente."""
        datos = (
            self.entry_nombre.get(),
            self.entry_nacionalidad.get(),
            self.entry_club.get(),
            self.entry_general.get(),
            self.entry_gk_diving.get(),
            self.entry_gk_handling.get(),
            self.entry_gk_kicking.get(),
            self.entry_gk_reflexes.get(),
            self.entry_gk_speed.get(),
            self.entry_gk_positioning.get(),
        )
        if self.modo == "alta":
            self.vista_padre.alta_arquero_callback(*datos)
        elif self.modo == "modificar":
            id_carta = self.datos_carta[0]
            self.vista_padre.modificar_arquero_callback(id_carta, *datos)
        self.root.destroy()

    def iniciar(self):
        """Inicia el formulario."""
        self.root.mainloop()
