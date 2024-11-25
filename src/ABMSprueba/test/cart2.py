import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


class ABMCarta:
    def __init__(self, root):
        self.root = root
        self.root.title("ABM de Carta")
        self.root.geometry("600x640")  # Ajustar la resolución de la ventana

        # Configuración de la base de datos
        self.conn = sqlite3.connect("usuarios.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS carta
                            (id_carta INTEGER PRIMARY KEY, short_name TEXT, nacionality TEXT,
                            attribute1 TEXT, attribute2 TEXT, attribute3 TEXT, attribute4 TEXT,
                            attribute5 TEXT, attribute6 TEXT, attribute7 TEXT, attribute8 TEXT,
                            attribute9 TEXT, attribute10 TEXT, attribute11 TEXT, attribute12 TEXT,
                            attribute13 TEXT, attribute14 TEXT, attribute15 TEXT, attribute16 TEXT,
                            attribute17 TEXT, attribute18 TEXT, attribute19 TEXT)""")
        self.conn.commit()

        # Elementos de la interfaz
        self.scrollable_frame = ScrollableFrame(root)
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Definición de los campos de entrada
        self.fields = [
            ("ID Carta", "id_carta"),
            ("Nombre Corto", "short_name"),
            ("Nacionalidad", "nacionality"),
            ("Atributo 1", "attribute1"),
            ("Atributo 2", "attribute2"),
            ("Atributo 3", "attribute3"),
            ("Atributo 4", "attribute4"),
            ("Atributo 5", "attribute5"),
            ("Atributo 6", "attribute6"),
            ("Atributo 7", "attribute7"),
            ("Atributo 8", "attribute8"),
            ("Atributo 9", "attribute9"),
            ("Atributo 10", "attribute10"),
            ("Atributo 11", "attribute11"),
            ("Atributo 12", "attribute12"),
            ("Atributo 13", "attribute13"),
            ("Atributo 14", "attribute14"),
            ("Atributo 15", "attribute15"),
            ("Atributo 16", "attribute16"),
            ("Atributo 17", "attribute17"),
            ("Atributo 18", "attribute18"),
            ("Atributo 19", "attribute19"),
        ]

        self.entries = {}
        for i, (label_text, field_name) in enumerate(self.fields):
            row, col = divmod(i, 2)  # Dividir los campos en dos columnas
            label = tk.Label(
                self.scrollable_frame.scrollable_frame, text=label_text + ":"
            )
            label.grid(row=row, column=col * 2, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.scrollable_frame.scrollable_frame)
            entry.grid(row=row, column=col * 2 + 1, padx=10, pady=5, sticky="w")
            self.entries[field_name] = entry

        # Botones de acción
        self.add_button = tk.Button(
            self.scrollable_frame.scrollable_frame,
            text="Agregar",
            command=self.agregar_carta,
        )
        self.add_button.grid(row=20, column=0, padx=10, pady=5)
        self.update_button = tk.Button(
            self.scrollable_frame.scrollable_frame,
            text="Modificar",
            command=self.modificar_carta,
        )
        self.update_button.grid(row=20, column=1, padx=10, pady=5)
        self.delete_button = tk.Button(
            self.scrollable_frame.scrollable_frame,
            text="Eliminar",
            command=self.eliminar_carta,
        )
        self.delete_button.grid(row=20, column=2, padx=10, pady=5)
        self.load_button = tk.Button(
            self.scrollable_frame.scrollable_frame,
            text="Actualizar",
            command=self.cargar_cartas,
        )
        self.load_button.grid(row=20, column=3, padx=10, pady=5)

        self.cartas_list = tk.Listbox(
            self.scrollable_frame.scrollable_frame, height=10, width=80
        )
        self.cartas_list.grid(row=21, column=0, columnspan=4, padx=10, pady=5)
        self.cartas_list.bind("<<ListboxSelect>>", self.on_carta_select)

        # Cargar las cartas al iniciar la aplicación
        self.cargar_cartas()

    def agregar_carta(self):
        values = {field: self.entries[field].get() for field in self.entries}

        if all(values.values()):
            self.cursor.execute(
                "INSERT INTO carta (id_carta, short_name, nacionality, attribute1, attribute2, attribute3, attribute4, attribute5, attribute6, attribute7, attribute8, attribute9, attribute10, attribute11, attribute12, attribute13, attribute14, attribute15, attribute16, attribute17, attribute18, attribute19) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                tuple(values.values()),
            )
            self.conn.commit()
            self.cargar_cartas()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def eliminar_carta(self):
        id_carta = self.entries["id_carta"].get()
        if id_carta:
            self.cursor.execute("DELETE FROM carta WHERE id_carta = ?", (id_carta,))
            self.conn.commit()
            self.cargar_cartas()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "ID es obligatorio para eliminar")

    def modificar_carta(self):
        values = {field: self.entries[field].get() for field in self.entries}

        if values["id_carta"] and any(values.values()):
            for field, value in values.items():
                if value:
                    self.cursor.execute(
                        f"UPDATE carta SET {field} = ? WHERE id_carta = ?",
                        (value, values["id_carta"]),
                    )
            self.conn.commit()
            self.cargar_cartas()
            self.limpiar_campos()
        else:
            messagebox.showwarning(
                "Advertencia",
                "ID es obligatorio y al menos un campo debe ser llenado para modificar",
            )

    def cargar_cartas(self):
        self.cartas_list.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM carta")
        for row in self.cursor.fetchall():
            self.cartas_list.insert(tk.END, row)

    def on_carta_select(self, event):
        try:
            index = self.cartas_list.curselection()[0]
            selected_carta = self.cartas_list.get(index)

            for i, field in enumerate(self.entries):
                self.entries[field].delete(0, tk.END)
                self.entries[field].insert(tk.END, selected_carta[i])
        except IndexError:
            pass

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("540x640")  # Ajustar la resolución de la ventana
    app = ABMCarta(root)
    root.mainloop()
