# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_mutasi_masuk.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1286, 794)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tbl_daftar_calon_siswa = QTableWidget(Form)
        self.tbl_daftar_calon_siswa.setObjectName(u"tbl_daftar_calon_siswa")

        self.gridLayout_3.addWidget(self.tbl_daftar_calon_siswa, 1, 0, 2, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)

        self.tbl_diterima = QTableWidget(self.frame_2)
        self.tbl_diterima.setObjectName(u"tbl_diterima")

        self.gridLayout_2.addWidget(self.tbl_diterima, 1, 0, 1, 2)

        self.btn_batal = QPushButton(self.frame_2)
        self.btn_batal.setObjectName(u"btn_batal")
        self.btn_batal.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.btn_batal, 2, 0, 1, 2)


        self.gridLayout_3.addWidget(self.frame_2, 2, 1, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(450, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.btn_terima = QPushButton(self.frame)
        self.btn_terima.setObjectName(u"btn_terima")
        self.btn_terima.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.btn_terima, 2, 2, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.tbl_calon_belum = QTableWidget(self.frame)
        self.tbl_calon_belum.setObjectName(u"tbl_calon_belum")

        self.gridLayout.addWidget(self.tbl_calon_belum, 1, 0, 1, 3)

        self.line_tgl_masuk = QLineEdit(self.frame)
        self.line_tgl_masuk.setObjectName(u"line_tgl_masuk")
        self.line_tgl_masuk.setMinimumSize(QSize(150, 24))
        self.line_tgl_masuk.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.line_tgl_masuk, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 1, 1, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 15, 2, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 13, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 9, 1, 1)

        self.cbo_jk = QComboBox(self.widget)
        self.cbo_jk.addItem("")
        self.cbo_jk.addItem("")
        self.cbo_jk.setObjectName(u"cbo_jk")
        self.cbo_jk.setMinimumSize(QSize(50, 24))
        self.cbo_jk.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_4.addWidget(self.cbo_jk, 0, 6, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 5, 1, 1)

        self.line_no_urut = QLineEdit(self.widget)
        self.line_no_urut.setObjectName(u"line_no_urut")
        self.line_no_urut.setMinimumSize(QSize(50, 24))
        self.line_no_urut.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.line_no_urut, 0, 2, 1, 1)

        self.cbo_kelas = QComboBox(self.widget)
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItem("")
        self.cbo_kelas.setObjectName(u"cbo_kelas")
        self.cbo_kelas.setMinimumSize(QSize(50, 24))
        self.cbo_kelas.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.cbo_kelas, 0, 10, 1, 1)

        self.btn_tambah = QPushButton(self.widget)
        self.btn_tambah.setObjectName(u"btn_tambah")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_tambah.sizePolicy().hasHeightForWidth())
        self.btn_tambah.setSizePolicy(sizePolicy1)
        self.btn_tambah.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_4.addWidget(self.btn_tambah, 0, 14, 1, 1)

        self.line_nama_lengkap = QLineEdit(self.widget)
        self.line_nama_lengkap.setObjectName(u"line_nama_lengkap")
        self.line_nama_lengkap.setMinimumSize(QSize(240, 24))
        self.line_nama_lengkap.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_4.addWidget(self.line_nama_lengkap, 0, 4, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 2)

        self.gridLayout_3.setColumnStretch(0, 1)
        QWidget.setTabOrder(self.tbl_daftar_calon_siswa, self.tbl_calon_belum)
        QWidget.setTabOrder(self.tbl_calon_belum, self.line_tgl_masuk)
        QWidget.setTabOrder(self.line_tgl_masuk, self.btn_terima)
        QWidget.setTabOrder(self.btn_terima, self.tbl_diterima)
        QWidget.setTabOrder(self.tbl_diterima, self.btn_batal)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Daftar siswa sudah diterima", None))
        self.btn_batal.setText(QCoreApplication.translate("Form", u"Batalkan", None))
        self.label.setText(QCoreApplication.translate("Form", u"Daftar siswa belum diterima", None))
        self.btn_terima.setText(QCoreApplication.translate("Form", u"Terima Semua", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"No Urut", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Nama Lengkap", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.cbo_jk.setItemText(0, QCoreApplication.translate("Form", u"L", None))
        self.cbo_jk.setItemText(1, QCoreApplication.translate("Form", u"P", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"JK", None))
        self.cbo_kelas.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.cbo_kelas.setItemText(1, QCoreApplication.translate("Form", u"2", None))
        self.cbo_kelas.setItemText(2, QCoreApplication.translate("Form", u"3", None))
        self.cbo_kelas.setItemText(3, QCoreApplication.translate("Form", u"4", None))
        self.cbo_kelas.setItemText(4, QCoreApplication.translate("Form", u"5", None))
        self.cbo_kelas.setItemText(5, QCoreApplication.translate("Form", u"6", None))

        self.btn_tambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
    # retranslateUi

