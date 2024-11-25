import sqlite3
import tkinter as tk
from tkinter import messagebox


class ABMUsuarios:
    def __init__(self, root):
        self.root = root
        self.root.title("ABM de Usuarios")

        # Configuración de la base de datos
        self.conn = sqlite3.connect("usuarios.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios
                            (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT, telefono TEXT)""")
        self.conn.commit()

        # Elementos de la interfaz
        self.id_label = tk.Label(root, text="ID Usuario (para eliminar/modificar):")
        self.id_label.grid(row=0, column=0, padx=10, pady=5)
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        self.nombre_label = tk.Label(root, text="Nombre Usuario:")
        self.nombre_label.grid(row=1, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.telefono_label = tk.Label(root, text="Teléfono:")
        self.telefono_label.grid(row=3, column=0, padx=10, pady=5)
        self.telefono_entry = tk.Entry(root)
        self.telefono_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Agregar", command=self.agregar_usuario)
        self.add_button.grid(row=4, column=0, padx=10, pady=5)
        self.update_button = tk.Button(
            root, text="Modificar", command=self.modificar_usuario
        )
        self.update_button.grid(row=4, column=1, padx=10, pady=5)
        self.delete_button = tk.Button(
            root, text="Eliminar", command=self.eliminar_usuario
        )
        self.delete_button.grid(row=4, column=2, padx=10, pady=5)
        self.load_button = tk.Button(
            root, text="Actualizar", command=self.cargar_usuarios
        )
        self.load_button.grid(row=4, column=3, padx=10, pady=5)

        self.usuarios_list = tk.Listbox(root, height=10, width=80)
        self.usuarios_list.grid(row=5, column=0, columnspan=4, padx=10, pady=5)
        self.usuarios_list.bind("<<ListboxSelect>>", self.on_usuario_select)

        # Cargar los usuarios al iniciar la aplicación
        self.cargar_usuarios()

    def agregar_usuario(self):
        nombre = self.nombre_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()

        if nombre and email and telefono:
            self.cursor.execute(
                "INSERT INTO usuarios (nombre, email, telefono) VALUES (?, ?, ?)",
                (nombre, email, telefono),
            )
            self.conn.commit()
            self.cargar_usuarios()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def eliminar_usuario(self):
        id_usuario = self.id_entry.get()
        if id_usuario:
            self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
            self.conn.commit()
            self.cargar_usuarios()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "ID es obligatorio para eliminar")

    def modificar_usuario(self):
        id_usuario = self.id_entry.get()
        nombre = self.nombre_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()

        if id_usuario and (nombre or email or telefono):
            if nombre:
                self.cursor.execute(
                    "UPDATE usuarios SET nombre = ? WHERE id = ?", (nombre, id_usuario)
                )
            if email:
                self.cursor.execute(
                    "UPDATE usuarios SET email = ? WHERE id = ?", (email, id_usuario)
                )
            if telefono:
                self.cursor.execute(
                    "UPDATE usuarios SET telefono = ? WHERE id = ?",
                    (telefono, id_usuario),
                )
            self.conn.commit()
            self.cargar_usuarios()
            self.limpiar_campos()
        else:
            messagebox.showwarning(
                "Advertencia",
                "ID es obligatorio y al menos un campo debe ser llenado para modificar",
            )

    def cargar_usuarios(self):
        self.usuarios_list.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM usuarios")
        for row in self.cursor.fetchall():
            self.usuarios_list.insert(tk.END, row)

    def on_usuario_select(self, event):
        try:
            index = self.usuarios_list.curselection()[0]
            selected_user = self.usuarios_list.get(index)

            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(tk.END, selected_user[0])
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(tk.END, selected_user[1])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, selected_user[2])
            self.telefono_entry.delete(0, tk.END)
            self.telefono_entry.insert(tk.END, selected_user[3])
        except IndexError:
            pass

    def limpiar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ABMUsuarios(root)
    root.mainloop()
