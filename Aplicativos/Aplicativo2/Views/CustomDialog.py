from Views.ui_Mensaje import Ui_Error
from PySide6.QtWidgets import QDialog

class Error(QDialog, Ui_Error):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    