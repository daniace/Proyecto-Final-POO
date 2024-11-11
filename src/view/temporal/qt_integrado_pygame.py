import sys
import pygame
from PyQt5 import QtWidgets, uic, QtCore, QtGui

class PygameWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_pygame()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_pygame)
        self.timer.start(30)  # Actualizar cada 30 ms (~33 FPS)

    def init_pygame(self):
        # Inicializar Pygame y configuraciones de la pelota
        pygame.init()
        self.bg_color = (0, 0, 0)
        self.ball_color = (255, 0, 0)
        self.ball_radius = 30
        self.ball_pos = [self.width() // 2, self.height() // 2]
        self.ball_vel = [5, 5]
        self.screen = pygame.Surface((self.width(), self.height()))

    def update_pygame(self):
        # Actualizar posición de la pelota
        for i in range(2):
            self.ball_pos[i] += self.ball_vel[i]
            # Rebotar en los bordes
            if self.ball_pos[i] - self.ball_radius <= 0 or self.ball_pos[i] + self.ball_radius >= [self.width(), self.height()][i]:
                self.ball_vel[i] = -self.ball_vel[i]

        # Dibujar en la superficie de Pygame
        self.screen.fill(self.bg_color)
        pygame.draw.circle(self.screen, self.ball_color, self.ball_pos, self.ball_radius)

        # Convertir la superficie de Pygame a QImage y dibujar en el widget
        self.update()

    def paintEvent(self, event):
        # Convierte la superficie de Pygame en una imagen de Qt para mostrar en el widget
        qimage = self.convert_pygame_surface_to_qimage(self.screen)
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, qimage)
        painter.end()

    def convert_pygame_surface_to_qimage(self, surface):
        width, height = surface.get_size()
        data = surface.get_buffer().raw
        qimage = QtGui.QImage(data, width, height, QtGui.QImage.Format_RGB32)
        return qimage

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mi_interfaz.ui", self)  # Cargar el archivo .ui
        # Crear el widget Pygame y añadirlo al diseño de la ventana de Qt
        self.pygame_widget = PygameWidget(self.pygame_widget)  # Enlazar al espacio en la interfaz
        self.pygame_widget.setFixedSize(400, 300)  # Tamaño del área de Pygame (ajústalo según sea necesario)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
