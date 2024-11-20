from abc import ABC, abstractmethod


class DaoInterfaz(ABC):  # Interfaz a implementar en los ABM de Equipo, Jugador, Carta.
    @abstractmethod
    def get_por_id(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def insertar(self, objeto):
        pass

    @abstractmethod
    def actualizar(self, objeto):
        pass

    @abstractmethod
    def borrar(self, id):
        pass
