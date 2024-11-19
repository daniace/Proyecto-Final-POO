from abc import ABC,abstractmethod

class Dificultad(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._probabilidad=100
    
    @abstractmethod
    def get_probabilidad(self):
        pass

class Facil(Dificultad):
    
    def get_probabilidad(self):
        return self._probabilidad * 1

class Medio(Dificultad):
    
    def get_probabilidad(self):
        return int(self._probabilidad * 1.2)

class Dificil(Dificultad):
    def get_probabilidad(self):
        return int(self._probabilidad * 1.5)

