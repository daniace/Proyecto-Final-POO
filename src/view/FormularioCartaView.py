import customtkinter as ctk

from view.ABMView import centrar_ventana


class FormularioCarta(ctk.CTkToplevel):
    def __init__(self, vista_padre, modo, datos_carta=None):
        super().__init__()
        self.__vista_padre = vista_padre
        self.__modo = modo
        self.__datos_carta = datos_carta

        # Formulario
        self.title("Formulario Carta")
        self.resizable(False, False)

        # Variables de control para los radio buttons
        self.__radio_var = ctk.StringVar()
        self.__posicion_var = ctk.StringVar()

        # Campos de entrada
        self.__entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
        self.__entry_nacionalidad = ctk.CTkEntry(self, placeholder_text="Nacionalidad")
        self.__entry_club = ctk.CTkEntry(self, placeholder_text="Club")
        self.__entry_general = ctk.CTkEntry(self, placeholder_text="Overall")
        self.__entry_pace = ctk.CTkEntry(self, placeholder_text="Pace")
        self.__entry_shooting = ctk.CTkEntry(self, placeholder_text="Shooting")
        self.__entry_passing = ctk.CTkEntry(self, placeholder_text="Passing")
        self.__entry_dribbling = ctk.CTkEntry(self, placeholder_text="Dribbling")
        self.__entry_defending = ctk.CTkEntry(self, placeholder_text="Defending")
        self.__entry_physic = ctk.CTkEntry(self, placeholder_text="Physic")

        self.__desplegable_posicion = ctk.CTkComboBox(
            self,
            values=[
                "Defensa Central (CB)",
                "Lateral Izquierdo (LB)",
                "Lateral Derecho (RB)",
                "Carrilero Izquierdo (LWB)",
                "Carrilero Derecho (RWB)",
                "Mediocampista Defensivo (CDM)",
                "Mediocampista Central (CM)",
                "Mediocampista Ofensivo (CAM)",
                "Mediocampista Izquierdo (LM)",
                "Mediocampista Derecho (RM)",
                "Extremo Izquierdo (LW)",
                "Extremo Derecho (RW)",
                "Delantero Centro (CF)",
                "Delantero (ST)",
                "Delantero Izquierdo (LF)",
                "Delantero Derecho (RF)",
            ],
            state="readonly",
            width=200,
            variable=self.__posicion_var,
        )
        self.__desplegable_posicion.grid(row=4, column=2, pady=10, padx=10)

        # Radio buttons
        self.__checkbox_cb = ctk.CTkRadioButton(
            self,
            text="Defensa Central (CB)",
            variable=self.__radio_var,
            value="CB",
        )
        self.__checkbox_lb = ctk.CTkRadioButton(
            self,
            text="Lateral Derecho (LB)",
            variable=self.__radio_var,
            value="LB",
        )
        self.__checkbox_rb = ctk.CTkRadioButton(
            self,
            text="Lateral Izquierdo (RB)",
            variable=self.__radio_var,
            value="RB",
        )
        self.__checkbox_cm = ctk.CTkRadioButton(
            self, text="Centro Medio (CM)", variable=self.__radio_var, value="CM"
        )
        self.__checkbox_rm = ctk.CTkRadioButton(
            self,
            text="Extremo Derecho (RM)",
            variable=self.__radio_var,
            value="RM",
        )
        self.__checkbox_lm = ctk.CTkRadioButton(
            self,
            text="Extremo Izquierdo (LM)",
            variable=self.__radio_var,
            value="LM",
        )
        self.__checkbox_lw = ctk.CTkRadioButton(
            self,
            text="Delantero Izquierdo (LW)",
            variable=self.__radio_var,
            value="LW",
        )
        self.__checkbox_rw = ctk.CTkRadioButton(
            self,
            text="Delantero Derecho (RW)",
            variable=self.__radio_var,
            value="RW",
        )
        self.__checkbox_st = ctk.CTkRadioButton(
            self,
            text="Delantero Centro (ST)",
            variable=self.__radio_var,
            value="ST",
        )
        self.__checkbox_lwb = ctk.CTkRadioButton(
            self,
            text="Carrilero Izquierdo (LWB)",
            variable=self.__radio_var,
            value="LWB",
        )
        self.__checkbox_rwb = ctk.CTkRadioButton(
            self,
            text="Carrilero Derecho (RWB)",
            variable=self.__radio_var,
            value="RWB",
        )
        self.__checkbox_cdm = ctk.CTkRadioButton(
            self,
            text="Mediocentro Defensivo (CDM)",
            variable=self.__radio_var,
            value="CDM",
        )
        self.__checkbox_cam = ctk.CTkRadioButton(
            self,
            text="Mediocentro Ofensivo (CAM)",
            variable=self.__radio_var,
            value="CAM",
        )

        # Botón de guardar
        self.__btn_guardar = ctk.CTkButton(self, text="Guardar", command=self.__guardar)

        # Boton Cancelar
        self.__btn_cancelar = ctk.CTkButton(self, text="Cancelar", command=self.destroy)

        # Ubicación de los widgets usando grid
        self.__entry_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.__entry_nacionalidad.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.__entry_club.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.__entry_general.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.__entry_pace.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.__entry_shooting.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.__entry_passing.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.__entry_dribbling.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.__entry_defending.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.__entry_physic.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Ubicacion de los radio buttons
        self.__checkbox_cb.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.__checkbox_lb.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.__checkbox_rb.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        self.__checkbox_cm.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        self.__checkbox_rm.grid(row=0, column=3, padx=10, pady=5, sticky="w")
        self.__checkbox_lm.grid(row=1, column=3, padx=10, pady=5, sticky="w")
        self.__checkbox_lw.grid(row=2, column=3, padx=10, pady=5, sticky="w")
        self.__checkbox_rw.grid(row=3, column=3, padx=10, pady=5, sticky="w")

        self.__checkbox_st.grid(row=0, column=4, padx=10, pady=5, sticky="w")
        self.__checkbox_lwb.grid(row=1, column=4, padx=10, pady=5, sticky="w")
        self.__checkbox_rwb.grid(row=2, column=4, padx=10, pady=5, sticky="w")
        self.__checkbox_cdm.grid(row=3, column=4, padx=10, pady=5, sticky="w")
        self.__checkbox_cam.grid(row=4, column=4, padx=10, pady=5, sticky="w")

        # Coloca el botón debajo de todos los campos
        self.__btn_guardar.grid(row=9, column=1, columnspan=2, pady=20)
        self.__btn_cancelar.grid(row=9, column=2, columnspan=2, pady=20)

        # Si estamos en modo "modificar", llenar los campos con los datos existentes
        if self.__modo == "modificar" and self.__datos_carta:
            self.__entry_nombre.insert(0, self.__datos_carta[1])
            self.__entry_nacionalidad.insert(0, self.__datos_carta[2])
            self.__entry_club.insert(0, self.__datos_carta[3])
            self.__entry_general.insert(0, self.__datos_carta[4])
            self.__radio_var.set(self.__datos_carta[5])
            self.__entry_pace.insert(0, self.__datos_carta[6])
            self.__entry_shooting.insert(0, self.__datos_carta[7])
            self.__entry_passing.insert(0, self.__datos_carta[8])
            self.__entry_dribbling.insert(0, self.__datos_carta[9])
            self.__entry_defending.insert(0, self.__datos_carta[10])
            self.__entry_physic.insert(0, self.__datos_carta[11])

    def __guardar(self):
        """Llama al callback correspondiente."""
        datos = (
            self.__entry_nombre.get(),
            self.__entry_nacionalidad.get(),
            self.__entry_club.get(),
            self.__entry_general.get(),
            self.__radio_var.get(),
            self.__entry_pace.get(),
            self.__entry_shooting.get(),
            self.__entry_passing.get(),
            self.__entry_dribbling.get(),
            self.__entry_defending.get(),
            self.__entry_physic.get(),
        )
        if self.__modo == "alta":
            self.__vista_padre._alta_carta_callback(*datos)
        elif self.__modo == "modificar":
            id_carta = self.__datos_carta[0]
            self.__vista_padre._modificar_carta_callback(id_carta, *datos)
        self.withdraw()

    def iniciar(self):
        """Inicia el formulario."""
        centrar_ventana(self, 900, 250)
        self.grab_set()
        self.deiconify()
