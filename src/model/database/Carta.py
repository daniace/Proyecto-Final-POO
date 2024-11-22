class Carta:
    def __init__(
        self,
        id_carta=None,
        nombre: str = "",
        nacionalidad: str = "",
        club: str = "",
        valoracion: int = 0,
        posicion: str = "",
        posicion_equipo: str = "",
        dorsal: int = 0,
        velocidad: int = 0,
        disparo: int = 0,
        pase: int = 0,
        gambeta: int = 0,
        defensa: int = 0,
        fisico: int = 0,
        gk_diving: int = 0,
        gk_handling: int = 0,
        gk_kicking: int = 0,
        gk_reflexes: int = 0,
        gk_speed: int = 0,
        gk_positioning: int = 0,
    ):
        self.__id_carta: int = id_carta
        self.__nombre: str = nombre
        self.__nacionalidad: str = nacionalidad
        self.__club: str = club
        self.__valoracion: int = valoracion
        self.__posicion: str = posicion
        self.__posicion_equipo: str = posicion_equipo
        self.__dorsal: int = dorsal
        self.__velocidad: int = velocidad
        self.__disparo: int = disparo
        self.__pase: int = pase
        self.__gambeta: int = gambeta
        self.__defensa: int = defensa
        self.__fisico: int = fisico
        self.__gk_diving: int = gk_diving
        self.__gk_handling: int = gk_handling
        self.__gk_kicking: int = gk_kicking
        self.__gk_reflexes: int = gk_reflexes
        self.__gk_speed: int = gk_speed
        self.__gk_positioning: int = gk_positioning
        self.__tenencia = False

    def get_nombre(self):
        return self.__nombre

    def get_dorsal(self):
        return self.__dorsal

    def get_posicion(self):
        posiciones = self.__posicion.split(",")[:2]
        posiciones_clasificadas = []
        for pos in posiciones:
            if pos == "GK":
                posiciones_clasificadas.append("ARQUERO")
            elif pos in ["CB", "LB", "RB", "LWB", "RWB"]:
                posiciones_clasificadas.append("DEFENSOR")
            elif pos in ["CDM", "CM", "CAM", "LM", "RM"]:
                posiciones_clasificadas.append("MEDIOCAMPISTA")
            elif pos in ["LW", "RW", "CF", "ST", "LF", "RF"]:
                posiciones_clasificadas.append("DELANTERO")
        return posiciones_clasificadas

    def get_posicion_equipo(self):
        return self.__posicion_equipo

    def get_club(self):
        return self.__club

    def get_nacionalidad(self):
        return self.__nacionalidad

    def get_velocidad(self):
        if self.__posicion == "GK":
            return self.__gk_diving
        else:
            return self.__velocidad

    def get_disparo(self):
        if self.__posicion == "GK":
            return self.__gk_handling
        else:
            return self.__disparo

    def get_pase(self):
        if self.__posicion == "GK":
            return self.__gk_kicking
        else:
            return self.__pase

    def get_gambeta(self):
        if self.__posicion == "GK":
            return self.__gk_reflexes
        else:
            return self.__gambeta

    def get_defensa(self):
        if self.__posicion == "GK":
            return self.__gk_speed
        else:
            return self.__defensa

    def get_fisico(self):
        if self.__posicion == "GK":
            return self.__gk_positioning
        else:
            return self.__fisico

    def get_diving(self):
        return self.__gk_diving

    def get_handling(self):
        return self.__gk_handling

    def get_kicking(self):
        return self.__gk_kicking

    def get_reflexes(self):
        return self.__gk_reflexes

    def get_speed(self):
        return self.__gk_speed

    def get_positioning(self):
        return self.__gk_positioning

    def get_tenencia(self):
        return self.__tenencia

    def get_valoracion(self):
        return self.__valoracion

    def get_id(self):
        return self.__id_carta

    def set_tenencia(self):
        if not self.__tenencia:
            self.__tenencia = True
        else:
            self.__tenencia = False

    def __str__(self) -> str:
        if self.__posicion == "GK":
            return f"{self.__nombre} ({self.__club}) - {self.get_posicion()} - {self.__valoracion} - {self.__gk_diving} - {self.__gk_handling} - {self.__gk_kicking} - {self.__gk_reflexes} - {self.__gk_speed} - {self.__gk_positioning}"
        else:
            return f"{self.__nombre} ({self.__club}) - {self.get_posicion()} - {self.__valoracion} - {self.__velocidad} - {self.__disparo} - {self.__pase} - {self.__gambeta} - {self.__defensa} - {self.__fisico}"

    def __repr__(self):
        return self.__str__()

    def get_str(self):
        return (
            f"{self.__nombre} \n"
            f"  {self.__velocidad}-{self.__disparo} \n"
            f"  {self.__pase}-{self.__gambeta} \n"
            f"  {self.__defensa}-{self.__fisico} \n"
        )

    def get_posicion_arquero(self):
        return self.__posicion
