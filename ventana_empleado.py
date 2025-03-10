
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
from bd_empleados import BD_empleados  # Importa la clase BD_empleados
import os

class VentanaEmpleados(QMainWindow):
    def __init__(self):
        super(VentanaEmpleados, self).__init__()

        ui_file = os.path.join(os.path.dirname(__file__), "ventana_empleado.ui")
        uic.loadUi(ui_file, self)

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

        # Conectar botones a sus funciones
        self.bt_registrar_empleado.clicked.connect(self.registrar_empleado)
        self.bt_mostrar_empleados.clicked.connect(self.mostrar_empleados)
        self.bt_buscar_empleado.clicked.connect(self.buscar_empleado)
        self.bt_eliminar_empleado.clicked.connect(self.eliminar_empleado)
        self.bt_actualizar_empleado.clicked.connect(self.actualizar_empleado)
        self.bt_atras.clicked.connect(self.ir_atras)
        self.bt_informe.clicked.connect(self.generar_informe)

    def registrar_empleado(self):
        """Registra un nuevo empleado en la base de datos."""
        nombre = self.text_nombre_empleado.text()
        apellido = self.text_apellido_empleado.text()
        cargo = self.text_cargo.text()
        email = self.text_email_empleado.text()
        telefono = self.text_telefono_empleado.text()

        # Validar que los campos no estén vacíos
        if not (nombre and apellido and cargo and email and telefono):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        bd = BD_empleados()
        exito, msg = bd.insertar_empleado(nombre, apellido, cargo, email, telefono)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            # Limpiar los campos después de registrar
            self.text_nombre_empleado.clear()
            self.text_apellido_empleado.clear()
            self.text_cargo.clear()
            self.text_email_empleado.clear()
            self.text_telefono_empleado.clear()
        else:
            QMessageBox.warning(self, "Error", msg)

    def mostrar_empleados(self):
        """Muestra todos los empleados en la tabla."""
        empleados = BD_empleados().obtener_empleados()

        if len(empleados) == 0:
            self.tabla_empleados.setRowCount(0)
            QMessageBox.warning(self, "Advertencia", "No hay empleados registrados.")
        else:
            # Crear una tabla para mostrar los empleados
            self.tabla_empleados.setRowCount(len(empleados))  # Número de filas
            self.tabla_empleados.setColumnCount(6)  # 6 columnas: id, nombre, apellido, cargo, email, telefono

            # Configurar los encabezados de las columnas
            self.tabla_empleados.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "Cargo", "Email", "Teléfono"])

            # Llenar la tabla con los datos de los empleados
            for row, empleado in enumerate(empleados):
                for col, value in enumerate(empleado):
                    self.tabla_empleados.setItem(row, col, QTableWidgetItem(str(value)))

    def buscar_empleado(self):
        """Busca un empleado por su email y lo muestra en la tabla."""
        email = self.text_email_buscar_empleado.text()

        # Validar que el campo no esté vacío
        if not email:
            QMessageBox.warning(self, "Error", "El campo es obligatorio.")
            return

        empleado = BD_empleados().buscar_empleado_por_email(email)

        if empleado is None:
            QMessageBox.warning(self, "Advertencia", "No se encontró un empleado con ese email.")
        else:
            # Crear una tabla para mostrar el empleado
            self.tabla_empleados.setRowCount(1)  # Número de filas
            self.tabla_empleados.setColumnCount(6)  # 6 columnas: id, nombre, apellido, cargo, email, telefono

            # Configurar los encabezados de las columnas
            self.tabla_empleados.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "Cargo", "Email", "Teléfono"])

            # Llenar la tabla con los datos del empleado
            for col, value in enumerate(empleado):
                self.tabla_empleados.setItem(0, col, QTableWidgetItem(str(value)))

    def eliminar_empleado(self):
        """Elimina un empleado de la base de datos."""
        email_empleado = self.text_borrar_empleado.text()  # Obtener el ID del empleado a eliminar

        if not email_empleado:  # Verificar el email del empleado
            QMessageBox.warning(self, "Error", "Campo obligatorio.")
            return

        bd = BD_empleados()
        exito, msg = bd.eliminar_empleado(email_empleado)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_empleados()  # Volver a cargar la lista de empleados
        else:
            QMessageBox.warning(self, "Error", msg)

        self.text_borrar_empleado.clear()

    def actualizar_empleado(self):
        """Actualiza los datos de un empleado en la base de datos."""
        empleado_id = self.text_id_empleado.text() 
        nombre = self.text_nombre_empleado.text()
        apellido = self.text_apellido_empleado.text()
        cargo = self.text_cargo.text()
        email = self.text_email_empleado.text()
        telefono = self.text_telefono_empleado.text()

        # Validar que los campos no estén vacíos
        if not (nombre and apellido and cargo and email and telefono and empleado_id.isdigit()):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios y el ID debe ser válido.")
            return

        bd = BD_empleados()
        exito, msg = bd.actualizar_empleado(int(empleado_id), nombre, apellido, cargo, email, telefono)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_empleados()  # Volver a cargar la lista de empleados
        else:
            QMessageBox.warning(self, "Error", msg)

    # Generar un informe en PDF con los datos de los empleados
    def generar_informe(self):
        from empleado_pdf import EmpleadoPDF
        pdf = EmpleadoPDF()   # Instancia de la clase PDFReport
        pdf.create_pdf()    # Genera el PDF

    def ir_atras(self):
        """Vuelve a la ventana principal."""
        from window_main import VentanaPrincipal
        self.window_main = VentanaPrincipal()
        self.window_main.show()
        self.hide()

