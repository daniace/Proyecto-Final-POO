import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Añadir nuevas columnas a la tabla usuarios
cursor.execute("ALTER TABLE usuarios ADD COLUMN email TEXT")
cursor.execute("ALTER TABLE usuarios ADD COLUMN telefono TEXT")

# Cerrar la conexión
conn.close()
