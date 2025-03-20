# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_riwayat_biaya.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1095, 718)
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tbl_biaya_siswa = QTableWidget(Form)
        self.tbl_biaya_siswa.setObjectName(u"tbl_biaya_siswa")
        self.tbl_biaya_siswa.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_4.addWidget(self.tbl_biaya_siswa, 1, 1, 1, 1)

        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 24))

        self.gridLayout_5.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(130, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget_4, 0, 1, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 24))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_9.setFont(font)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.tbl_riwayat_biaya = QTableWidget(self.widget)
        self.tbl_riwayat_biaya.setObjectName(u"tbl_riwayat_biaya")
        self.tbl_riwayat_biaya.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_3.addWidget(self.tbl_riwayat_biaya, 2, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_generate_biaya = QPushButton(self.widget_2)
        self.btn_generate_biaya.setObjectName(u"btn_generate_biaya")
        self.btn_generate_biaya.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.btn_generate_biaya, 1, 4, 1, 1)

        self.btn_clear_tagihan = QPushButton(self.widget_2)
        self.btn_clear_tagihan.setObjectName(u"btn_clear_tagihan")
        self.btn_clear_tagihan.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.btn_clear_tagihan, 1, 5, 1, 1)


        self.gridLayout_3.addWidget(self.widget_2, 4, 0, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_5)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_13 = QLabel(self.widget_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.btn_biaya = QPushButton(self.widget_5)
        self.btn_biaya.setObjectName(u"btn_biaya")
        self.btn_biaya.setMaximumSize(QSize(24, 16777215))

        self.gridLayout_6.addWidget(self.btn_biaya, 1, 1, 1, 1)

        self.txt_tapel = QLabel(self.widget_5)
        self.txt_tapel.setObjectName(u"txt_tapel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_tapel.sizePolicy().hasHeightForWidth())
        self.txt_tapel.setSizePolicy(sizePolicy)
        self.txt_tapel.setMinimumSize(QSize(0, 24))
        self.txt_tapel.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_6.addWidget(self.txt_tapel, 1, 2, 1, 1)

        self.line_periode = QLineEdit(self.widget_5)
        self.line_periode.setObjectName(u"line_periode")
        self.line_periode.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.line_periode, 1, 3, 1, 1)

        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 3, 1, 1)

        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 0, 4, 1, 1)

        self.line_nominal = QLineEdit(self.widget_5)
        self.line_nominal.setObjectName(u"line_nominal")
        self.line_nominal.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.line_nominal, 1, 4, 1, 1)

        self.cbo_biaya = QComboBox(self.widget_5)
        self.cbo_biaya.setObjectName(u"cbo_biaya")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbo_biaya.sizePolicy().hasHeightForWidth())
        self.cbo_biaya.setSizePolicy(sizePolicy1)
        self.cbo_biaya.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.cbo_biaya, 1, 0, 1, 1)

        self.btn_tambah = QPushButton(self.widget_5)
        self.btn_tambah.setObjectName(u"btn_tambah")

        self.gridLayout_6.addWidget(self.btn_tambah, 1, 5, 1, 1)


        self.gridLayout_3.addWidget(self.widget_5, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 2, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Filter", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"DAFTAR BIAYA PENDIDIKAN", None))
        self.btn_generate_biaya.setText(QCoreApplication.translate("Form", u"Generate Biaya Ke Santri", None))
        self.btn_clear_tagihan.setText(QCoreApplication.translate("Form", u"Clear Tagihan by Riwayat Biaya", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Tapel", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Biaya", None))
        self.btn_biaya.setText(QCoreApplication.translate("Form", u"+", None))
        self.txt_tapel.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"Periode", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Nominal", None))
        self.btn_tambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
    # retranslateUi

