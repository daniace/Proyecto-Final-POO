from controller.ControladorMenuABM import ControladorMenuABM
from model.ModeloLoginAdmin import ModeloLoginAdmin
from view.LoginAdminView import LoginAdmin


class ControladorLoginaAdmin:
    def __init__(self):
        self.__modelo = ModeloLoginAdmin()
        self.__vista = LoginAdmin()
        self.__vista._conectar_boton_login(self.__validar_login)
        self.__vista_menuabm = ControladorMenuABM()

    def __validar_login(self):
        """Valida las credenciales ingresadas."""
        username, password = self.__vista._obtener_credenciales()
        if self.__modelo._validar_usuario(username, password):
            self.__vista._mostrar_resultado("Login exitoso")
            self.__abrir_ventana_menu_abm()
        else:
            self.__vista._mostrar_resultado("Login fallido")

    def __abrir_ventana_menu_abm(self):
        """Abre la ventana principal con los tres botones."""
        self.close()
        self.__vista.after(1000, self.__vista_menuabm.run())

    def run(self):
        """Inicia la aplicación."""
        self.__vista.iniciar()

    def close(self):
        """Cierra la ventana de la vista."""
        self.__vista.destroy()


if __name__ == "__main__":
    app = ControladorLoginaAdmin()
    app.run()
