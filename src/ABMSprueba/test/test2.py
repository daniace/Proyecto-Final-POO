import PySimpleGUI as sg


# --- Funciones del CRUD (solo las necesarias para la vista) ---
def obtener_objetos():
    # Aquí iría la lógica para obtener los datos.
    # En el ejemplo anterior, usaba SQLite, pero puedes adaptarlo a tu método.
    # Este ejemplo devuelve datos de prueba:
    return [[1, "Espada", 100], [2, "Escudo", 50], [3, "Pocion", 25]]


# --- Interfaz con PySimpleGUI ---
def abrir_ventana_crud():
    layout = [
        [sg.Text("Nombre:"), sg.Input(key="nombre")],
        [sg.Text("Valor:"), sg.Input(key="valor")],
        [sg.Button("Agregar"), sg.Button("Cancelar")],
        [
            sg.Table(
                values=obtener_objetos(),
                headings=["ID", "Nombre", "Valor"],
                key="tabla_objetos",
                autosize_mode="fit",
            )
        ],
    ]

    window = sg.Window("CRUD", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            break
        if event == "Agregar":
            nombre = values["nombre"]
            valor = values["valor"]
            # Aquí iría la lógica para agregar el objeto a la base de datos
            print(f"Agregar objeto: Nombre={nombre}, Valor={valor}")  # Placeholder
            # Luego de agregar, actualiza la tabla:
            window["tabla_objetos"].update(values=obtener_objetos())
            window["nombre"].update("")  # Limpiar campos de entrada
            window["valor"].update("")

    window.close()


# --- Para probar la vista ---
abrir_ventana_crud()  # Llama a la función para que se muestre
