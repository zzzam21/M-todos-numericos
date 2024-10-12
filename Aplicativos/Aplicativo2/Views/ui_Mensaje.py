# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MensajeZpifcu.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from .Images import imagenes

class Ui_Error(object):
    def setupUi(self, Error):
        if not Error.objectName():
            Error.setObjectName(u"Error")
        Error.resize(400, 324)
        Error.setMinimumSize(QSize(400, 324))
        Error.setMaximumSize(QSize(400, 324))
        icon = QIcon()
        icon.addFile(u":/Metodos/ErrorIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        Error.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Error)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Error)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel {\n"
"	font: 300 11pt \"Segoe UI\";\n"
"}\n"
"QPushButton {\n"
"	border-radius: 10px; \n"
"	font: 700 10pt \"Segoe UI\";\n"
"	background-color: rgb(237, 201, 44);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	 border-radius: 10px; \n"
"	background-color: rgb(255, 219, 15);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lb_imagenError = QLabel(self.frame)
        self.lb_imagenError.setObjectName(u"lb_imagenError")
        self.lb_imagenError.setMinimumSize(QSize(100, 100))
        self.lb_imagenError.setMaximumSize(QSize(100, 100))
        self.lb_imagenError.setPixmap(QPixmap(u":/Metodos/error.png"))
        self.lb_imagenError.setScaledContents(True)

        self.horizontalLayout.addWidget(self.lb_imagenError)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.lb_error = QLabel(self.frame)
        self.lb_error.setObjectName(u"lb_error")
        self.lb_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_error)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.pb_reintentar = QPushButton(self.frame)
        self.pb_reintentar.setObjectName(u"pb_reintentar")
        self.pb_reintentar.setMinimumSize(QSize(130, 40))
        self.pb_reintentar.setMaximumSize(QSize(130, 40))

        self.horizontalLayout_2.addWidget(self.pb_reintentar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Error)

        QMetaObject.connectSlotsByName(Error)
    # setupUi

    def retranslateUi(self, Error):
        Error.setWindowTitle(QCoreApplication.translate("Error", u"Error", None))
        self.lb_imagenError.setText("")
        self.lb_error.setText(QCoreApplication.translate("Error", u"Espacios sin llenar!", None))
        self.pb_reintentar.setText(QCoreApplication.translate("Error", u"Reintentar", None))
    # retranslateUi

