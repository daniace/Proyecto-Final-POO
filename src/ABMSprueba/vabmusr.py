from tkinter import messagebox, ttk

import customtkinter as ctk
from CTkTable import CTkTable

# from ABMSprueba.formulariousuario import FormularioUsuario
from formulariousuario import FormularioUsuario


class VistaABMUsuarios:
    def __init__(self):
        # Ventana principal
        self.root = ctk.CTk()
        self.root.title("Gestión de Usuarios")
        self.centrar_ventana()
        self.visible = False
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar)

        # Título
        self.label_titulo = ctk.CTkLabel(
            self.root, text="Gestión de Usuarios", font=("Arial", 20)
        )
        self.label_titulo.pack(pady=10)

        # Frame para la tabla y scrollbars
        frame_tabla = ctk.CTkFrame(self.root)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Tabla para listar usuarios
        self.tabla = CTkTable(frame_tabla, row=10, column=4, corner_radius=0)

        self.tabla.insert(0, 0, "ID")
        self.tabla.insert(0, 1, "Nombre")
        self.tabla.insert(0, 2, "Admin")
        self.tabla.insert(0, 3, "Score")

        self.tabla.pack(fill="both", expand=True)

        # # Scrollbars
        # scrollbar_vertical = ttk.Scrollbar(frame_tabla, orient="vertical")
        # scrollbar_horizontal = ttk.Scrollbar(frame_tabla, orient="horizontal")

        # Tabla para listar usuarios
        # self.tabla = ttk.Treeview(
        #     frame_tabla,
        #     columns=("ID", "Nombre", "Admin", "Score"),
        #     show="headings",
        #     yscrollcommand=scrollbar_vertical.set,
        #     xscrollcommand=scrollbar_horizontal.set,
        # )
        # self.tabla.heading("ID", text="ID")
        # self.tabla.heading("Nombre", text="Nombre Usuario")
        # self.tabla.heading("Admin", text="Admin")
        # self.tabla.heading("Score", text="Score")

        # self.tabla.column("ID", width=50)
        # self.tabla.column("Nombre", width=150)
        # self.tabla.column("Admin", width=50)
        # self.tabla.column("Score", width=50)

        # Botones
        self.btn_alta = ctk.CTkButton(
            self.root, text="Agregar Usuario", command=self.abrir_formulario_alta
        )
        self.btn_alta.pack(side="left", padx=10, pady=10)

        self.btn_modificar = ctk.CTkButton(
            self.root, text="Modificar Usuario", command=self.abrir_formulario_modificar
        )
        self.btn_modificar.pack(side="left", padx=10, pady=10)

        self.btn_eliminar = ctk.CTkButton(
            self.root, text="Eliminar Usuario", command=self.eliminar_usuario
        )
        self.btn_eliminar.pack(side="left", padx=10, pady=10)

        self.btn_cerrar = ctk.CTkButton(self.root, text="Cerrar", command=self.cerrar)
        self.btn_cerrar.pack(side="right", padx=10, pady=10)

        # # Configurar las scrollbars
        # scrollbar_vertical.config(command=self.tabla.yview)
        # scrollbar_horizontal.config(command=self.tabla.xview)

        # # Empaquetar elementos
        # scrollbar_vertical.pack(side="right", fill="y")
        # scrollbar_horizontal.pack(side="bottom", fill="x")
        # self.tabla.pack(fill="both", expand=True)

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

    def cargar_usuarios(self, usuarios):
        """Carga la tabla con los usuarios recibidos."""
        for i, usuario in enumerate(usuarios):
            self.tabla.insert(i + 1, 0, usuario[0])
            self.tabla.insert(i + 1, 1, usuario[1])
            self.tabla.insert(i + 1, 2, usuario[2])
            self.tabla.insert(i + 1, 3, usuario[3])

    def abrir_formulario_alta(self):
        """Abre un formulario para agregar un nuevo usuario."""
        FormularioUsuario(self, modo="alta").iniciar()

    def abrir_formulario_modificar(self):
        """Abre un formulario para modificar el usuario seleccionado."""
        seleccion = self.tabla.select_row()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un usuario para modificar.")
            return
        datos_usuario = self.tabla.get_row(seleccion)
        FormularioUsuario(self, modo="modificar", datos_usuario=datos_usuario).iniciar()

    def eliminar_usuario(self):
        """Elimina el usuario seleccionado."""
        seleccion = self.tabla.focus()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un usuario para eliminar.")
            return
        id_usuario = self.tabla.item(seleccion, "values")[0]
        if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar este usuario?"):
            self.eliminar_usuario_callback(id_usuario)

    def conectar_eliminar_usuario(self, callback):
        """Conecta el botón eliminar a un callback."""
        self.eliminar_usuario_callback = callback

    def conectar_alta_usuario(self, callback):
        """Conecta el botón alta a un callback."""
        self.alta_usuario_callback = callback

    def conectar_modificar_usuario(self, callback):
        """Conecta el botón modificar a un callback."""
        self.modificar_usuario_callback = callback

    def iniciar(self):
        """Inicia la vista."""
        self.visible = True
        self.root.mainloop()

    def cerrar(self):
        """Cierra la ventana de la vista."""
        self.visible = False
        self.root.destroy()


if __name__ == "__main__":
    VistaABMUsuarios().iniciar()
