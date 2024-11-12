class Mapa:
    def __init__(self):
        self.posiciones = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def setterar_formacion(self, formacion):
        for jugador in formacion:
            x, y = jugador.posicion
            self.posiciones[x][y] = jugador


"LA MAQUINA TIENE UNA FORMACION FIJA, PERO LA DEL JUGADOR SE PUEDE CAMBIAR"
