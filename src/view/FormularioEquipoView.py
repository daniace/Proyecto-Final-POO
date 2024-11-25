import customtkinter as ctk


class FormularioEquipo:
    def __init__(self, vista_padre, modo, datos_equipo=None):
        self.vista_padre = vista_padre
        self.modo = modo
        self.datos_equipo = datos_equipo

        # Ventana de formulario
        self.root = ctk.CTkToplevel()
        self.root.title("Formulario equipo")
        self.root.resizable(False, False)
        self.centrar_ventana()

        # Campos
        self.entry_nombre = ctk.CTkEntry(self.root, placeholder_text="Nombre de equipo")
        self.entry_nombre.grid(row=0, column=0, pady=10, padx=10)

        self.entry_carta1 = ctk.CTkEntry(self.root, placeholder_text="Carta 1")
        self.entry_carta1.grid(row=1, column=0, pady=10, padx=10)

        self.entry_carta2 = ctk.CTkEntry(self.root, placeholder_text="Carta 2")
        self.entry_carta2.grid(row=2, column=0, pady=10, padx=10)

        self.entry_carta3 = ctk.CTkEntry(self.root, placeholder_text="Carta 3")
        self.entry_carta3.grid(row=3, column=0, pady=10, padx=10)

        self.entry_carta4 = ctk.CTkEntry(self.root, placeholder_text="Carta 4")
        self.entry_carta4.grid(row=4, column=0, pady=10, padx=10)

        self.entry_carta5 = ctk.CTkEntry(self.root, placeholder_text="Carta 5")
        self.entry_carta5.grid(row=5, column=0, pady=10, padx=10)

        self.entry_carta6 = ctk.CTkEntry(self.root, placeholder_text="Carta 6")
        self.entry_carta6.grid(row=0, column=1, pady=10, padx=10)

        self.entry_carta7 = ctk.CTkEntry(self.root, placeholder_text="Carta 7")
        self.entry_carta7.grid(row=1, column=1, pady=10, padx=10)

        self.entry_carta8 = ctk.CTkEntry(self.root, placeholder_text="Carta 8")
        self.entry_carta8.grid(row=2, column=1, pady=10, padx=10)

        self.entry_carta9 = ctk.CTkEntry(self.root, placeholder_text="Carta 9")
        self.entry_carta9.grid(row=3, column=1, pady=10, padx=10)

        self.entry_carta10 = ctk.CTkEntry(self.root, placeholder_text="Carta 10")
        self.entry_carta10.grid(row=4, column=1, pady=10, padx=10)

        self.entry_carta11 = ctk.CTkEntry(self.root, placeholder_text="Carta 11")
        self.entry_carta11.grid(row=5, column=1, pady=10, padx=10)

        # Botón de guardar
        self.btn_guardar = ctk.CTkButton(
            self.root, text="Guardar", command=self.guardar
        )
        self.btn_guardar.grid(row=6, column=0, columnspan=2, pady=20)

        # Cargar datos si es modificación
        if self.modo == "modificar" and self.datos_equipo:
            self.entry_nombre.insert(0, self.datos_equipo[2])
            self.entry_carta1.insert(0, self.datos_equipo[4])
            self.entry_carta2.insert(0, self.datos_equipo[5])
            self.entry_carta3.insert(0, self.datos_equipo[6])
            self.entry_carta4.insert(0, self.datos_equipo[7])
            self.entry_carta5.insert(0, self.datos_equipo[8])
            self.entry_carta6.insert(0, self.datos_equipo[9])
            self.entry_carta7.insert(0, self.datos_equipo[10])
            self.entry_carta8.insert(0, self.datos_equipo[11])
            self.entry_carta9.insert(0, self.datos_equipo[12])
            self.entry_carta10.insert(0, self.datos_equipo[13])
            self.entry_carta11.insert(0, self.datos_equipo[14])

    def centrar_ventana(self):
        """Centra la ventana en la pantalla."""
        ancho_ventana = 350  # Ancho de la ventana
        alto_ventana = 350  # Alto de la ventana

        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Calcular la posición centrada
        pos_x = int((ancho_pantalla - ancho_ventana) / 2)
        pos_y = int((alto_pantalla - alto_ventana) / 2)

        # Establecer la geometría de la ventana
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    def guardar(self):
        """Guarda el equipo."""
        nombre = self.entry_nombre.get()
        carta1 = self.entry_carta1.get()
        carta2 = self.entry_carta2.get()
        carta3 = self.entry_carta3.get()
        carta4 = self.entry_carta4.get()
        carta5 = self.entry_carta5.get()
        carta6 = self.entry_carta6.get()
        carta7 = self.entry_carta7.get()
        carta8 = self.entry_carta8.get()
        carta9 = self.entry_carta9.get()
        carta10 = self.entry_carta10.get()
        carta11 = self.entry_carta11.get()

        if self.modo == "alta":
            self.vista_padre.alta_equipo_callback(
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
        elif self.modo == "modificar":
            id_equipo = self.datos_equipo[0]
            self.vista_padre.modificar_equipo_callback(
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
        self.root.destroy()

    def iniciar(self):
        """Inicia el formulario."""
        self.root.grab_set()
        self.root.mainloop()
