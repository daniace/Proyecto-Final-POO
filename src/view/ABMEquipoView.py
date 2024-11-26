from tkinter import messagebox, ttk

import customtkinter as ctk

from view.ABMView import centrar_ventana, configurar_estilo_tabla
from view.FormularioEquipoView import FormularioEquipo


class VistaABMEquipo(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        # Ventana principal
        self.title("ABM de Equipos")
        configurar_estilo_tabla(self)
        centrar_ventana(self, 800, 600)
        # Título
        self.__label_titulo = ctk.CTkLabel(
            self, text="ABM de Equipos", font=("Arial", 20)
        )
        self.__label_titulo.pack(pady=10)

        # Frame para la tabla y scrollbars
        frame_tabla = ctk.CTkFrame(self)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbars
        scrollbar_vertical = ttk.Scrollbar(frame_tabla, orient="vertical")
        scrollbar_horizontal = ttk.Scrollbar(frame_tabla, orient="horizontal")

        # Tabla para listar equipos
        self.__tabla = ttk.Treeview(
            frame_tabla,
            columns=(
                "ID_Equipo",
                "Nombre_Usuario",
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

        self.__tabla.heading("ID_Equipo", text="ID_Equipo")
        self.__tabla.heading("Nombre_Usuario", text="Nombre_Usuario")
        self.__tabla.heading("Nombre_Equipo", text="Nombre_Equipo")
        self.__tabla.heading("Carta 1", text="Carta 1")
        self.__tabla.heading("Carta 2", text="Carta 2")
        self.__tabla.heading("Carta 3", text="Carta 3")
        self.__tabla.heading("Carta 4", text="Carta 4")
        self.__tabla.heading("Carta 5", text="Carta 5")
        self.__tabla.heading("Carta 6", text="Carta 6")
        self.__tabla.heading("Carta 7", text="Carta 7")
        self.__tabla.heading("Carta 8", text="Carta 8")
        self.__tabla.heading("Carta 9", text="Carta 9")
        self.__tabla.heading("Carta 10", text="Carta 10")
        self.__tabla.heading("Carta 11", text="Carta 11")

        self.__tabla.column("ID_Equipo", width=50, anchor="center")
        self.__tabla.column("Nombre_Usuario", width=50, anchor="center")
        self.__tabla.column("Nombre_Equipo", width=100, anchor="center")
        self.__tabla.column("Carta 1", width=70, anchor="center")
        self.__tabla.column("Carta 2", width=70, anchor="center")
        self.__tabla.column("Carta 3", width=70, anchor="center")
        self.__tabla.column("Carta 4", width=70, anchor="center")
        self.__tabla.column("Carta 5", width=70, anchor="center")
        self.__tabla.column("Carta 6", width=70, anchor="center")
        self.__tabla.column("Carta 7", width=70, anchor="center")
        self.__tabla.column("Carta 8", width=70, anchor="center")
        self.__tabla.column("Carta 9", width=70, anchor="center")
        self.__tabla.column("Carta 10", width=70, anchor="center")
        self.__tabla.column("Carta 11", width=70, anchor="center")

        # Botones
        self.__btn_alta = ctk.CTkButton(
            self, text="Agregar Equipo", command=self.__abrir_formulario_alta
        )
        self.__btn_alta.pack(side="left", padx=10, pady=10)

        self.__btn_modificar = ctk.CTkButton(
            self,
            text="Modificar Equipo",
            command=self.__abrir_formulario_modificar,
        )
        self.__btn_modificar.pack(side="left", padx=10, pady=10)

        self.__btn_eliminar = ctk.CTkButton(
            self, text="Eliminar Equipo", command=self._eliminar_equipo
        )
        self.__btn_eliminar.pack(side="left", padx=10, pady=10)

        self.__btn_cerrar = ctk.CTkButton(self, text="Cerrar", command=self.withdraw)
        self.__btn_cerrar.pack(side="right", padx=10, pady=10)

        # Configurar las scrollbars
        scrollbar_vertical.config(command=self.__tabla.yview)
        scrollbar_horizontal.config(command=self.__tabla.xview)

        # Empaquetar elementos
        scrollbar_vertical.pack(side="right", fill="y")
        scrollbar_horizontal.pack(side="bottom", fill="x")
        self.__tabla.pack(fill="both", expand=True)

    def _cargar_equipos(self, equipos):
        """Carga la tabla con los equipos recibidos."""
        for item in self.__tabla.get_children():
            self.__tabla.delete(item)
        for equipo in equipos:
            self.__tabla.insert("", "end", values=equipo)

    def __abrir_formulario_alta(self):
        """Abre un formulario para agregar un nuevo equipo."""
        FormularioEquipo(self, modo="alta").iniciar()

    def __abrir_formulario_modificar(self):
        """Abre un formulario para modificar el equipo seleccionado."""
        seleccion = self.__tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un equipo para modificar.")
            return
        datos_equipo = self.__tabla.item(seleccion, "values")
        FormularioEquipo(self, modo="modificar", datos_equipo=datos_equipo).iniciar()

    def _eliminar_equipo(self):
        """Elimina el equipo seleccionado."""
        seleccion = self.__tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un equipo para eliminar.")
            return
        id_equipo = self.__tabla.item(seleccion, "values")[0]
        if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar este equipo?"):
            self._eliminar_equipo_callback(id_equipo)

    def _conectar_eliminar_equipo(self, callback):
        """Conecta el botón eliminar a un callback."""
        self._eliminar_equipo_callback = callback

    def _conectar_alta_equipo(self, callback):
        """Conecta el botón alta a un callback."""
        self._alta_equipo_callback = callback

    def _conectar_modificar_equipo(self, callback):
        """Conecta el botón modificar a un callback."""
        self._modificar_equipo_callback = callback

    def iniciar(self):
        self.deiconify()
