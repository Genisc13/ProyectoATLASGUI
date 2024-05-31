import sys
from PyQt6.QtWidgets import (QApplication, QDialog, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox)
from PyQt6.QtGui import QFont, QPixmap

from registro import RegistroUsuarioView
from API_MAIN import Main


class Login(QWidget):

    def __init__(self):
        super().__init__()

        self.registry_page = RegistroUsuarioView(self)
        
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Login")
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20, 28)

        "variable global"
        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 25)

        password_label = QLabel(self)
        password_label.setText("Password:")
        password_label.setFont(QFont('Arial', 10))
        password_label.move(20, 86)

        "variable global"
        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)
        self.password_input.move(90, 82)
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("Ver Contraseña")
        self.check_view_password.move(90, 110)
        self.check_view_password.clicked.connect(self.mostrar_password)

        login_button = QPushButton(self)
        login_button.setText("Login")
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.iniciar_mainview)

        register_button = QPushButton(self)
        register_button.setText("Register")
        register_button.resize(320, 34)
        register_button.move(20, 180)
        register_button.clicked.connect(self.registrar_usuario)


    def mostrar_password(self, clicked):
        if clicked:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Normal   
            )
        else:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Password
            )

    def iniciar_mainview(self):
        pass

    def registrar_usuario(self):
        if self.registry_page.isVisible():
            self.registry_page.hide()
        else:
            self.registry_page.show()
            self.showMinimized()

    def iniciar_mainview(self):
        users = []
        self.user_path = 'AtlasGUI/ProyectoATLASGUI/usuarios.txt'
        try:

            with open(self.user_path, 'r') as f:
                for linea in f:
                    users.append(linea.strip("\n"))
            login_information =  f"{self.user_input.text()},{self.password_input.text()}"

            if login_information in users: 
                QMessageBox.information(self,"Inicio sesión",
                "Inicio de sesión exitoso",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.is_logged = True
                self.close()
                self.open_main()

            else: 

                QMessageBox.warning(self,'Error',
                'Usuario no encontrado',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)

        except FileNotFoundError as e:

                QMessageBox.warning(self,'Error',
                'Base de datos usuarios no encontrada: {e}',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
        
        except Exception as e:

                QMessageBox.warning(self,'Error',
                'Error en el servidor: {e}',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)

    def open_main(self):
        self.main_window = Main(self)
        if self.main_window.isVisible():
            self.main_window.hide()
        else:
            self.main_window.show()
            self.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Login()
    w.show()
    sys.exit(app.exec())

