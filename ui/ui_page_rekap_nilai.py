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
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDoubleSpinBox, QGridLayout,
    QHeaderView, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(886, 678)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
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
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 129, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.margin_left_spin = QDoubleSpinBox(self.widget_5)
        self.margin_left_spin.setObjectName(u"margin_left_spin")
        self.margin_left_spin.setMinimumSize(QSize(0, 24))
        self.margin_left_spin.setDecimals(2)
        self.margin_left_spin.setMinimum(0.500000000000000)
        self.margin_left_spin.setMaximum(30.000000000000000)
        self.margin_left_spin.setSingleStep(0.100000000000000)
        self.margin_left_spin.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.margin_left_spin, 1, 1, 1, 1)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 3, 2, 1, 1)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 2, 1, 1)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.margin_right_spin = QDoubleSpinBox(self.widget_5)
        self.margin_right_spin.setObjectName(u"margin_right_spin")
        self.margin_right_spin.setMinimumSize(QSize(0, 24))
        self.margin_right_spin.setDecimals(2)
        self.margin_right_spin.setMinimum(0.500000000000000)
        self.margin_right_spin.setMaximum(30.000000000000000)
        self.margin_right_spin.setSingleStep(0.100000000000000)
        self.margin_right_spin.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.margin_right_spin, 3, 1, 1, 1)

        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setBold(False)
        self.label_4.setFont(font1)

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.margin_top_spin = QDoubleSpinBox(self.widget_5)
        self.margin_top_spin.setObjectName(u"margin_top_spin")
        self.margin_top_spin.setMinimumSize(QSize(0, 24))
        self.margin_top_spin.setDecimals(2)
        self.margin_top_spin.setMinimum(0.500000000000000)
        self.margin_top_spin.setMaximum(30.000000000000000)
        self.margin_top_spin.setSingleStep(0.100000000000000)
        self.margin_top_spin.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.margin_top_spin, 1, 3, 1, 1)

        self.margin_bottom_spin = QDoubleSpinBox(self.widget_5)
        self.margin_bottom_spin.setObjectName(u"margin_bottom_spin")
        self.margin_bottom_spin.setMinimumSize(QSize(0, 24))
        self.margin_bottom_spin.setDecimals(2)
        self.margin_bottom_spin.setMinimum(0.500000000000000)
        self.margin_bottom_spin.setMaximum(30.000000000000000)
        self.margin_bottom_spin.setSingleStep(0.100000000000000)
        self.margin_bottom_spin.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.margin_bottom_spin, 3, 3, 1, 1)


        self.gridLayout_5.addWidget(self.widget_5, 2, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.a4_radio = QRadioButton(self.widget_3)
        self.a4_radio.setObjectName(u"a4_radio")

        self.gridLayout_2.addWidget(self.a4_radio, 0, 2, 1, 1)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.f4_radio = QRadioButton(self.widget_3)
        self.f4_radio.setObjectName(u"f4_radio")
        self.f4_radio.setChecked(True)

        self.gridLayout_2.addWidget(self.f4_radio, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.portait_radio = QRadioButton(self.widget_4)
        self.portait_radio.setObjectName(u"portait_radio")
        self.portait_radio.setChecked(True)

        self.gridLayout_3.addWidget(self.portait_radio, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.landscape_radio = QRadioButton(self.widget_4)
        self.landscape_radio.setObjectName(u"landscape_radio")

        self.gridLayout_3.addWidget(self.landscape_radio, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_6 = QGridLayout(self.widget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.singkat_radio = QRadioButton(self.widget_7)
        self.singkat_radio.setObjectName(u"singkat_radio")
        self.singkat_radio.setChecked(True)

        self.gridLayout_7.addWidget(self.singkat_radio, 0, 2, 1, 1)

        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)

        self.lengkap_radio = QRadioButton(self.widget_7)
        self.lengkap_radio.setObjectName(u"lengkap_radio")

        self.gridLayout_7.addWidget(self.lengkap_radio, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.widget_7, 1, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_10 = QGridLayout(self.widget_10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_12 = QLabel(self.widget_10)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_10.addWidget(self.label_12, 0, 0, 1, 1)

        self.kolom_pelajaran_spin = QDoubleSpinBox(self.widget_10)
        self.kolom_pelajaran_spin.setObjectName(u"kolom_pelajaran_spin")
        self.kolom_pelajaran_spin.setMinimumSize(QSize(0, 24))
        self.kolom_pelajaran_spin.setDecimals(2)
        self.kolom_pelajaran_spin.setSingleStep(0.100000000000000)
        self.kolom_pelajaran_spin.setValue(0.500000000000000)

        self.gridLayout_10.addWidget(self.kolom_pelajaran_spin, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.widget_10, 3, 0, 1, 1)

        self.widget_13 = QWidget(self.widget_6)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_14 = QGridLayout(self.widget_13)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_15 = QLabel(self.widget_13)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_14.addWidget(self.label_15, 0, 0, 1, 1)

        self.nilai_merah_spin = QSpinBox(self.widget_13)
        self.nilai_merah_spin.setObjectName(u"nilai_merah_spin")
        self.nilai_merah_spin.setMaximum(100)
        self.nilai_merah_spin.setValue(50)

        self.gridLayout_14.addWidget(self.nilai_merah_spin, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.widget_13, 4, 0, 1, 1)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_8 = QGridLayout(self.widget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_10 = QLabel(self.widget_8)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)

        self.kolom_nama_spin = QDoubleSpinBox(self.widget_8)
        self.kolom_nama_spin.setObjectName(u"kolom_nama_spin")
        self.kolom_nama_spin.setMinimumSize(QSize(0, 24))
        self.kolom_nama_spin.setDecimals(2)
        self.kolom_nama_spin.setSingleStep(0.100000000000000)
        self.kolom_nama_spin.setValue(6.000000000000000)

        self.gridLayout_8.addWidget(self.kolom_nama_spin, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.widget_8, 2, 0, 1, 1)

        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_6, 4, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_11 = QGridLayout(self.widget_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tiga_besar_radio = QRadioButton(self.widget_11)
        self.tiga_besar_radio.setObjectName(u"tiga_besar_radio")

        self.gridLayout_11.addWidget(self.tiga_besar_radio, 2, 0, 1, 1)

        self.label_13 = QLabel(self.widget_11)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_11.addWidget(self.label_13, 0, 0, 1, 1)

        self.perkelas_radio = QRadioButton(self.widget_11)
        self.perkelas_radio.setObjectName(u"perkelas_radio")
        self.perkelas_radio.setChecked(True)

        self.gridLayout_11.addWidget(self.perkelas_radio, 1, 0, 1, 1)

        self.pertama_radio = QRadioButton(self.widget_11)
        self.pertama_radio.setObjectName(u"pertama_radio")

        self.gridLayout_11.addWidget(self.pertama_radio, 3, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_11, 5, 0, 1, 1)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_9 = QGridLayout(self.widget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_11 = QLabel(self.widget_9)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_9.addWidget(self.label_11, 0, 0, 1, 1)

        self.tinggi_baris_spin = QDoubleSpinBox(self.widget_9)
        self.tinggi_baris_spin.setObjectName(u"tinggi_baris_spin")
        self.tinggi_baris_spin.setMinimumSize(QSize(0, 24))
        self.tinggi_baris_spin.setDecimals(2)
        self.tinggi_baris_spin.setSingleStep(0.100000000000000)
        self.tinggi_baris_spin.setValue(0.600000000000000)

        self.gridLayout_9.addWidget(self.tinggi_baris_spin, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_9, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.pushButton, 7, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)

        self.pdf_viewer = QPdfView(Form)
        self.pdf_viewer.setObjectName(u"pdf_viewer")

        self.gridLayout.addWidget(self.pdf_viewer, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 400)
        self.gridLayout.setColumnMinimumWidth(2, 350)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"List Kegiatan", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"List Kelas", None))
        self.margin_left_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Bottom", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Top", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Margin", None))
        self.margin_right_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Right", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Left", None))
        self.margin_top_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.margin_bottom_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.a4_radio.setText(QCoreApplication.translate("Form", u"A4", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ukuran Kertas", None))
        self.f4_radio.setText(QCoreApplication.translate("Form", u"F4", None))
        self.portait_radio.setText(QCoreApplication.translate("Form", u"Portait", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Orientasi", None))
        self.landscape_radio.setText(QCoreApplication.translate("Form", u"Landscape", None))
        self.singkat_radio.setText(QCoreApplication.translate("Form", u"Singkat", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.lengkap_radio.setText(QCoreApplication.translate("Form", u"Lengkap", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Kolom Pelajaran", None))
        self.kolom_pelajaran_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Nilai Merah", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Kolom Nama", None))
        self.kolom_nama_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Ukuran Kolom", None))
        self.tiga_besar_radio.setText(QCoreApplication.translate("Form", u"Daftar Peringkat 3 Besar", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Data Rekap", None))
        self.perkelas_radio.setText(QCoreApplication.translate("Form", u"Rekap Nilai Per Kelas", None))
        self.pertama_radio.setText(QCoreApplication.translate("Form", u"Daftar Peringkat Pertama", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Tinggi Baris", None))
        self.tinggi_baris_spin.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PRINT", None))
    # retranslateUi

