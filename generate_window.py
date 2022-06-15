# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QApplication, QFileDialog, QPushButton, QVBoxLayout, QWidget
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
      self.confirmation = ""

      self.window_width, self.window_height = 400, 100
      self.setMinimumSize(self.window_width, self.window_height)
      self.setWindowTitle("Coordinates Convertor")

      layout = QVBoxLayout()
      self.setLayout(layout)

      self.input_file_label = QLabel(self)
      self.output_folder_label = QLabel(self)
      self.confirmation_label = QLabel(self)

      file_button = QPushButton("Input File")
      file_button.clicked.connect(self.get_input_file)
      layout.addWidget(file_button)

      self.input_file_label.setText(self.input_file)
      self.input_file_label.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.input_file_label)

      folder_button = QPushButton("Output Folder")
      folder_button.clicked.connect(self.get_output_folder)
      layout.addWidget(folder_button)

      self.output_folder_label.setText(self.output_folder)
      self.output_folder_label.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.output_folder_label)

      run_button = QPushButton("Run")
      run_button.clicked.connect(self.clicked_run_button)
      layout.addWidget(run_button)

      self.confirmation_label.setText(self.confirmation)
      self.confirmation_label.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.confirmation_label)


   def get_input_file(self):
      response = QFileDialog.getOpenFileName(
         parent = self,
         caption = "Select a data file",
         dir = os.getcwd()
         )
      self.input_file = response[0]
      self.input_file_label.setText(self.input_file)

   def get_output_folder(self):
      response = QFileDialog.getExistingDirectory(
         self,
         caption = "Select an output folder"
         )
      self.output_folder = response
      self.output_folder_label.setText(self.output_folder)

   def clicked_run_button(self):
      self.input_file_name = os.path.basename(self.input_file).split(".")[0]
      self.output_file = osj(self.output_folder, self.input_file_name + "_output.geo")
      convertor.convertor(self.input_file, self.output_file)
      self.confirmation_label.setText("Done !")


def create_window():
   app = QApplication(sys.argv)
   w = MainWindow()
   w.show()
   app.exec()

if __name__ == '__main__':
   create_window()