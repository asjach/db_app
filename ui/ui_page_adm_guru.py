# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_adm_guru.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(898, 757)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Aptos Narrow"])
        font.setPointSize(11)
        self.widget_2.setFont(font)
        self.viewer_layout = QGridLayout(self.widget_2)
        self.viewer_layout.setObjectName(u"viewer_layout")

        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(500, 0))
        self.widget_3.setMaximumSize(QSize(500, 16777215))
        self.widget_3.setFont(font)
        self.gridLayout_9 = QGridLayout(self.widget_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(5)
        self.gridLayout_9.setVerticalSpacing(20)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setFont(font)
        self.gridLayout_8 = QGridLayout(self.widget_4)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font)
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.cbo_kelas = QComboBox(self.widget)
        self.cbo_kelas.setObjectName(u"cbo_kelas")
        self.cbo_kelas.setMinimumSize(QSize(80, 24))
        self.cbo_kelas.setFont(font)

        self.gridLayout_2.addWidget(self.cbo_kelas, 1, 0, 1, 1)

        self.cbo_guru = QComboBox(self.widget)
        self.cbo_guru.setObjectName(u"cbo_guru")
        self.cbo_guru.setMinimumSize(QSize(220, 24))
        self.cbo_guru.setFont(font)

        self.gridLayout_2.addWidget(self.cbo_guru, 1, 2, 1, 1)

        self.cbo_semester = QComboBox(self.widget)
        self.cbo_semester.addItem("")
        self.cbo_semester.addItem("")
        self.cbo_semester.setObjectName(u"cbo_semester")
        self.cbo_semester.setMinimumSize(QSize(80, 24))
        self.cbo_semester.setFont(font)

        self.gridLayout_2.addWidget(self.cbo_semester, 1, 1, 1, 1)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout_2.addWidget(self.label_18, 0, 2, 1, 1)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout_8.addWidget(self.widget, 4, 0, 1, 3)

        self.widget_11 = QWidget(self.widget_4)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setFont(font)
        self.gridLayout_10 = QGridLayout(self.widget_11)
        self.gridLayout_10.setSpacing(5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, -1, 0)
        self.cbo_kertas = QComboBox(self.widget_11)
        self.cbo_kertas.addItem("")
        self.cbo_kertas.addItem("")
        self.cbo_kertas.setObjectName(u"cbo_kertas")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbo_kertas.sizePolicy().hasHeightForWidth())
        self.cbo_kertas.setSizePolicy(sizePolicy1)
        self.cbo_kertas.setMinimumSize(QSize(0, 24))
        self.cbo_kertas.setFont(font)

        self.gridLayout_10.addWidget(self.cbo_kertas, 0, 1, 1, 1)

        self.label_9 = QLabel(self.widget_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_10.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.widget_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_10.addWidget(self.label_10, 0, 3, 1, 1)

        self.label_11 = QLabel(self.widget_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_10.addWidget(self.label_11, 0, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.spin_sisi_jilid = QDoubleSpinBox(self.widget_11)
        self.spin_sisi_jilid.setObjectName(u"spin_sisi_jilid")
        sizePolicy1.setHeightForWidth(self.spin_sisi_jilid.sizePolicy().hasHeightForWidth())
        self.spin_sisi_jilid.setSizePolicy(sizePolicy1)
        self.spin_sisi_jilid.setMinimumSize(QSize(0, 24))
        self.spin_sisi_jilid.setFont(font)
        self.spin_sisi_jilid.setAlignment(Qt.AlignCenter)
        self.spin_sisi_jilid.setDecimals(1)
        self.spin_sisi_jilid.setSingleStep(0.100000000000000)
        self.spin_sisi_jilid.setValue(2.500000000000000)

        self.gridLayout_10.addWidget(self.spin_sisi_jilid, 0, 4, 1, 1)

        self.spin_sisi_lain = QDoubleSpinBox(self.widget_11)
        self.spin_sisi_lain.setObjectName(u"spin_sisi_lain")
        sizePolicy1.setHeightForWidth(self.spin_sisi_lain.sizePolicy().hasHeightForWidth())
        self.spin_sisi_lain.setSizePolicy(sizePolicy1)
        self.spin_sisi_lain.setMinimumSize(QSize(0, 24))
        self.spin_sisi_lain.setFont(font)
        self.spin_sisi_lain.setAlignment(Qt.AlignCenter)
        self.spin_sisi_lain.setDecimals(1)
        self.spin_sisi_lain.setSingleStep(0.100000000000000)
        self.spin_sisi_lain.setValue(1.000000000000000)

        self.gridLayout_10.addWidget(self.spin_sisi_lain, 0, 7, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)


        self.gridLayout_8.addWidget(self.widget_11, 7, 0, 1, 3)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setFamilies([u"Aptos Narrow"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_8.setFont(font1)

        self.gridLayout_8.addWidget(self.label_8, 6, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 5, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_4, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 157, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 13, 1, 1, 1)

        self.widget_9 = QWidget(self.widget_3)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setFont(font)
        self.gridLayout_3 = QGridLayout(self.widget_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_save_pdf = QPushButton(self.widget_9)
        self.btn_save_pdf.setObjectName(u"btn_save_pdf")
        self.btn_save_pdf.setMinimumSize(QSize(0, 30))
        self.btn_save_pdf.setFont(font)

        self.gridLayout_3.addWidget(self.btn_save_pdf, 1, 0, 1, 1)

        self.btn_print = QPushButton(self.widget_9)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setMinimumSize(QSize(0, 30))
        self.btn_print.setFont(font)

        self.gridLayout_3.addWidget(self.btn_print, 1, 1, 1, 1)

        self.radio_open_pdf = QRadioButton(self.widget_9)
        self.radio_open_pdf.setObjectName(u"radio_open_pdf")
        self.radio_open_pdf.setChecked(True)

        self.gridLayout_3.addWidget(self.radio_open_pdf, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_9, 14, 0, 1, 2)

        self.widget_15 = QWidget(self.widget_3)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setFont(font)
        self.gridLayout_15 = QGridLayout(self.widget_15)
        self.gridLayout_15.setSpacing(5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(5, 5, 5, 5)
        self.radio_cover = QRadioButton(self.widget_15)
        self.radio_cover.setObjectName(u"radio_cover")
        self.radio_cover.setFont(font)
        self.radio_cover.setChecked(True)
        self.radio_cover.setAutoExclusive(False)

        self.gridLayout_15.addWidget(self.radio_cover, 1, 0, 1, 1)

        self.radio_agenda = QRadioButton(self.widget_15)
        self.radio_agenda.setObjectName(u"radio_agenda")
        sizePolicy1.setHeightForWidth(self.radio_agenda.sizePolicy().hasHeightForWidth())
        self.radio_agenda.setSizePolicy(sizePolicy1)
        self.radio_agenda.setFont(font)
        self.radio_agenda.setChecked(True)
        self.radio_agenda.setAutoExclusive(False)

        self.gridLayout_15.addWidget(self.radio_agenda, 3, 0, 1, 1)

        self.radio_presensi = QRadioButton(self.widget_15)
        self.radio_presensi.setObjectName(u"radio_presensi")
        self.radio_presensi.setFont(font)
        self.radio_presensi.setChecked(True)
        self.radio_presensi.setAutoExclusive(False)

        self.gridLayout_15.addWidget(self.radio_presensi, 4, 0, 1, 1)

        self.spin_agenda = QSpinBox(self.widget_15)
        self.spin_agenda.setObjectName(u"spin_agenda")
        self.spin_agenda.setMinimumSize(QSize(100, 24))
        self.spin_agenda.setMaximumSize(QSize(100, 16777215))
        self.spin_agenda.setFont(font)
        self.spin_agenda.setAlignment(Qt.AlignCenter)
        self.spin_agenda.setMinimum(1)
        self.spin_agenda.setValue(1)

        self.gridLayout_15.addWidget(self.spin_agenda, 3, 1, 1, 1)

        self.spin_nilai = QSpinBox(self.widget_15)
        self.spin_nilai.setObjectName(u"spin_nilai")
        self.spin_nilai.setMinimumSize(QSize(100, 24))
        self.spin_nilai.setMaximumSize(QSize(100, 16777215))
        self.spin_nilai.setFont(font)
        self.spin_nilai.setAlignment(Qt.AlignCenter)
        self.spin_nilai.setMinimum(1)
        self.spin_nilai.setValue(1)

        self.gridLayout_15.addWidget(self.spin_nilai, 5, 1, 1, 1)

        self.radio_penyerahan = QRadioButton(self.widget_15)
        self.radio_penyerahan.setObjectName(u"radio_penyerahan")
        self.radio_penyerahan.setFont(font)
        self.radio_penyerahan.setChecked(True)
        self.radio_penyerahan.setAutoExclusive(False)

        self.gridLayout_15.addWidget(self.radio_penyerahan, 4, 3, 1, 1)

        self.radio_identitas = QRadioButton(self.widget_15)
        self.radio_identitas.setObjectName(u"radio_identitas")
        self.radio_identitas.setFont(font)
        self.radio_identitas.setChecked(True)
        self.radio_identitas.setAutoExclusive(False)

        self.gridLayout_15.addWidget(self.radio_identitas, 5, 3, 1, 1)

        self.radio_nilai = QRadioButton(self.widget_15)
        self.radio_nilai.setObjectName(u"radio_nilai")
        self.radio_nilai.setFont(font)
        self.radio_nilai.setChecked(True)
        self.radio_nilai.setAutoExclusive(False)

        self.gridLayout_15.addWidget(self.radio_nilai, 5, 0, 1, 1)

        self.radio_pengembalian = QRadioButton(self.widget_15)
        self.radio_pengembalian.setObjectName(u"radio_pengembalian")
        self.radio_pengembalian.setFont(font)
        self.radio_pengembalian.setChecked(True)
        self.radio_pengembalian.setAutoExclusive(False)

        self.gridLayout_15.addWidget(self.radio_pengembalian, 3, 3, 1, 1)

        self.spin_presensi = QSpinBox(self.widget_15)
        self.spin_presensi.setObjectName(u"spin_presensi")
        self.spin_presensi.setMinimumSize(QSize(100, 24))
        self.spin_presensi.setMaximumSize(QSize(100, 16777215))
        self.spin_presensi.setFont(font)
        self.spin_presensi.setAlignment(Qt.AlignCenter)
        self.spin_presensi.setMinimum(1)
        self.spin_presensi.setValue(1)

        self.gridLayout_15.addWidget(self.spin_presensi, 4, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_7, 4, 2, 1, 1)

        self.label_13 = QLabel(self.widget_15)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_15.addWidget(self.label_13, 0, 0, 1, 4)

        self.gridLayout_15.setColumnStretch(2, 1)
        self.gridLayout_15.setColumnStretch(3, 1)

        self.gridLayout_9.addWidget(self.widget_15, 2, 0, 1, 2)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.spin_ibu = QSpinBox(self.widget_5)
        self.spin_ibu.setObjectName(u"spin_ibu")
        self.spin_ibu.setMinimumSize(QSize(100, 24))
        self.spin_ibu.setMaximumSize(QSize(100, 16777215))
        self.spin_ibu.setFont(font)
        self.spin_ibu.setAlignment(Qt.AlignCenter)
        self.spin_ibu.setMinimum(30)
        self.spin_ibu.setSingleStep(1)
        self.spin_ibu.setValue(45)

        self.gridLayout_4.addWidget(self.spin_ibu, 13, 5, 1, 1)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_26 = QLabel(self.widget_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.gridLayout_4.addWidget(self.label_26, 1, 0, 1, 1)

        self.cbo_baris_agenda = QComboBox(self.widget_5)
        self.cbo_baris_agenda.addItem("")
        self.cbo_baris_agenda.addItem("")
        self.cbo_baris_agenda.setObjectName(u"cbo_baris_agenda")
        self.cbo_baris_agenda.setMinimumSize(QSize(100, 24))
        self.cbo_baris_agenda.setMaximumSize(QSize(100, 16777215))
        self.cbo_baris_agenda.setFont(font)

        self.gridLayout_4.addWidget(self.cbo_baris_agenda, 6, 5, 1, 1)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_4.addWidget(self.label_15, 6, 4, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 6, 3, 1, 1)

        self.spin_tinggi_baris_agenda = QDoubleSpinBox(self.widget_5)
        self.spin_tinggi_baris_agenda.setObjectName(u"spin_tinggi_baris_agenda")
        self.spin_tinggi_baris_agenda.setMinimumSize(QSize(100, 24))
        self.spin_tinggi_baris_agenda.setMaximumSize(QSize(100, 16777215))
        self.spin_tinggi_baris_agenda.setFont(font)
        self.spin_tinggi_baris_agenda.setAlignment(Qt.AlignCenter)
        self.spin_tinggi_baris_agenda.setDecimals(1)
        self.spin_tinggi_baris_agenda.setSingleStep(0.100000000000000)
        self.spin_tinggi_baris_agenda.setValue(6.500000000000000)

        self.gridLayout_4.addWidget(self.spin_tinggi_baris_agenda, 6, 2, 1, 1)

        self.label_25 = QLabel(self.widget_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.gridLayout_4.addWidget(self.label_25, 5, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.label_22 = QLabel(self.widget_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.gridLayout_4.addWidget(self.label_22, 13, 4, 1, 1)

        self.spin_ayah = QSpinBox(self.widget_5)
        self.spin_ayah.setObjectName(u"spin_ayah")
        self.spin_ayah.setMinimumSize(QSize(100, 24))
        self.spin_ayah.setMaximumSize(QSize(100, 16777215))
        self.spin_ayah.setFont(font)
        self.spin_ayah.setAlignment(Qt.AlignCenter)
        self.spin_ayah.setMinimum(30)
        self.spin_ayah.setSingleStep(1)
        self.spin_ayah.setValue(45)

        self.gridLayout_4.addWidget(self.spin_ayah, 12, 5, 1, 1)

        self.spin_kolom_nama_lengkap = QSpinBox(self.widget_5)
        self.spin_kolom_nama_lengkap.setObjectName(u"spin_kolom_nama_lengkap")
        self.spin_kolom_nama_lengkap.setMinimumSize(QSize(100, 24))
        self.spin_kolom_nama_lengkap.setMaximumSize(QSize(100, 16777215))
        self.spin_kolom_nama_lengkap.setFont(font)
        self.spin_kolom_nama_lengkap.setAlignment(Qt.AlignCenter)
        self.spin_kolom_nama_lengkap.setMinimum(0)
        self.spin_kolom_nama_lengkap.setSingleStep(1)
        self.spin_kolom_nama_lengkap.setValue(60)

        self.gridLayout_4.addWidget(self.spin_kolom_nama_lengkap, 12, 2, 1, 1)

        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 5)

        self.spin_tinggi_baris = QDoubleSpinBox(self.widget_5)
        self.spin_tinggi_baris.setObjectName(u"spin_tinggi_baris")
        self.spin_tinggi_baris.setMinimumSize(QSize(100, 24))
        self.spin_tinggi_baris.setMaximumSize(QSize(100, 16777215))
        self.spin_tinggi_baris.setFont(font)
        self.spin_tinggi_baris.setAlignment(Qt.AlignCenter)
        self.spin_tinggi_baris.setDecimals(1)
        self.spin_tinggi_baris.setSingleStep(0.100000000000000)
        self.spin_tinggi_baris.setValue(6.500000000000000)

        self.gridLayout_4.addWidget(self.spin_tinggi_baris, 3, 5, 1, 1)

        self.spin_jumlah_baris = QSpinBox(self.widget_5)
        self.spin_jumlah_baris.setObjectName(u"spin_jumlah_baris")
        self.spin_jumlah_baris.setMinimumSize(QSize(100, 24))
        self.spin_jumlah_baris.setMaximumSize(QSize(100, 16777215))
        self.spin_jumlah_baris.setFont(font)
        self.spin_jumlah_baris.setAlignment(Qt.AlignCenter)
        self.spin_jumlah_baris.setMinimum(1)
        self.spin_jumlah_baris.setSingleStep(1)
        self.spin_jumlah_baris.setValue(30)

        self.gridLayout_4.addWidget(self.spin_jumlah_baris, 2, 5, 1, 1)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_5, 2, 4, 1, 1)

        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_4.addWidget(self.label_16, 3, 4, 1, 1)

        self.label_27 = QLabel(self.widget_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.gridLayout_4.addWidget(self.label_27, 11, 0, 1, 3)

        self.label_12 = QLabel(self.widget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_4.addWidget(self.label_12, 12, 0, 1, 1)

        self.label_21 = QLabel(self.widget_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout_4.addWidget(self.label_21, 12, 4, 1, 1)

        self.label_28 = QLabel(self.widget_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.gridLayout_4.addWidget(self.label_28, 8, 0, 1, 4)

        self.label_23 = QLabel(self.widget_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_4.addWidget(self.label_23, 13, 0, 1, 1)

        self.spin_alamat = QSpinBox(self.widget_5)
        self.spin_alamat.setObjectName(u"spin_alamat")
        self.spin_alamat.setMinimumSize(QSize(100, 24))
        self.spin_alamat.setMaximumSize(QSize(100, 16777215))
        self.spin_alamat.setFont(font)
        self.spin_alamat.setAlignment(Qt.AlignCenter)
        self.spin_alamat.setMinimum(20)
        self.spin_alamat.setSingleStep(1)
        self.spin_alamat.setValue(35)

        self.gridLayout_4.addWidget(self.spin_alamat, 13, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 10, 0, 1, 1)

        self.spin_kolom_nama_singkat = QSpinBox(self.widget_5)
        self.spin_kolom_nama_singkat.setObjectName(u"spin_kolom_nama_singkat")
        self.spin_kolom_nama_singkat.setMinimumSize(QSize(100, 24))
        self.spin_kolom_nama_singkat.setMaximumSize(QSize(100, 16777215))
        self.spin_kolom_nama_singkat.setFont(font)
        self.spin_kolom_nama_singkat.setAlignment(Qt.AlignCenter)
        self.spin_kolom_nama_singkat.setMinimum(0)
        self.spin_kolom_nama_singkat.setSingleStep(1)
        self.spin_kolom_nama_singkat.setValue(50)

        self.gridLayout_4.addWidget(self.spin_kolom_nama_singkat, 2, 2, 1, 1)

        self.spin_kolom_tanggal = QDoubleSpinBox(self.widget_5)
        self.spin_kolom_tanggal.setObjectName(u"spin_kolom_tanggal")
        self.spin_kolom_tanggal.setMinimumSize(QSize(100, 24))
        self.spin_kolom_tanggal.setMaximumSize(QSize(100, 16777215))
        self.spin_kolom_tanggal.setFont(font)
        self.spin_kolom_tanggal.setAlignment(Qt.AlignCenter)
        self.spin_kolom_tanggal.setDecimals(1)
        self.spin_kolom_tanggal.setSingleStep(0.100000000000000)
        self.spin_kolom_tanggal.setValue(4.500000000000000)

        self.gridLayout_4.addWidget(self.spin_kolom_tanggal, 8, 5, 1, 1)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 8, 4, 1, 1)


        self.gridLayout_9.addWidget(self.widget_5, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Semester", None))
        self.cbo_semester.setItemText(0, QCoreApplication.translate("Form", u"Ganjil", None))
        self.cbo_semester.setItemText(1, QCoreApplication.translate("Form", u"Genap", None))

        self.label_18.setText(QCoreApplication.translate("Form", u"Guru", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.cbo_kertas.setItemText(0, QCoreApplication.translate("Form", u"A4", None))
        self.cbo_kertas.setItemText(1, QCoreApplication.translate("Form", u"F4", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"Kertas", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Sisi Jilid", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Sisi Lain", None))
#if QT_CONFIG(tooltip)
        self.spin_sisi_jilid.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>jarak dari pinggir yang akan dijilid, biasanya lebih lebar dari sisi lain</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.spin_sisi_jilid.setSuffix(QCoreApplication.translate("Form", u" cm", None))
#if QT_CONFIG(tooltip)
        self.spin_sisi_lain.setToolTip(QCoreApplication.translate("Form", u"sisi bagian yang akan digeser", None))
#endif // QT_CONFIG(tooltip)
        self.spin_sisi_lain.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Pengaturan Kertas", None))
        self.btn_save_pdf.setText(QCoreApplication.translate("Form", u"Save PDF", None))
        self.btn_print.setText(QCoreApplication.translate("Form", u"Print", None))
        self.radio_open_pdf.setText(QCoreApplication.translate("Form", u"Buka Explorer", None))
        self.radio_cover.setText(QCoreApplication.translate("Form", u"Cover", None))
        self.radio_agenda.setText(QCoreApplication.translate("Form", u"Agenda Harian", None))
        self.radio_presensi.setText(QCoreApplication.translate("Form", u"Presensi Harian", None))
        self.spin_agenda.setSuffix(QCoreApplication.translate("Form", u" lembar", None))
        self.spin_nilai.setSuffix(QCoreApplication.translate("Form", u" lembar", None))
        self.radio_penyerahan.setText(QCoreApplication.translate("Form", u"Penyerahan Rapor", None))
        self.radio_identitas.setText(QCoreApplication.translate("Form", u"Identitas Siswa", None))
        self.radio_nilai.setText(QCoreApplication.translate("Form", u"Daftar Nilai", None))
        self.radio_pengembalian.setText(QCoreApplication.translate("Form", u"Pengembalian Rapor", None))
        self.spin_presensi.setSuffix(QCoreApplication.translate("Form", u" lembar", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"HALAMAN YANG AKAN DICETAK", None))
        self.spin_ibu.setSuffix(QCoreApplication.translate("Form", u" mm", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"lebar kolom nama", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Umum", None))
        self.cbo_baris_agenda.setItemText(0, QCoreApplication.translate("Form", u"2 baris", None))
        self.cbo_baris_agenda.setItemText(1, QCoreApplication.translate("Form", u"3 baris", None))

#if QT_CONFIG(tooltip)
        self.cbo_baris_agenda.setToolTip(QCoreApplication.translate("Form", u"jumlah baris tiap hari", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Tinggi baris", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Baris Per Hari", None))
        self.spin_tinggi_baris_agenda.setPrefix("")
        self.spin_tinggi_baris_agenda.setSuffix(QCoreApplication.translate("Form", u" mm", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Halaman Agenda", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Ibu", None))
        self.spin_ayah.setSuffix(QCoreApplication.translate("Form", u" mm", None))
        self.spin_kolom_nama_lengkap.setSuffix(QCoreApplication.translate("Form", u" mm", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"PENGATURAN SPESIFIK HALAMAN", None))
        self.spin_tinggi_baris.setPrefix("")
        self.spin_tinggi_baris.setSuffix(QCoreApplication.translate("Form", u" mm", None))
#if QT_CONFIG(tooltip)
        self.spin_jumlah_baris.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>jumlah baris yang ditampilkan, set melebihi jumlah santri jika ingin menambahkan baris kosong</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.spin_jumlah_baris.setSuffix(QCoreApplication.translate("Form", u" baris", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Jumlah Baris", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Tinggi Baris", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Halaman Identitas", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Nama Lengkap", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Ayah", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Halaman Daftar Nilai", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.spin_alamat.setSuffix(QCoreApplication.translate("Form", u" mm", None))
#if QT_CONFIG(tooltip)
        self.spin_kolom_nama_singkat.setToolTip(QCoreApplication.translate("Form", u"lebar kolom nama pada tabel", None))
#endif // QT_CONFIG(tooltip)
        self.spin_kolom_nama_singkat.setSuffix(QCoreApplication.translate("Form", u" mm", None))
        self.spin_kolom_tanggal.setPrefix("")
        self.spin_kolom_tanggal.setSuffix(QCoreApplication.translate("Form", u" mm", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Lebar tanggal", None))
    # retranslateUi

