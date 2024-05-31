import sys
from PyQt6.QtWidgets import (QApplication, QDialog, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox)
from PyQt6.QtGui import QFont, QPixmap

from registro import RegistroUsuarioView

class Main(QWidget):

    def __init__(self,main_window):
      super().__init__()
      self.main_window = main_window      
      self.setGeometry(100,100,500,500)
      self.setWindowTitle("Ventana Principal")

      image_path = 'AtlasGUI/ProyectoATLASGUI/Logo.png'

      try: 
            with open(image_path):
                image_label = QLabel(self)
                image_label.setPixmap(QPixmap(image_path))

      except FileNotFoundError as e:

            QMessageBox.warning(self,'Error',
            'Imagen no encontrada: {e}',
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)

      except Exception as e:

                QMessageBox.warning(self,'Error',
                'Error en el main: {e}',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
        
