from PySide6.QtWidgets import QApplication, QMainWindow
from Vistas.ui_Interfaz import Ui_Aplicativo1
import sys

class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_Aplicativo1()
        self.ui.setupUi(self)

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = MainWindow()
     window.show()
     sys.exit(app.exec())
     