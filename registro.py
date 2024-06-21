from PyQt6.QtWidgets import (QDialog, QLabel, QPushButton, QLineEdit, QMessageBox, QWidget)
import requests
from PyQt6.QtGui import QFont, QPixmap
from pydantic import BaseModel

class Usuario:
    def __init__(self, nombre, contraseña, mail):
        self.name = nombre
        self.password = contraseña
        self.mail = mail


class RegistroUsuarioView(QWidget):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Registratrion Window")

        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20, 44)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 40)

        password_1_label = QLabel(self)
        password_1_label.setText("Password:")
        password_1_label.setFont(QFont('Arial', 10))
        password_1_label.move(20, 74)

        self.password_1_input = QLineEdit(self)
        self.password_1_input.resize(250, 24)
        self.password_1_input.move(90, 70)
        self.password_1_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        password_2_label = QLabel(self)
        password_2_label.setText("Password:")
        password_2_label.setFont(QFont('Arial', 10))
        password_2_label.move(20, 104)

        self.password_2_input = QLineEdit(self)
        self.password_2_input.resize(250, 24)
        self.password_2_input.move(90, 100)
        self.password_2_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )


        mail_label = QLabel(self)
        mail_label.setText("Mail:")
        mail_label.setFont(QFont('Arial', 10))
        mail_label.move(20, 144)

        self.mail_input = QLineEdit(self)
        self.mail_input.resize(250, 24)
        self.mail_input.move(90, 140)
        

        create_button=QPushButton(self)
        create_button.setText("Crear")
        create_button.resize(150,32)
        create_button.move(20,170)
        create_button.clicked.connect(self.crear_usuario)

        cancel_button=QPushButton(self)
        cancel_button.setText("Cancelar")
        cancel_button.resize(150,32)
        cancel_button.move(170,170)
        cancel_button.clicked.connect(self.cancelar_usuario)

    def closeEvent(self, event):
        self.main_window.showNormal()
        event.accept()
    
    def cancelar_usuario(self):
        self.close()
    
    def crear_usuario(self):
        
        user_path ='AtlasGUI/ProyectoATLASGUI/usuarios.txt'
        usuario = self.user_input.text()
        password1 = self.password_1_input.text()
        password2 = self.password_2_input.text()
        mail=self.mail_input.text()
        usuario_data = Usuario(usuario, password1, mail)
        
        #usuario_data.name=usuario
        #usuario_data.password=password1
        #usuario_data.mail=mail

        if password1 == '' or password2 == '' or usuario == '':
            QMessageBox.warning(self,'Error',
            'Los campos no pueden estar vacios',
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)

        elif password1 != password2:
            QMessageBox.warning(self,'Error',
            'Las contraseñas no son iguales',
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
        
        else: 
            try: 
                
                auth_data = {'name':usuario_data.name,'password':usuario_data.password,'mail':usuario_data.mail}
                
                resp = requests.post('http://127.0.0.1:8000/add_usuario', json= auth_data)
                QMessageBox.information(self, 'Creación Completada',
                'Usuario creado correctamente',
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.close()

            except FileNotFoundError as e:
                QMessageBox.warning(self,'Error',
                f'La base de datos no existe:{e}',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
                

    
