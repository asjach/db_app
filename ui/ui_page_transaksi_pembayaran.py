# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_transaksi_pembayaran.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1378, 615)
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.tbl_tagihan = QTableWidget(self.widget_4)
        self.tbl_tagihan.setObjectName(u"tbl_tagihan")

        self.gridLayout_2.addWidget(self.tbl_tagihan, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tbl_siswa = QTableWidget(self.widget_3)
        self.tbl_siswa.setObjectName(u"tbl_siswa")

        self.gridLayout.addWidget(self.tbl_siswa, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_3, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 4, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tbl_transaksi = QTableWidget(self.widget)
        self.tbl_transaksi.setObjectName(u"tbl_transaksi")

        self.gridLayout_4.addWidget(self.tbl_transaksi, 1, 0, 1, 2)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QSize(0, 100))
        self.gridLayout_9 = QGridLayout(self.widget_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.widget_7 = QWidget(self.widget_8)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_8 = QGridLayout(self.widget_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 1, 0, 1, 1)

        self.txt_nama_tagihan = QLabel(self.widget_7)
        self.txt_nama_tagihan.setObjectName(u"txt_nama_tagihan")
        self.txt_nama_tagihan.setMinimumSize(QSize(120, 24))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.txt_nama_tagihan.setFont(font)
        self.txt_nama_tagihan.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.txt_nama_tagihan, 1, 1, 1, 1)

        self.txt_nama_tagihan_2 = QLabel(self.widget_7)
        self.txt_nama_tagihan_2.setObjectName(u"txt_nama_tagihan_2")
        self.txt_nama_tagihan_2.setMinimumSize(QSize(120, 24))
        self.txt_nama_tagihan_2.setFont(font)
        self.txt_nama_tagihan_2.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.txt_nama_tagihan_2, 0, 1, 1, 1)

        self.txt_status_tagihan = QLabel(self.widget_7)
        self.txt_status_tagihan.setObjectName(u"txt_status_tagihan")
        self.txt_status_tagihan.setMinimumSize(QSize(120, 24))
        self.txt_status_tagihan.setFont(font)
        self.txt_status_tagihan.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.txt_status_tagihan, 2, 1, 1, 1)

        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_8.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_14 = QLabel(self.widget_7)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_8.addWidget(self.label_14, 2, 3, 1, 1)

        self.label_nama_3 = QLabel(self.widget_7)
        self.label_nama_3.setObjectName(u"label_nama_3")
        self.label_nama_3.setMinimumSize(QSize(120, 24))
        self.label_nama_3.setFont(font)
        self.label_nama_3.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.label_nama_3, 0, 4, 1, 1)

        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_8.addWidget(self.label_10, 0, 3, 1, 1)

        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_8.addWidget(self.label_13, 1, 3, 1, 1)

        self.txt_status_tagihan_3 = QLabel(self.widget_7)
        self.txt_status_tagihan_3.setObjectName(u"txt_status_tagihan_3")
        self.txt_status_tagihan_3.setMinimumSize(QSize(120, 24))
        self.txt_status_tagihan_3.setFont(font)
        self.txt_status_tagihan_3.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.txt_status_tagihan_3, 1, 4, 1, 1)

        self.txt_status_tagihan_2 = QLabel(self.widget_7)
        self.txt_status_tagihan_2.setObjectName(u"txt_status_tagihan_2")
        self.txt_status_tagihan_2.setMinimumSize(QSize(120, 24))
        self.txt_status_tagihan_2.setFont(font)
        self.txt_status_tagihan_2.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.txt_status_tagihan_2, 2, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)


        self.gridLayout_9.addWidget(self.widget_7, 0, 1, 1, 1)

        self.widget_6 = QWidget(self.widget_8)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(150, 0))
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.widget_6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.lineEdit_6, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 24))
        self.pushButton_2.setMaximumSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.widget_6)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 24))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton.setFont(font1)

        self.gridLayout_7.addWidget(self.pushButton, 2, 0, 1, 2)


        self.gridLayout_9.addWidget(self.widget_6, 0, 3, 1, 1)

        self.widget_5 = QWidget(self.widget_8)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, -1, 0, 0)
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 0, 3, 1, 1)

        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_nama = QLabel(self.widget_5)
        self.label_nama.setObjectName(u"label_nama")
        self.label_nama.setMinimumSize(QSize(0, 24))
        self.label_nama.setFont(font)
        self.label_nama.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_6.addWidget(self.label_nama, 1, 1, 1, 4)

        self.label_ortu = QLabel(self.widget_5)
        self.label_ortu.setObjectName(u"label_ortu")
        self.label_ortu.setMinimumSize(QSize(0, 24))
        self.label_ortu.setFont(font)
        self.label_ortu.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_6.addWidget(self.label_ortu, 2, 1, 1, 4)

        self.label_nis_lokal = QLabel(self.widget_5)
        self.label_nis_lokal.setObjectName(u"label_nis_lokal")
        self.label_nis_lokal.setMinimumSize(QSize(120, 24))
        self.label_nis_lokal.setFont(font)
        self.label_nis_lokal.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_6.addWidget(self.label_nis_lokal, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(60, 24))
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_6.addWidget(self.label_12, 0, 4, 1, 1)


        self.gridLayout_9.addWidget(self.widget_5, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_8, 0, 0, 1, 2)

        self.gridLayout_4.setColumnStretch(0, 1)

        self.gridLayout_5.addWidget(self.widget, 0, 1, 3, 1)

        self.gridLayout_5.setRowStretch(2, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_5.setColumnMinimumWidth(0, 400)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Daftar Tagihan/Tunggakan", None))
        self.label.setText(QCoreApplication.translate("Form", u"Daftar Santri", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ID Tagihan", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Nama Tagihan", None))
        self.txt_nama_tagihan.setText("")
        self.txt_nama_tagihan_2.setText("")
        self.txt_status_tagihan.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Status Tagihan", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Total Setelah Dispensasi", None))
        self.label_nama_3.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"Nominal Tagihan", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Dispensasi", None))
        self.txt_status_tagihan_3.setText("")
        self.txt_status_tagihan_2.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Nominal Pembayaran", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u">>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"BAYAR", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"NIS Lokal", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Nama Siswa", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Orang Tua", None))
        self.label_nama.setText("")
        self.label_ortu.setText("")
        self.label_nis_lokal.setText("")
        self.label_12.setText("")
    # retranslateUi

