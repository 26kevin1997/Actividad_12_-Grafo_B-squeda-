# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(681, 522)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ide_lineEdit = QLineEdit(self.groupBox)
        self.ide_lineEdit.setObjectName(u"ide_lineEdit")

        self.gridLayout.addWidget(self.ide_lineEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.red_spinBox_7 = QSpinBox(self.groupBox)
        self.red_spinBox_7.setObjectName(u"red_spinBox_7")
        self.red_spinBox_7.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox_7, 7, 1, 1, 1)

        self.blue_spinBox_9 = QSpinBox(self.groupBox)
        self.blue_spinBox_9.setObjectName(u"blue_spinBox_9")
        self.blue_spinBox_9.setMaximum(255)

        self.gridLayout.addWidget(self.blue_spinBox_9, 9, 1, 1, 1)

        self.green_spinBox_8 = QSpinBox(self.groupBox)
        self.green_spinBox_8.setObjectName(u"green_spinBox_8")
        self.green_spinBox_8.setMaximum(255)

        self.gridLayout.addWidget(self.green_spinBox_8, 8, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.origeny_spinBox_3 = QSpinBox(self.groupBox)
        self.origeny_spinBox_3.setObjectName(u"origeny_spinBox_3")
        self.origeny_spinBox_3.setMaximum(500)

        self.gridLayout.addWidget(self.origeny_spinBox_3, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.agregarinicio_pushButton = QPushButton(self.groupBox)
        self.agregarinicio_pushButton.setObjectName(u"agregarinicio_pushButton")

        self.gridLayout.addWidget(self.agregarinicio_pushButton, 11, 0, 1, 2)

        self.velocidad_lineEdit_2 = QLineEdit(self.groupBox)
        self.velocidad_lineEdit_2.setObjectName(u"velocidad_lineEdit_2")

        self.gridLayout.addWidget(self.velocidad_lineEdit_2, 5, 1, 1, 1)

        self.origenx_spinBox_2 = QSpinBox(self.groupBox)
        self.origenx_spinBox_2.setObjectName(u"origenx_spinBox_2")
        self.origenx_spinBox_2.setMaximum(500)

        self.gridLayout.addWidget(self.origenx_spinBox_2, 1, 1, 1, 1)

        self.destinoy_spinBox_5 = QSpinBox(self.groupBox)
        self.destinoy_spinBox_5.setObjectName(u"destinoy_spinBox_5")
        self.destinoy_spinBox_5.setMaximum(500)

        self.gridLayout.addWidget(self.destinoy_spinBox_5, 4, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 12, 0, 1, 2)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.agregarfinal_pushButton = QPushButton(self.groupBox)
        self.agregarfinal_pushButton.setObjectName(u"agregarfinal_pushButton")

        self.gridLayout.addWidget(self.agregarfinal_pushButton, 10, 0, 1, 2)

        self.destinox_spinBox_4 = QSpinBox(self.groupBox)
        self.destinox_spinBox_4.setObjectName(u"destinox_spinBox_4")
        self.destinox_spinBox_4.setMaximum(500)

        self.gridLayout.addWidget(self.destinox_spinBox_4, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.velocidad_boton_orde = QPushButton(self.tab_4)
        self.velocidad_boton_orde.setObjectName(u"velocidad_boton_orde")

        self.gridLayout_4.addWidget(self.velocidad_boton_orde, 2, 3, 1, 1)

        self.buscar_lineEdit = QLineEdit(self.tab_4)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.tabla = QTableWidget(self.tab_4)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 4)

        self.id_botonorde = QPushButton(self.tab_4)
        self.id_botonorde.setObjectName(u"id_botonorde")

        self.gridLayout_4.addWidget(self.id_botonorde, 2, 1, 1, 1)

        self.buscar_pushButton_2 = QPushButton(self.tab_4)
        self.buscar_pushButton_2.setObjectName(u"buscar_pushButton_2")

        self.gridLayout_4.addWidget(self.buscar_pushButton_2, 1, 1, 1, 1)

        self.distancia_botonorde = QPushButton(self.tab_4)
        self.distancia_botonorde.setObjectName(u"distancia_botonorde")

        self.gridLayout_4.addWidget(self.distancia_botonorde, 2, 2, 1, 1)

        self.mostrar__tabla_pushButton_3 = QPushButton(self.tab_4)
        self.mostrar__tabla_pushButton_3.setObjectName(u"mostrar__tabla_pushButton_3")

        self.gridLayout_4.addWidget(self.mostrar__tabla_pushButton_3, 1, 2, 1, 2)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.dibujar = QPushButton(self.tab)
        self.dibujar.setObjectName(u"dibujar")
        self.dibujar.setGeometry(QRect(480, 280, 75, 23))
        self.limpiar = QPushButton(self.tab)
        self.limpiar.setObjectName(u"limpiar")
        self.limpiar.setGeometry(QRect(570, 280, 75, 23))
        self.graphicsView = QGraphicsView(self.tab)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(9, 9, 631, 261))
        self.grafos_plainTextEdit_2 = QPlainTextEdit(self.tab)
        self.grafos_plainTextEdit_2.setObjectName(u"grafos_plainTextEdit_2")
        self.grafos_plainTextEdit_2.setGeometry(QRect(10, 280, 256, 151))
        self.grafos_pushButton_2 = QPushButton(self.tab)
        self.grafos_pushButton_2.setObjectName(u"grafos_pushButton_2")
        self.grafos_pushButton_2.setGeometry(QRect(280, 280, 80, 23))
        self.busqueda_pushButton_2 = QPushButton(self.tab)
        self.busqueda_pushButton_2.setObjectName(u"busqueda_pushButton_2")
        self.busqueda_pushButton_2.setGeometry(QRect(460, 360, 111, 31))
        self.xbus_spinBox = QSpinBox(self.tab)
        self.xbus_spinBox.setObjectName(u"xbus_spinBox")
        self.xbus_spinBox.setGeometry(QRect(290, 400, 71, 22))
        self.xbus_spinBox.setMaximum(1000)
        self.ybus_spinBox_2 = QSpinBox(self.tab)
        self.ybus_spinBox_2.setObjectName(u"ybus_spinBox_2")
        self.ybus_spinBox_2.setGeometry(QRect(370, 400, 71, 22))
        self.ybus_spinBox_2.setMaximum(1000)
        self.buspro_pushButton_2 = QPushButton(self.tab)
        self.buspro_pushButton_2.setObjectName(u"buspro_pushButton_2")
        self.buspro_pushButton_2.setGeometry(QRect(460, 400, 111, 31))
        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 681, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en X", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color (RGB)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en Y", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.agregarinicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.agregarfinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.velocidad_boton_orde.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id ", None))
        self.id_botonorde.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.buscar_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.distancia_botonorde.setText(QCoreApplication.translate("MainWindow", u"Distancia", None))
        self.mostrar__tabla_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.grafos_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar Grafos", None))
        self.busqueda_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Busqueda amplitud ", None))
        self.buspro_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Busqueda profundida", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Grafica", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

