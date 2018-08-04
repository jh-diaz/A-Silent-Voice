import random, time

from PyQt5.QtCore import pyqtSlot, QByteArray, QTimer, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
import iconpack
from PyQt5.uic.properties import QtCore


class LogInForm(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('login_Form.ui', self)
        self.setFixedSize(420, 550)
        movie = QMovie("loading.gif")
        self.logoIMG.setMovie(movie)
        movie.start()
        #self.loadMainForm()
        #self.button_skip.clicked.connect(self.openMainForm)
        self.button_skip.clicked.connect(self.loadMainForm)

    def loadMainForm(self): #for calling the main menu
        from mainController import MainForm
        self.window = MainForm(self)
        self.window.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.hide()
        self.window.show()

    def openMainForm(self):
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = LogInForm()
    window.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec_())# program still runs even if you quit on login window