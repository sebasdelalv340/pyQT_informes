# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro_user.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 724)
        MainWindow.setMinimumSize(QSize(1050, 680))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 81, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 140, 71, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 210, 71, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 350, 71, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 280, 71, 16))
        self.bt_registrar_cliente = QPushButton(self.centralwidget)
        self.bt_registrar_cliente.setObjectName(u"bt_registrar_cliente")
        self.bt_registrar_cliente.setGeometry(QRect(130, 420, 75, 24))
        self.bt_registrar_cliente.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.textNombre = QLineEdit(self.centralwidget)
        self.textNombre.setObjectName(u"textNombre")
        self.textNombre.setGeometry(QRect(50, 95, 241, 31))
        self.textApellido1 = QLineEdit(self.centralwidget)
        self.textApellido1.setObjectName(u"textApellido1")
        self.textApellido1.setGeometry(QRect(50, 160, 241, 31))
        self.textApellido2 = QLineEdit(self.centralwidget)
        self.textApellido2.setObjectName(u"textApellido2")
        self.textApellido2.setGeometry(QRect(50, 230, 241, 31))
        self.textDNI = QLineEdit(self.centralwidget)
        self.textDNI.setObjectName(u"textDNI")
        self.textDNI.setGeometry(QRect(50, 300, 241, 31))
        self.textEmail = QLineEdit(self.centralwidget)
        self.textEmail.setObjectName(u"textEmail")
        self.textEmail.setGeometry(QRect(50, 370, 241, 31))
        self.bt_mostrar_clientes = QPushButton(self.centralwidget)
        self.bt_mostrar_clientes.setObjectName(u"bt_mostrar_clientes")
        self.bt_mostrar_clientes.setGeometry(QRect(630, 510, 121, 31))
        self.bt_mostrar_clientes.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.tablaClientes = QTableWidget(self.centralwidget)
        self.tablaClientes.setObjectName(u"tablaClientes")
        self.tablaClientes.setEnabled(True)
        self.tablaClientes.setGeometry(QRect(390, 10, 611, 481))
        self.textIdDelete = QLineEdit(self.centralwidget)
        self.textIdDelete.setObjectName(u"textIdDelete")
        self.textIdDelete.setGeometry(QRect(80, 560, 181, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 540, 141, 16))
        self.bt_eliminar_cliente = QPushButton(self.centralwidget)
        self.bt_eliminar_cliente.setObjectName(u"bt_eliminar_cliente")
        self.bt_eliminar_cliente.setGeometry(QRect(130, 600, 75, 24))
        self.bt_eliminar_cliente.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.bt_actualizar_cliente = QPushButton(self.centralwidget)
        self.bt_actualizar_cliente.setObjectName(u"bt_actualizar_cliente")
        self.bt_actualizar_cliente.setGeometry(QRect(130, 460, 75, 24))
        self.bt_actualizar_cliente.setStyleSheet(u"background-color: rgb(255, 170, 0);")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1050, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Apellido 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apellido 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DNI", None))
        self.bt_registrar_cliente.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.bt_mostrar_clientes.setText(QCoreApplication.translate("MainWindow", u"Mostrar usuarios", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Introduce email del cliente", None))
        self.bt_eliminar_cliente.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.bt_actualizar_cliente.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.bt_atras.setText("")
    # retranslateUi

