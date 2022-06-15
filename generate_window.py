# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QApplication, QFileDialog, QPushButton, QVBoxLayout, QWidget
import __main__
import sys
import convertor
import os
from os.path import join as osj

class MainWindow(QWidget):

   def __init__(self):
      super().__init__()
      self.input_file = ""
      self.output_folder = ""
      self.window_width, self.window_height = 400, 100
      self.setMinimumSize(self.window_width, self.window_height)
      self.setWindowTitle("Coordinates Convertor")

      layout = QVBoxLayout()
      self.setLayout(layout)
      
      file_button = QPushButton("Input File")
      file_button.clicked.connect(self.get_input_file)
      layout.addWidget(file_button)

      folder_button = QPushButton("Output Folder")
      folder_button.clicked.connect(self.get_output_folder)
      layout.addWidget(folder_button)

      run_button = QPushButton("Run")
      run_button.clicked.connect(self.clicked_run_button)
      layout.addWidget(run_button)


   def get_input_file(self):
      response = QFileDialog.getOpenFileName(
         parent = self,
         caption = "Select a data file",
         dir = os.getcwd()
         )
      self.input_file = response[0]

   def get_output_folder(self):
      response = QFileDialog.getExistingDirectory(
         self,
         caption = "Select an output folder"
         )
      self.output_folder = response

   def clicked_run_button(self):
      self.input_file_name = os.path.basename(self.input_file).split(".")[0]
      self.output_file = osj(self.output_folder, self.input_file_name + "_output.geo")
      convertor.convertor(self.input_file, self.output_file)


def create_window():
   app = QApplication(sys.argv)
   w = MainWindow()
   w.show()
   app.exec()

if __name__ == '__main__':
   create_window()