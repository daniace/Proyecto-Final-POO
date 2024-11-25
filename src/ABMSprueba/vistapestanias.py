import customtkinter
from controladorabmusuario import ControladorABMUsuarios
from vistaabmcarta import VistaABMCartas
from vistaabmequipo import VistaABMEquipo
from vistaabmusuario import VistaABMUsuarios


class VistaPestanias(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("ABMS")
        self.controlador_usuarios = ControladorABMUsuarios()

        # Create the tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.pack(padx=20, pady=(10, 0), fill="both", expand=True)

        self.tabview.add("ABM Usuarios")
        self.tabview.add("ABM Equipo")
        self.tabview.add("ABM Cartas")

        # Create the ABM views within the tabs
        # self.vista_usuarios = VistaABMUsuarios(self.tabview.tab("ABM Usuarios"))
        # self.vista_usuarios.pack(fill="both", expand=True)

        # self.vista_equipo = VistaABMEquipo(self.tabview.tab("ABM Equipo"))
        # self.vista_equipo.pack(fill="both", expand=True)

        # self.vista_cartas = VistaABMCartas(self.tabview.tab("ABM Cartas"))
        # self.vista_cartas.pack(fill="both", expand=True)

        self.btn_abrir_usuarios = customtkinter.CTkButton(
            self, text="ABM Usuarios", command=self.abrir_abm_usuarios
        )

        self.tabview.set("ABM Cartas")  # Set default tab

    def abrir_abm_usuarios(self):
        self.controlador_usuarios.iniciar()


if __name__ == "__main__":
    app = VistaPestanias()
    app.mainloop()
