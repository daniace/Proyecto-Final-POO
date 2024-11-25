import sqlite3
from sqlite3 import Error
from threading import Lock


class SingletonMeta(type):
    _instancias = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instancias:
                instancia = super().__call__(*args, **kwargs)
                cls._instancias[cls] = instancia
        return cls._instancias[cls]


class Database(metaclass=SingletonMeta):
    """Clase Singleton para la base de datos.
    Se encarga de establecer la conexión, ejecutar consultas y operaciones,
    y cerrar la conexión a la base de datos."""

    def __init__(self):
        super().__init__()
        self.connection = None

    def connect(self):
        """Establece la conexión a la base de datos."""
        if self.connection is None:
            try:
                self.connection = sqlite3.connect(
                    r"src\model\database\heroesdelbalon.db"
                )
                print("Conexión a la base de datos establecida.")
            except Error as e:
                print(f"Error al conectar a la base de datos: {e}")
        return self.connection

    def close_connection(self):
        """Cierra la conexión a la base de datos."""
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Conexión a la base de datos cerrada.")

    def execute_query(self, query, parameters=None):
        """Ejecuta una consulta a la base de datos.
        Por ejemplo: SELECT."""
        if self.connection is None:
            print("Conexión no establecida. Llama a 'connect' primero.")
            return None

        cursor = self.connection.cursor()
        try:
            if parameters:
                # Asegura que los parámetros se pasen como una tupla, incluso si es un solo valor
                cursor.execute(
                    query,
                    parameters
                    if isinstance(parameters, (tuple, list))
                    else (parameters,),
                )
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def execute_non_query(self, query, parameters=None):
        """Ejecuta una operación que no devuelve resultados.
        Por ejemplo: INSERT, UPDATE, DELETE."""
        if self.connection is None:
            print("Conexión no establecida. Llama a 'connect' primero.")
            return

        cursor = self.connection.cursor()
        try:
            if parameters:
                cursor.execute(
                    query,
                    parameters
                    if isinstance(parameters, (tuple, list))
                    else (parameters,),
                )
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Operación ejecutada exitosamente.")
        except Error as e:
            print(f"Error al ejecutar la operación: {e}")


if __name__ == "__main__":
    pass
