import os

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QSettings

from PyQt6.uic import loadUi
from helpers.RSPaperHelper import resource_path as rp

class BaseWindow:
    def __init__(self):
        if isinstance(self, QMainWindow):
            self.center()
        ui = rp('views/ui/{}.ui'.format(self.__class__.__name__))
        if os.path.isfile(ui):
            loadUi(ui, self)

        self.load_theme()
        self.config_interface()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        cp.setX(cp.x() - 160)
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def load_theme(self):
        dark_mode = QSettings("dark_mode").value("dark_mode", False, bool)
        if dark_mode:
            stylesheet = rp('views/styles/dark.css')
        else:
            stylesheet = rp('views/styles/light.css')
        with open(stylesheet, "r") as f:
            stylesheet_content = f.read()                
        stylesheet_content = stylesheet_content.replace('url(views/styles/', 'url(' + rp('views/styles/'))
        stylesheet_content = stylesheet_content.replace("\\", "/")

        self.setStyleSheet(stylesheet_content)

    def config_interface(self):
        pass