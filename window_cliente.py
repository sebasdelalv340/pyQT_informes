
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
from bd_clientes import BD_clientes
import os

class VentanaClientes(QMainWindow):
    def __init__(self):
        super(VentanaClientes, self).__init__()

        ui_file = os.path.join(os.path.dirname(__file__), "registro_user.ui")

        uic.loadUi(ui_file,self)
        self.setWindowTitle("Registro Cliente")

        fondo = os.path.join(os.path.dirname(__file__), "fondo.jpg")
        fondo = fondo.replace("\\", "/")  # Asegura compatibilidad con QSS en Windows

        # Establecer la imagen de fondo usando CSS
        self.setStyleSheet(f"""
            QMainWindow {{
                background-image: url("{fondo}");  /* Se agregan comillas */
                background-position: center;
                background-repeat: no-repeat;
            }}
        """)

        self.bt_registrar_cliente.clicked.connect(self.registrar_cliente)
        self.bt_mostrar_clientes.clicked.connect(self.mostrar_clientes)
        self.bt_buscar_cliente.clicked.connect(self.buscar_cliente)
        self.bt_eliminar_cliente.clicked.connect(self.eliminar_cliente)
        self.bt_actualizar_cliente.clicked.connect(self.actualizar_cliente)
        self.bt_atras.clicked.connect(self.ir_atras)
        self.bt_informe.clicked.connect(self.generar_informe)

    def registrar_cliente(self):
        nombre = self.textNombre.text()
        apellido1 = self.textApellido1.text()
        apellido2 = self.textApellido2.text()
        dni = self.textDNI.text()
        email = self.textEmail.text()

        # Validar que los campos no estén vacíos
        if not (nombre and apellido1 and apellido2 and dni and email):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        bd = BD_clientes()
        exito, msg = bd.insertar_cliente(nombre, apellido1, apellido2, dni, email)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            # Limpiar los campos después de registrar
            self.textNombre.clear()
            self.textApellido1.clear()
            self.textApellido2.clear()
            self.textDNI.clear()
            self.textEmail.clear()
        else:
            QMessageBox.warning(self, "Error", msg)


    def mostrar_clientes(self):
        clientes = BD_clientes().obtener_clientes()

        if (clientes.__len__() == 0):
            self.tablaClientes.setRowCount(0)
            QMessageBox.warning(self, "Advertencia", "No hay clientes registrados.")
        else:
            # Crear una tabla para mostrar los usuarios
            self.tablaClientes.setRowCount(len(clientes))  # Número de filas
            self.tablaClientes.setColumnCount(6)  # 6 columnas: id, nombre, apellido1, apellido2, dni, email

            # Configurar los encabezados de las columnas
            self.tablaClientes.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido1", "Apellido2", "Email", "DNI"])

            # Llenar la tabla con los datos de los usuarios
            for row, cliente in enumerate(clientes):
                for col, value in enumerate(cliente):
                    self.tablaClientes.setItem(row, col, QTableWidgetItem(str(value)))

    def buscar_cliente(self):
        email = self.text_email_buscar.text()

        # Validar que los campos no estén vacíos
        if not (email):
            QMessageBox.warning(self, "Error", "Campo obligatorio.")
            return
        
        cliente = BD_clientes().buscar_cliente_por_email(email)

        if cliente is None:
            QMessageBox.warning(self, "Advertencia", "No se encontró un cliente con ese email.")
        else:
            # Crear una tabla para mostrar los usuarios
            self.tablaClientes.setRowCount(1)  # Número de filas
            self.tablaClientes.setColumnCount(6)  # 6 columnas: id, nombre, apellido1, apellido2, dni, email

            # Configurar los encabezados de las columnas
            self.tablaClientes.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido1", "Apellido2", "Email", "DNI"])

            # Llenar la tabla con los datos de los usuarios
            for col, value in enumerate(cliente):
                self.tablaClientes.setItem(0, col, QTableWidgetItem(str(value)))


    def eliminar_cliente(self):
        # Obtener el email del clienteque se desea eliminar (puede ser desde una selección en una tabla, por ejemplo)
        email_cliente = self.text_email_cliente.text()  # Suponiendo que tienes un campo de texto para ingresar el email del cliente

        if not email_cliente:  # Verificar el email del cliente
            QMessageBox.warning(self, "Error", "Campo obligatorio.")
            return

        bd = BD_clientes()
        exito, msg = bd.eliminar_cliente(email_cliente)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_clientes()  # Volver a cargar la lista de usuarios
        else:
            QMessageBox.warning(self, "Error", msg)
        
        self.text_email_cliente.clear()


    def actualizar_cliente(self):
        # Obtener los datos del cliente (suponiendo que tienes campos de texto en la UI)
        user_id = self.textUserID.text()  # ID del usuario que deseas actualizar
        nombre = self.textNombre.text()  # Nuevo nombre
        apellido1 = self.textApellido1.text()  # Nuevo apellido
        apellido2 = self.textApellido2.text()  # Nuevo apellido
        dni = self.textDNI.text()  # Nuevo DNI
        email = self.textEmail.text()  # Nuevo email

        # Validar que los campos no estén vacíos
        if not (nombre and apellido1 and apellido2 and dni and email and user_id.isdigit()):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios y el ID debe ser válido.")
            return

        bd = BD_clientes()
        exito, msg = bd.actualizar_cliente(int(user_id), nombre, apellido1, apellido2, dni, email)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_clientes()  # Volver a cargar la lista de clientes
        else:
            QMessageBox.warning(self, "Error", msg)

    # Generar un informe en PDF con los datos de los clientes
    def generar_informe(self):
        from cliente_pdf import ClientePDF
        pdf = ClientePDF()   # Instancia de la clase PDFReport
        pdf.create_pdf()    # Genera el PDF


    
    # Vuelve a la ventana principal
    def ir_atras(self):
        from window_main import VentanaPrincipal
        self.window_main = VentanaPrincipal()
        self.window_main.show()
        self.hide()

