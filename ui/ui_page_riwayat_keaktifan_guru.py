# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_riwayat_keaktifan_guru.ui'
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
        Form.resize(707, 657)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 5, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.cbo_guru = QComboBox(Form)
        self.cbo_guru.setObjectName(u"cbo_guru")
        self.cbo_guru.setMinimumSize(QSize(200, 24))

        self.gridLayout.addWidget(self.cbo_guru, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btn_tapel_sebelumnya = QPushButton(Form)
        self.btn_tapel_sebelumnya.setObjectName(u"btn_tapel_sebelumnya")
        self.btn_tapel_sebelumnya.setMinimumSize(QSize(250, 24))

        self.gridLayout.addWidget(self.btn_tapel_sebelumnya, 0, 5, 1, 1)

        self.tbl_keaktifan = QTableWidget(Form)
        self.tbl_keaktifan.setObjectName(u"tbl_keaktifan")

        self.gridLayout.addWidget(self.tbl_keaktifan, 1, 0, 1, 6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Tambah Manual", None))
        self.label.setText(QCoreApplication.translate("Form", u"Riwayat Keaktifan Guru", None))
        self.btn_tapel_sebelumnya.setText(QCoreApplication.translate("Form", u"Aktifkan Guru dari Tapel Sebelumnya", None))
    # retranslateUi

