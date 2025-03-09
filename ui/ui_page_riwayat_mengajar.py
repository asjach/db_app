# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_riwayat_mengajar.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1032, 537)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)

        self.tbl_riwayat_mengajar = QTableWidget(self.widget)
        self.tbl_riwayat_mengajar.setObjectName(u"tbl_riwayat_mengajar")
        self.tbl_riwayat_mengajar.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tbl_riwayat_mengajar, 2, 0, 1, 8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 6, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.cbo_kelas = QComboBox(self.widget)
        self.cbo_kelas.setObjectName(u"cbo_kelas")
        self.cbo_kelas.setMinimumSize(QSize(0, 24))
        self.cbo_kelas.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.cbo_kelas, 1, 1, 1, 1)

        self.btn_insert = QPushButton(self.widget)
        self.btn_insert.setObjectName(u"btn_insert")
        self.btn_insert.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.btn_insert, 1, 5, 1, 1)

        self.cbo_guru = QComboBox(self.widget)
        self.cbo_guru.setObjectName(u"cbo_guru")
        self.cbo_guru.setMinimumSize(QSize(200, 24))

        self.gridLayout.addWidget(self.cbo_guru, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Daftar Guru Aktif", None))
        self.label.setText(QCoreApplication.translate("Form", u"Daftar Kelas", None))
        self.btn_insert.setText(QCoreApplication.translate("Form", u"INSERT", None))
    # retranslateUi

