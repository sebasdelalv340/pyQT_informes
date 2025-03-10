from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
from bd_habitaciones import BD_habitaciones
import os

class VentanaHabitaciones(QMainWindow):
    def __init__(self):
        super(VentanaHabitaciones, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "habitaciones.ui")

        uic.loadUi(ui_file, self)
        self.setWindowTitle("Registro de Habitaciones")

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

        # Conectar botones con funciones
        self.bt_registrar_habitacion.clicked.connect(self.registrar_habitacion)
        self.bt_mostrar_habitaciones.clicked.connect(self.mostrar_habitaciones)
        self.bt_buscar_habitacion.clicked.connect(self.buscar_habitacion)
        self.bt_eliminar_habitacion.clicked.connect(self.eliminar_habitacion)
        self.bt_actualizar_habitacion.clicked.connect(self.actualizar_habitacion)
        self.bt_atras.clicked.connect(self.ir_atras)
        self.bt_informe.clicked.connect(self.generar_informe)

    def registrar_habitacion(self):
        numero = self.textNumero.text()
        tipo = self.comboTipo.currentText()
        precio_noche = self.textprecio_noche.text()
        disponible = self.disponible.isChecked()

        if not (numero and tipo and precio_noche):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        
        bd = BD_habitaciones()
        exito, msg = bd.insertar_habitacion(numero, tipo, precio_noche, disponible)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.textNumero.clear()
            self.comboTipo.setCurrentIndex(0)
            self.textprecio_noche.clear()
            self.disponible.setChecked(False)
        else:
            QMessageBox.warning(self, "Error", msg)

    def mostrar_habitaciones(self):
        habitaciones = BD_habitaciones().obtener_habitaciones()

        if len(habitaciones) == 0:
            self.tablahabitaciones.setRowCount(0)
            QMessageBox.warning(self, "Advertencia", "No hay habitaciones registradas.")
        else:
            self.tablahabitaciones.setRowCount(len(habitaciones))
            self.tablahabitaciones.setColumnCount(5)
            self.tablahabitaciones.setHorizontalHeaderLabels(["ID", "Número", "Precio por Noche","Tipo" , "Disponible"])

            for row, habitacion in enumerate(habitaciones):
                for col, value in enumerate(habitacion):
                    self.tablahabitaciones.setItem(row, col, QTableWidgetItem(str(value)))

    def buscar_habitacion(self):
        numero = self.text_buscar_numero.text()

        # Validar que los campos no estén vacíos
        if not (numero):
            QMessageBox.warning(self, "Error", "Campo obligatorio.")
            return
        
        habitacion = BD_habitaciones().buscar_habitacion_por_numero(numero)

        if habitacion is None:
            QMessageBox.warning(self, "Advertencia", "No se encontró una habitación con ese número.")
        else:
            # Crear una tabla para mostrar los usuarios
            self.tablaHabitaciones.setRowCount(1)  # Número de filas
            self.tablaHabitaciones.setColumnCount(6)  # 6 columnas: id, nombre, apellido1, apellido2, dni, email

            # Configurar los encabezados de las columnas
            self.tablaHabitaciones.setHorizontalHeaderLabels(["ID, Número", "Precio por Noche","Tipo" , "Disponible"])

            # Llenar la tabla con los datos de los usuarios
            for col, value in enumerate(habitacion):
                self.tablaHabitaciones.setItem(0, col, QTableWidgetItem(str(value)))


    def eliminar_habitacion(self):
        numero = self.textIdDelete.text()

        if not numero.isdigit():
            QMessageBox.warning(self, "Error", "El número ingresado no es válido.")
            return

        bd = BD_habitaciones()
        exito, msg = bd.eliminar_habitacion(int(numero))

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_habitaciones()
        else:
            QMessageBox.warning(self, "Error", msg)

        self.textIdDelete.clear()

    def actualizar_habitacion(self):
        numero = self.textUserID.text()
        disponible = self.textDisponible.text()

        if not (numero.isdigit() and disponible):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios y el número debe ser válido.")
            return

        bd = BD_habitaciones()
        exito, msg = bd.actualizar_habitacion(int(numero), disponible)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_habitaciones()
        else:
            QMessageBox.warning(self, "Error", msg)

    # Generar un informe en PDF con los datos de los clientes
    def generar_informe(self):
        from habitacion_pdf import HabitacionPDF
        pdf = HabitacionPDF()   # Instancia de la clase PDFReport
        pdf.create_pdf()    # Genera el PDF

    def ir_atras(self):
        from window_main import VentanaPrincipal
        self.window_main = VentanaPrincipal()
        self.window_main.show()
        self.hide()

