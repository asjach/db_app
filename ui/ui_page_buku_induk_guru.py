# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_buku_induk_guru.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1048, 618)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tbl_daftar_guru = QTableWidget(Form)
        self.tbl_daftar_guru.setObjectName(u"tbl_daftar_guru")

        self.gridLayout.addWidget(self.tbl_daftar_guru, 1, 0, 1, 6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.btn_save = QPushButton(Form)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.btn_save, 0, 1, 1, 1)

        self.radio_input = QRadioButton(Form)
        self.radio_input.setObjectName(u"radio_input")
        self.radio_input.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.radio_input, 0, 4, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.radio_input.setText(QCoreApplication.translate("Form", u"Mode Input", None))
    # retranslateUi

