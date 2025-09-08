# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_ceklis_emis.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(904, 544)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.tbl_ya = QTableWidget(self.widget_2)
        self.tbl_ya.setObjectName(u"tbl_ya")

        self.gridLayout_3.addWidget(self.tbl_ya, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 1, 2, 1, 1)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 30))

        self.gridLayout_4.addWidget(self.pushButton, 0, 4, 1, 1)

        self.cbo_cek = QComboBox(self.widget_3)
        self.cbo_cek.addItem("")
        self.cbo_cek.addItem("")
        self.cbo_cek.setObjectName(u"cbo_cek")

        self.gridLayout_4.addWidget(self.cbo_cek, 0, 1, 1, 1)

        self.btn_show_all = QPushButton(self.widget_3)
        self.btn_show_all.setObjectName(u"btn_show_all")
        self.btn_show_all.setMaximumSize(QSize(30, 16777215))
        self.btn_show_all.setCheckable(True)

        self.gridLayout_4.addWidget(self.btn_show_all, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 3)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.tbl_ya_tidak = QTableWidget(self.widget)
        self.tbl_ya_tidak.setObjectName(u"tbl_ya_tidak")

        self.gridLayout_2.addWidget(self.tbl_ya_tidak, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.tbl_tidak = QTableWidget(self.widget_4)
        self.tbl_tidak.setObjectName(u"tbl_tidak")

        self.gridLayout_5.addWidget(self.tbl_tidak, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_4, 1, 1, 1, 1)


        self.retranslateUi(Form)
        self.btn_show_all.toggled.connect(self.widget.setHidden)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"CEK", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Set Tidak Semua", None))
        self.cbo_cek.setItemText(0, QCoreApplication.translate("Form", u"EMIS", None))
        self.cbo_cek.setItemText(1, QCoreApplication.translate("Form", u"VervalPD", None))

        self.btn_show_all.setText(QCoreApplication.translate("Form", u"<", None))
    # retranslateUi

