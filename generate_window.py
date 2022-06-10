# -*- coding: utf-8 -*-
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

from random import randint

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None
        self.button = QPushButton("Push for Window")
        self.setFixedSize(QSize(600, 300))
        self.setCentralWidget(self.button)

def create_window():
   app = QApplication(sys.argv)
   w = MainWindow()
   w.show()
   app.exec_()

if __name__ == '__main__':
   create_window()