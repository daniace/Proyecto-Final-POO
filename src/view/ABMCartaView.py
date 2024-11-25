from tkinter import messagebox, ttk

import customtkinter as ctk

from view.FormularioArqueroView import FormularioArquero
from view.FormularioCartaView import FormularioCarta


class VistaABMCartas(ctk.CTkToplevel):
    def __init__(self):
        # Ventana principal
        self.root = ctk.CTk()
        self.root.title("ABM de Cartas")
        self.centrar_ventana()

        # Título
        self.label_titulo = ctk.CTkLabel(
            self.root, text="ABM de Cartas", font=("Arial", 20)
        )
        self.label_titulo.pack(pady=10)

        # Frame para la tabla y scrollbars
        frame_tabla = ctk.CTkFrame(self.root)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbars
        scrollbar_vertical = ttk.Scrollbar(frame_tabla, orient="vertical")
        scrollbar_horizontal = ttk.Scrollbar(frame_tabla, orient="horizontal")

        # Tabla para listar cartas
        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=(
                "ID",
                "Nombre",
                "Nacionalidad",
                "Club",
                "General",
                "Posición",
                "Pace",
                "Shooting",
                "Passing",
                "Dribbling",
                "Defending",
                "Physic",
                "GK Diving",
                "GK Handling",
                "GK Kicking",
                "GK Reflexes",
                "GK Speed",
                "GK Positioning",
            ),
            show="headings",
            yscrollcommand=scrollbar_vertical.set,
            xscrollcommand=scrollbar_horizontal.set,
        )

        # Configuración de encabezados
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Nacionalidad", text="Nacionalidad")
        self.tabla.heading("Club", text="Club")
        self.tabla.heading("General", text="General")
        self.tabla.heading("Posición", text="Posición")
        self.tabla.heading("Pace", text="Pace")
        self.tabla.heading("Shooting", text="Shooting")
        self.tabla.heading("Passing", text="Passing")
        self.tabla.heading("Dribbling", text="Dribbling")
        self.tabla.heading("Defending", text="Defending")
        self.tabla.heading("Physic", text="Physic")
        self.tabla.heading("GK Diving", text="GK Diving")
        self.tabla.heading("GK Handling", text="GK Handling")
        self.tabla.heading("GK Kicking", text="GK Kicking")
        self.tabla.heading("GK Reflexes", text="GK Reflexes")
        self.tabla.heading("GK Speed", text="GK Speed")
        self.tabla.heading("GK Positioning", text="GK Positioning")

        # Configuración de columnas
        self.tabla.column("ID", width=50, anchor="center")
        self.tabla.column("Nombre", width=100, anchor="center")
        self.tabla.column("Nacionalidad", width=100, anchor="center")
        self.tabla.column("Club", width=100, anchor="center")
        self.tabla.column("General", width=60, anchor="center")
        self.tabla.column("Posición", width=100, anchor="center")
        self.tabla.column("Pace", width=50, anchor="center")
        self.tabla.column("Shooting", width=50, anchor="center")
        self.tabla.column("Passing", width=50, anchor="center")
        self.tabla.column("Dribbling", width=50, anchor="center")
        self.tabla.column("Defending", width=50, anchor="center")
        self.tabla.column("Physic", width=50, anchor="center")
        self.tabla.column("GK Diving", width=50, anchor="center")
        self.tabla.column("GK Handling", width=50, anchor="center")
        self.tabla.column("GK Kicking", width=50, anchor="center")
        self.tabla.column("GK Reflexes", width=50, anchor="center")
        self.tabla.column("GK Speed", width=50, anchor="center")
        self.tabla.column("GK Positioning", width=50, anchor="center")

        # Estilo de la tabla
        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Treeview",
            background="#2a2d2e",
            foreground="white",
            rowheight=25,
            fieldbackground="#343638",
            bordercolor="#343638",
            borderwidth=0,
        )
        style.map("Treeview", background=[("selected", "#22559b")])

        style.configure(
            "Treeview.Heading", background="#565b5e", foreground="white", relief="flat"
        )
        style.map("Treeview.Heading", background=[("active", "#3484F0")])

        # Botones
        self.btn_alta = ctk.CTkButton(
            self.root, text="Agregar Carta", command=self.abrir_formulario_alta
        )
        self.btn_alta.pack(side="left", padx=10, pady=10)

        self.btn_alta_arquero = ctk.CTkButton(
            self.root,
            text="Agregar Arquero",
            command=self.abrir_formulario_alta_arquero,
        )
        self.btn_alta_arquero.pack(side="left", padx=10, pady=10)

        self.btn_modificar = ctk.CTkButton(
            self.root, text="Modificar Carta", command=self.abrir_formulario_modificar
        )
        self.btn_modificar.pack(side="left", padx=10, pady=10)

        self.btn_eliminar = ctk.CTkButton(
            self.root, text="Eliminar Carta", command=self.eliminar_carta
        )
        self.btn_eliminar.pack(side="left", padx=10, pady=10)

        self.btn_cerrar = ctk.CTkButton(self.root, text="Cerrar", command=self.cerrar)
        self.btn_cerrar.pack(side="right", padx=10, pady=10)

        # Configurar las scrollbars
        scrollbar_vertical.config(command=self.tabla.yview)
        scrollbar_horizontal.config(command=self.tabla.xview)

        # Empaquetar elementos
        scrollbar_vertical.pack(side="right", fill="y")
        scrollbar_horizontal.pack(side="bottom", fill="x")
        self.tabla.configure(style="Treeview")
        self.tabla.pack(fill="both", expand=True)

    def centrar_ventana(self):
        """Centra la ventana en la pantalla."""
        ancho_ventana = 800  # Ancho de la ventana
        alto_ventana = 400  # Alto de la ventana

        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Calcular la posición centrada
        pos_x = int((ancho_pantalla - ancho_ventana) / 2)
        pos_y = int((alto_pantalla - alto_ventana) / 2)

        # Establecer la geometría de la ventana
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    def cargar_cartas(self, cartas):
        """Carga la tabla con las cartas recibidas."""
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for carta in cartas:
            self.tabla.insert("", "end", values=carta)

    def abrir_formulario_alta(self):
        """Abre el formulario para agregar una carta."""
        FormularioCarta(
            self,
            modo="alta",
        ).iniciar()

    def abrir_formulario_alta_arquero(self):
        """Abre el formulario para agregar un arquero."""
        FormularioArquero(
            self,
            modo="alta",
        ).iniciar()

    def abrir_formulario_modificar(self):
        """Abre el formulario para modificar la carta seleccionada."""
        seleccion = self.tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar una carta para modificar.")
            return
        datos_carta = self.tabla.item(
            seleccion,
            "values",
        )
        datos_carta_arquero = datos_carta[0:5] + datos_carta[12:]
        datos_carta_jugador = datos_carta[0:5] + datos_carta[5:12]
        if datos_carta[5] == "GK":
            FormularioArquero(
                self,
                modo="modificar",
                datos_carta=datos_carta_arquero,
            ).iniciar()
        else:
            FormularioCarta(
                self,
                modo="modificar",
                datos_carta=datos_carta_jugador,
            ).iniciar()

    def eliminar_carta(self):
        """Elimina la carta seleccionada."""
        seleccion = self.tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar una carta para eliminar.")
            return
        id_carta = self.tabla.item(seleccion, "values")[0]
        if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar esta carta?"):
            self.eliminar_carta_callback(id_carta)

    def conectar_eliminar_carta(self, callback):
        self.eliminar_carta_callback = callback

    def conectar_alta_carta(self, callback):
        self.alta_carta_callback = callback

    def conectar_alta_arquero(self, callback):
        self.alta_arquero_callback = callback

    def conectar_modificar_carta(self, callback):
        self.modificar_carta_callback = callback

    def conectar_modificar_arquero(self, callback):
        self.modificar_arquero_callback = callback

    def iniciar(self):
        """Inicia la vista."""
        self.root.deiconify()

    def cerrar(self):
        """Cierra la vista."""
        self.root.withdraw()
