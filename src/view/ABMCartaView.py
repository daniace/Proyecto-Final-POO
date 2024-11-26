from tkinter import messagebox, ttk

import customtkinter as ctk

from view.ABMView import centrar_ventana, configurar_estilo_tabla
from view.FormularioArqueroView import FormularioArquero
from view.FormularioCartaView import FormularioCarta


class VistaABMCartas(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        # Ventana principal
        self.title("ABM de Cartas")
        configurar_estilo_tabla(self)
        centrar_ventana(self, 1200, 600)
        # Título
        self.__label_titulo = ctk.CTkLabel(
            self, text="ABM de Cartas", font=("Arial", 20)
        )
        self.__label_titulo.pack(pady=10)

        # Frame para la tabla y scrollbars
        frame_tabla = ctk.CTkFrame(self)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbars
        scrollbar_vertical = ttk.Scrollbar(frame_tabla, orient="vertical")
        scrollbar_horizontal = ttk.Scrollbar(frame_tabla, orient="horizontal")

        # Tabla para listar cartas
        self.__tabla = ttk.Treeview(
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
        self.__tabla.heading("ID", text="ID")
        self.__tabla.heading("Nombre", text="Nombre")
        self.__tabla.heading("Nacionalidad", text="Nacionalidad")
        self.__tabla.heading("Club", text="Club")
        self.__tabla.heading("General", text="General")
        self.__tabla.heading("Posición", text="Posición")
        self.__tabla.heading("Pace", text="Pace")
        self.__tabla.heading("Shooting", text="Shooting")
        self.__tabla.heading("Passing", text="Passing")
        self.__tabla.heading("Dribbling", text="Dribbling")
        self.__tabla.heading("Defending", text="Defending")
        self.__tabla.heading("Physic", text="Physic")
        self.__tabla.heading("GK Diving", text="GK Diving")
        self.__tabla.heading("GK Handling", text="GK Handling")
        self.__tabla.heading("GK Kicking", text="GK Kicking")
        self.__tabla.heading("GK Reflexes", text="GK Reflexes")
        self.__tabla.heading("GK Speed", text="GK Speed")
        self.__tabla.heading("GK Positioning", text="GK Positioning")

        # Configuración de columnas
        self.__tabla.column("ID", width=50, anchor="center")
        self.__tabla.column("Nombre", width=100, anchor="center")
        self.__tabla.column("Nacionalidad", width=100, anchor="center")
        self.__tabla.column("Club", width=100, anchor="center")
        self.__tabla.column("General", width=60, anchor="center")
        self.__tabla.column("Posición", width=100, anchor="center")
        self.__tabla.column("Pace", width=50, anchor="center")
        self.__tabla.column("Shooting", width=50, anchor="center")
        self.__tabla.column("Passing", width=50, anchor="center")
        self.__tabla.column("Dribbling", width=50, anchor="center")
        self.__tabla.column("Defending", width=50, anchor="center")
        self.__tabla.column("Physic", width=50, anchor="center")
        self.__tabla.column("GK Diving", width=50, anchor="center")
        self.__tabla.column("GK Handling", width=50, anchor="center")
        self.__tabla.column("GK Kicking", width=50, anchor="center")
        self.__tabla.column("GK Reflexes", width=50, anchor="center")
        self.__tabla.column("GK Speed", width=50, anchor="center")
        self.__tabla.column("GK Positioning", width=50, anchor="center")

        # Botones
        self.__btn_alta = ctk.CTkButton(
            self, text="Agregar Carta", command=self.__abrir_formulario_alta
        )
        self.__btn_alta.pack(side="left", padx=10, pady=10)

        self.__btn_alta_arquero = ctk.CTkButton(
            self,
            text="Agregar Arquero",
            command=self.__abrir_formulario_alta_arquero,
        )
        self.__btn_alta_arquero.pack(side="left", padx=10, pady=10)

        self.__btn_modificar = ctk.CTkButton(
            self,
            text="Modificar Carta",
            command=self.__abrir_formulario_modificar,
        )
        self.__btn_modificar.pack(side="left", padx=10, pady=10)

        self.__btn_eliminar = ctk.CTkButton(
            self, text="Eliminar Carta", command=self._eliminar_carta
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

    def _cargar_cartas(self, cartas):
        """Carga la tabla con las cartas recibidas."""
        for item in self.__tabla.get_children():
            self.__tabla.delete(item)
        for carta in cartas:
            self.__tabla.insert("", "end", values=carta)

    def __abrir_formulario_alta(self):
        """Abre el formulario para agregar una carta."""
        FormularioCarta(
            self,
            modo="alta",
        ).iniciar()

    def __abrir_formulario_alta_arquero(self):
        """Abre el formulario para agregar un arquero."""
        FormularioArquero(
            self,
            modo="alta",
        ).iniciar()

    def __abrir_formulario_modificar(self):
        """Abre el formulario para modificar la carta seleccionada."""
        seleccion = self.__tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar una carta para modificar.")
            return
        datos_carta = self.__tabla.item(
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

    def _eliminar_carta(self):
        """Elimina la carta seleccionada."""
        seleccion = self.__tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar una carta para eliminar.")
            return
        id_carta = self.__tabla.item(seleccion, "values")[0]
        if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar esta carta?"):
            self._eliminar_carta_callback(id_carta)

    def _conectar_eliminar_carta(self, callback):
        self._eliminar_carta_callback = callback

    def _conectar_alta_carta(self, callback):
        self._alta_carta_callback = callback

    def _conectar_alta_arquero(self, callback):
        self._alta_arquero_callback = callback

    def _conectar_modificar_carta(self, callback):
        self._modificar_carta_callback = callback

    def _conectar_modificar_arquero(self, callback):
        self._modificar_arquero_callback = callback

    def iniciar(self):
        self.deiconify()
