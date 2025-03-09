import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi
from firebase_config import auth
from PyQt6.QtWidgets import QLineEdit
import sqlite3
import os

def ejecutar_sql():
    """Ejecuta el archivo .sql que contiene las instrucciones de creación de tablas."""
    try:
        with open("hotel.sql", "r") as archivo_sql:
            sql_script = archivo_sql.read()

        conexion = sqlite3.connect('hotel.db')
        cursor = conexion.cursor()
        cursor.executescript(sql_script)
        conexion.commit()
        conexion.close()
        print("Base de datos configurada correctamente.")
    except Exception as e:
        print(f"Error al ejecutar el script SQL: {e}")

class Login(QMainWindow):
    def __init__(self):
        super().__init__()

        # Obtener la ruta correcta al archivo .ui
        ui_file = self.get_ui_path("FireBase/ui/login.ui")

        # Cargar el archivo .ui
        loadUi(ui_file, self)

        # Obtener la ruta correcta a la imagen de fondo
        fondo_path = self.get_ui_path("fondo.jpg")

        # Establecer la imagen de fondo usando CSS
        self.setStyleSheet(f"""
            QMainWindow {{
                background-image: url({fondo_path});
                background-position: center;
                background-repeat: no-repeat;
            }}
        """)

        self.loginbutton.clicked.connect(self.loginfunction)

        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.createaccbutton.clicked.connect(self.gotocreate)

    def get_ui_path(self, relative_path):
        """
        Obtiene la ruta absoluta al archivo .ui, teniendo en cuenta si el programa
        está empaquetado con PyInstaller o no.
        """
        if getattr(sys, 'frozen', False):
            # Si está empaquetado con PyInstaller
            base_dir = sys._MEIPASS
        else:
            # Si se está ejecutando desde el código fuente
            base_dir = os.path.dirname(os.path.abspath(__file__))

        # Construir la ruta completa al archivo .ui
        return os.path.join(base_dir, relative_path)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        #email = "123456@gmail.com"
        #password = "123456"

        if not email or not password:
            QMessageBox.warning(self, "Input Error", "Please enter both email and password.")
            return
        
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            QMessageBox.information(self, "Success", f"Welcome {user['email']}!")
            self.gotomain()

        except Exception as e:
            print(f"Error during login: {e}")
            self.invalid.setVisible(True)
            QMessageBox.critical(self, "Login Error", "Invalid email or password. Please try again.")
    
    def gotomain(self):
        # Aquí instanciamos la ventana principal correctamente
        from principal.window_main import VentanaPrincipal
        self.window_main = VentanaPrincipal()
        self.window_main.show()
        self.close()  # Cierra la ventana de login actual

    def gotocreate(self):
        # Aquí instanciamos la ventana de creación de cuenta correctamente
        self.createacc = CreateAcc()
        self.createacc.show()
        self.close()  # Cierra la ventana de login y muestra la de creación de cuenta

class CreateAcc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QMainWindow {
                background-image: url(fondo.jpg);
                background-position: center;
                background-repeat: no-repeat;
            }
        """)
        loadUi("FireBase/ui/createacc.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirmpass.setEchoMode(QLineEdit.EchoMode.Password)
        self.login.clicked.connect(self.gotologin)

    def createaccfunction(self):
        email = self.email.text()
        password = self.password.text()
        confirm_password = self.confirmpass.text()
        
        if not email or not password or not confirm_password:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return
        
        if password != confirm_password:
            QMessageBox.warning(self, "Password Error", "Passwords do not match. Please try again.")
            return
        
        try:
            auth.create_user_with_email_and_password(email, password)
            QMessageBox.information(self, "Success", "Account created successfully!")
            self.gotologin()
        except Exception as e:
            print(f"Error during account creation: {e}")
            QMessageBox.critical(self, "Signup Error", "Failed to create account. Please try again.")

    def gotologin(self):
        self.login = Login()  # Reusamos Login aquí
        self.login.show()
        self.close()  # Cierra la ventana actual de creación de cuenta

if __name__ == "__main__":
    ejecutar_sql()
    # Crear la aplicación
    app = QApplication(sys.argv)

    # Crear una instancia de la ventana de inicio de sesión
    login_window = Login()

    # Mostrar la ventana de inicio de sesión
    login_window.show()

    # Ejecutar la aplicación
    sys.exit(app.exec())