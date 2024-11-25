import customtkinter as ctk


class FormularioCarta:
    def __init__(self, vista_padre, modo, datos_carta=None):
        self.vista_padre = vista_padre
        self.modo = modo
        self.datos_carta = datos_carta

        # Formulario
        self.root = ctk.CTkToplevel()
        self.root.title("Formulario Carta")
        self.root.resizable(False, False)
        self.centrar_ventana()

        # Variables de control para los radio buttons
        self.radio_var = ctk.StringVar()

        # Campos de entrada
        self.entry_nombre = ctk.CTkEntry(self.root, placeholder_text="Nombre")
        self.entry_nacionalidad = ctk.CTkEntry(
            self.root, placeholder_text="Nacionalidad"
        )
        self.entry_club = ctk.CTkEntry(self.root, placeholder_text="Club")
        self.entry_general = ctk.CTkEntry(self.root, placeholder_text="Overall")
        self.entry_pace = ctk.CTkEntry(self.root, placeholder_text="Pace")
        self.entry_shooting = ctk.CTkEntry(self.root, placeholder_text="Shooting")
        self.entry_passing = ctk.CTkEntry(self.root, placeholder_text="Passing")
        self.entry_dribbling = ctk.CTkEntry(self.root, placeholder_text="Dribbling")
        self.entry_defending = ctk.CTkEntry(self.root, placeholder_text="Defending")
        self.entry_physic = ctk.CTkEntry(self.root, placeholder_text="Physic")

        # Radio buttons
        self.checkbox_cb = ctk.CTkRadioButton(
            self.root, text="Defensa Central (CB)", variable=self.radio_var, value="CB"
        )
        self.checkbox_lb = ctk.CTkRadioButton(
            self.root, text="Lateral Derecho (LB)", variable=self.radio_var, value="LB"
        )
        self.checkbox_rb = ctk.CTkRadioButton(
            self.root,
            text="Lateral Izquierdo (RB)",
            variable=self.radio_var,
            value="RB",
        )
        self.checkbox_cm = ctk.CTkRadioButton(
            self.root, text="Centro Medio (CM)", variable=self.radio_var, value="CM"
        )
        self.checkbox_rm = ctk.CTkRadioButton(
            self.root, text="Extremo Derecho (RM)", variable=self.radio_var, value="RM"
        )
        self.checkbox_lm = ctk.CTkRadioButton(
            self.root,
            text="Extremo Izquierdo (LM)",
            variable=self.radio_var,
            value="LM",
        )
        self.checkbox_lw = ctk.CTkRadioButton(
            self.root,
            text="Delantero Izquierdo (LW)",
            variable=self.radio_var,
            value="LW",
        )
        self.checkbox_rw = ctk.CTkRadioButton(
            self.root,
            text="Delantero Derecho (RW)",
            variable=self.radio_var,
            value="RW",
        )
        self.checkbox_st = ctk.CTkRadioButton(
            self.root, text="Delantero Centro (ST)", variable=self.radio_var, value="ST"
        )
        self.checkbox_lwb = ctk.CTkRadioButton(
            self.root,
            text="Carrilero Izquierdo (LWB)",
            variable=self.radio_var,
            value="LWB",
        )
        self.checkbox_rwb = ctk.CTkRadioButton(
            self.root,
            text="Carrilero Derecho (RWB)",
            variable=self.radio_var,
            value="RWB",
        )
        self.checkbox_cdm = ctk.CTkRadioButton(
            self.root,
            text="Mediocentro Defensivo (CDM)",
            variable=self.radio_var,
            value="CDM",
        )
        self.checkbox_cam = ctk.CTkRadioButton(
            self.root,
            text="Mediocentro Ofensivo (CAM)",
            variable=self.radio_var,
            value="CAM",
        )

        # Botón de guardar
        self.btn_guardar = ctk.CTkButton(
            self.root, text="Guardar", command=self.guardar
        )

        # Boton Cancelar
        self.btn_cancelar = ctk.CTkButton(
            self.root, text="Cancelar", command=self.root.destroy
        )

        # Ubicación de los widgets usando grid
        self.entry_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_nacionalidad.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_club.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_general.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_pace.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.entry_shooting.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.entry_passing.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.entry_dribbling.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.entry_defending.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.entry_physic.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Ubicacion de los radio buttons
        self.checkbox_cb.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.checkbox_lb.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.checkbox_rb.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        self.checkbox_cm.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        self.checkbox_rm.grid(row=0, column=3, padx=10, pady=5, sticky="w")
        self.checkbox_lm.grid(row=1, column=3, padx=10, pady=5, sticky="w")
        self.checkbox_lw.grid(row=2, column=3, padx=10, pady=5, sticky="w")
        self.checkbox_rw.grid(row=3, column=3, padx=10, pady=5, sticky="w")

        self.checkbox_st.grid(row=0, column=4, padx=10, pady=5, sticky="w")
        self.checkbox_lwb.grid(row=1, column=4, padx=10, pady=5, sticky="w")
        self.checkbox_rwb.grid(row=2, column=4, padx=10, pady=5, sticky="w")
        self.checkbox_cdm.grid(row=3, column=4, padx=10, pady=5, sticky="w")

        # Coloca el botón debajo de todos los campos
        self.btn_guardar.grid(row=9, column=1, columnspan=2, pady=20)
        self.btn_cancelar.grid(row=9, column=2, columnspan=2, pady=20)

        # Si estamos en modo "modificar", llenar los campos con los datos existentes
        if self.modo == "modificar" and self.datos_carta:
            self.entry_nombre.insert(0, self.datos_carta[1])
            self.entry_nacionalidad.insert(0, self.datos_carta[2])
            self.entry_club.insert(0, self.datos_carta[3])
            self.entry_general.insert(0, self.datos_carta[4])
            self.radio_var.set(self.datos_carta[5])
            self.entry_pace.insert(0, self.datos_carta[6])
            self.entry_shooting.insert(0, self.datos_carta[7])
            self.entry_passing.insert(0, self.datos_carta[8])
            self.entry_dribbling.insert(0, self.datos_carta[9])
            self.entry_defending.insert(0, self.datos_carta[10])
            self.entry_physic.insert(0, self.datos_carta[11])

    def centrar_ventana(self):
        """Centra la ventana en la pantalla."""
        ancho_ventana = 900  # Ancho de la ventana
        alto_ventana = 250  # Alto de la ventana

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
            self.radio_var.get(),
            self.entry_pace.get(),
            self.entry_shooting.get(),
            self.entry_passing.get(),
            self.entry_dribbling.get(),
            self.entry_defending.get(),
            self.entry_physic.get(),
        )
        if self.modo == "alta":
            self.vista_padre.alta_carta_callback(*datos)
        elif self.modo == "modificar":
            id_carta = self.datos_carta[0]
            self.vista_padre.modificar_carta_callback(id_carta, *datos)
        self.root.destroy()

    def iniciar(self):
        """Inicia el formulario."""
        self.root.mainloop()
