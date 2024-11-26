import customtkinter as ctk

from view.ABMView import centrar_ventana


class FormularioEquipo(ctk.CTkToplevel):
    def __init__(self, vista_padre, modo, datos_equipo=None):
        super().__init__()
        self.__vista_padre = vista_padre
        self.__modo = modo
        self.__datos_equipo = datos_equipo

        # Ventana de formulario
        self.title("Formulario equipo")
        self.resizable(False, False)

        # Campos
        self.__lista_usuarios = ctk.CTkComboBox(
            self, values=["Usuario1", "Usuario2", "Usuario3"], state="readonly"
        )
        self.__lista_usuarios.grid(row=6, column=0, pady=10, padx=10)

        self.__entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre de equipo")
        self.__entry_nombre.grid(row=0, column=0, pady=10, padx=10)

        self.__entry_carta1 = ctk.CTkEntry(self, placeholder_text="Carta 1")
        self.__entry_carta1.grid(row=1, column=0, pady=10, padx=10)

        self.__entry_carta2 = ctk.CTkEntry(self, placeholder_text="Carta 2")
        self.__entry_carta2.grid(row=2, column=0, pady=10, padx=10)

        self.__entry_carta3 = ctk.CTkEntry(self, placeholder_text="Carta 3")
        self.__entry_carta3.grid(row=3, column=0, pady=10, padx=10)

        self.__entry_carta4 = ctk.CTkEntry(self, placeholder_text="Carta 4")
        self.__entry_carta4.grid(row=4, column=0, pady=10, padx=10)

        self.__entry_carta5 = ctk.CTkEntry(self, placeholder_text="Carta 5")
        self.__entry_carta5.grid(row=5, column=0, pady=10, padx=10)

        self.__entry_carta6 = ctk.CTkEntry(self, placeholder_text="Carta 6")
        self.__entry_carta6.grid(row=0, column=1, pady=10, padx=10)

        self.__entry_carta7 = ctk.CTkEntry(self, placeholder_text="Carta 7")
        self.__entry_carta7.grid(row=1, column=1, pady=10, padx=10)

        self.__entry_carta8 = ctk.CTkEntry(self, placeholder_text="Carta 8")
        self.__entry_carta8.grid(row=2, column=1, pady=10, padx=10)

        self.__entry_carta9 = ctk.CTkEntry(self, placeholder_text="Carta 9")
        self.__entry_carta9.grid(row=3, column=1, pady=10, padx=10)

        self.__entry_carta10 = ctk.CTkEntry(self, placeholder_text="Carta 10")
        self.__entry_carta10.grid(row=4, column=1, pady=10, padx=10)

        self.__entry_carta11 = ctk.CTkEntry(self, placeholder_text="Carta 11")
        self.__entry_carta11.grid(row=5, column=1, pady=10, padx=10)

        # Botón de guardar
        self.__btn_guardar = ctk.CTkButton(self, text="Guardar", command=self.__guardar)
        self.__btn_guardar.grid(row=6, column=1, columnspan=2, pady=20)

        # Cargar datos si es modificación
        if self.__modo == "modificar" and self.__datos_equipo:
            self.__entry_nombre.insert(0, self.__datos_equipo[2])
            self.__entry_carta1.insert(0, self.__datos_equipo[3])
            self.__entry_carta2.insert(0, self.__datos_equipo[4])
            self.__entry_carta3.insert(0, self.__datos_equipo[5])
            self.__entry_carta4.insert(0, self.__datos_equipo[6])
            self.__entry_carta5.insert(0, self.__datos_equipo[7])
            self.__entry_carta6.insert(0, self.__datos_equipo[8])
            self.__entry_carta7.insert(0, self.__datos_equipo[9])
            self.__entry_carta8.insert(0, self.__datos_equipo[10])
            self.__entry_carta9.insert(0, self.__datos_equipo[11])
            self.__entry_carta10.insert(0, self.__datos_equipo[12])
            self.__entry_carta11.insert(0, self.__datos_equipo[13])

    def __guardar(self):
        """Guarda el equipo."""
        nombre = self.__entry_nombre.get()
        carta1 = self.__entry_carta1.get()
        carta2 = self.__entry_carta2.get()
        carta3 = self.__entry_carta3.get()
        carta4 = self.__entry_carta4.get()
        carta5 = self.__entry_carta5.get()
        carta6 = self.__entry_carta6.get()
        carta7 = self.__entry_carta7.get()
        carta8 = self.__entry_carta8.get()
        carta9 = self.__entry_carta9.get()
        carta10 = self.__entry_carta10.get()
        carta11 = self.__entry_carta11.get()

        if self.__modo == "alta":
            self.__vista_padre._alta_equipo_callback(
                nombre,
                carta1,
                carta2,
                carta3,
                carta4,
                carta5,
                carta6,
                carta7,
                carta8,
                carta9,
                carta10,
                carta11,
            )
        elif self.__modo == "modificar":
            id_equipo = self.__datos_equipo[0]
            self.__vista_padre._modificar_equipo_callback(
                id_equipo,
                nombre,
                carta1,
                carta2,
                carta3,
                carta4,
                carta5,
                carta6,
                carta7,
                carta8,
                carta9,
                carta10,
                carta11,
            )
        self.withdraw()

    def iniciar(self):
        """Inicia el formulario."""
        centrar_ventana(self, 350, 350)
        # self.transient(master=self.__vista_padre)
        self.grab_set()
        self.deiconify()
