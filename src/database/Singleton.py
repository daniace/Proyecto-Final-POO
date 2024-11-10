import sqlite3
from sqlite3 import Error


class Database:
    """Clase Singleton para la base de datos.
    Se encarga de establecer la conexión, ejecutar consultas y operaciones,
    y cerrar la conexión a la base de datos."""

    _instance = None

    def __new__(cls, db_path="src\database\heroesdelbalon.db"):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = None
            cls._instance.db_path = db_path
        return cls._instance

    def connect(self):
        """Establece la conexión a la base de datos."""
        if self.connection is None:
            try:
                self.connection = sqlite3.connect(self.db_path)
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
            #for row in results:
                #return row
                #print(row)
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
