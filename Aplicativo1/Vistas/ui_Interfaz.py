# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfazoQQRWa.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
from .Imagenes import img

class Ui_Aplicativo1(object):
    def setupUi(self, Aplicativo1):
        if not Aplicativo1.objectName():
            Aplicativo1.setObjectName(u"Aplicativo1")
        Aplicativo1.resize(800, 601)
        Aplicativo1.setMaximumSize(QSize(800, 601))
        icon = QIcon()
        icon.addFile(u":/Aplicativo/Icono_Aplicativo.png", QSize(), QIcon.Normal, QIcon.Off)
        Aplicativo1.setWindowIcon(icon)
        self.centralwidget = QWidget(Aplicativo1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_izquierda = QFrame(self.centralwidget)
        self.fr_izquierda.setObjectName(u"fr_izquierda")
        self.fr_izquierda.setFrameShape(QFrame.StyledPanel)
        self.fr_izquierda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_izquierda)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.fr_izquierda)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_logo = QLabel(self.frame_4)
        self.lb_logo.setObjectName(u"lb_logo")
        self.lb_logo.setMinimumSize(QSize(350, 125))
        self.lb_logo.setMaximumSize(QSize(350, 125))
        self.lb_logo.setPixmap(QPixmap(u":/Aplicativo/Banner.jpg"))
        self.lb_logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.lb_logo)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.fr_izquierda)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 50, -1, 50)
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-radius: 40px;\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lb_titulo = QLabel(self.frame)
        self.lb_titulo.setObjectName(u"lb_titulo")
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(16)
        font.setBold(True)
        self.lb_titulo.setFont(font)
        self.lb_titulo.setStyleSheet(u"background-color: none;")
        self.lb_titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lb_titulo)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 300))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 50, 20, 50)
        self.lb_ncs = QLabel(self.frame_2)
        self.lb_ncs.setObjectName(u"lb_ncs")
        self.lb_ncs.setMinimumSize(QSize(0, 25))
        self.lb_ncs.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setBold(True)
        self.lb_ncs.setFont(font1)

        self.verticalLayout_7.addWidget(self.lb_ncs)

        self.le_ncs = QLineEdit(self.frame_2)
        self.le_ncs.setObjectName(u"le_ncs")

        self.verticalLayout_7.addWidget(self.le_ncs)

        self.lb_x = QLabel(self.frame_2)
        self.lb_x.setObjectName(u"lb_x")
        self.lb_x.setMinimumSize(QSize(0, 25))
        self.lb_x.setMaximumSize(QSize(16777215, 25))
        self.lb_x.setFont(font1)

        self.verticalLayout_7.addWidget(self.lb_x)

        self.le_x = QLineEdit(self.frame_2)
        self.le_x.setObjectName(u"le_x")

        self.verticalLayout_7.addWidget(self.le_x)

        self.lb_selfun = QLabel(self.frame_2)
        self.lb_selfun.setObjectName(u"lb_selfun")
        self.lb_selfun.setMinimumSize(QSize(0, 25))
        self.lb_selfun.setMaximumSize(QSize(16777215, 25))
        self.lb_selfun.setFont(font1)

        self.verticalLayout_7.addWidget(self.lb_selfun)

        self.cb_selfun = QComboBox(self.frame_2)
        self.cb_selfun.addItem("")
        self.cb_selfun.addItem("")
        self.cb_selfun.setObjectName(u"cb_selfun")

        self.verticalLayout_7.addWidget(self.cb_selfun)


        self.verticalLayout_6.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 10)

        self.horizontalLayout.addWidget(self.fr_izquierda)

        self.fr_derecha = QFrame(self.centralwidget)
        self.fr_derecha.setObjectName(u"fr_derecha")
        self.fr_derecha.setFrameShape(QFrame.StyledPanel)
        self.fr_derecha.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.fr_derecha)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.fr_derecha)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_criterioError = QLabel(self.frame_6)
        self.lb_criterioError.setObjectName(u"lb_criterioError")
        self.lb_criterioError.setFont(font1)
        self.lb_criterioError.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_criterioError)

        self.tv_datos = QTableView(self.frame_6)
        self.tv_datos.setObjectName(u"tv_datos")

        self.verticalLayout_2.addWidget(self.tv_datos)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.fr_botones = QFrame(self.fr_derecha)
        self.fr_botones.setObjectName(u"fr_botones")
        self.fr_botones.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(75, 211, 123);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QFrame {\n"
"	border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.fr_botones.setFrameShape(QFrame.StyledPanel)
        self.fr_botones.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_botones)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_limpiar = QPushButton(self.fr_botones)
        self.pb_limpiar.setObjectName(u"pb_limpiar")
        self.pb_limpiar.setMinimumSize(QSize(0, 30))
        self.pb_limpiar.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(132, 182, 244);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(113, 156, 208);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Aplicativo/escoba.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_limpiar.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pb_limpiar)

        self.pb_calcular = QPushButton(self.fr_botones)
        self.pb_calcular.setObjectName(u"pb_calcular")
        self.pb_calcular.setMinimumSize(QSize(0, 30))
        self.pb_calcular.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(68, 190, 111);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Aplicativo/icons8-comprobado-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_calcular.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pb_calcular)


        self.verticalLayout_5.addWidget(self.fr_botones)

        self.verticalLayout_5.setStretch(0, 9)
        self.verticalLayout_5.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.fr_derecha)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 8)
        Aplicativo1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Aplicativo1)

        QMetaObject.connectSlotsByName(Aplicativo1)
    # setupUi

    def retranslateUi(self, Aplicativo1):
        Aplicativo1.setWindowTitle(QCoreApplication.translate("Aplicativo1", u"Aplicativo 1", None))
        self.lb_logo.setText("")
        self.lb_titulo.setText(QCoreApplication.translate("Aplicativo1", u"PARAMETROS", None))
        self.lb_ncs.setText(QCoreApplication.translate("Aplicativo1", u"Numero de cifras cignificativas:", None))
        self.lb_x.setText(QCoreApplication.translate("Aplicativo1", u"Valor de X:", None))
        self.lb_selfun.setText(QCoreApplication.translate("Aplicativo1", u"Selecci\u00f3ne una funci\u00f3n:", None))
        self.cb_selfun.setItemText(0, QCoreApplication.translate("Aplicativo1", u"Sen(x)", None))
        self.cb_selfun.setItemText(1, QCoreApplication.translate("Aplicativo1", u"Cos(X)", None))

        self.lb_criterioError.setText(QCoreApplication.translate("Aplicativo1", u"Criterio de error (Es): ", None))
        self.pb_limpiar.setText(QCoreApplication.translate("Aplicativo1", u"Limpiar", None))
        self.pb_calcular.setText(QCoreApplication.translate("Aplicativo1", u"Calcular", None))
    # retranslateUi

