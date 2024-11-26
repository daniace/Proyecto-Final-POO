from tkinter import ttk


# Estilo de la tabla
def configurar_estilo_tabla(ventana):
    style = ttk.Style(ventana)

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


def centrar_ventana(ventana, ancho_ventana, alto_ventana):
    """Centra la ventana en la pantalla."""

    # Obtener el tamaño de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    # Calcular la posición centrada
    pos_x = int((ancho_pantalla - ancho_ventana) / 2)
    pos_y = int((alto_pantalla - alto_ventana) / 2)
    # Establecer la geometría de la ventana
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
