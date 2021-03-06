import sys, os
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic.properties import QtGui
from PyQt5.uic import loadUi
from Modules.FileFinder import resource_path

# Class to show the quit prompt when exiting the program
class QuitPrompt(QDialog):
    def __init__(self, mainWindow):
        super().__init__()
        if getattr(sys, 'frozen', False):
            ui = resource_path('quit_prompt.ui')
        else:
            ui = 'Modules/UserInterface/quit_prompt.ui'
        loadUi(ui, self)
        self.quitYesButton.clicked.connect(self.logoutAction)
        self.quitNoButton.clicked.connect(self.closePrompt)
        self.mainWindow = mainWindow
        self.ans = False

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        try:
            x = event.globalX()
            y = event.globalY()
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.move(x - x_w, y - y_w)
        except:
            print("crash in quitcontroller.py")

    def getButtonPressed(self):
        print(self.ans)
        return self.ans

    @pyqtSlot()
    def logoutAction(self):
        self.ans = True
        self.hide()

    @pyqtSlot()
    def closePrompt(self):
        self.ans = False
        self.hide()
