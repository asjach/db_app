# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_static_values.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1087, 693)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_simpan = QPushButton(self.widget)
        self.btn_simpan.setObjectName(u"btn_simpan")
        self.btn_simpan.setMinimumSize(QSize(0, 28))

        self.gridLayout.addWidget(self.btn_simpan, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(912, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.btn_batal = QPushButton(self.widget)
        self.btn_batal.setObjectName(u"btn_batal")
        self.btn_batal.setMinimumSize(QSize(0, 28))

        self.gridLayout.addWidget(self.btn_batal, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)

        self.plain_static_values = QPlainTextEdit(Form)
        self.plain_static_values.setObjectName(u"plain_static_values")
        font = QFont()
        font.setFamilies([u"Aptos Display"])
        font.setPointSize(10)
        self.plain_static_values.setFont(font)

        self.gridLayout_2.addWidget(self.plain_static_values, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_simpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btn_batal.setText(QCoreApplication.translate("Form", u"Batal", None))
    # retranslateUi

