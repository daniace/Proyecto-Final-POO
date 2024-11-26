import customtkinter as ctk

from view.ABMView import centrar_ventana


class MenuABM(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Configuración de customtkinter
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Ventana principal
        self.resizable(False, False)
        self.title("Menú Administrador")

        # Título
        self.__label_titulo = ctk.CTkLabel(self, text="Menú ABM", font=("Arial", 20))
        self.__label_titulo.pack(pady=20)

        # Botones
        self.__btn_abm_usuarios = ctk.CTkButton(self, text="ABM Usuarios")
        self.__btn_abm_usuarios.pack(pady=10)

        self.__btn_abm_equipo = ctk.CTkButton(self, text="ABM Equipo")
        self.__btn_abm_equipo.pack(pady=10)

        self.__btn_abm_carta = ctk.CTkButton(self, text="ABM Carta")
        self.__btn_abm_carta.pack(pady=10)

        self.__btn_salir = ctk.CTkButton(self, text="Salir", command=self.destroy)
        self.__btn_salir.pack(pady=20)

    def _conectar_abm_usuarios(self, callback):
        self.__btn_abm_usuarios.configure(command=callback)

    def _conectar_abm_equipos(self, callback):
        self.__btn_abm_equipo.configure(command=callback)

    def _conectar_abm_cartas(self, callback):
        self.__btn_abm_carta.configure(command=callback)

    def iniciar(self):
        centrar_ventana(self, 300, 300)
        self.mainloop()
