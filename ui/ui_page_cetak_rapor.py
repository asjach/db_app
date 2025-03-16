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
        Form.resize(817, 769)
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
        self.cbo_kegiatan = QComboBox(self.widget_4)
        self.cbo_kegiatan.setObjectName(u"cbo_kegiatan")
        self.cbo_kegiatan.setMinimumSize(QSize(0, 24))
        self.cbo_kegiatan.setMaximumSize(QSize(75, 16777215))

        self.gridLayout.addWidget(self.cbo_kegiatan, 0, 4, 1, 1)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.cbo_kelas = QComboBox(self.widget_4)
        self.cbo_kelas.setObjectName(u"cbo_kelas")
        self.cbo_kelas.setMinimumSize(QSize(0, 24))
        self.cbo_kelas.setMaximumSize(QSize(75, 16777215))

        self.gridLayout.addWidget(self.cbo_kelas, 0, 1, 1, 1)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_save_pdf = QPushButton(self.widget_7)
        self.btn_save_pdf.setObjectName(u"btn_save_pdf")
        self.btn_save_pdf.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.btn_save_pdf, 0, 0, 1, 1)

        self.btn_print = QPushButton(self.widget_7)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.btn_print, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.widget_7, 5, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(15)
        self.btn_generate_pdf = QPushButton(self.widget_5)
        self.btn_generate_pdf.setObjectName(u"btn_generate_pdf")
        self.btn_generate_pdf.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.btn_generate_pdf, 9, 0, 1, 1)

        self.widget_15 = QWidget(self.widget_5)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_15 = QGridLayout(self.widget_15)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btn_reset_setting = QPushButton(self.widget_15)
        self.btn_reset_setting.setObjectName(u"btn_reset_setting")
        self.btn_reset_setting.setMinimumSize(QSize(80, 24))

        self.gridLayout_15.addWidget(self.btn_reset_setting, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_15, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_5)
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
        self.opsi_id_siswa.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_id_siswa, 4, 0, 1, 1)

        self.opsi_cover = QRadioButton(self.widget_8)
        self.opsi_cover.setObjectName(u"opsi_cover")
        self.opsi_cover.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_cover, 1, 0, 1, 1)

        self.opsi_id_madrasah = QRadioButton(self.widget_8)
        self.opsi_id_madrasah.setObjectName(u"opsi_id_madrasah")
        self.opsi_id_madrasah.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_id_madrasah, 2, 0, 1, 1)

        self.opsi_petunjuk = QRadioButton(self.widget_8)
        self.opsi_petunjuk.setObjectName(u"opsi_petunjuk")
        self.opsi_petunjuk.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_petunjuk, 3, 0, 1, 1)

        self.opsi_catatan = QRadioButton(self.widget_8)
        self.opsi_catatan.setObjectName(u"opsi_catatan")
        self.opsi_catatan.setChecked(True)
        self.opsi_catatan.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_catatan, 2, 1, 1, 1)

        self.opsi_nilai = QRadioButton(self.widget_8)
        self.opsi_nilai.setObjectName(u"opsi_nilai")
        self.opsi_nilai.setChecked(True)
        self.opsi_nilai.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_nilai, 1, 1, 1, 1)

        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_5.setFont(font)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 2)

        self.opsi_mutasi = QRadioButton(self.widget_8)
        self.opsi_mutasi.setObjectName(u"opsi_mutasi")
        self.opsi_mutasi.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_mutasi, 3, 1, 1, 1)


        self.gridLayout_10.addWidget(self.widget_8, 1, 0, 1, 2)


        self.gridLayout_5.addWidget(self.widget_6, 6, 0, 1, 1)

        self.widget_14 = QWidget(self.widget_5)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_14 = QGridLayout(self.widget_14)
        self.gridLayout_14.setSpacing(5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.spin_tinggi_baris = QDoubleSpinBox(self.widget_14)
        self.spin_tinggi_baris.setObjectName(u"spin_tinggi_baris")
        self.spin_tinggi_baris.setMinimumSize(QSize(75, 24))
        self.spin_tinggi_baris.setAlignment(Qt.AlignCenter)
        self.spin_tinggi_baris.setAccelerated(True)
        self.spin_tinggi_baris.setDecimals(1)
        self.spin_tinggi_baris.setMaximum(2.000000000000000)
        self.spin_tinggi_baris.setSingleStep(0.100000000000000)
        self.spin_tinggi_baris.setValue(0.600000000000000)

        self.gridLayout_14.addWidget(self.spin_tinggi_baris, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget_14)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_14.addWidget(self.label_12, 0, 0, 1, 1)

        self.spin_jarak_catatan = QDoubleSpinBox(self.widget_14)
        self.spin_jarak_catatan.setObjectName(u"spin_jarak_catatan")
        self.spin_jarak_catatan.setMinimumSize(QSize(75, 24))
        self.spin_jarak_catatan.setAlignment(Qt.AlignCenter)
        self.spin_jarak_catatan.setAccelerated(True)
        self.spin_jarak_catatan.setDecimals(0)
        self.spin_jarak_catatan.setMaximum(50.000000000000000)
        self.spin_jarak_catatan.setSingleStep(3.000000000000000)
        self.spin_jarak_catatan.setValue(12.000000000000000)

        self.gridLayout_14.addWidget(self.spin_jarak_catatan, 1, 2, 1, 1)

        self.label_21 = QLabel(self.widget_14)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_14.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.widget_14)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_14.addWidget(self.label_22, 2, 0, 1, 1)

        self.spin_ukuran_catatan = QDoubleSpinBox(self.widget_14)
        self.spin_ukuran_catatan.setObjectName(u"spin_ukuran_catatan")
        self.spin_ukuran_catatan.setMinimumSize(QSize(75, 24))
        self.spin_ukuran_catatan.setAlignment(Qt.AlignCenter)
        self.spin_ukuran_catatan.setAccelerated(True)
        self.spin_ukuran_catatan.setDecimals(0)
        self.spin_ukuran_catatan.setMaximum(50.000000000000000)
        self.spin_ukuran_catatan.setSingleStep(1.000000000000000)
        self.spin_ukuran_catatan.setValue(12.000000000000000)

        self.gridLayout_14.addWidget(self.spin_ukuran_catatan, 2, 2, 1, 1)


        self.gridLayout_5.addWidget(self.widget_14, 5, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_5)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 24))
        self.gridLayout_4 = QGridLayout(self.widget_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_10)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 3, 0, 1, 1)

        self.spin_left = QDoubleSpinBox(self.widget_10)
        self.spin_left.setObjectName(u"spin_left")
        self.spin_left.setMinimumSize(QSize(75, 24))
        self.spin_left.setAlignment(Qt.AlignCenter)
        self.spin_left.setAccelerated(True)
        self.spin_left.setDecimals(1)
        self.spin_left.setSingleStep(0.100000000000000)
        self.spin_left.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_left, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 3, 3, 1, 1)

        self.spin_bottom = QDoubleSpinBox(self.widget_10)
        self.spin_bottom.setObjectName(u"spin_bottom")
        self.spin_bottom.setMinimumSize(QSize(75, 24))
        self.spin_bottom.setAlignment(Qt.AlignCenter)
        self.spin_bottom.setAccelerated(True)
        self.spin_bottom.setDecimals(1)
        self.spin_bottom.setSingleStep(0.100000000000000)
        self.spin_bottom.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_bottom, 3, 4, 1, 1)

        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)

        self.spin_right = QDoubleSpinBox(self.widget_10)
        self.spin_right.setObjectName(u"spin_right")
        self.spin_right.setMinimumSize(QSize(75, 24))
        self.spin_right.setAlignment(Qt.AlignCenter)
        self.spin_right.setAccelerated(True)
        self.spin_right.setDecimals(1)
        self.spin_right.setSingleStep(0.100000000000000)
        self.spin_right.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_right, 3, 1, 1, 1)

        self.label_10 = QLabel(self.widget_10)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 5)

        self.spin_top = QDoubleSpinBox(self.widget_10)
        self.spin_top.setObjectName(u"spin_top")
        self.spin_top.setMinimumSize(QSize(75, 24))
        self.spin_top.setAlignment(Qt.AlignCenter)
        self.spin_top.setAccelerated(True)
        self.spin_top.setDecimals(1)
        self.spin_top.setSingleStep(0.100000000000000)
        self.spin_top.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_top, 2, 4, 1, 1)

        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 2, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.widget_9 = QWidget(self.widget_10)
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
        self.cbo_kertas.setMinimumSize(QSize(75, 24))

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
        self.cbo_orientasi.setMinimumSize(QSize(75, 24))

        self.gridLayout_3.addWidget(self.cbo_orientasi, 0, 4, 1, 1)


        self.gridLayout_4.addWidget(self.widget_9, 0, 0, 1, 5)


        self.gridLayout_5.addWidget(self.widget_10, 1, 0, 1, 1)

        self.widget_13 = QWidget(self.widget_5)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_12 = QGridLayout(self.widget_13)
        self.gridLayout_12.setSpacing(5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout_12.addWidget(self.label_13, 0, 0, 1, 5)

        self.radio_walas = QRadioButton(self.widget_13)
        self.radio_walas.setObjectName(u"radio_walas")

        self.gridLayout_12.addWidget(self.radio_walas, 1, 0, 1, 5)

        self.label_16 = QLabel(self.widget_13)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_12.addWidget(self.label_16, 3, 0, 1, 1)

        self.spin_x_walas = QDoubleSpinBox(self.widget_13)
        self.spin_x_walas.setObjectName(u"spin_x_walas")
        self.spin_x_walas.setMinimumSize(QSize(0, 24))
        self.spin_x_walas.setAlignment(Qt.AlignCenter)
        self.spin_x_walas.setAccelerated(True)
        self.spin_x_walas.setDecimals(1)
        self.spin_x_walas.setMinimum(-5.000000000000000)
        self.spin_x_walas.setSingleStep(0.100000000000000)

        self.gridLayout_12.addWidget(self.spin_x_walas, 2, 1, 1, 1)

        self.label_15 = QLabel(self.widget_13)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_12.addWidget(self.label_15, 2, 3, 1, 1)

        self.label_14 = QLabel(self.widget_13)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_12.addWidget(self.label_14, 2, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self.spin_size_walas = QDoubleSpinBox(self.widget_13)
        self.spin_size_walas.setObjectName(u"spin_size_walas")
        self.spin_size_walas.setMinimumSize(QSize(0, 24))
        self.spin_size_walas.setAlignment(Qt.AlignCenter)
        self.spin_size_walas.setAccelerated(True)
        self.spin_size_walas.setDecimals(1)
        self.spin_size_walas.setMinimum(-5.000000000000000)
        self.spin_size_walas.setSingleStep(0.100000000000000)

        self.gridLayout_12.addWidget(self.spin_size_walas, 2, 4, 1, 1)

        self.spin_y_walas = QDoubleSpinBox(self.widget_13)
        self.spin_y_walas.setObjectName(u"spin_y_walas")
        self.spin_y_walas.setMinimumSize(QSize(0, 24))
        self.spin_y_walas.setAlignment(Qt.AlignCenter)
        self.spin_y_walas.setAccelerated(True)
        self.spin_y_walas.setDecimals(1)
        self.spin_y_walas.setMinimum(-5.000000000000000)
        self.spin_y_walas.setSingleStep(0.100000000000000)

        self.gridLayout_12.addWidget(self.spin_y_walas, 3, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_13, 3, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_13 = QGridLayout(self.widget_11)
        self.gridLayout_13.setSpacing(5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_11)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setFont(font)

        self.gridLayout_13.addWidget(self.label_17, 0, 0, 1, 5)

        self.label_19 = QLabel(self.widget_11)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_13.addWidget(self.label_19, 1, 0, 1, 1)

        self.spin_x_mudir = QDoubleSpinBox(self.widget_11)
        self.spin_x_mudir.setObjectName(u"spin_x_mudir")
        self.spin_x_mudir.setMinimumSize(QSize(0, 24))
        self.spin_x_mudir.setAlignment(Qt.AlignCenter)
        self.spin_x_mudir.setAccelerated(True)
        self.spin_x_mudir.setDecimals(1)
        self.spin_x_mudir.setMinimum(-5.000000000000000)
        self.spin_x_mudir.setSingleStep(0.100000000000000)

        self.gridLayout_13.addWidget(self.spin_x_mudir, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(37, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.label_18 = QLabel(self.widget_11)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_13.addWidget(self.label_18, 1, 3, 1, 1)

        self.label_20 = QLabel(self.widget_11)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_13.addWidget(self.label_20, 2, 0, 1, 1)

        self.spin_size_mudir = QDoubleSpinBox(self.widget_11)
        self.spin_size_mudir.setObjectName(u"spin_size_mudir")
        self.spin_size_mudir.setMinimumSize(QSize(0, 24))
        self.spin_size_mudir.setAlignment(Qt.AlignCenter)
        self.spin_size_mudir.setAccelerated(True)
        self.spin_size_mudir.setDecimals(1)
        self.spin_size_mudir.setMinimum(-5.000000000000000)
        self.spin_size_mudir.setSingleStep(0.100000000000000)

        self.gridLayout_13.addWidget(self.spin_size_mudir, 1, 4, 1, 1)

        self.spin_y_mudir = QDoubleSpinBox(self.widget_11)
        self.spin_y_mudir.setObjectName(u"spin_y_mudir")
        self.spin_y_mudir.setMinimumSize(QSize(0, 24))
        self.spin_y_mudir.setAlignment(Qt.AlignCenter)
        self.spin_y_mudir.setAccelerated(True)
        self.spin_y_mudir.setDecimals(1)
        self.spin_y_mudir.setMinimum(-5.000000000000000)
        self.spin_y_mudir.setSingleStep(0.100000000000000)

        self.gridLayout_13.addWidget(self.spin_y_mudir, 2, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_11, 4, 0, 1, 1)

        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_11 = QGridLayout(self.widget_12)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.radio_peringkat_10 = QRadioButton(self.widget_12)
        self.radio_peringkat_10.setObjectName(u"radio_peringkat_10")
        self.radio_peringkat_10.setChecked(True)

        self.gridLayout_11.addWidget(self.radio_peringkat_10, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_12, 8, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_5, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget_2, 0, 2, 1, 1)

        self.gridLayout_8.setColumnStretch(1, 1)
        self.gridLayout_8.setColumnMinimumWidth(0, 350)
        self.gridLayout_8.setColumnMinimumWidth(2, 350)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.btn_save_pdf.setText(QCoreApplication.translate("Form", u"Save PDF", None))
        self.btn_print.setText(QCoreApplication.translate("Form", u"Print", None))
        self.btn_generate_pdf.setText(QCoreApplication.translate("Form", u"Generate PDF (Perkelas)", None))
        self.btn_reset_setting.setText(QCoreApplication.translate("Form", u"Reset Setting", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Opsi Halaman", None))
        self.cbo_halaman.setItemText(0, QCoreApplication.translate("Form", u"Nilai dan Identitas", None))
        self.cbo_halaman.setItemText(1, QCoreApplication.translate("Form", u"Nilai", None))
        self.cbo_halaman.setItemText(2, QCoreApplication.translate("Form", u"Identitas", None))
        self.cbo_halaman.setItemText(3, QCoreApplication.translate("Form", u"Custom", None))

        self.opsi_id_siswa.setText(QCoreApplication.translate("Form", u"Identitas Siswa", None))
        self.opsi_cover.setText(QCoreApplication.translate("Form", u"Cover", None))
        self.opsi_id_madrasah.setText(QCoreApplication.translate("Form", u"Identitas Madrasah", None))
        self.opsi_petunjuk.setText(QCoreApplication.translate("Form", u"Petunjuk", None))
        self.opsi_catatan.setText(QCoreApplication.translate("Form", u"Catatan", None))
        self.opsi_nilai.setText(QCoreApplication.translate("Form", u"Nilai", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Halaman Rapor", None))
        self.opsi_mutasi.setText(QCoreApplication.translate("Form", u"Mutasi", None))
        self.spin_tinggi_baris.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Tinggi Baris Tabel", None))
        self.spin_jarak_catatan.setSuffix(QCoreApplication.translate("Form", u" pt", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Jarak Catatan", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Ukuran Font Catatan", None))
        self.spin_ukuran_catatan.setSuffix(QCoreApplication.translate("Form", u" pt", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Right", None))
        self.spin_left.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Bottom", None))
        self.spin_bottom.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Left", None))
        self.spin_right.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Margin Kertas", None))
        self.spin_top.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Top", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Kertas", None))
        self.cbo_kertas.setItemText(0, QCoreApplication.translate("Form", u"A4", None))
        self.cbo_kertas.setItemText(1, QCoreApplication.translate("Form", u"F4", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Orientasi", None))
        self.cbo_orientasi.setItemText(0, QCoreApplication.translate("Form", u"Portrait", None))
        self.cbo_orientasi.setItemText(1, QCoreApplication.translate("Form", u"Landscape", None))

        self.label_13.setText(QCoreApplication.translate("Form", u"Koreksi Tanda Tangan Wali Kelas", None))
        self.radio_walas.setText(QCoreApplication.translate("Form", u"tampilkan tanda tangan", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Y", None))
        self.spin_x_walas.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Ukuran", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"X", None))
        self.spin_size_walas.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_y_walas.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Koreksi Tanda Mudir", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"X", None))
        self.spin_x_mudir.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Ukuran", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Y", None))
        self.spin_size_mudir.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_y_mudir.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.radio_peringkat_10.setText(QCoreApplication.translate("Form", u"Ranking sampai 10 besar", None))
    # retranslateUi

