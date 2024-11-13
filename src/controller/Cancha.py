class Cancha:
    def __init__(self) -> None:
        self._cancha=[[0,0,0,0,0,0,0],#arquero jugador#
                      [0,0,0,0,0,0,0],#defensa jugador#
                      [0,0,0,0,0,0,0],#delantero cpu#
                      [0,0,0,0,0,0,0],#mediocampo jugardor#
                      [0,0,0,0,0,0,0],#mediocampo cpu
                      [0,0,0,0,0,0,0],#delatero jugador#
                      [0,0,0,0,0,0,0],#defensa cpu
                      [0,0,0,0,0,0,0]]#arquero cpu

    def mostrar_cancha(self):
        for i in self._cancha:
            print(i)

    def agregar_plantilla_uno(self,formacion):
        self._cancha[0]=formacion[0]
        self._cancha[1]=formacion[1]
        self._cancha[3]=formacion[2]
        self._cancha[5]=formacion[3]
    def agregar_plantilla_dos(self,formacion):
        self._cancha[2]=formacion[0]
        self._cancha[4]=formacion[1]
        self._cancha[6]=formacion[2]
        self._cancha[7]=formacion[3]


# matr=Cancha()
# matr.mostrar_cancha()
# plantilla=[[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]
# plantilla2=[[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2]]
# matr.agregar_plantilla_uno(plantilla)
# matr.agregar_plantilla_dos(plantilla2)
# print()
# matr.mostrar_cancha()