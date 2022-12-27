from sys import argv
from PyQt5.QtWidgets import QApplication
from screens.screen_startmenu import startmenu

if __name__ == '__main__':
    app = QApplication(argv)
    start = startmenu()
    start.show()
    exit(app.exec_())


