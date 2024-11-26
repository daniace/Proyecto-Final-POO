import customtkinter as ctk

from view.ABMView import centrar_ventana


class FormularioArquero(ctk.CTkToplevel):
    def __init__(self, vista_padre, modo, datos_carta=None):
        super().__init__()
        self.__vista_padre = vista_padre
        self.__modo = modo
        self.__datos_carta = datos_carta

        # Formulario
        self.title("Formulario Carta")

        self.resizable(False, False)

        # Campos de entrada
        self.__entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
        self.__entry_nacionalidad = ctk.CTkEntry(self, placeholder_text="Nacionalidad")
        self.__entry_club = ctk.CTkEntry(self, placeholder_text="Club")
        self.__entry_general = ctk.CTkEntry(self, placeholder_text="Overall")
        self.__entry_gk_diving = ctk.CTkEntry(self, placeholder_text="GK Diving")
        self.__entry_gk_handling = ctk.CTkEntry(self, placeholder_text="GK Handling")
        self.__entry_gk_kicking = ctk.CTkEntry(self, placeholder_text="GK Kicking")
        self.__entry_gk_reflexes = ctk.CTkEntry(self, placeholder_text="GK Reflexes")
        self.__entry_gk_speed = ctk.CTkEntry(self, placeholder_text="GK Speed")
        self.__entry_gk_positioning = ctk.CTkEntry(
            self, placeholder_text="GK Positioning"
        )

        # Botón de guardar
        self.__btn_guardar = ctk.CTkButton(self, text="Guardar", command=self.__guardar)

        # Ubicación de los widgets usando grid
        self.__entry_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.__entry_nacionalidad.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.__entry_club.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.__entry_general.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.__entry_gk_diving.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.__entry_gk_handling.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.__entry_gk_kicking.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.__entry_gk_reflexes.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.__entry_gk_speed.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.__entry_gk_positioning.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Coloca el botón debajo de todos los campos
        self.__btn_guardar.grid(row=9, column=0, columnspan=2, pady=20)

        # Si estamos en modo "modificar", llenar los campos con los datos existentes
        if self.__modo == "modificar" and self.__datos_carta:
            self.__entry_nombre.insert(0, self.__datos_carta[1])
            self.__entry_nacionalidad.insert(0, self.__datos_carta[2])
            self.__entry_club.insert(0, self.__datos_carta[3])
            self.__entry_general.insert(0, self.__datos_carta[4])
            self.__entry_gk_diving.insert(0, self.__datos_carta[5])
            self.__entry_gk_handling.insert(0, self.__datos_carta[6])
            self.__entry_gk_kicking.insert(0, self.__datos_carta[7])
            self.__entry_gk_reflexes.insert(0, self.__datos_carta[8])
            self.__entry_gk_speed.insert(0, self.__datos_carta[9])
            self.__entry_gk_positioning.insert(0, self.__datos_carta[10])

    def __guardar(self):
        """Llama al callback correspondiente."""
        datos = (
            self.__entry_nombre.get(),
            self.__entry_nacionalidad.get(),
            self.__entry_club.get(),
            self.__entry_general.get(),
            self.__entry_gk_diving.get(),
            self.__entry_gk_handling.get(),
            self.__entry_gk_kicking.get(),
            self.__entry_gk_reflexes.get(),
            self.__entry_gk_speed.get(),
            self.__entry_gk_positioning.get(),
        )
        if self.__modo == "alta":
            self.__vista_padre._alta_arquero_callback(*datos)
        elif self.__modo == "modificar":
            id_carta = self.__datos_carta[0]
            self.__vista_padre._modificar_arquero_callback(id_carta, *datos)
        self.withdraw()

    def iniciar(self):
        """Inicia el formulario."""
        centrar_ventana(self, 350, 300)
        self.grab_set()
        self.deiconify()
