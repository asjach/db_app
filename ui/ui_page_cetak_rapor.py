# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_cetak_rapor.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDoubleSpinBox,
    QGridLayout, QHeaderView, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1073, 514)
        self.gridLayout_8 = QGridLayout(Form)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_9 = QGridLayout(self.widget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.cbo_kelas = QComboBox(self.widget_4)
        self.cbo_kelas.setObjectName(u"cbo_kelas")
        self.cbo_kelas.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_kelas, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.cbo_kegiatan = QComboBox(self.widget_4)
        self.cbo_kegiatan.setObjectName(u"cbo_kegiatan")
        self.cbo_kegiatan.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_kegiatan, 0, 4, 1, 1)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)


        self.gridLayout_9.addWidget(self.widget_4, 0, 0, 1, 1)

        self.tbl_siswa = QTableWidget(self.widget)
        self.tbl_siswa.setObjectName(u"tbl_siswa")
        self.tbl_siswa.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_9.addWidget(self.tbl_siswa, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.viewer_layout = QGridLayout(self.widget_3)
        self.viewer_layout.setObjectName(u"viewer_layout")

        self.gridLayout_8.addWidget(self.widget_3, 0, 1, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_7 = QGridLayout(self.widget_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_3 = QGridLayout(self.widget_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_9)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.cbo_kertas = QComboBox(self.widget_9)
        self.cbo_kertas.addItem("")
        self.cbo_kertas.addItem("")
        self.cbo_kertas.setObjectName(u"cbo_kertas")
        self.cbo_kertas.setMinimumSize(QSize(80, 24))

        self.gridLayout_3.addWidget(self.cbo_kertas, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_4 = QLabel(self.widget_9)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 3, 1, 1)

        self.cbo_orientasi = QComboBox(self.widget_9)
        self.cbo_orientasi.addItem("")
        self.cbo_orientasi.addItem("")
        self.cbo_orientasi.setObjectName(u"cbo_orientasi")
        self.cbo_orientasi.setMinimumSize(QSize(80, 24))

        self.gridLayout_3.addWidget(self.cbo_orientasi, 0, 4, 1, 1)


        self.gridLayout_5.addWidget(self.widget_9, 0, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_5)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_4 = QGridLayout(self.widget_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_10)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)

        self.spin_right = QDoubleSpinBox(self.widget_10)
        self.spin_right.setObjectName(u"spin_right")
        self.spin_right.setMinimumSize(QSize(0, 24))
        self.spin_right.setDecimals(1)
        self.spin_right.setSingleStep(0.100000000000000)
        self.spin_right.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_right, 2, 1, 1, 1)

        self.spin_left = QDoubleSpinBox(self.widget_10)
        self.spin_left.setObjectName(u"spin_left")
        self.spin_left.setMinimumSize(QSize(0, 24))
        self.spin_left.setDecimals(1)
        self.spin_left.setSingleStep(0.100000000000000)
        self.spin_left.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_left, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 2, 3, 1, 1)

        self.spin_bottom = QDoubleSpinBox(self.widget_10)
        self.spin_bottom.setObjectName(u"spin_bottom")
        self.spin_bottom.setMinimumSize(QSize(0, 24))
        self.spin_bottom.setDecimals(1)
        self.spin_bottom.setSingleStep(0.100000000000000)
        self.spin_bottom.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_bottom, 2, 4, 1, 1)

        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 1, 3, 1, 1)

        self.spin_top = QDoubleSpinBox(self.widget_10)
        self.spin_top.setObjectName(u"spin_top")
        self.spin_top.setMinimumSize(QSize(0, 24))
        self.spin_top.setDecimals(1)
        self.spin_top.setSingleStep(0.100000000000000)
        self.spin_top.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_top, 1, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.label_10 = QLabel(self.widget_10)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 5)


        self.gridLayout_5.addWidget(self.widget_10, 1, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 200))
        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 10, 157, 24))

        self.gridLayout_5.addWidget(self.widget_11, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_10 = QGridLayout(self.widget_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_10.addWidget(self.label_11, 0, 0, 1, 1)

        self.cbo_halaman = QComboBox(self.widget_6)
        self.cbo_halaman.addItem("")
        self.cbo_halaman.addItem("")
        self.cbo_halaman.addItem("")
        self.cbo_halaman.setObjectName(u"cbo_halaman")
        self.cbo_halaman.setMinimumSize(QSize(0, 24))

        self.gridLayout_10.addWidget(self.cbo_halaman, 0, 1, 1, 1)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_6 = QGridLayout(self.widget_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.opsi_id_siswa = QRadioButton(self.widget_8)
        self.opsi_id_siswa.setObjectName(u"opsi_id_siswa")

        self.gridLayout_6.addWidget(self.opsi_id_siswa, 4, 0, 1, 1)

        self.opsi_cover = QRadioButton(self.widget_8)
        self.opsi_cover.setObjectName(u"opsi_cover")

        self.gridLayout_6.addWidget(self.opsi_cover, 1, 0, 1, 1)

        self.opsi_id_madrasah = QRadioButton(self.widget_8)
        self.opsi_id_madrasah.setObjectName(u"opsi_id_madrasah")

        self.gridLayout_6.addWidget(self.opsi_id_madrasah, 2, 0, 1, 1)

        self.opsi_petunjuk = QRadioButton(self.widget_8)
        self.opsi_petunjuk.setObjectName(u"opsi_petunjuk")

        self.gridLayout_6.addWidget(self.opsi_petunjuk, 3, 0, 1, 1)

        self.opsi_catatan = QRadioButton(self.widget_8)
        self.opsi_catatan.setObjectName(u"opsi_catatan")

        self.gridLayout_6.addWidget(self.opsi_catatan, 2, 1, 1, 1)

        self.opsi_nilai = QRadioButton(self.widget_8)
        self.opsi_nilai.setObjectName(u"opsi_nilai")

        self.gridLayout_6.addWidget(self.opsi_nilai, 1, 1, 1, 1)

        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 2)

        self.opsi_mutasi = QRadioButton(self.widget_8)
        self.opsi_mutasi.setObjectName(u"opsi_mutasi")

        self.gridLayout_6.addWidget(self.opsi_mutasi, 3, 1, 1, 1)


        self.gridLayout_10.addWidget(self.widget_8, 1, 0, 1, 2)


        self.gridLayout_7.addWidget(self.widget_6, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_save_pdf = QPushButton(self.widget_7)
        self.btn_save_pdf.setObjectName(u"btn_save_pdf")
        self.btn_save_pdf.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.btn_save_pdf, 0, 0, 1, 1)

        self.btn_print = QPushButton(self.widget_7)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.btn_print, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.widget_7, 3, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget_2, 0, 2, 1, 1)

        self.gridLayout_8.setColumnStretch(1, 1)
        self.gridLayout_8.setColumnMinimumWidth(0, 400)
        self.gridLayout_8.setColumnMinimumWidth(2, 300)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Kertas", None))
        self.cbo_kertas.setItemText(0, QCoreApplication.translate("Form", u"A4", None))
        self.cbo_kertas.setItemText(1, QCoreApplication.translate("Form", u"F4", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Orientasi", None))
        self.cbo_orientasi.setItemText(0, QCoreApplication.translate("Form", u"Portait", None))
        self.cbo_orientasi.setItemText(1, QCoreApplication.translate("Form", u"Landscape", None))

        self.label_8.setText(QCoreApplication.translate("Form", u"Right", None))
        self.spin_right.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_left.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Left", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Bottom", None))
        self.spin_bottom.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Top", None))
        self.spin_top.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Margin Kertas", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Pengaturan Posisi", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Opsi Halaman", None))
        self.cbo_halaman.setItemText(0, QCoreApplication.translate("Form", u"Custom", None))
        self.cbo_halaman.setItemText(1, QCoreApplication.translate("Form", u"Nilai", None))
        self.cbo_halaman.setItemText(2, QCoreApplication.translate("Form", u"Identitas", None))

        self.opsi_id_siswa.setText(QCoreApplication.translate("Form", u"Identitas Siswa", None))
        self.opsi_cover.setText(QCoreApplication.translate("Form", u"Cover", None))
        self.opsi_id_madrasah.setText(QCoreApplication.translate("Form", u"Identitas Madrasah", None))
        self.opsi_petunjuk.setText(QCoreApplication.translate("Form", u"Petunjuk", None))
        self.opsi_catatan.setText(QCoreApplication.translate("Form", u"Catatan", None))
        self.opsi_nilai.setText(QCoreApplication.translate("Form", u"Nilai", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Halaman Rapor", None))
        self.opsi_mutasi.setText(QCoreApplication.translate("Form", u"Mutasi", None))
        self.btn_save_pdf.setText(QCoreApplication.translate("Form", u"Save PDF", None))
        self.btn_print.setText(QCoreApplication.translate("Form", u"Print", None))
    # retranslateUi

