from AbmUsuario import AbmUsuario
from Usuario import Usuario


class PruebaRank:
    def __init__(self):
        self.abm = AbmUsuario()
        self.usuarios = self.abm.get_all()

    partido_ganado = True

    def mostrar_lista_score(self):
        for usuario in self.usuarios:
            print(f"{usuario.get_nombre()} - {usuario.get_score()}")

    def mostrar_score(self, id):
        usuario = self.abm.get_por_id(id)
        print(f"{usuario.get_nombre()} - {usuario.get_score()}")


if __name__ == "__main__":
    pr = PruebaRank()
    pr.mostrar_lista_score()
    usuario = pr.abm.get_por_id(1)
    usuario.set_score(25)
    pr.abm.actualizar(usuario)
    pr.mostrar_score(1)
    print(usuario)
    pr.abm.close()
