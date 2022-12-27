from ui_files.ui_startmenu import Ui_Form
from PyQt5.QtWidgets import QWidget


class startmenu(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self), self.retranslateUi(self)
        self.myInit()

    def myInit(self):
        pass
