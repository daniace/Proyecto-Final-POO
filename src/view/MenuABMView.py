import customtkinter as ctk

from controller.ControladorABMCarta import ControladorABMCartas
from controller.ControladorABMEquipo import ControladorABMEquipo
from controller.ControladorABMUsuario import ControladorABMUsuarios


class MenuABM(ctk.CTk):
    def __init__(self):
        # Configuración de customtkinter
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.ventana_abm_usuarios = None
        self.ventana_abm_carta = None
        self.ventana_abm_equipo = None

        # Ventana principal
        self.root = ctk.CTk()
        self.root.resizable(False, False)
        self.root.title("Menú Administrador")
        self.visible = False
        self.centrar_ventana()

        # Título
        self.label_titulo = ctk.CTkLabel(self.root, text="Menú ABM", font=("Arial", 20))
        self.label_titulo.pack(pady=20)

        # Botones
        self.btn_abm_usuarios = ctk.CTkButton(
            self.root, text="ABM Usuarios", command=self.accion_abm_usuarios
        )
        self.btn_abm_usuarios.pack(pady=10)

        self.btn_abm_equipo = ctk.CTkButton(
            self.root, text="ABM Equipo", command=self.accion_abm_equipo
        )
        self.btn_abm_equipo.pack(pady=10)

        self.btn_abm_carta = ctk.CTkButton(
            self.root, text="ABM Carta", command=self.accion_abm_carta
        )
        self.btn_abm_carta.pack(pady=10)

        self.btn_salir = ctk.CTkButton(self.root, text="Salir", command=self.cerrar)
        self.btn_salir.pack(pady=20)

    def centrar_ventana(self):
        """Centra la ventana en la pantalla."""
        ancho_ventana = 350  # Ancho de la ventana
        alto_ventana = 350  # Alto de la ventana

        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Calcular la posición centrada
        pos_x = int((ancho_pantalla - ancho_ventana) / 2)
        pos_y = int((alto_pantalla - alto_ventana) / 2)

        # Establecer la geometría de la ventana
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    def accion_abm_usuarios(self):
        """Acción al presionar el botón ABM Usuarios."""
        print("ABM Usuarios seleccionado")
        if (
            self.ventana_abm_usuarios is None
            or not self.ventana_abm_usuarios.vista.winfo_exists()
        ):
            self.ventana_abm_usuarios = ControladorABMUsuarios()
            self.ventana_abm_usuarios.iniciar()
        else:
            self.ventana_abm_usuarios.focus()

    def accion_abm_equipo(self):
        """Acción al presionar el botón ABM Equipo."""
        print("ABM Equipo seleccionado")
        if (
            self.ventana_abm_equipo is None
            or not self.ventana_abm_equipo.vista.winfo_exists()
        ):
            self.ventana_abm_equipo = ControladorABMEquipo()
            self.ventana_abm_equipo.iniciar()
        else:
            self.ventana_abm_equipo.focus()

    def accion_abm_carta(self):
        """Acción al presionar el botón ABM Carta."""
        print("ABM Carta seleccionado")
        if (
            self.ventana_abm_carta is None
            or not self.ventana_abm_carta.vista.winfo_exists()
        ):
            self.ventana_abm_carta = ControladorABMCartas()
            self.ventana_abm_carta.iniciar()
        else:
            self.ventana_abm_carta.focus()

    def iniciar(self):
        """Inicia el bucle principal de la ventana."""
        self.visible = True
        self.root.mainloop()

    def cerrar(self):
        """Cierra la ventana."""
        self.visible = False
        self.root.destroy()
