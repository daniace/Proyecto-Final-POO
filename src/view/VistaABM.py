import re
from tkinter import messagebox, ttk

import customtkinter as ctk


def centrar_ventana(self, ancho, alto):
    # Obtener el tamaño de la pantalla
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()

    # Obtener el tamaño de la ventana
    window_width = ancho
    window_height = alto

    # Calcular la posición de la ventana para centrarla
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Establecer la geometría de la ventana
    self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")


class LoginView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Login")
        # self.geometry("250x250")
        self.resizable(False, False)
        centrar_ventana(self, 250, 250)

        # Login UI
        self.label_usuario = ctk.CTkLabel(self, text="Usuario")
        self.label_usuario.pack(pady=10)
        self.entry_usuario = ctk.CTkEntry(self)
        self.entry_usuario.pack()

        self.label_password = ctk.CTkLabel(self, text="Contraseña")
        self.label_password.pack(pady=10)
        self.entry_password = ctk.CTkEntry(self, show="*")
        self.entry_password.pack()

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        # Lógica para login
        if self.controller.validar_login(
            self.entry_usuario.get(), self.entry_password.get()
        ):
            # usuario = self.entry_usuario.get()
            # password = self.entry_password.get()
            # if usuario == "admin" and password == "admin":
            self.destroy()  # Cerrar ventana de login
            MainView(self.controller).mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")


class MainView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de la Aplicación")
        # self.geometry("800x600")
        centrar_ventana(self, 800, 600)
        # Crear pestañas
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True)

        # Pestañas
        self.tab_usuarios = self.tabview.add("ABM Usuarios")
        self.tab_equipos = self.tabview.add("ABM Equipos")
        self.tab_cartas = self.tabview.add("ABM Cartas")

        # Configurar cada pestaña
        self.setup_tab_usuarios()
        self.setup_tab_equipos()
        self.setup_tab_cartas()

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

    def setup_tab_usuarios(self):
        # Frame para contener la tabla y el scrollbar
        frame_tabla_usuarios = ctk.CTkFrame(self.tab_usuarios)
        frame_tabla_usuarios.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbar vertical
        scrollbar_y = ctk.CTkScrollbar(frame_tabla_usuarios, orientation="vertical")
        scrollbar_y.pack(side="right", fill="y")

        # Scrollbar horizontal
        scrollbar_x = ctk.CTkScrollbar(frame_tabla_usuarios, orientation="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        # Tabla para Usuarios
        self.tree_usuarios = ttk.Treeview(
            frame_tabla_usuarios,
            columns=("ID", "Nombre", "Password", "Admin", "Score"),
            show="headings",
        )
        self.tree_usuarios.heading("ID", text="ID")
        self.tree_usuarios.heading("Nombre", text="Nombre")
        self.tree_usuarios.heading("Password", text="Password")
        self.tree_usuarios.heading("Admin", text="Admin")
        self.tree_usuarios.heading("Score", text="Score")

        self.tree_usuarios.column("ID", width=15, anchor="center")
        self.tree_usuarios.column("Nombre", width=200, anchor="center")
        self.tree_usuarios.column("Password", width=200, anchor="center")
        self.tree_usuarios.column("Admin", width=15, anchor="center")
        self.tree_usuarios.column("Score", width=15, anchor="center")
        self.tree_usuarios.pack(fill="both", expand=True)

        # Configurar los scrollbars
        scrollbar_y.configure(command=self.tree_usuarios.yview)
        scrollbar_x.configure(command=self.tree_usuarios.xview)
        self.tree_usuarios.configure(
            yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set
        )

        # Botones para agregar/actualizar/eliminar
        frame_botones_usuarios = ctk.CTkFrame(self.tab_usuarios)
        frame_botones_usuarios.pack(fill="x", padx=10, pady=10)

        # Agregar Usuario
        self.btn_agregar_usuario = ctk.CTkButton(
            frame_botones_usuarios,
            text="Agregar Usuario",
            command=self.formulario_agregar_usuario,
        )
        self.btn_agregar_usuario.pack(side="left", pady=10, padx=10)

        # Modificar Usuario
        self.btn_modificar_usuario = ctk.CTkButton(
            frame_botones_usuarios,
            text="Modificar Usuario",
            command=self.modificar_usuario,
        )
        self.btn_modificar_usuario.pack(side="left", pady=10, padx=10)

        # Eliminar Usuario
        self.btn_eliminar_usuario = ctk.CTkButton(
            frame_botones_usuarios,
            text="Eliminar Usuario",
            command=self.eliminar_usuario,
        )
        self.btn_eliminar_usuario.pack(side="left", pady=10, padx=10)

        # Cargar datos
        self.load_usuarios()

    def load_usuarios(self):
        for row in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(row)
        usuarios = self.controller.get_usuario()
        for usuario in usuarios:
            self.tree_usuarios.insert("", "end", values=usuario)

    def eliminar_usuario(self):
        seleccion = self.tree_usuarios.focus()
        if seleccion:
            usuario_seleccionado = self.tree_usuarios.item(seleccion)["values"]
            id_usuario = usuario_seleccionado[0]
            self.controller.delete_usuario(id_usuario)
            self.load_usuarios()

    def formulario_agregar_usuario(self):
        # Crear una nueva ventana para el formulario de agregar usuario
        formulario_usuario = ctk.CTkToplevel(self)
        # Poner la ventana en frente
        formulario_usuario.attributes("-topmost", True)
        formulario_usuario.title("Agregar Usuario")
        # formulario_usuario.geometry("300x300")
        formulario_usuario.resizable(False, False)
        centrar_ventana(formulario_usuario, 300, 300)

        # Campos del formulario
        label_nombre = ctk.CTkLabel(formulario_usuario, text="Nombre")
        label_nombre.pack(pady=10)

        entry_nombre = ctk.CTkEntry(formulario_usuario)
        entry_nombre.pack()

        label_password = ctk.CTkLabel(formulario_usuario, text="Password")
        label_password.pack(pady=10)

        entry_password = ctk.CTkEntry(formulario_usuario, show="*")
        entry_password.pack()

        entry_admin = ctk.CTkCheckBox(formulario_usuario, text="Admin")
        entry_admin.pack(pady=10)

        def guardar_usuario():
            nombre = entry_nombre.get()
            password = entry_password.get()
            admin = entry_admin.get()
            self.controller.add_usuario(nombre, password, admin)
            formulario_usuario.destroy()
            self.load_usuarios()

        # Botón para guardar el usuario
        btn_guardar = ctk.CTkButton(
            formulario_usuario, text="Guardar", command=guardar_usuario
        )
        btn_guardar.pack(pady=10)

    def modificar_usuario(self):
        seleccion = self.tree_usuarios.focus()
        usuario_seleccionado = self.tree_usuarios.item(seleccion)["values"]

        if not seleccion:
            messagebox.showerror("Error", "Seleccione un usuario para modificar")
            return

        # Obtener los datos del usuario seleccionado
        id_usuario = usuario_seleccionado[0]
        nombre = usuario_seleccionado[1]
        password = usuario_seleccionado[2]
        admin = usuario_seleccionado[3]
        score = usuario_seleccionado[4]

        self.formulario_modificar_usuario(id_usuario, nombre, password, admin, score)

    def formulario_modificar_usuario(self, id_usuario, nombre, password, admin, score):
        # Crear una nueva ventana para el formulario de modificar usuario
        formulario_usuario = ctk.CTkToplevel(self)
        # Poner la ventana en frente
        formulario_usuario.attributes("-topmost", True)
        formulario_usuario.title("Modificar Usuario")
        # formulario_usuario.geometry("300x380")
        formulario_usuario.resizable(False, False)
        centrar_ventana(formulario_usuario, 300, 380)

        # Campos del formulario
        label_nombre = ctk.CTkLabel(formulario_usuario, text="Nombre")
        label_nombre.pack(pady=10)

        entry_nombre = ctk.CTkEntry(formulario_usuario)
        entry_nombre.insert(0, nombre)
        entry_nombre.pack()

        label_password = ctk.CTkLabel(formulario_usuario, text="Password")
        label_password.pack(pady=10)

        entry_password = ctk.CTkEntry(formulario_usuario, show="*")
        entry_password.insert(0, password)
        entry_password.pack()

        label_score = ctk.CTkLabel(formulario_usuario, text="Score")
        label_score.pack(pady=10)

        entry_score = ctk.CTkEntry(formulario_usuario)
        entry_score.insert(0, score)
        entry_score.pack()

        entry_admin = ctk.CTkCheckBox(formulario_usuario, text="Admin")
        if admin == 1:
            entry_admin.select()
        entry_admin.pack(pady=10)

        def __modificar_usuario(id_usuario=id_usuario):
            id_usuario = id_usuario
            nombre = entry_nombre.get()
            password = entry_password.get()
            admin = entry_admin.get()
            score = entry_score.get()
            self.controller.update_usuario(id_usuario, nombre, password, admin, score)
            formulario_usuario.destroy()
            self.load_usuarios()

        # Botón para guardar el usuario
        btn_guardar = ctk.CTkButton(
            formulario_usuario, text="Guardar", command=__modificar_usuario
        )
        btn_guardar.pack(pady=10)

    def setup_tab_equipos(self):
        # Frame para contener la tabla y el scrollbar
        frame_tabla_equipos = ctk.CTkFrame(self.tab_equipos)
        frame_tabla_equipos.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbar vertical
        scrollbar_y = ctk.CTkScrollbar(frame_tabla_equipos, orientation="vertical")
        scrollbar_y.pack(side="right", fill="y")

        # Scrollbar horizontal
        scrollbar_x = ctk.CTkScrollbar(frame_tabla_equipos, orientation="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        # Tabla para Equipos
        self.tree_equipos = ttk.Treeview(
            frame_tabla_equipos,
            columns=(
                "ID Equipo",
                "Usuario",
                "Nombre Equipo",
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
        )

        self.tree_equipos.heading("ID Equipo", text="ID Equipo")
        self.tree_equipos.heading("Usuario", text="Usuario")
        self.tree_equipos.heading("Nombre Equipo", text="Nombre Equipo")
        self.tree_equipos.heading("Carta 1", text="Carta 1")
        self.tree_equipos.heading("Carta 2", text="Carta 2")
        self.tree_equipos.heading("Carta 3", text="Carta 3")
        self.tree_equipos.heading("Carta 4", text="Carta 4")
        self.tree_equipos.heading("Carta 5", text="Carta 5")
        self.tree_equipos.heading("Carta 6", text="Carta 6")
        self.tree_equipos.heading("Carta 7", text="Carta 7")
        self.tree_equipos.heading("Carta 8", text="Carta 8")
        self.tree_equipos.heading("Carta 9", text="Carta 9")
        self.tree_equipos.heading("Carta 10", text="Carta 10")
        self.tree_equipos.heading("Carta 11", text="Carta 11")

        self.tree_equipos.column("ID Equipo", width=80, anchor="center")
        self.tree_equipos.column("Usuario", width=80, anchor="center")
        self.tree_equipos.column("Nombre Equipo", width=100, anchor="center")
        self.tree_equipos.column("Carta 1", width=80, anchor="center")
        self.tree_equipos.column("Carta 2", width=80, anchor="center")
        self.tree_equipos.column("Carta 3", width=80, anchor="center")
        self.tree_equipos.column("Carta 4", width=80, anchor="center")
        self.tree_equipos.column("Carta 5", width=80, anchor="center")
        self.tree_equipos.column("Carta 6", width=80, anchor="center")
        self.tree_equipos.column("Carta 7", width=80, anchor="center")
        self.tree_equipos.column("Carta 8", width=80, anchor="center")
        self.tree_equipos.column("Carta 9", width=80, anchor="center")
        self.tree_equipos.column("Carta 10", width=80, anchor="center")
        self.tree_equipos.column("Carta 11", width=80, anchor="center")

        self.tree_equipos.pack(fill="both", expand=True)

        # Configurar los scrollbars
        scrollbar_y.configure(command=self.tree_equipos.yview)
        scrollbar_x.configure(command=self.tree_equipos.xview)
        self.tree_equipos.configure(
            yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set
        )

        # Botones para agregar/actualizar/eliminar
        frame_botones_equipos = ctk.CTkFrame(self.tab_equipos)
        frame_botones_equipos.pack(fill="x", padx=10, pady=10)

        # Agregar Equipo
        self.btn_agregar_equipo = ctk.CTkButton(
            frame_botones_equipos,
            text="Agregar Equipo",
            command=self.formulario_agregar_equipo,
        )
        self.btn_agregar_equipo.pack(side="left", pady=10, padx=10)

        # Modificar Equipo
        self.btn_modificar_equipo = ctk.CTkButton(
            frame_botones_equipos,
            text="Modificar Equipo",
            command=self.modificar_equipo,
        )
        self.btn_modificar_equipo.pack(side="left", pady=10, padx=10)

        # Eliminar Equipo
        self.btn_eliminar_equipo = ctk.CTkButton(
            frame_botones_equipos, text="Eliminar Equipo", command=self.eliminar_equipo
        )
        self.btn_eliminar_equipo.pack(side="left", pady=10, padx=10)

        # Cargar datos
        self.load_equipos()

    def load_equipos(self):
        for row in self.tree_equipos.get_children():
            self.tree_equipos.delete(row)
        equipos = self.controller.get_equipos()
        for equipo in equipos:
            self.tree_equipos.insert("", "end", values=equipo)

    def formulario_agregar_equipo(self):
        # Crear una nueva ventana para el formulario de agregar equipo
        formulario_equipo = ctk.CTkToplevel(self)
        formulario_equipo.attributes("-topmost", True)
        formulario_equipo.title("Agregar Equipo")
        formulario_equipo.resizable(False, False)
        centrar_ventana(formulario_equipo, 350, 400)

        frame_formulario = ctk.CTkFrame(formulario_equipo)
        frame_formulario.pack(fill="both", expand=True, padx=10, pady=10)

        # Obtener los diccionarios originales
        dict_usuarios = self.controller.get_equipo_usuario()
        dict_cartas = self.controller.get_equipo_carta()

        # Campos del formulario
        entry_nombre_equipo = ctk.CTkEntry(
            frame_formulario, placeholder_text="Nombre Equipo"
        )

        entry_nombre_usuario = ctk.CTkComboBox(
            frame_formulario,
            values=list(dict_usuarios.values()),
            state="readonly",
        )
        entry_nombre_usuario.set("Usuario")

        # Crear entradas de cartas dinámicamente
        cartas_entries = []
        for i in range(1, 12):
            entry_carta = ctk.CTkComboBox(
                frame_formulario,
                values=list(dict_cartas.values()),
                state="readonly",
            )
            entry_carta.set(f"Carta {i}")
            cartas_entries.append(entry_carta)

        # Posicionar Widgets
        entry_nombre_equipo.grid(row=0, pady=10, padx=10)
        entry_nombre_usuario.grid(row=1, column=0, pady=10, padx=10)

        for i, entry_carta in enumerate(cartas_entries, start=1):
            entry_carta.grid(row=(i // 2) + 1, column=(i % 2), pady=10, padx=10)

        def guardar_equipo():
            nombre_equipo = entry_nombre_equipo.get()

            # Validar nombre del equipo
            if not nombre_equipo.strip():
                messagebox.showerror(
                    "Error", "El nombre del equipo no puede estar vacío."
                )
                return

            # Obtener el ID del usuario seleccionado
            nombre_usuario = entry_nombre_usuario.get()
            id_usuario = next(
                (
                    id
                    for id, nombre in dict_usuarios.items()
                    if nombre == nombre_usuario
                ),
                None,
            )

            if not id_usuario:
                messagebox.showerror("Error", "Debe seleccionar un usuario.")
                return

            # Obtener los IDs de las cartas seleccionadas
            cartas_ids = []
            for entry_carta in cartas_entries:
                nombre_carta = entry_carta.get()
                id_carta = next(
                    (
                        id
                        for id, nombre in dict_cartas.items()
                        if nombre == nombre_carta
                    ),
                    None,
                )
                if not id_carta:  # Validar que cada carta tenga un valor
                    messagebox.showerror(
                        "Error", "Debe seleccionar una carta para cada posición."
                    )
                    return
                cartas_ids.append(id_carta)

            # Llamar al controlador con los IDs
            try:
                self.controller.add_equipo(
                    nombre_equipo,
                    id_usuario,
                    *cartas_ids,  # Pasar los IDs de las cartas como argumentos
                )
                formulario_equipo.destroy()
                self.load_equipos()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al guardar: {e}")

        # Botón para guardar
        boton_guardar = ctk.CTkButton(
            frame_formulario, text="Guardar", command=guardar_equipo, width=300
        )
        boton_guardar.grid(
            row=8, column=0, columnspan=2, pady=10, padx=10, sticky="nsew"
        )

    def modificar_equipo(self):
        seleccion = self.tree_equipos.focus()
        equipo_seleccionado = self.tree_equipos.item(seleccion)["values"]

        if not seleccion:
            messagebox.showerror("Error", "Seleccione un equipo para modificar")
            return

        # Obtener los datos del equipo seleccionado
        id_equipo = equipo_seleccionado[0]
        nombre_equipo = equipo_seleccionado[1]
        id_usuario = equipo_seleccionado[2]
        cartas_ids = equipo_seleccionado[3:]

        self.formulario_modificar_equipo(
            id_equipo, nombre_equipo, id_usuario, *cartas_ids
        )

    def formulario_modificar_equipo(
        self, id_equipo, nombre_equipo, id_usuario, *cartas_ids
    ):
        # Crear una nueva ventana para el formulario de modificar equipo
        formulario_equipo = ctk.CTkToplevel(self)
        formulario_equipo.attributes("-topmost", True)
        formulario_equipo.title("Modificar Equipo")
        formulario_equipo.resizable(False, False)
        centrar_ventana(formulario_equipo, 350, 400)

        frame_formulario = ctk.CTkFrame(formulario_equipo)
        frame_formulario.pack(fill="both", expand=True, padx=10, pady=10)

        # Obtener los diccionarios originales
        dict_usuarios = self.controller.get_equipo_usuario()
        dict_cartas = self.controller.get_equipo_carta()

        # Campos del formulario
        entry_nombre_equipo = ctk.CTkEntry(
            frame_formulario, placeholder_text="Nombre Equipo"
        )
        entry_nombre_equipo.insert(0, nombre_equipo)

        entry_nombre_usuario = ctk.CTkComboBox(
            frame_formulario,
            values=list(dict_usuarios.values()),
            state="readonly",
        )

        # Seleccionar el usuario actual
        entry_nombre_usuario.set(dict_usuarios[id_usuario])

        # Verificar si id_usuario está en el diccionario
        if id_usuario in dict_usuarios:
            entry_nombre_usuario.set(dict_usuarios[id_usuario])
        else:
            # Manejar el caso en que no se encuentre el id_usuario
            messagebox.showerror(
                "Error", f"No se encontró el usuario con id {id_usuario}"
            )
            return

        # Crear entradas de cartas dinámicamente
        cartas_entries = []
        for i in range(1, 12):
            entry_carta = ctk.CTkComboBox(
                frame_formulario,
                values=list(dict_cartas.values()),
                state="readonly",
            )
            entry_carta.set(dict_cartas[cartas_ids[i - 1]])
            cartas_entries.append(entry_carta)

        # Posicionar Widgets
        entry_nombre_equipo.grid(row=0, pady=10, padx=10)
        entry_nombre_usuario.grid(row=1, pady=10, padx=10)
        for i, entry_carta in enumerate(cartas_entries, start=2):
            entry_carta.grid(row=i, pady=10, padx=10)

        def guardar_equipo():
            nombre_equipo = entry_nombre_equipo.get()
            nombre_usuario = entry_nombre_usuario.get()

            # Validar nombre del equipo
            if not nombre_equipo.strip():
                messagebox.showerror(
                    "Error", "El nombre del equipo no puede estar vacío."
                )
                return

            # Obtener el ID del usuario seleccionado
            id_usuario = next(
                (
                    id
                    for id, nombre in dict_usuarios.items()
                    if nombre == nombre_usuario
                ),
                None,
            )

            if not id_usuario:
                messagebox.showerror("Error", "Debe seleccionar un usuario.")
                return

            # Obtener los IDs de las cartas seleccionadas
            cartas_ids = []
            for entry_carta in cartas_entries:
                nombre_carta = entry_carta.get()
                id_carta = next(
                    (
                        id
                        for id, nombre in dict_cartas.items()
                        if nombre == nombre_carta
                    ),
                    None,
                )
                if not id_carta:  # Validar que cada carta tenga un valor
                    messagebox.showerror(
                        "Error", "Debe seleccionar una carta para cada posición."
                    )
                    return
                cartas_ids.append(id_carta)

            # Llamar al controlador con los IDs
            try:
                self.controller.update_equipo(
                    id_equipo,
                    nombre_equipo,
                    id_usuario,
                    *cartas_ids,  # Pasar los IDs de las cartas como argumentos
                )
                formulario_equipo.destroy()
                self.load_equipos()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al guardar: {e}")

        # Botón para guardar
        boton_guardar = ctk.CTkButton(
            frame_formulario, text="Guardar", command=guardar_equipo, width=300
        )
        boton_guardar.grid(
            row=8, column=0, columnspan=2, pady=10, padx=10, sticky="nsew"
        )

    def eliminar_equipo(self):
        seleccion = self.tree_equipos.focus()
        if seleccion:
            equipo_seleccionado = self.tree_equipos.item(seleccion)["values"]
            id_equipo = equipo_seleccionado[0]
            self.controller.delete_equipo(id_equipo)
            self.load_equipos()

    def setup_tab_cartas(self):
        # Frame para contener la tabla y el scrollbar
        frame_tabla_cartas = ctk.CTkFrame(self.tab_cartas)
        frame_tabla_cartas.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbar vertical
        scrollbar_y = ctk.CTkScrollbar(frame_tabla_cartas, orientation="vertical")
        scrollbar_y.pack(side="right", fill="y")

        # Scrollbar horizontal
        scrollbar_x = ctk.CTkScrollbar(frame_tabla_cartas, orientation="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        # Tabla de cartas
        self.tree_cartas = ttk.Treeview(
            frame_tabla_cartas,
            columns=(
                "ID Carta",
                "Nombre Carta",
                "Nacionalidad",
                "Club",
                "Promedio",
                "Posicion",
                "Dorsal",
                "Velocidad",
                "Tiro",
                "Pase",
                "Gambeta",
                "Defensa",
                "Fisico",
                "(GK) Salto",
                "(GK) Control",
                "(GK) Despeje",
                "(GK) Reflejos",
                "(GK) Velocidad",
                "(GK) Posicionamiento",
            ),
            show="headings",
        )

        self.tree_cartas.heading("ID Carta", text="ID Carta")
        self.tree_cartas.heading("Nombre Carta", text="Nombre Carta")
        self.tree_cartas.heading("Nacionalidad", text="Nacionalidad")
        self.tree_cartas.heading("Club", text="Club")
        self.tree_cartas.heading("Promedio", text="Promedio")
        self.tree_cartas.heading("Posicion", text="Posicion")
        self.tree_cartas.heading("Dorsal", text="Dorsal")
        self.tree_cartas.heading("Velocidad", text="Velocidad")
        self.tree_cartas.heading("Tiro", text="Tiro")
        self.tree_cartas.heading("Pase", text="Pase")
        self.tree_cartas.heading("Gambeta", text="Gambeta")
        self.tree_cartas.heading("Defensa", text="Defensa")
        self.tree_cartas.heading("Fisico", text="Fisico")
        self.tree_cartas.heading("(GK) Salto", text="(GK) Salto")
        self.tree_cartas.heading("(GK) Control", text="(GK) Control")
        self.tree_cartas.heading("(GK) Despeje", text="(GK) Despeje")
        self.tree_cartas.heading("(GK) Reflejos", text="(GK) Reflejos")
        self.tree_cartas.heading("(GK) Velocidad", text="(GK) Velocidad")
        self.tree_cartas.heading("(GK) Posicionamiento", text="(GK) Posicionamiento")

        self.tree_cartas.column("ID Carta", width=50, anchor="center")
        self.tree_cartas.column("Nombre Carta", width=100, anchor="center")
        self.tree_cartas.column("Nacionalidad", width=100, anchor="center")
        self.tree_cartas.column("Club", width=100, anchor="center")
        self.tree_cartas.column("Promedio", width=50, anchor="center")
        self.tree_cartas.column("Posicion", width=50, anchor="center")
        self.tree_cartas.column("Dorsal", width=50, anchor="center")
        self.tree_cartas.column("Velocidad", width=50, anchor="center")
        self.tree_cartas.column("Tiro", width=50, anchor="center")
        self.tree_cartas.column("Pase", width=50, anchor="center")
        self.tree_cartas.column("Gambeta", width=50, anchor="center")
        self.tree_cartas.column("Defensa", width=50, anchor="center")
        self.tree_cartas.column("Fisico", width=50, anchor="center")
        self.tree_cartas.column("(GK) Salto", width=50, anchor="center")
        self.tree_cartas.column("(GK) Control", width=50, anchor="center")
        self.tree_cartas.column("(GK) Despeje", width=50, anchor="center")
        self.tree_cartas.column("(GK) Reflejos", width=50, anchor="center")
        self.tree_cartas.column("(GK) Velocidad", width=50, anchor="center")
        self.tree_cartas.column("(GK) Posicionamiento", width=50, anchor="center")

        self.tree_cartas.pack(fill="both", expand=True)

        # Configurar los scrollbars
        scrollbar_y.configure(command=self.tree_cartas.yview)
        scrollbar_x.configure(command=self.tree_cartas.xview)
        self.tree_cartas.configure(
            yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set
        )

        # Botones para agregar/actualizar/eliminar
        frame_botones_cartas = ctk.CTkFrame(self.tab_cartas)
        frame_botones_cartas.pack(fill="x", padx=10, pady=10)

        btn_agregar_carta = ctk.CTkButton(
            frame_botones_cartas,
            text="Agregar Carta",
            command=self.formulario_agregar_carta,
        )
        btn_agregar_carta.pack(side="left", pady=10, padx=10)

        btn_agregar_arquero = ctk.CTkButton(
            frame_botones_cartas,
            text="Agregar Arquero",
            command=self.formulario_agregar_arquero,
        )
        btn_agregar_arquero.pack(side="left", pady=10, padx=10)

        btn_modificar_carta = ctk.CTkButton(
            frame_botones_cartas,
            text="Modificar Carta",
            command=self.modificar_carta,
        )
        btn_modificar_carta.pack(side="left", pady=10, padx=10)

        btn_eliminar_carta = ctk.CTkButton(
            frame_botones_cartas, text="Eliminar Carta", command=self.eliminar_carta
        )
        btn_eliminar_carta.pack(side="left", pady=10, padx=10)

        # Cargar datos
        self.load_cartas()

    def load_cartas(self):
        for row in self.tree_cartas.get_children():
            self.tree_cartas.delete(row)
        cartas = self.controller.get_cartas()
        for carta in cartas:
            self.tree_cartas.insert("", "end", values=carta)

    def eliminar_carta(self):
        selected_item = self.tree_cartas.selection()[0]
        carta_id = self.tree_cartas.item(selected_item)["values"][0]
        self.controller.delete_carta(carta_id)
        self.load_cartas()

    def formulario_agregar_carta(self):
        # Crear una nueva ventana para el formulario de agregar carta
        formulario_carta = ctk.CTkToplevel(self)
        # Poner la ventana en frente
        formulario_carta.attributes("-topmost", True)
        formulario_carta.title("Agregar Carta")
        # formulario_carta.geometry("300x300")
        formulario_carta.resizable(False, False)
        centrar_ventana(formulario_carta, 350, 300)

        frame_formulario = ctk.CTkFrame(formulario_carta)
        frame_formulario.pack(fill="both", expand=True, padx=10, pady=10)

        # Campos del formulario
        entry_nombre = ctk.CTkEntry(frame_formulario, placeholder_text="Nombre")
        entry_promedio = ctk.CTkEntry(frame_formulario, placeholder_text="Promedio")
        entry_dorsal = ctk.CTkEntry(frame_formulario, placeholder_text="Dorsal")
        entry_velocidad = ctk.CTkEntry(frame_formulario, placeholder_text="Velocidad")
        entry_tiro = ctk.CTkEntry(frame_formulario, placeholder_text="Tiro")
        entry_pase = ctk.CTkEntry(frame_formulario, placeholder_text="Pase")
        entry_gambeta = ctk.CTkEntry(frame_formulario, placeholder_text="Gambeta")
        entry_defensa = ctk.CTkEntry(frame_formulario, placeholder_text="Defensa")
        entry_fisico = ctk.CTkEntry(frame_formulario, placeholder_text="Fisico")
        desplegable_nacionalidad = ctk.CTkComboBox(
            frame_formulario,
            values=self.controller.get_carta_nacionalidad(),
            state="readonly",
        )
        desplegable_nacionalidad.set("Nacionalidad")
        desplegable_posicion = ctk.CTkComboBox(
            frame_formulario,
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
            command=self.get_posicion,
        )
        desplegable_posicion.set("Posicion")

        desplegable_club = ctk.CTkComboBox(
            frame_formulario, values=self.controller.get_carta_club(), state="readonly"
        )
        desplegable_club.set("Club")

        def guardar_carta():
            nombre = entry_nombre.get()
            nacionalidad = desplegable_nacionalidad.get()
            club = desplegable_club.get()
            promedio = entry_promedio.get()
            posicion = self.get_posicion(desplegable_posicion.get())
            dorsal = entry_dorsal.get()
            velocidad = entry_velocidad.get()
            tiro = entry_tiro.get()
            pase = entry_pase.get()
            gambeta = entry_gambeta.get()
            defensa = entry_defensa.get()
            fisico = entry_fisico.get()
            self.controller.add_carta_jugador(
                nombre,
                nacionalidad,
                club,
                promedio,
                posicion,
                dorsal,
                velocidad,
                tiro,
                pase,
                gambeta,
                defensa,
                fisico,
            )
            formulario_carta.destroy()
            self.load_cartas()

        btn_guardar = ctk.CTkButton(
            frame_formulario, text="Guardar", command=guardar_carta
        )

        # Ubicacion de los widgets usando grid
        entry_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_promedio.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        desplegable_club.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        desplegable_posicion.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        entry_dorsal.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        entry_tiro.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        entry_pase.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        entry_gambeta.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        entry_defensa.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        entry_fisico.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        desplegable_nacionalidad.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        entry_velocidad.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        btn_guardar.grid(row=6, column=0, columnspan=2, pady=10)

    def get_posicion(self, seleccionado):
        match = re.search(r"\((.*?)\)", seleccionado)
        if match:
            posicion = match.group(1)
            return posicion

    def formulario_agregar_arquero(self):
        # Crear una nueva ventana para el formulario de agregar arquero
        formulario_arquero = ctk.CTkToplevel(self)
        # Poner la ventana en frente
        formulario_arquero.attributes("-topmost", True)
        formulario_arquero.title("Agregar Arquero")
        # formulario_arquero.geometry("300x300")
        formulario_arquero.resizable(False, False)
        centrar_ventana(formulario_arquero, 350, 250)

        frame_formulario = ctk.CTkFrame(formulario_arquero)
        frame_formulario.pack(fill="both", expand=True, padx=10, pady=10)

        # Campos del formulario
        entry_nombre = ctk.CTkEntry(frame_formulario, placeholder_text="Nombre")
        entry_nacionalidad = ctk.CTkComboBox(
            frame_formulario,
            values=self.controller.get_carta_nacionalidad(),
            state="readonly",
        )
        entry_nacionalidad.set("Nacionalidad")
        entry_club = ctk.CTkComboBox(
            frame_formulario, values=self.controller.get_carta_club(), state="readonly"
        )
        entry_club.set("Club")
        entry_promedio = ctk.CTkEntry(frame_formulario, placeholder_text="Promedio")
        entry_dorsal = ctk.CTkEntry(frame_formulario, placeholder_text="Dorsal")
        entry_salto = ctk.CTkEntry(frame_formulario, placeholder_text="Salto")
        entry_control = ctk.CTkEntry(frame_formulario, placeholder_text="Control")
        entry_despeje = ctk.CTkEntry(frame_formulario, placeholder_text="Despeje")
        entry_reflejos = ctk.CTkEntry(frame_formulario, placeholder_text="Reflejos")
        entry_velocidad = ctk.CTkEntry(frame_formulario, placeholder_text="Velocidad")
        entry_posicionamiento = ctk.CTkEntry(
            frame_formulario, placeholder_text="Posicionamiento"
        )

        def guardar_arquero():
            nombre = entry_nombre.get()
            nacionalidad = entry_nacionalidad.get()
            club = entry_club.get()
            promedio = entry_promedio.get()
            dorsal = entry_dorsal.get()
            salto = entry_salto.get()
            control = entry_control.get()
            despeje = entry_despeje.get()
            reflejos = entry_reflejos.get()
            velocidad = entry_velocidad.get()
            posicionamiento = entry_posicionamiento.get()
            self.controller.add_carta_arquero(
                nombre,
                nacionalidad,
                club,
                promedio,
                dorsal,
                salto,
                control,
                despeje,
                reflejos,
                velocidad,
                posicionamiento,
            )
            formulario_arquero.destroy()
            self.load_cartas()

        btn_guardar = ctk.CTkButton(
            frame_formulario, text="Guardar", command=guardar_arquero
        )

        # Ubicacion de los widgets usando grid
        entry_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_nacionalidad.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        entry_club.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        entry_promedio.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_dorsal.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        entry_salto.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        entry_control.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        entry_despeje.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        entry_reflejos.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        entry_velocidad.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        entry_posicionamiento.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        btn_guardar.grid(row=5, column=1, columnspan=2, pady=10)

    def modificar_carta(self):
        seleccion = self.tree_cartas.selection()
        carta_seleccionada = self.tree_cartas.item(seleccion)["values"]

        if not seleccion:
            messagebox.showerror("Error", "Seleccione una carta para modificar")
            return

        # Obtener los datos de la carta seleccionada
        id_carta = carta_seleccionada[0]
        nombre = carta_seleccionada[1]
        nacionalidad = carta_seleccionada[2]
        club = carta_seleccionada[3]
        promedio = carta_seleccionada[4]
        posicion = carta_seleccionada[5]
        dorsal = carta_seleccionada[6]
        velocidad = carta_seleccionada[7]
        tiro = carta_seleccionada[8]
        pase = carta_seleccionada[9]
        gambeta = carta_seleccionada[10]
        defensa = carta_seleccionada[11]
        fisico = carta_seleccionada[12]
        salto = carta_seleccionada[13]
        control = carta_seleccionada[14]
        despeje = carta_seleccionada[15]
        reflejos = carta_seleccionada[16]
        velocidad_gk = carta_seleccionada[17]
        posicionamiento = carta_seleccionada[18]

        if carta_seleccionada[5] == "GK":
            self.formulario_modificar_arquero(
                id_carta,
                nombre,
                nacionalidad,
                club,
                promedio,
                dorsal,
                salto,
                control,
                despeje,
                reflejos,
                velocidad_gk,
                posicionamiento,
            )
        else:
            self.formulario_modificar_carta(
                id_carta,
                nombre,
                nacionalidad,
                club,
                promedio,
                posicion,
                dorsal,
                velocidad,
                tiro,
                pase,
                gambeta,
                defensa,
                fisico,
            )

    def formulario_modificar_carta(
        self,
        id_carta,
        nombre,
        nacionalidad,
        club,
        promedio,
        posicion,
        dorsal,
        velocidad,
        tiro,
        pase,
        gambeta,
        defensa,
        fisico,
    ):
        # Crear una nueva ventana para el formulario de modificar carta
        formulario_carta = ctk.CTkToplevel(self)
        # Poner la ventana en frente
        formulario_carta.attributes("-topmost", True)
        formulario_carta.title("Modificar Carta")
        # formulario_carta.geometry("300x300")
        formulario_carta.resizable(False, False)
        centrar_ventana(formulario_carta, 350, 300)

        frame_formulario = ctk.CTkFrame(formulario_carta)
        frame_formulario.pack(fill="both", expand=True, padx=10, pady=10)

        # Campos del formulario
        entry_nombre = ctk.CTkEntry(frame_formulario, placeholder_text="Nombre")
        entry_nombre.insert(0, nombre)
        entry_nacionalidad = ctk.CTkComboBox(
            frame_formulario,
            values=self.controller.get_carta_nacionalidad(),
            state="readonly",
        )
        entry_nacionalidad.set(nacionalidad)
        entry_club = ctk.CTkComboBox(
            frame_formulario, values=self.controller.get_carta_club(), state="readonly"
        )
        entry_club.set(club)
        entry_promedio = ctk.CTkEntry(frame_formulario, placeholder_text="Promedio")
        entry_promedio.insert(0, promedio)
        entry_posicion = ctk.CTkComboBox(
            frame_formulario,
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
        )
        entry_posicion.set(posicion)
        entry_dorsal = ctk.CTkEntry(frame_formulario, placeholder_text="Dorsal")
        entry_dorsal.insert(0, dorsal)
        entry_velocidad = ctk.CTkEntry(frame_formulario, placeholder_text="Velocidad")
        entry_velocidad.insert(0, velocidad)
        entry_tiro = ctk.CTkEntry(frame_formulario, placeholder_text="Tiro")
        entry_tiro.insert(0, tiro)
        entry_pase = ctk.CTkEntry(frame_formulario, placeholder_text="Pase")
        entry_pase.insert(0, pase)
        entry_gambeta = ctk.CTkEntry(frame_formulario, placeholder_text="Gambeta")
        entry_gambeta.insert(0, gambeta)
        entry_defensa = ctk.CTkEntry(frame_formulario, placeholder_text="Defensa")
        entry_defensa.insert(0, defensa)
        entry_fisico = ctk.CTkEntry(frame_formulario, placeholder_text="Fisico")
        entry_fisico.insert(0, fisico)

        # Ubicacion de los widgets usando grid
        entry_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_dorsal.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_club.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        entry_velocidad.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        entry_tiro.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        entry_pase.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        entry_nacionalidad.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        entry_promedio.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        entry_posicion.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        entry_gambeta.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        entry_defensa.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        entry_fisico.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        # Llenar los campos con los datos de la carta seleccionada
        def __modificar_carta(id_carta=id_carta):
            nombre = entry_nombre.get()
            nacionalidad = entry_nacionalidad.get()
            club = entry_club.get()
            promedio = entry_promedio.get()
            posicion = self.get_posicion(entry_posicion.get())
            dorsal = entry_dorsal.get()
            velocidad = entry_velocidad.get()
            tiro = entry_tiro.get()
            pase = entry_pase.get()
            gambeta = entry_gambeta.get()
            defensa = entry_defensa.get()
            fisico = entry_fisico.get()
            self.controller.update_carta_jugador(
                id_carta,
                nombre,
                nacionalidad,
                club,
                promedio,
                posicion,
                dorsal,
                velocidad,
                tiro,
                pase,
                gambeta,
                defensa,
                fisico,
            )
            formulario_carta.destroy()
            self.load_cartas()

        # Funcionalidad de los botones
        btn_guardar = ctk.CTkButton(
            frame_formulario, text="Guardar", command=__modificar_carta, width=200
        )

        btn_guardar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def formulario_modificar_arquero(
        self,
        id_carta,
        nombre,
        nacionalidad,
        club,
        promedio,
        dorsal,
        velocidad,
        salto,
        control,
        despeje,
        reflejos,
        posicionamiento,
    ):
        # Crear una nueva ventana para el formulario de modificar arquero
        formulario_arquero = ctk.CTkToplevel(self)
        # Poner la ventana en frente
        formulario_arquero.attributes("-topmost", True)
        formulario_arquero.title("Modificar Arquero")
        # formulario_arquero.geometry("300x300")
        formulario_arquero.resizable(False, False)
        centrar_ventana(formulario_arquero, 350, 300)

        frame_formulario = ctk.CTkFrame(formulario_arquero)
        frame_formulario.pack(fill="both", expand=True, padx=10, pady=10)

        # Campos del formulario
        entry_nombre = ctk.CTkEntry(frame_formulario, placeholder_text="Nombre")
        entry_nombre.insert(0, nombre)
        entry_nacionalidad = ctk.CTkComboBox(
            frame_formulario,
            values=self.controller.get_carta_nacionalidad(),
            state="readonly",
        )
        entry_nacionalidad.set(nacionalidad)
        entry_club = ctk.CTkComboBox(
            frame_formulario,
            values=self.controller.get_carta_club(),
            state="readonly",
        )
        entry_club.set(club)
        entry_promedio = ctk.CTkEntry(frame_formulario, placeholder_text="Promedio")
        entry_promedio.insert(0, promedio)
        entry_dorsal = ctk.CTkEntry(frame_formulario, placeholder_text="Dorsal")
        entry_dorsal.insert(0, dorsal)
        entry_salto = ctk.CTkEntry(frame_formulario, placeholder_text="Salto")
        entry_salto.insert(0, salto)
        entry_control = ctk.CTkEntry(frame_formulario, placeholder_text="Control")
        entry_control.insert(0, control)
        entry_despeje = ctk.CTkEntry(frame_formulario, placeholder_text="Despeje")
        entry_despeje.insert(0, despeje)
        entry_reflejos = ctk.CTkEntry(frame_formulario, placeholder_text="Reflejos")
        entry_reflejos.insert(0, reflejos)
        entry_velocidad = ctk.CTkEntry(frame_formulario, placeholder_text="Velocidad")
        entry_velocidad.insert(0, velocidad)
        entry_posicionamiento = ctk.CTkEntry(
            frame_formulario, placeholder_text="Posicionamiento"
        )
        entry_posicionamiento.insert(0, posicionamiento)

        entry_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        entry_nacionalidad.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        entry_club.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        entry_promedio.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        entry_dorsal.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        entry_salto.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        entry_control.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        entry_despeje.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        entry_reflejos.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        entry_velocidad.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        entry_posicionamiento.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        def __modificar_arquero(id_carta=id_carta):
            nombre = entry_nombre.get()
            nacionalidad = entry_nacionalidad.get()
            club = entry_club.get()
            promedio = entry_promedio.get()
            dorsal = entry_dorsal.get()
            velocidad = entry_velocidad.get()
            salto = entry_salto.get()
            control = entry_control.get()
            despeje = entry_despeje.get()
            reflejos = entry_reflejos.get()
            posicionamiento = entry_posicionamiento.get()
            self.controller.update_carta_arquero(
                id_carta,
                nombre,
                nacionalidad,
                club,
                promedio,
                dorsal,
                velocidad,
                salto,
                control,
                despeje,
                reflejos,
                posicionamiento,
            )
            formulario_arquero.destroy()
            self.load_cartas()

        # Funcionalidad de los botones
        btn_guardar = ctk.CTkButton(
            frame_formulario, text="Guardar", command=__modificar_arquero
        )

        btn_guardar.grid(row=5, column=1, pady=10)
