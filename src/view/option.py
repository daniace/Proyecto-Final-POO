import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"src\view\option.ui", self)  # Carga el archivo .ui

app = QApplication(sys.argv)
option = MainWindow()
option.show()
sys.exit(app.exec_())
