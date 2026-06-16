# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_buku_induk.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(854, 653)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cbo_opsi_data = QComboBox(self.widget_2)
        self.cbo_opsi_data.addItem("")
        self.cbo_opsi_data.addItem("")
        self.cbo_opsi_data.addItem("")
        self.cbo_opsi_data.addItem("")
        self.cbo_opsi_data.addItem("")
        self.cbo_opsi_data.addItem("")
        self.cbo_opsi_data.setObjectName(u"cbo_opsi_data")
        self.cbo_opsi_data.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_opsi_data, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tbl_daftar_siswa = QTableWidget(self.widget)
        self.tbl_daftar_siswa.setObjectName(u"tbl_daftar_siswa")

        self.gridLayout_2.addWidget(self.tbl_daftar_siswa, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Opsi Data", None))
        self.cbo_opsi_data.setItemText(0, QCoreApplication.translate("Form", u"Seluruh Siswa Aktif", None))
        self.cbo_opsi_data.setItemText(1, QCoreApplication.translate("Form", u"Siswa MI", None))
        self.cbo_opsi_data.setItemText(2, QCoreApplication.translate("Form", u"Siswa MD", None))
        self.cbo_opsi_data.setItemText(3, QCoreApplication.translate("Form", u"Siswa MI Saja", None))
        self.cbo_opsi_data.setItemText(4, QCoreApplication.translate("Form", u"Siswa MD Saja", None))
        self.cbo_opsi_data.setItemText(5, QCoreApplication.translate("Form", u"Seluruh Siswa", None))

    # retranslateUi

