from model.database.DaoInterfaz import DaoInterfaz
from model.database.Equipo import Equipo
from model.database.Singleton import Database


class AbmEquipo(DaoInterfaz):
    def __init__(self):
        self.__database = Database()
        self.__database.connect

    def get_por_id(self, id):  # FUNCIONA
        resultado = self.__database.execute_query(
            "SELECT * FROM equipo WHERE id_equipo = ? AND baja_equipo = 0", (id)
        )
        if not resultado:
            print(f"No se encontró el equipo con el id: {id}")
        else:
            return Equipo(
                resultado[0][0],
                resultado[0][1],
                resultado[0][2],
                resultado[0][3],
                resultado[0][4],
                resultado[0][5],
                resultado[0][6],
                resultado[0][7],
                resultado[0][8],
                resultado[0][9],
                resultado[0][10],
                resultado[0][11],
                resultado[0][12],
                resultado[0][13],
            )  # Retorna el objeto equipo

    def get_all(self):  # FUNCIONA
        equipos = []
        resultado = self.__database.execute_query(
            "SELECT * FROM equipo WHERE baja_equipo = 0"  # esta query devuelve en resultado una lista de los equipos
        )
        if resultado is None:
            print("No se encontraron equipos")
        else:
            for equipo in resultado:
                objeto = Equipo(
                    equipo[0],
                    equipo[1],
                    equipo[2],
                    equipo[3],
                    equipo[4],
                    equipo[5],
                    equipo[6],
                    equipo[7],
                    equipo[8],
                    equipo[9],
                    equipo[10],
                    equipo[11],
                    equipo[12],
                    equipo[13],
                )  # creo un objeto Equipo para cada índice de la lista
                equipos.append(objeto)
            return equipos

    def insertar(self, objeto):  # FUNCIONA
        self.__database.execute_non_query(
            "INSERT INTO equipo (id_equipo, id_usuario, nombre_equipo,baja_equipo, id_carta1, id_carta2, id_carta3, id_carta4, id_carta5, id_carta6, id_carta7, id_carta8, id_carta9, id_carta10, id_carta11) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                objeto.get_id_equipo(),
                objeto.get_nombre(),
                objeto.get_id_usuario(),
                objeto.get_baja_equipo(),
                objeto.get_id_carta1(),
                objeto.get_id_carta2(),
                objeto.get_id_carta3(),
                objeto.get_id_carta4(),
                objeto.get_id_carta5(),
                objeto.get_id_carta6(),
                objeto.get_id_carta7(),
                objeto.get_id_carta8(),
                objeto.get_id_carta9(),
                objeto.get_id_carta10(),
                objeto.get_id_carta11(),
            ),
        )

    def actualizar(self, objeto):  # FUNCIONA
        self.__database.execute_non_query(
            "UPDATE equipo SET nombre_equipo = ?, baja_equipo = ?, id_carta1 = ?, id_carta2 = ?, id_carta3 = ?, id_carta4 = ?, id_carta5 = ?, id_carta6 = ?, id_carta7 = ?, id_carta8 = ?, id_carta9 = ?, id_carta10 = ?, id_carta11 = ? WHERE id_equipo = ?",
            (
                objeto.get_nombre(),
                objeto.get_baja_equipo(),
                objeto.get_id_equipo(),
                objeto.get_id_carta1(),
                objeto.get_id_carta2(),
                objeto.get_id_carta3(),
                objeto.get_id_carta4(),
                objeto.get_id_carta5(),
                objeto.get_id_carta6(),
                objeto.get_id_carta7(),
                objeto.get_id_carta8(),
                objeto.get_id_carta9(),
                objeto.get_id_carta10(),
                objeto.get_id_carta11(),
            ),
        )

    def borrar(self, id):  # FUNCIONA
        self.__database.execute_non_query(
            "UPDATE equipo SET baja_equipo = 1 WHERE id_equipo = ? AND baja_equipo = 0",
            (id),
        )

    def close(self):
        self.__database.close_connection()
