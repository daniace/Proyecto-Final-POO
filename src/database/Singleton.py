import sqlite3


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.connection = sqlite3.connect("heroesdelbalon.db")
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def query(self, query, params=()):
        return self.cursor.execute(query, params)

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchmany(self, size):
        return self.cursor.fetchmany(size)

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Ejemplo de uso
# with Database() as db:
#     db.query('SELECT * FROM users')
#     users = db.fetchall()
#     print(users)
#     db.query('INSERT INTO users VALUES (?, ?)', (1, 'John'))
#     db.commit()
#     db.query('SELECT * FROM users')
#     users = db.fetchall()
#     print(users)
#     db.query('DELETE FROM users')
#     db.commit()
#     db.query('SELECT * FROM users')
#     users = db.fetchall()
#     print(users)

# Salida
# [(1, 'John')]
# []

# Explicación
# En este ejemplo, creamos una instancia de la clase Database y la usamos para ejecutar algunas consultas SQL.
# Primero, seleccionamos todos los usuarios de la tabla de usuarios y los imprimimos.
# Luego, insertamos un nuevo usuario en la tabla y confirmamos los cambios con el método commit().
# Después de eso, seleccionamos todos los usuarios de nuevo y los imprimimos.
# Finalmente, eliminamos todos los usuarios de la tabla y confirmamos los cambios con el método commit().
# Al seleccionar todos los usuarios por última vez, vemos que la tabla de usuarios está vacía.

# Referencia

# https://realpython.com/python-singleton/
# https://es.wikipedia.org/wiki/Singleton
# https://refactoring.guru/es/design-patterns/singleton/python/example
# https://www.geeksforgeeks.org/singleton-method-python-design-patterns/
# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
# https://www.programiz.com/python-programming/methods/built-in/super
# https://docs.python.org/3/library/sqlite3.html
