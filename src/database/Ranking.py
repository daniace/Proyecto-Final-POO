class Ranking:
    def __init__(self, id_usuario):
        self.__id_usuario = id_usuario
        self.__score = None

    def get_id_usuario(self):
        return self.__id_usuario

    def get_score(self):
        return self.__score
