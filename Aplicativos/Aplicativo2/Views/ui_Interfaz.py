# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfazvKyFGA.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from .Images import imagenes

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(834, 600)
        icon = QIcon()
        icon.addFile(u":/Metodos/icono.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #ffffff; /* Blanco */\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #4CAF50; /* Verde claro */\n"
"    color: #ffffff; /* Texto blanco */\n"
"    border: 2px solid #388E3C; /* Verde oscuro */\n"
"    border-radius: 5px;\n"
"    padding: 8px 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #388E3C; /* Verde oscuro al pasar el rat\u00f3n */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #9dff75; /* Amarillo al presionar */\n"
"    color: #000000; /* Texto negro */\n"
"}\n"
"\n"
"/* Line Edits (cajas de texto) */\n"
"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    color: #4CAF50; /* Texto en verde claro */\n"
"    border: 2px solid #388E3C; /* Borde verde oscuro */\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    color: #4CAF50; /* Texto en verde claro */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Tablas */\n"
"QTableWidget"
                        " {\n"
"    background-color: #ffffff; /* Fondo blanco */\n"
"    color: #4CAF50; /* Texto verde claro */\n"
"    border: 2px solid #388E3C; /* Borde verde oscuro */\n"
"    gridline-color: #388E3C; /* L\u00edneas de la tabla verde oscuro */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #388E3C; /* Verde oscuro para los encabezados */\n"
"    color: #ffffff; /* Texto blanco */\n"
"    padding: 5px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(300, 0))
        self.widget_9.setMaximumSize(QSize(300, 16777215))
        self.widget_9.setSizeIncrement(QSize(0, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_Titulo = QLabel(self.widget_9)
        self.lb_Titulo.setObjectName(u"lb_Titulo")
        self.lb_Titulo.setStyleSheet(u"font-size:20px;")

        self.horizontalLayout_5.addWidget(self.lb_Titulo, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pb_p1 = QPushButton(self.widget_10)
        self.pb_p1.setObjectName(u"pb_p1")

        self.horizontalLayout_4.addWidget(self.pb_p1)

        self.pb_p2 = QPushButton(self.widget_10)
        self.pb_p2.setObjectName(u"pb_p2")

        self.horizontalLayout_4.addWidget(self.pb_p2)

        self.pb_p3 = QPushButton(self.widget_10)
        self.pb_p3.setObjectName(u"pb_p3")

        self.horizontalLayout_4.addWidget(self.pb_p3)


        self.horizontalLayout_3.addWidget(self.widget_10)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.punto1 = QWidget()
        self.punto1.setObjectName(u"punto1")
        self.verticalLayout_3 = QVBoxLayout(self.punto1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_4 = QWidget(self.punto1)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 45))
        self.widget_4.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(300, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_Xip1 = QLabel(self.widget_8)
        self.lb_Xip1.setObjectName(u"lb_Xip1")

        self.horizontalLayout_8.addWidget(self.lb_Xip1)

        self.le_xip1 = QLineEdit(self.widget_8)
        self.le_xip1.setObjectName(u"le_xip1")

        self.horizontalLayout_8.addWidget(self.le_xip1)

        self.lb_Xsp2 = QLabel(self.widget_8)
        self.lb_Xsp2.setObjectName(u"lb_Xsp2")

        self.horizontalLayout_8.addWidget(self.lb_Xsp2)

        self.le_xsp1 = QLineEdit(self.widget_8)
        self.le_xsp1.setObjectName(u"le_xsp1")

        self.horizontalLayout_8.addWidget(self.le_xsp1)

        self.pb_calcp1 = QPushButton(self.widget_8)
        self.pb_calcp1.setObjectName(u"pb_calcp1")
        self.pb_calcp1.setMinimumSize(QSize(0, 30))
        self.pb_calcp1.setMaximumSize(QSize(16777215, 30))
        self.pb_calcp1.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.pb_calcp1)


        self.horizontalLayout_2.addWidget(self.widget_8)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.punto1)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tw_bisecp1 = QTableWidget(self.widget_5)
        if (self.tw_bisecp1.columnCount() < 6):
            self.tw_bisecp1.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_bisecp1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_bisecp1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_bisecp1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_bisecp1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_bisecp1.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_bisecp1.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tw_bisecp1.setObjectName(u"tw_bisecp1")

        self.verticalLayout_5.addWidget(self.tw_bisecp1)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tw_fpP1 = QTableWidget(self.widget_6)
        if (self.tw_fpP1.columnCount() < 7):
            self.tw_fpP1.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_fpP1.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_fpP1.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_fpP1.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_fpP1.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_fpP1.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_fpP1.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_fpP1.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.tw_fpP1.setObjectName(u"tw_fpP1")

        self.verticalLayout_6.addWidget(self.tw_fpP1)


        self.horizontalLayout.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.punto1)
        self.punto2 = QWidget()
        self.punto2.setObjectName(u"punto2")
        self.verticalLayout_7 = QVBoxLayout(self.punto2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.punto2)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.widget_11)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.le_xp2 = QLineEdit(self.widget_11)
        self.le_xp2.setObjectName(u"le_xp2")

        self.horizontalLayout_6.addWidget(self.le_xp2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.pb_calcp2 = QPushButton(self.widget_11)
        self.pb_calcp2.setObjectName(u"pb_calcp2")

        self.horizontalLayout_6.addWidget(self.pb_calcp2)


        self.verticalLayout_7.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.punto2)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_8 = QVBoxLayout(self.widget_12)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tw_p2 = QTableWidget(self.widget_12)
        if (self.tw_p2.columnCount() < 5):
            self.tw_p2.setColumnCount(5)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_p2.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_p2.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_p2.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tw_p2.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tw_p2.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        self.tw_p2.setObjectName(u"tw_p2")

        self.verticalLayout_8.addWidget(self.tw_p2)


        self.verticalLayout_7.addWidget(self.widget_12)

        self.stackedWidget.addWidget(self.punto2)
        self.punto3 = QWidget()
        self.punto3.setObjectName(u"punto3")
        self.verticalLayout_9 = QVBoxLayout(self.punto3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.punto3)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 50))
        self.widget_13.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.widget_13)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.le_xp3 = QLineEdit(self.widget_13)
        self.le_xp3.setObjectName(u"le_xp3")

        self.horizontalLayout_7.addWidget(self.le_xp3)

        self.label_3 = QLabel(self.widget_13)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.le_xip3 = QLineEdit(self.widget_13)
        self.le_xip3.setObjectName(u"le_xip3")

        self.horizontalLayout_7.addWidget(self.le_xip3)

        self.label_4 = QLabel(self.widget_13)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.le_xsp3 = QLineEdit(self.widget_13)
        self.le_xsp3.setObjectName(u"le_xsp3")

        self.horizontalLayout_7.addWidget(self.le_xsp3)

        self.pb_calcp3 = QPushButton(self.widget_13)
        self.pb_calcp3.setObjectName(u"pb_calcp3")

        self.horizontalLayout_7.addWidget(self.pb_calcp3)


        self.verticalLayout_9.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.punto3)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout = QGridLayout(self.widget_14)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(400, 237))
        self.widget_16.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.widget_16)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.widget_16)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_11.addWidget(self.label_6)

        self.tw_Fsp3 = QTableWidget(self.widget_16)
        if (self.tw_Fsp3.columnCount() < 7):
            self.tw_Fsp3.setColumnCount(7)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tw_Fsp3.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tw_Fsp3.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tw_Fsp3.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tw_Fsp3.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tw_Fsp3.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tw_Fsp3.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tw_Fsp3.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        self.tw_Fsp3.setObjectName(u"tw_Fsp3")

        self.verticalLayout_11.addWidget(self.tw_Fsp3)


        self.gridLayout.addWidget(self.widget_16, 0, 1, 1, 1)

        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(400, 237))
        self.widget_15.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.widget_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.widget_15)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_10.addWidget(self.label_5)

        self.tw_BisecP3 = QTableWidget(self.widget_15)
        if (self.tw_BisecP3.columnCount() < 6):
            self.tw_BisecP3.setColumnCount(6)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tw_BisecP3.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tw_BisecP3.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tw_BisecP3.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tw_BisecP3.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tw_BisecP3.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tw_BisecP3.setHorizontalHeaderItem(5, __qtablewidgetitem30)
        self.tw_BisecP3.setObjectName(u"tw_BisecP3")

        self.verticalLayout_10.addWidget(self.tw_BisecP3)


        self.gridLayout.addWidget(self.widget_15, 0, 0, 1, 1)

        self.widget_18 = QWidget(self.widget_14)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.widget_18)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.widget_18)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_13.addWidget(self.label_8)

        self.tw_NRP3 = QTableWidget(self.widget_18)
        if (self.tw_NRP3.columnCount() < 5):
            self.tw_NRP3.setColumnCount(5)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tw_NRP3.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tw_NRP3.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tw_NRP3.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tw_NRP3.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tw_NRP3.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        self.tw_NRP3.setObjectName(u"tw_NRP3")

        self.verticalLayout_13.addWidget(self.tw_NRP3)


        self.gridLayout.addWidget(self.widget_18, 1, 1, 1, 1)

        self.widget_17 = QWidget(self.widget_14)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_12 = QVBoxLayout(self.widget_17)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.widget_17)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_12.addWidget(self.label_7)

        self.tw_secP3 = QTableWidget(self.widget_17)
        if (self.tw_secP3.columnCount() < 6):
            self.tw_secP3.setColumnCount(6)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tw_secP3.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tw_secP3.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tw_secP3.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tw_secP3.setHorizontalHeaderItem(3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tw_secP3.setHorizontalHeaderItem(4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tw_secP3.setHorizontalHeaderItem(5, __qtablewidgetitem41)
        self.tw_secP3.setObjectName(u"tw_secP3")

        self.verticalLayout_12.addWidget(self.tw_secP3)


        self.gridLayout.addWidget(self.widget_17, 1, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_14)

        self.stackedWidget.addWidget(self.punto3)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metodos num\u00e9ricos", None))
        self.lb_Titulo.setText("")
        self.pb_p1.setText(QCoreApplication.translate("MainWindow", u"Punto 1", None))
        self.pb_p2.setText(QCoreApplication.translate("MainWindow", u"Punto 2", None))
        self.pb_p3.setText(QCoreApplication.translate("MainWindow", u"Punto3", None))
        self.lb_Xip1.setText(QCoreApplication.translate("MainWindow", u"Xi:", None))
        self.le_xip1.setText("")
        self.lb_Xsp2.setText(QCoreApplication.translate("MainWindow", u"Xs:", None))
        self.pb_calcp1.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        ___qtablewidgetitem = self.tw_bisecp1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Xi", None));
        ___qtablewidgetitem1 = self.tw_bisecp1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Xs", None));
        ___qtablewidgetitem2 = self.tw_bisecp1.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Xr", None));
        ___qtablewidgetitem3 = self.tw_bisecp1.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"F(Xi)", None));
        ___qtablewidgetitem4 = self.tw_bisecp1.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"F(Xr)", None));
        ___qtablewidgetitem5 = self.tw_bisecp1.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"E%", None));
        ___qtablewidgetitem6 = self.tw_fpP1.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Xi", None));
        ___qtablewidgetitem7 = self.tw_fpP1.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Xs", None));
        ___qtablewidgetitem8 = self.tw_fpP1.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Xr", None));
        ___qtablewidgetitem9 = self.tw_fpP1.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"F(Xi)", None));
        ___qtablewidgetitem10 = self.tw_fpP1.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"F(Xs)", None));
        ___qtablewidgetitem11 = self.tw_fpP1.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"F(Xr)", None));
        ___qtablewidgetitem12 = self.tw_fpP1.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"E%", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pb_calcp2.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        ___qtablewidgetitem13 = self.tw_p2.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Xi", None));
        ___qtablewidgetitem14 = self.tw_p2.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Xn+1", None));
        ___qtablewidgetitem15 = self.tw_p2.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"F(Xi)", None));
        ___qtablewidgetitem16 = self.tw_p2.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"F'(Xi)", None));
        ___qtablewidgetitem17 = self.tw_p2.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"E%", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Xi", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Xs", None))
        self.pb_calcp3.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"M. Falsa posici\u00f3n", None))
        ___qtablewidgetitem18 = self.tw_Fsp3.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Xi", None));
        ___qtablewidgetitem19 = self.tw_Fsp3.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Xs", None));
        ___qtablewidgetitem20 = self.tw_Fsp3.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Xr", None));
        ___qtablewidgetitem21 = self.tw_Fsp3.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"F(Xi)", None));
        ___qtablewidgetitem22 = self.tw_Fsp3.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"F(Xs)", None));
        ___qtablewidgetitem23 = self.tw_Fsp3.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"F(Xr)", None));
        ___qtablewidgetitem24 = self.tw_Fsp3.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"E%", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"M. Bisecci\u00f3n", None))
        ___qtablewidgetitem25 = self.tw_BisecP3.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Xi", None));
        ___qtablewidgetitem26 = self.tw_BisecP3.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Xs", None));
        ___qtablewidgetitem27 = self.tw_BisecP3.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Xr", None));
        ___qtablewidgetitem28 = self.tw_BisecP3.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"F(Xi)", None));
        ___qtablewidgetitem29 = self.tw_BisecP3.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"F(Xr)", None));
        ___qtablewidgetitem30 = self.tw_BisecP3.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"E%", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"M. de Newthon-Raphson", None))
        ___qtablewidgetitem31 = self.tw_NRP3.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Xi", None));
        ___qtablewidgetitem32 = self.tw_NRP3.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Xn+1", None));
        ___qtablewidgetitem33 = self.tw_NRP3.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"F(Xi)", None));
        ___qtablewidgetitem34 = self.tw_NRP3.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"F'(Xi)", None));
        ___qtablewidgetitem35 = self.tw_NRP3.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"E%", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"M. de la secante", None))
        ___qtablewidgetitem36 = self.tw_secP3.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Xi-1", None));
        ___qtablewidgetitem37 = self.tw_secP3.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Xi", None));
        ___qtablewidgetitem38 = self.tw_secP3.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Xi+1", None));
        ___qtablewidgetitem39 = self.tw_secP3.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"F(Xi-1)", None));
        ___qtablewidgetitem40 = self.tw_secP3.horizontalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"F(Xi)", None));
        ___qtablewidgetitem41 = self.tw_secP3.horizontalHeaderItem(5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"E%", None));
    # retranslateUi

