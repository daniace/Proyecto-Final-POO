import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"src\view\diseño.ui", self)  # Carga el archivo .ui

app = QApplication(sys.argv)
menu = MainWindow()
menu.show()
sys.exit(app.exec_())
