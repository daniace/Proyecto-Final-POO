from tkinter import messagebox, ttk

import customtkinter as ctk

from view.FormularioEquipoView import FormularioEquipo


class VistaABMEquipo(ctk.CTkToplevel):
    def __init__(self):
        # Ventana principal
        self.root = ctk.CTk()
        self.root.title("ABM de Equipos")
        self.centrar_ventana()
        # Título
        self.label_titulo = ctk.CTkLabel(
            self.root, text="ABM de Equipos", font=("Arial", 20)
        )
        self.label_titulo.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar)

        # Frame para la tabla y scrollbars
        frame_tabla = ctk.CTkFrame(self.root)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbars
        scrollbar_vertical = ttk.Scrollbar(frame_tabla, orient="vertical")
        scrollbar_horizontal = ttk.Scrollbar(frame_tabla, orient="horizontal")

        # Tabla para listar equipos
        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=(
                "ID_Equipo",
                "ID_Usuario",
                "Nombre_Equipo",
                "Carta 1",
                "Carta 2",
                "Carta 3",
                "Carta 4",
                "Carta 5",
                "Carta 6",
                "Carta 7",
                "Carta 8",
                "Carta 9",
                "Carta 10",
                "Carta 11",
            ),
            show="headings",
            yscrollcommand=scrollbar_vertical.set,
            xscrollcommand=scrollbar_horizontal.set,
        )

        self.tabla.heading("ID_Equipo", text="ID_Equipo")
        self.tabla.heading("ID_Usuario", text="ID_Usuario")
        self.tabla.heading("Nombre_Equipo", text="Nombre_Equipo")
        self.tabla.heading("Carta 1", text="Carta 1")
        self.tabla.heading("Carta 2", text="Carta 2")
        self.tabla.heading("Carta 3", text="Carta 3")
        self.tabla.heading("Carta 4", text="Carta 4")
        self.tabla.heading("Carta 5", text="Carta 5")
        self.tabla.heading("Carta 6", text="Carta 6")
        self.tabla.heading("Carta 7", text="Carta 7")
        self.tabla.heading("Carta 8", text="Carta 8")
        self.tabla.heading("Carta 9", text="Carta 9")
        self.tabla.heading("Carta 10", text="Carta 10")
        self.tabla.heading("Carta 11", text="Carta 11")

        self.tabla.column("ID_Equipo", width=50, anchor="center")
        self.tabla.column("ID_Usuario", width=50, anchor="center")
        self.tabla.column("Nombre_Equipo", width=100, anchor="center")
        self.tabla.column("Carta 1", width=50, anchor="center")
        self.tabla.column("Carta 2", width=50, anchor="center")
        self.tabla.column("Carta 3", width=50, anchor="center")
        self.tabla.column("Carta 4", width=50, anchor="center")
        self.tabla.column("Carta 5", width=50, anchor="center")
        self.tabla.column("Carta 6", width=50, anchor="center")
        self.tabla.column("Carta 7", width=50, anchor="center")
        self.tabla.column("Carta 8", width=50, anchor="center")
        self.tabla.column("Carta 9", width=50, anchor="center")
        self.tabla.column("Carta 10", width=50, anchor="center")
        self.tabla.column("Carta 11", width=50, anchor="center")

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
            self.root, text="Agregar Equipo", command=self.abrir_formulario_alta
        )
        self.btn_alta.pack(side="left", padx=10, pady=10)

        self.btn_modificar = ctk.CTkButton(
            self.root, text="Modificar Equipo", command=self.abrir_formulario_modificar
        )
        self.btn_modificar.pack(side="left", padx=10, pady=10)

        self.btn_eliminar = ctk.CTkButton(
            self.root, text="Eliminar Equipo", command=self.eliminar_equipo
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
        ancho_ventana = 600  # Ancho de la ventana
        alto_ventana = 400  # Alto de la ventana

        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Calcular la posición centrada
        pos_x = int((ancho_pantalla - ancho_ventana) / 2)
        pos_y = int((alto_pantalla - alto_ventana) / 2)

        # Establecer la geometría de la ventana
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    def cargar_equipos(self, equipos):
        """Carga la tabla con los equipos recibidos."""
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for equipo in equipos:
            self.tabla.insert("", "end", values=equipo)

    def abrir_formulario_alta(self):
        """Abre un formulario para agregar un nuevo equipo."""
        FormularioEquipo(self, modo="alta").iniciar()

    def abrir_formulario_modificar(self):
        """Abre un formulario para modificar el equipo seleccionado."""
        seleccion = self.tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un equipo para modificar.")
            return
        datos_equipo = self.tabla.item(seleccion, "values")
        FormularioEquipo(self, modo="modificar", datos_equipo=datos_equipo).iniciar()

    def eliminar_equipo(self):
        """Elimina el equipo seleccionado."""
        seleccion = self.tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un equipo para eliminar.")
            return
        id_equipo = self.tabla.item(seleccion, "values")[0]
        if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar este equipo?"):
            self.eliminar_equipo_callback(id_equipo)

    def conectar_eliminar_equipo(self, callback):
        """Conecta el botón eliminar a un callback."""
        self.eliminar_equipo_callback = callback

    def conectar_alta_equipo(self, callback):
        """Conecta el botón alta a un callback."""
        self.alta_equipo_callback = callback

    def conectar_modificar_equipo(self, callback):
        """Conecta el botón modificar a un callback."""
        self.modificar_equipo_callback = callback

    def iniciar(self):
        """Inicia la vista."""
        self.root.deiconify()

    def cerrar(self):
        """Cierra la ventana de la vista."""
        self.root.withdraw()
