# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore, uic

PPMainWindow, Base = uic.loadUiType("MainWindow.ui")


class PPMainWindow(QtGui.QMainWindow, PPMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setCentralWidget(self.centralwidget)
        self.connect(self.actionDateLocalDBCreate, QtCore.SIGNAL("triggered()"),
                     self.on_date_local_db_create)

    def on_date_local_db_create(self):
        print("Выбран пункт меню - Создать локальную базу данных")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = PPMainWindow()
    window.show()
    sys.exit(app.exec_())

