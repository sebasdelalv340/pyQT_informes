from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
from bd_pagos import BD_pagos
import os

class VentanaPagos(QMainWindow):
    def __init__(self):
        super(VentanaPagos, self).__init__()
        ui_file = os.path.join(os.path.dirname(__file__), "pagos.ui")


        uic.loadUi(ui_file, self)
        self.setWindowTitle("Registro de Pagos")

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
        self.bt_registrar_pago.clicked.connect(self.registrar_pago)
        self.bt_mostrar_pagos.clicked.connect(self.mostrar_pagos)
        self.bt_buscar_pago.clicked.connect(self.buscar_pago)
        self.bt_eliminar_pago.clicked.connect(self.eliminar_pago)
        self.bt_actualizar_pago.clicked.connect(self.actualizar_pago)
        self.bt_atras.clicked.connect(self.ir_atras)
        self.bt_informe.clicked.connect(self.generar_informe)

    # Métodos de la clase
    def registrar_pago(self):
        id_reserva = self.textIdReserva.text()
        monto = self.textMonto.text()
        metodo_pago = self.comboMetodo_pago.currentText()
        fecha_pago = QDateTime.currentDateTime().toString("yyyy-MM-dd")

        if not (id_reserva and monto and metodo_pago):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        
        bd = BD_pagos()
        exito, msg = bd.insertar_pago(None, id_reserva, monto, metodo_pago, fecha_pago)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.textIdReserva.clear()
            self.textMonto.clear()
            self.comboMetodo_pago.setCurrentIndex(0)
        else:
            QMessageBox.warning(self, "Error", msg)

    def mostrar_pagos(self):
        pagos = BD_pagos().obtener_pagos()

        if len(pagos) == 0:
            self.tablaPagos.setRowCount(0)
            QMessageBox.warning(self, "Advertencia", "No hay pagos registrados.")
        else:
            self.tablaPagos.setRowCount(len(pagos))
            self.tablaPagos.setColumnCount(5)
            self.tablaPagos.setHorizontalHeaderLabels(["ID", "Reserva", "Monto", "Método de Pago", "Fecha"])

            for row, pago in enumerate(pagos):
                for col, value in enumerate(pago):
                    self.tablaPagos.setItem(row, col, QTableWidgetItem(str(value)))

    def buscar_pago(self):
        email = self.text_email.cliente.text()

        # Validar que los campos no estén vacíos
        if not (email):
            QMessageBox.warning(self, "Error", "Campo obligatorio.")
            return
        
        pagos = BD_pagos().buscar_pagos_por_email(email)

        if len(pagos) == 0:
            QMessageBox.warning(self, "Advertencia", "No hay pagos registrados.")
        else:
            self.tablaPagos.setRowCount(len(pagos))
            self.tablaPagos.setColumnCount(5)
            self.tablaPagos.setHorizontalHeaderLabels(["ID", "Reserva", "Monto", "Método de Pago", "Fecha"])

            for row, pago in enumerate(pagos):
                for col, value in enumerate(pago):
                    self.tablaPagos.setItem(row, col, QTableWidgetItem(str(value)))

    def eliminar_pago(self):
        id_pago = self.textIdDelete.text()

        if not id_pago.isdigit():
            QMessageBox.warning(self, "Error", "El ID del pago ingresado no es válido.")
            return

        bd = BD_pagos()
        exito, msg = bd.eliminar_pago(int(id_pago))

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_pagos()
        else:
            QMessageBox.warning(self, "Error", msg)

        self.textIdDelete.clear()

    def actualizar_pago(self):
        id_pago = self.textUserID.text()
        id_reserva = self.textIdReserva.text()
        monto = self.textMonto.text()
        metodo_pago = self.comboMetodo_pago.currentText()
        fecha_pago = QDateTime.currentDateTime().toString("yyyy-MM-dd")

        if not (id_pago and id_reserva and monto and metodo_pago):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        bd = BD_pagos()
        exito, msg = bd.actualizar_pago(int(id_pago), id_reserva, monto, metodo_pago, fecha_pago)

        if exito:
            QMessageBox.information(self, "Éxito", msg)
            self.mostrar_pagos()
        else:
            QMessageBox.warning(self, "Error", msg)

    # Generar un informe en PDF con los datos de los pagos
    def generar_informe(self):
        from pago_pdf import PagoPDF
        pdf = PagoPDF()   # Instancia de la clase PDFReport
        pdf.create_pdf()    # Genera el PDF

    def ir_atras(self):
        from window_main import VentanaPrincipal
        self.window_main = VentanaPrincipal()
        self.window_main.show()
        self.hide()