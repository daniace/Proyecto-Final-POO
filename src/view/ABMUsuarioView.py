from tkinter import messagebox, ttk

import customtkinter as ctk

from view.ABMView import centrar_ventana, configurar_estilo_tabla
from view.FormularioUsuarioView import FormularioUsuario


class VistaABMUsuarios(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        # Ventana principal
        self.title("ABM de Usuarios")
        configurar_estilo_tabla(self)
        centrar_ventana(self, 800, 600)

        # Título
        self.__label_titulo = ctk.CTkLabel(
            self, text="ABM de Usuarios", font=("Arial", 20)
        )
        self.__label_titulo.pack(pady=10)

        # Frame para la tabla y scrollbars
        frame_tabla = ctk.CTkFrame(self)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbars
        scrollbar_vertical = ttk.Scrollbar(frame_tabla, orient="vertical")
        scrollbar_horizontal = ttk.Scrollbar(frame_tabla, orient="horizontal")

        # Tabla para listar usuarios
        self.__tabla = ttk.Treeview(
            frame_tabla,
            columns=("ID", "Nombre", "Password", "Admin", "Score"),
            show="headings",
            yscrollcommand=scrollbar_vertical.set,
            xscrollcommand=scrollbar_horizontal.set,
        )

        self.__tabla.heading("ID", text="ID")
        self.__tabla.heading("Nombre", text="Nombre Usuario")
        self.__tabla.heading("Password", text="Password")
        self.__tabla.heading("Admin", text="Admin")
        self.__tabla.heading("Score", text="Score")

        self.__tabla.column("ID", width=50, anchor="center")
        self.__tabla.column("Nombre", width=150, anchor="center")
        self.__tabla.column("Password", width=150, anchor="center")
        self.__tabla.column("Admin", width=50, anchor="center")
        self.__tabla.column("Score", width=50, anchor="center")

        # Botones
        self.__btn_alta = ctk.CTkButton(
            self, text="Agregar Usuario", command=self.__abrir_formulario_alta
        )
        self.__btn_alta.pack(side="left", padx=10, pady=10)

        self.__btn_modificar = ctk.CTkButton(
            self,
            text="Modificar Usuario",
            command=self.__abrir_formulario_modificar,
        )
        self.__btn_modificar.pack(side="left", padx=10, pady=10)

        self.__btn_eliminar = ctk.CTkButton(
            self, text="Eliminar Usuario", command=self._eliminar_usuario
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

    def _cargar_usuarios(self, usuarios):
        """Carga la tabla con los usuarios recibidos."""
        for item in self.__tabla.get_children():
            self.__tabla.delete(item)
        for usuario in usuarios:
            self.__tabla.insert("", "end", values=usuario)

    def __abrir_formulario_alta(self):
        """Abre un formulario para agregar un nuevo usuario."""
        FormularioUsuario(self, modo="alta").iniciar()

    def __abrir_formulario_modificar(self):
        """Abre un formulario para modificar el usuario seleccionado."""
        seleccion = self.__tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un usuario para modificar.")
            return
        datos_usuario = self.__tabla.item(seleccion, "values")
        FormularioUsuario(self, modo="modificar", datos_usuario=datos_usuario).iniciar()

    def _eliminar_usuario(self):
        """Elimina el usuario seleccionado."""
        seleccion = self.__tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un usuario para eliminar.")
            return
        id_usuario = self.__tabla.item(seleccion, "values")[0]
        if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar este usuario?"):
            self._eliminar_usuario_callback(id_usuario)

    def _conectar_eliminar_usuario(self, callback):
        """Conecta el botón eliminar a un callback."""
        self._eliminar_usuario_callback = callback

    def _conectar_alta_usuario(self, callback):
        """Conecta el botón alta a un callback."""
        self._alta_usuario_callback = callback

    def _conectar_modificar_usuario(self, callback):
        """Conecta el botón modificar a un callback."""
        self._modificar_usuario_callback = callback

    def iniciar(self):
        self.deiconify()
