from AbmCarta import AbmCarta
from Carta import Carta


class PruebaCarta:
    def __init__(self):
        self.__abmC = AbmCarta()
        self.__cartas = []

    def test(self):
        defensores = self.__abmC.get_defensores()
        mediocampistas = self.__abmC.get_mediocampistas()
        delanteros = self.__abmC.get_delanteros()
        porteros = self.__abmC.get_porteros()

        print("--- Cartas ---")

        print("--- Defensores ---")
        for defensor in defensores:
            print(defensor)

        print("--- Mediocampistas ---")
        for mediocampista in mediocampistas:
            print(mediocampista)

        print("--- Delanteros ---")
        for delantero in delanteros:
            print(delantero)

        print("--- Porteros ---")
        for portero in porteros:
            print(portero)
        self.__abmC.close()


if __name__ == "__main__":
    pr = PruebaCarta()
    pr.test()
