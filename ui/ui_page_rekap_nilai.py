# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_rekap_nilai.ui'
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
    QGridLayout, QHeaderView, QLabel, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(959, 853)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(Form)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.viewer_layout = QGridLayout(self.widget_15)
        self.viewer_layout.setObjectName(u"viewer_layout")

        self.gridLayout.addWidget(self.widget_15, 0, 1, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(400, 0))
        self.gridLayout_13 = QGridLayout(self.widget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setVerticalSpacing(5)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 250))
        self.gridLayout_15 = QGridLayout(self.widget_14)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_14)
        self.label_16.setObjectName(u"label_16")
        font = QFont()
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setIndent(10)

        self.gridLayout_15.addWidget(self.label_16, 0, 0, 1, 1)

        self.kegiatan_tbl = QTableWidget(self.widget_14)
        self.kegiatan_tbl.setObjectName(u"kegiatan_tbl")
        self.kegiatan_tbl.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_15.addWidget(self.kegiatan_tbl, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_14, 0, 0, 1, 1)

        self.widget_12 = QWidget(self.widget)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_12 = QGridLayout(self.widget_12)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setIndent(10)

        self.gridLayout_12.addWidget(self.label_14, 0, 0, 1, 1)

        self.kelas_tbl = QTableWidget(self.widget_12)
        self.kelas_tbl.setObjectName(u"kelas_tbl")
        self.kelas_tbl.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_12.addWidget(self.kelas_tbl, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_12, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(350, 0))
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_6 = QGridLayout(self.widget_6)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_8 = QGridLayout(self.widget_8)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.kolom_nama_spin = QDoubleSpinBox(self.widget_8)
        self.kolom_nama_spin.setObjectName(u"kolom_nama_spin")
        self.kolom_nama_spin.setMinimumSize(QSize(0, 24))
        self.kolom_nama_spin.setAlignment(Qt.AlignCenter)
        self.kolom_nama_spin.setDecimals(2)
        self.kolom_nama_spin.setSingleStep(0.100000000000000)
        self.kolom_nama_spin.setValue(6.000000000000000)

        self.gridLayout_8.addWidget(self.kolom_nama_spin, 1, 1, 1, 1)

        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_8.addWidget(self.label_12, 1, 2, 1, 1)

        self.label_15 = QLabel(self.widget_8)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_8.addWidget(self.label_15, 0, 2, 1, 1)

        self.kolom_pelajaran_spin = QDoubleSpinBox(self.widget_8)
        self.kolom_pelajaran_spin.setObjectName(u"kolom_pelajaran_spin")
        self.kolom_pelajaran_spin.setMinimumSize(QSize(0, 24))
        self.kolom_pelajaran_spin.setAlignment(Qt.AlignCenter)
        self.kolom_pelajaran_spin.setDecimals(2)
        self.kolom_pelajaran_spin.setSingleStep(0.050000000000000)
        self.kolom_pelajaran_spin.setValue(0.600000000000000)

        self.gridLayout_8.addWidget(self.kolom_pelajaran_spin, 1, 3, 1, 1)

        self.label_10 = QLabel(self.widget_8)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_8.addWidget(self.label_10, 1, 0, 1, 1)

        self.tinggi_baris_spin = QDoubleSpinBox(self.widget_8)
        self.tinggi_baris_spin.setObjectName(u"tinggi_baris_spin")
        self.tinggi_baris_spin.setMinimumSize(QSize(0, 24))
        self.tinggi_baris_spin.setAlignment(Qt.AlignCenter)
        self.tinggi_baris_spin.setDecimals(2)
        self.tinggi_baris_spin.setSingleStep(0.050000000000000)
        self.tinggi_baris_spin.setValue(0.600000000000000)

        self.gridLayout_8.addWidget(self.tinggi_baris_spin, 0, 1, 1, 1)

        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_8.addWidget(self.label_11, 0, 0, 1, 1)

        self.nilai_merah_spin = QDoubleSpinBox(self.widget_8)
        self.nilai_merah_spin.setObjectName(u"nilai_merah_spin")
        self.nilai_merah_spin.setAlignment(Qt.AlignCenter)
        self.nilai_merah_spin.setDecimals(0)
        self.nilai_merah_spin.setValue(60.000000000000000)

        self.gridLayout_8.addWidget(self.nilai_merah_spin, 0, 3, 1, 1)


        self.gridLayout_6.addWidget(self.widget_8, 5, 0, 1, 2)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_9 = QGridLayout(self.widget_9)
        self.gridLayout_9.setSpacing(5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.ayah_radio = QRadioButton(self.widget_9)
        self.ayah_radio.setObjectName(u"ayah_radio")
        self.ayah_radio.setMinimumSize(QSize(0, 24))
        self.ayah_radio.setChecked(True)
        self.ayah_radio.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.ayah_radio, 11, 0, 1, 1)

        self.label_21 = QLabel(self.widget_9)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_9.addWidget(self.label_21, 7, 0, 1, 1)

        self.nama_spin = QDoubleSpinBox(self.widget_9)
        self.nama_spin.setObjectName(u"nama_spin")
        self.nama_spin.setMinimumSize(QSize(0, 24))
        self.nama_spin.setAlignment(Qt.AlignCenter)
        self.nama_spin.setDecimals(2)
        self.nama_spin.setSingleStep(0.100000000000000)
        self.nama_spin.setValue(6.000000000000000)

        self.gridLayout_9.addWidget(self.nama_spin, 8, 1, 1, 1)

        self.ibu_radio = QRadioButton(self.widget_9)
        self.ibu_radio.setObjectName(u"ibu_radio")
        self.ibu_radio.setMinimumSize(QSize(0, 24))
        self.ibu_radio.setChecked(True)
        self.ibu_radio.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.ibu_radio, 12, 0, 1, 1)

        self.alamat_radio = QRadioButton(self.widget_9)
        self.alamat_radio.setObjectName(u"alamat_radio")
        self.alamat_radio.setMinimumSize(QSize(0, 24))
        self.alamat_radio.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.alamat_radio, 13, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.rata_rata_spin = QDoubleSpinBox(self.widget_9)
        self.rata_rata_spin.setObjectName(u"rata_rata_spin")
        self.rata_rata_spin.setMinimumSize(QSize(0, 24))
        self.rata_rata_spin.setAlignment(Qt.AlignCenter)
        self.rata_rata_spin.setDecimals(2)
        self.rata_rata_spin.setSingleStep(0.100000000000000)
        self.rata_rata_spin.setValue(6.000000000000000)

        self.gridLayout_9.addWidget(self.rata_rata_spin, 10, 1, 1, 1)

        self.jumlah_spin = QDoubleSpinBox(self.widget_9)
        self.jumlah_spin.setObjectName(u"jumlah_spin")
        self.jumlah_spin.setMinimumSize(QSize(0, 24))
        self.jumlah_spin.setAlignment(Qt.AlignCenter)
        self.jumlah_spin.setDecimals(2)
        self.jumlah_spin.setSingleStep(0.100000000000000)
        self.jumlah_spin.setValue(6.000000000000000)

        self.gridLayout_9.addWidget(self.jumlah_spin, 9, 1, 1, 1)

        self.widget_5 = QWidget(self.widget_9)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tinggi_baris_spin_3 = QDoubleSpinBox(self.widget_5)
        self.tinggi_baris_spin_3.setObjectName(u"tinggi_baris_spin_3")
        self.tinggi_baris_spin_3.setMinimumSize(QSize(0, 24))
        self.tinggi_baris_spin_3.setAlignment(Qt.AlignCenter)
        self.tinggi_baris_spin_3.setDecimals(2)
        self.tinggi_baris_spin_3.setSingleStep(0.050000000000000)
        self.tinggi_baris_spin_3.setValue(0.600000000000000)

        self.gridLayout_4.addWidget(self.tinggi_baris_spin_3, 0, 1, 1, 1)

        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_5, 1, 0, 1, 2)

        self.widget_4 = QWidget(self.widget_9)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)

        self.tinggi_baris_spin_1 = QDoubleSpinBox(self.widget_4)
        self.tinggi_baris_spin_1.setObjectName(u"tinggi_baris_spin_1")
        self.tinggi_baris_spin_1.setMinimumSize(QSize(0, 24))
        self.tinggi_baris_spin_1.setAlignment(Qt.AlignCenter)
        self.tinggi_baris_spin_1.setDecimals(2)
        self.tinggi_baris_spin_1.setSingleStep(0.050000000000000)
        self.tinggi_baris_spin_1.setValue(0.600000000000000)

        self.gridLayout_3.addWidget(self.tinggi_baris_spin_1, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.widget_4, 0, 0, 1, 2)

        self.widget_7 = QWidget(self.widget_9)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(10)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tinggi_baris_spin_10 = QDoubleSpinBox(self.widget_7)
        self.tinggi_baris_spin_10.setObjectName(u"tinggi_baris_spin_10")
        self.tinggi_baris_spin_10.setMinimumSize(QSize(0, 24))
        self.tinggi_baris_spin_10.setAlignment(Qt.AlignCenter)
        self.tinggi_baris_spin_10.setDecimals(2)
        self.tinggi_baris_spin_10.setSingleStep(0.050000000000000)
        self.tinggi_baris_spin_10.setValue(0.600000000000000)

        self.gridLayout_7.addWidget(self.tinggi_baris_spin_10, 0, 1, 1, 1)

        self.label_23 = QLabel(self.widget_7)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_7.addWidget(self.label_23, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_7, 2, 0, 1, 2)

        self.ayah_spin = QDoubleSpinBox(self.widget_9)
        self.ayah_spin.setObjectName(u"ayah_spin")
        self.ayah_spin.setMinimumSize(QSize(0, 24))
        self.ayah_spin.setAlignment(Qt.AlignCenter)
        self.ayah_spin.setDecimals(2)
        self.ayah_spin.setSingleStep(0.100000000000000)
        self.ayah_spin.setValue(6.000000000000000)

        self.gridLayout_9.addWidget(self.ayah_spin, 11, 1, 1, 1)

        self.alamat_spin = QDoubleSpinBox(self.widget_9)
        self.alamat_spin.setObjectName(u"alamat_spin")
        self.alamat_spin.setMinimumSize(QSize(0, 24))
        self.alamat_spin.setAlignment(Qt.AlignCenter)
        self.alamat_spin.setDecimals(2)
        self.alamat_spin.setSingleStep(0.100000000000000)
        self.alamat_spin.setValue(6.000000000000000)

        self.gridLayout_9.addWidget(self.alamat_spin, 13, 1, 1, 1)

        self.ibu_spin = QDoubleSpinBox(self.widget_9)
        self.ibu_spin.setObjectName(u"ibu_spin")
        self.ibu_spin.setMinimumSize(QSize(0, 24))
        self.ibu_spin.setAlignment(Qt.AlignCenter)
        self.ibu_spin.setDecimals(2)
        self.ibu_spin.setSingleStep(0.100000000000000)
        self.ibu_spin.setValue(6.000000000000000)

        self.gridLayout_9.addWidget(self.ibu_spin, 12, 1, 1, 1)

        self.label_19 = QLabel(self.widget_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.label_19, 8, 0, 1, 1)

        self.label_24 = QLabel(self.widget_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.label_24, 9, 0, 1, 1)

        self.label_25 = QLabel(self.widget_9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.label_25, 10, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_9, 7, 0, 1, 2)

        self.perkelas_radio = QRadioButton(self.widget_6)
        self.perkelas_radio.setObjectName(u"perkelas_radio")
        self.perkelas_radio.setChecked(True)

        self.gridLayout_6.addWidget(self.perkelas_radio, 0, 0, 1, 1)

        self.sepuluh_besar_radio = QRadioButton(self.widget_6)
        self.sepuluh_besar_radio.setObjectName(u"sepuluh_besar_radio")

        self.gridLayout_6.addWidget(self.sepuluh_besar_radio, 2, 1, 1, 1)

        self.tiga_besar_radio = QRadioButton(self.widget_6)
        self.tiga_besar_radio.setObjectName(u"tiga_besar_radio")

        self.gridLayout_6.addWidget(self.tiga_besar_radio, 2, 0, 1, 1)

        self.pertama_radio = QRadioButton(self.widget_6)
        self.pertama_radio.setObjectName(u"pertama_radio")

        self.gridLayout_6.addWidget(self.pertama_radio, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_5, 6, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 3, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_6, 4, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_17, 8, 0, 1, 1)

        self.folder_rekap_plain = QPlainTextEdit(self.widget_3)
        self.folder_rekap_plain.setObjectName(u"folder_rekap_plain")
        self.folder_rekap_plain.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_2.addWidget(self.folder_rekap_plain, 9, 0, 1, 4)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.margin_left_spin = QDoubleSpinBox(self.widget_3)
        self.margin_left_spin.setObjectName(u"margin_left_spin")
        self.margin_left_spin.setMinimumSize(QSize(0, 24))
        self.margin_left_spin.setAlignment(Qt.AlignCenter)
        self.margin_left_spin.setDecimals(2)
        self.margin_left_spin.setMinimum(0.500000000000000)
        self.margin_left_spin.setMaximum(30.000000000000000)
        self.margin_left_spin.setSingleStep(0.100000000000000)
        self.margin_left_spin.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.margin_left_spin, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 5, 0, 1, 1)

        self.margin_right_spin = QDoubleSpinBox(self.widget_3)
        self.margin_right_spin.setObjectName(u"margin_right_spin")
        self.margin_right_spin.setMinimumSize(QSize(0, 24))
        self.margin_right_spin.setAlignment(Qt.AlignCenter)
        self.margin_right_spin.setDecimals(2)
        self.margin_right_spin.setMinimum(0.500000000000000)
        self.margin_right_spin.setMaximum(30.000000000000000)
        self.margin_right_spin.setSingleStep(0.100000000000000)
        self.margin_right_spin.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.margin_right_spin, 3, 1, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setBold(False)
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)

        self.margin_top_spin = QDoubleSpinBox(self.widget_3)
        self.margin_top_spin.setObjectName(u"margin_top_spin")
        self.margin_top_spin.setMinimumSize(QSize(0, 24))
        self.margin_top_spin.setAlignment(Qt.AlignCenter)
        self.margin_top_spin.setDecimals(2)
        self.margin_top_spin.setMinimum(0.500000000000000)
        self.margin_top_spin.setMaximum(30.000000000000000)
        self.margin_top_spin.setSingleStep(0.100000000000000)
        self.margin_top_spin.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.margin_top_spin, 2, 3, 1, 1)

        self.cbo_kertas = QComboBox(self.widget_3)
        self.cbo_kertas.addItem("")
        self.cbo_kertas.addItem("")
        self.cbo_kertas.setObjectName(u"cbo_kertas")
        self.cbo_kertas.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.cbo_kertas, 0, 1, 1, 1)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.cbo_orientasi = QComboBox(self.widget_3)
        self.cbo_orientasi.addItem("")
        self.cbo_orientasi.addItem("")
        self.cbo_orientasi.setObjectName(u"cbo_orientasi")
        self.cbo_orientasi.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.cbo_orientasi, 0, 3, 1, 1)

        self.margin_bottom_spin = QDoubleSpinBox(self.widget_3)
        self.margin_bottom_spin.setObjectName(u"margin_bottom_spin")
        self.margin_bottom_spin.setMinimumSize(QSize(0, 24))
        self.margin_bottom_spin.setAlignment(Qt.AlignCenter)
        self.margin_bottom_spin.setDecimals(2)
        self.margin_bottom_spin.setMinimum(0.500000000000000)
        self.margin_bottom_spin.setMaximum(30.000000000000000)
        self.margin_bottom_spin.setSingleStep(0.100000000000000)
        self.margin_bottom_spin.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.margin_bottom_spin, 3, 3, 1, 1)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.browse_folder_rekap_btn = QPushButton(self.widget_3)
        self.browse_folder_rekap_btn.setObjectName(u"browse_folder_rekap_btn")

        self.gridLayout_2.addWidget(self.browse_folder_rekap_btn, 8, 3, 1, 1)

        self.lengkap_radio = QRadioButton(self.widget_3)
        self.lengkap_radio.setObjectName(u"lengkap_radio")
        self.lengkap_radio.setChecked(True)

        self.gridLayout_2.addWidget(self.lengkap_radio, 5, 1, 1, 1)

        self.singkat_radio = QRadioButton(self.widget_3)
        self.singkat_radio.setObjectName(u"singkat_radio")
        self.singkat_radio.setChecked(False)

        self.gridLayout_2.addWidget(self.singkat_radio, 5, 2, 1, 1)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 6, 0, 1, 1)

        self.font_size_spin = QDoubleSpinBox(self.widget_3)
        self.font_size_spin.setObjectName(u"font_size_spin")
        self.font_size_spin.setAlignment(Qt.AlignCenter)
        self.font_size_spin.setDecimals(0)
        self.font_size_spin.setMinimum(8.000000000000000)
        self.font_size_spin.setValue(11.000000000000000)

        self.gridLayout_2.addWidget(self.font_size_spin, 6, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_3, 0, 0, 1, 1, Qt.AlignTop)

        self.widget_16 = QWidget(self.widget_2)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_16 = QGridLayout(self.widget_16)
        self.gridLayout_16.setSpacing(5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(5, 5, 5, 5)
        self.radio_auto_open = QRadioButton(self.widget_16)
        self.radio_auto_open.setObjectName(u"radio_auto_open")
        self.radio_auto_open.setChecked(True)
        self.radio_auto_open.setAutoExclusive(False)

        self.gridLayout_16.addWidget(self.radio_auto_open, 2, 0, 1, 1)

        self.btn_print = QPushButton(self.widget_16)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setMinimumSize(QSize(0, 40))

        self.gridLayout_16.addWidget(self.btn_print, 1, 2, 1, 1)

        self.btn_save = QPushButton(self.widget_16)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 40))

        self.gridLayout_16.addWidget(self.btn_save, 1, 0, 1, 1)

        self.btn_excel = QPushButton(self.widget_16)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 40))

        self.gridLayout_16.addWidget(self.btn_excel, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_16, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 129, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)


        self.retranslateUi(Form)
        self.perkelas_radio.toggled.connect(self.widget_8.setVisible)
        self.pertama_radio.toggled.connect(self.widget_9.setVisible)
        self.tiga_besar_radio.toggled.connect(self.widget_9.setVisible)
        self.sepuluh_besar_radio.toggled.connect(self.widget_9.setVisible)
        self.pertama_radio.toggled.connect(self.widget_4.setVisible)
        self.tiga_besar_radio.toggled.connect(self.widget_5.setVisible)
        self.sepuluh_besar_radio.toggled.connect(self.widget_7.setVisible)
        self.pertama_radio.toggled.connect(self.widget_5.setHidden)
        self.pertama_radio.toggled.connect(self.widget_7.setHidden)
        self.tiga_besar_radio.toggled.connect(self.widget_4.setHidden)
        self.tiga_besar_radio.toggled.connect(self.widget_7.setHidden)
        self.sepuluh_besar_radio.toggled.connect(self.widget_4.setHidden)
        self.sepuluh_besar_radio.toggled.connect(self.widget_5.setHidden)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"List Kegiatan", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"List Kelas", None))
        self.kolom_nama_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Kolom Pelajaran", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Nilai Merah", None))
        self.kolom_pelajaran_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Kolom Nama", None))
        self.tinggi_baris_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Tinggi Baris", None))
        self.ayah_radio.setText(QCoreApplication.translate("Form", u"Ayah", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Kolom Yang Ditampilkan:", None))
        self.nama_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.ibu_radio.setText(QCoreApplication.translate("Form", u"Ibu", None))
        self.alamat_radio.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.rata_rata_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.jumlah_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.tinggi_baris_spin_3.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Tinggi Baris (3 Besar)", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Tinggi Baris (pertama saja)", None))
        self.tinggi_baris_spin_1.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.tinggi_baris_spin_10.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Tinggi Baris (10 Besar)", None))
        self.ayah_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.alamat_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.ibu_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Jumlah", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Rata-Rata", None))
        self.perkelas_radio.setText(QCoreApplication.translate("Form", u"Rekap Nilai Per Kelas", None))
        self.sepuluh_besar_radio.setText(QCoreApplication.translate("Form", u"Daftar Peringkat 10 Besar", None))
        self.tiga_besar_radio.setText(QCoreApplication.translate("Form", u"Daftar Peringkat 3 Besar", None))
        self.pertama_radio.setText(QCoreApplication.translate("Form", u"Daftar Peringkat Pertama", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Folder Rekap", None))
        self.margin_left_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.margin_right_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Left", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Margin", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Top", None))
        self.margin_top_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.cbo_kertas.setItemText(0, QCoreApplication.translate("Form", u"F4", None))
        self.cbo_kertas.setItemText(1, QCoreApplication.translate("Form", u"A4", None))

        self.label.setText(QCoreApplication.translate("Form", u"Ukuran Kertas", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Right", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Orientasi", None))
        self.cbo_orientasi.setItemText(0, QCoreApplication.translate("Form", u"Portrait", None))
        self.cbo_orientasi.setItemText(1, QCoreApplication.translate("Form", u"Landscape", None))

        self.margin_bottom_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Bottom", None))
        self.browse_folder_rekap_btn.setText(QCoreApplication.translate("Form", u"Pilih Folder", None))
        self.lengkap_radio.setText(QCoreApplication.translate("Form", u"Lengkap", None))
        self.singkat_radio.setText(QCoreApplication.translate("Form", u"Singkat", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Ukuran Font", None))
        self.radio_auto_open.setText(QCoreApplication.translate("Form", u"Buka Otomatis File PDF", None))
        self.btn_print.setText(QCoreApplication.translate("Form", u"PRINT", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"Save PDF", None))
        self.btn_excel.setText(QCoreApplication.translate("Form", u"Save Excel", None))
    # retranslateUi

