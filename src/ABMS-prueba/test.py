import tkinter as tk
from tkinter import ttk


def mostrar_usuarios():
    limpiar_frame_principal()
    # widgets para usuarios
    etiqueta_nombre.pack()
    entry_nombre.pack()
    etiqueta_password.pack()
    entry_password.pack()
    etiqueta_email.pack()
    entry_email.pack()

    boton_agregar.config(command=agregar_usuario)
    boton_modificar.config(command=modificar_usuario)
    boton_eliminar.config(command=eliminar_usuario)

    boton_agregar.pack()
    boton_modificar.pack()
    boton_eliminar.pack()

    actualizar_lista_usuarios()
    listbox_usuarios.pack()


def mostrar_equipos():
    limpiar_frame_principal()
    # ... (Widgets y lógica para la pestaña "equipo")
    label = tk.Label(frame_principal, text="Contenido de Equipos")
    label.pack()


def mostrar_cartas():
    limpiar_frame_principal()
    # ... (Widgets y lógica para la pestaña "carta")
    label = tk.Label(frame_principal, text="Contenido de Cartas")
    label.pack()


def limpiar_frame_principal():
    for widget in frame_principal.winfo_children():
        widget.pack_forget()


def agregar_usuario():
    nombre = entry_nombre.get()
    password = entry_password.get()
    email = entry_email.get()
    usuarios.append((nombre, password, email))  # lista para almacenar los datos.
    actualizar_lista_usuarios()


def modificar_usuario():
    # ... (Lógica para modificar usuario) ...
    pass


def eliminar_usuario():
    # ... (Lógica para eliminar usuario) ...
    pass


def actualizar_lista_usuarios():
    listbox_usuarios.delete(0, tk.END)
    for i, (nombre, password, email) in enumerate(usuarios, 1):
        listbox_usuarios.insert(tk.END, f"{i} - {nombre} - {password} - {email}")


# --- Configuración principal de la ventana ---

root = tk.Tk()
root.title("ABM")

# --- Pestañas ---
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

frame_usuarios = tk.Frame(notebook)
frame_equipos = tk.Frame(notebook)
frame_cartas = tk.Frame(notebook)

notebook.add(frame_usuarios, text="usuarios")
notebook.add(frame_equipos, text="equipo")
notebook.add(frame_cartas, text="carta")


# --- Frame principal donde se mostrará el contenido de cada pestaña ---

frame_principal = tk.Frame(frame_usuarios)  # Inicialmente mostramos usuarios
frame_principal.pack(fill="both", expand=True)


# --- Widgets para la pestaña de usuarios ---

etiqueta_nombre = tk.Label(frame_principal, text="nombre_usuario")
entry_nombre = tk.Entry(frame_principal)

etiqueta_password = tk.Label(frame_principal, text="password")
entry_password = tk.Entry(frame_principal, show="*")  # Ocultar contraseña

etiqueta_email = tk.Label(frame_principal, text="email")
entry_email = tk.Entry(frame_principal)

boton_agregar = tk.Button(frame_principal, text="agregar")
boton_modificar = tk.Button(frame_principal, text="modificar")
boton_eliminar = tk.Button(frame_principal, text="eliminar")


listbox_usuarios = tk.Listbox(frame_principal, width=50)


usuarios = []  # Lista para almacenar datos de usuarios

mostrar_usuarios()


# --- Eventos para cambiar el contenido según la pestaña seleccionada ---

notebook.bind(
    "<<NotebookTabChanged>>",
    lambda event: {0: mostrar_usuarios, 1: mostrar_equipos, 2: mostrar_cartas}[
        notebook.index(notebook.select())
    ](),
)


root.mainloop()
