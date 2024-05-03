
from PyQt6.QtWidgets import (QDialog, QLabel, QPushButton, QLineEdit,QMessageBox, QWidget)

from PyQt6.QtGui import QFont, QPixmap

class RegistroUsuarioView(QWidget):
    
    def __int__(self):
        super().__init__()
        "self.generar_formulario()"

    def generar_formulario(self):

        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Registratrion Window")
        

        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial',10))
        user_label.move(20,44)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,40)

        password_1_label = QLabel(self)
        password_1_label.setText("Password:")
        password_1_label.setFont(QFont('Arial',10))
        password_1_label.move(20,74)

        self.password_1_input = QLineEdit(self)
        self.password_1_input.resize(250,24)
        self.password_1_input.move(90,70)
        self.password_1_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        password_2_label = QLabel(self)
        password_2_label.setText("Password:")
        password_2_label.setFont(QFont('Arial',10))
        password_2_label.move(20,94)

        self.password_2_input = QLineEdit(self)
        self.password_2_input.resize(250,24)
        self.password_2_input.move(90, 90)
        self.password_2_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        self.show()