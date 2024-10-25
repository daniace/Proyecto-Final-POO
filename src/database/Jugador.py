

class Jugador(): # Clase que representa a un usuario del juego o un administrador
    def __init__(self,idUsuario,nombreUsuario,password):
        self.__idUsuario = idUsuario
        self.__nombreUsuario = nombreUsuario
        self.__password = password
        self.__admin = None
        self.__bajaUsuario = None
        
    def get_nombre(self):
        return self.__nombreUsuario
    
    def get_password(self):
        return self.__password

    def get_admin(self):
        return self.__admin
    
    def get_bajaUsuario(self):
        return self.__bajaUsuario