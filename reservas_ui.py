# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservas.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 724)
        MainWindow.setMinimumSize(QSize(1050, 680))
        MainWindow.setStyleSheet(u"background-color:;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 0, 71, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 100, 111, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 170, 81, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 240, 91, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 40, 71, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 310, 71, 16))
        self.bt_registrar_reserva = QPushButton(self.centralwidget)
        self.bt_registrar_reserva.setObjectName(u"bt_registrar_reserva")
        self.bt_registrar_reserva.setGeometry(QRect(130, 420, 75, 24))
        self.bt_registrar_reserva.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.textNumero_habitacion = QLineEdit(self.centralwidget)
        self.textNumero_habitacion.setObjectName(u"textNumero_habitacion")
        self.textNumero_habitacion.setGeometry(QRect(70, 125, 241, 31))
        self.textEmail = QLineEdit(self.centralwidget)
        self.textEmail.setObjectName(u"textEmail")
        self.textEmail.setGeometry(QRect(70, 60, 241, 31))
        self.bt_mostrar_reservas = QPushButton(self.centralwidget)
        self.bt_mostrar_reservas.setObjectName(u"bt_mostrar_reservas")
        self.bt_mostrar_reservas.setGeometry(QRect(630, 510, 121, 31))
        self.bt_mostrar_reservas.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.tablaReservas = QTableWidget(self.centralwidget)
        self.tablaReservas.setObjectName(u"tablaReservas")
        self.tablaReservas.setEnabled(True)
        self.tablaReservas.setGeometry(QRect(390, 10, 611, 481))
        self.textIdDelete = QLineEdit(self.centralwidget)
        self.textIdDelete.setObjectName(u"textIdDelete")
        self.textIdDelete.setGeometry(QRect(80, 560, 181, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 540, 141, 16))
        self.bt_eliminar_reservas = QPushButton(self.centralwidget)
        self.bt_eliminar_reservas.setObjectName(u"bt_eliminar_reservas")
        self.bt_eliminar_reservas.setGeometry(QRect(130, 600, 75, 24))
        self.bt_eliminar_reservas.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.bt_actualizar_reserva = QPushButton(self.centralwidget)
        self.bt_actualizar_reserva.setObjectName(u"bt_actualizar_reserva")
        self.bt_actualizar_reserva.setGeometry(QRect(130, 460, 75, 24))
        self.bt_actualizar_reserva.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.textUserID = QLineEdit(self.centralwidget)
        self.textUserID.setObjectName(u"textUserID")
        self.textUserID.setGeometry(QRect(240, 460, 61, 31))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 460, 21, 16))
        self.bt_atras = QPushButton(self.centralwidget)
        self.bt_atras.setObjectName(u"bt_atras")
        self.bt_atras.setGeometry(QRect(450, 610, 75, 51))
        icon = QIcon(QIcon.fromTheme(u"go-previous"))
        self.bt_atras.setIcon(icon)
        self.textIdBuscar = QLineEdit(self.centralwidget)
        self.textIdBuscar.setObjectName(u"textIdBuscar")
        self.textIdBuscar.setGeometry(QRect(790, 560, 181, 31))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(810, 540, 141, 16))
        self.bt_buscar_reserva = QPushButton(self.centralwidget)
        self.bt_buscar_reserva.setObjectName(u"bt_buscar_reserva")
        self.bt_buscar_reserva.setGeometry(QRect(840, 600, 75, 24))
        self.bt_buscar_reserva.setStyleSheet(u"background-color: rgb(170, 0, 255);")
        self.checkIn = QDateEdit(self.centralwidget)
        self.checkIn.setObjectName(u"checkIn")
        self.checkIn.setGeometry(QRect(70, 200, 241, 31))
        self.checkIn.setMaximumDateTime(QDateTime(QDate(2035, 12, 31), QTime(22, 59, 59)))
        self.checkIn.setMinimumDateTime(QDateTime(QDate(2025, 3, 15), QTime(0, 0, 0)))
        self.checkOut = QDateEdit(self.centralwidget)
        self.checkOut.setObjectName(u"checkOut")
        self.checkOut.setGeometry(QRect(70, 270, 241, 31))
        self.checkOut.setMaximumDateTime(QDateTime(QDate(2035, 12, 31), QTime(22, 59, 59)))
        self.checkOut.setMinimumDateTime(QDateTime(QDate(2025, 3, 15), QTime(0, 0, 0)))
        self.comboEstado = QComboBox(self.centralwidget)
        self.comboEstado.addItem("")
        self.comboEstado.addItem("")
        self.comboEstado.addItem("")
        self.comboEstado.addItem("")
        self.comboEstado.setObjectName(u"comboEstado")
        self.comboEstado.setGeometry(QRect(70, 340, 81, 22))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reservas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Numero habitacion", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fecha checkin", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"fecha_checkout", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
        self.bt_registrar_reserva.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.bt_mostrar_reservas.setText(QCoreApplication.translate("MainWindow", u"Mostrar Reservas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Introduce email del cliente", None))
        self.bt_eliminar_reservas.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.bt_actualizar_reserva.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.bt_atras.setText("")
        self.textIdBuscar.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Introduce email del cliente", None))
        self.bt_buscar_reserva.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.comboEstado.setItemText(0, QCoreApplication.translate("MainWindow", u"Pendiente", None))
        self.comboEstado.setItemText(1, QCoreApplication.translate("MainWindow", u"Confirmada", None))
        self.comboEstado.setItemText(2, QCoreApplication.translate("MainWindow", u"Cancelada", None))
        self.comboEstado.setItemText(3, QCoreApplication.translate("MainWindow", u"Finalizada", None))

    # retranslateUi

