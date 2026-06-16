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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDoubleSpinBox, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(996, 864)
        self.gridLayout_8 = QGridLayout(Form)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(400, 0))
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_generate_pdf = QPushButton(self.widget_7)
        self.btn_generate_pdf.setObjectName(u"btn_generate_pdf")
        self.btn_generate_pdf.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.btn_generate_pdf, 1, 0, 1, 1)

        self.btn_save_pdf = QPushButton(self.widget_7)
        self.btn_save_pdf.setObjectName(u"btn_save_pdf")
        self.btn_save_pdf.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.btn_save_pdf, 1, 1, 1, 1)

        self.btn_print = QPushButton(self.widget_7)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.btn_print, 1, 2, 1, 1)

        self.btn_send_whatsapp = QPushButton(self.widget_7)
        self.btn_send_whatsapp.setObjectName(u"btn_send_whatsapp")
        self.btn_send_whatsapp.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.btn_send_whatsapp, 2, 0, 1, 3)


        self.gridLayout_7.addWidget(self.widget_7, 3, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.widget_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 350, 552))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(5)
        self.gridLayout_12.setVerticalSpacing(10)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.gridLayout_11 = QGridLayout(self.groupBox_5)
        self.gridLayout_11.setSpacing(5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.radio_show_walas = QRadioButton(self.groupBox_5)
        self.radio_show_walas.setObjectName(u"radio_show_walas")
        self.radio_show_walas.setMinimumSize(QSize(100, 0))
        self.radio_show_walas.setChecked(True)
        self.radio_show_walas.setAutoExclusive(False)

        self.gridLayout_11.addWidget(self.radio_show_walas, 1, 0, 1, 1)

        self.radio_show_mudir = QRadioButton(self.groupBox_5)
        self.radio_show_mudir.setObjectName(u"radio_show_mudir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.radio_show_mudir.sizePolicy().hasHeightForWidth())
        self.radio_show_mudir.setSizePolicy(sizePolicy1)
        self.radio_show_mudir.setMinimumSize(QSize(100, 0))
        self.radio_show_mudir.setChecked(True)
        self.radio_show_mudir.setAutoExclusive(False)

        self.gridLayout_11.addWidget(self.radio_show_mudir, 0, 0, 1, 1)

        self.spin_size_walas = QDoubleSpinBox(self.groupBox_5)
        self.spin_size_walas.setObjectName(u"spin_size_walas")
        self.spin_size_walas.setMinimumSize(QSize(0, 25))
        self.spin_size_walas.setAlignment(Qt.AlignCenter)
        self.spin_size_walas.setAccelerated(True)
        self.spin_size_walas.setDecimals(1)
        self.spin_size_walas.setMinimum(-5.000000000000000)
        self.spin_size_walas.setSingleStep(0.100000000000000)
        self.spin_size_walas.setValue(2.000000000000000)

        self.gridLayout_11.addWidget(self.spin_size_walas, 1, 1, 1, 1)

        self.spin_size_mudir = QDoubleSpinBox(self.groupBox_5)
        self.spin_size_mudir.setObjectName(u"spin_size_mudir")
        self.spin_size_mudir.setMinimumSize(QSize(0, 25))
        self.spin_size_mudir.setAlignment(Qt.AlignCenter)
        self.spin_size_mudir.setAccelerated(True)
        self.spin_size_mudir.setDecimals(1)
        self.spin_size_mudir.setMinimum(-5.000000000000000)
        self.spin_size_mudir.setSingleStep(0.100000000000000)
        self.spin_size_mudir.setValue(1.400000000000000)

        self.gridLayout_11.addWidget(self.spin_size_mudir, 0, 1, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.group_bio = QGroupBox(self.scrollAreaWidgetContents)
        self.group_bio.setObjectName(u"group_bio")
        sizePolicy.setHeightForWidth(self.group_bio.sizePolicy().hasHeightForWidth())
        self.group_bio.setSizePolicy(sizePolicy)
        self.group_bio.setCheckable(False)
        self.group_bio.setChecked(False)
        self.verticalLayout_3 = QVBoxLayout(self.group_bio)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.widget_17 = QWidget(self.group_bio)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_16 = QGridLayout(self.widget_17)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_17)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_10 = QGridLayout(self.widget_13)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(3)
        self.gridLayout_10.setVerticalSpacing(5)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_14, 1, 1, 1, 1)

        self.label_16 = QLabel(self.widget_13)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_16, 1, 2, 1, 1)

        self.spin_bio_x_mudir = QDoubleSpinBox(self.widget_13)
        self.spin_bio_x_mudir.setObjectName(u"spin_bio_x_mudir")
        self.spin_bio_x_mudir.setMinimumSize(QSize(0, 25))
        self.spin_bio_x_mudir.setAlignment(Qt.AlignCenter)
        self.spin_bio_x_mudir.setAccelerated(True)
        self.spin_bio_x_mudir.setDecimals(1)
        self.spin_bio_x_mudir.setMinimum(-5.000000000000000)
        self.spin_bio_x_mudir.setSingleStep(0.100000000000000)

        self.gridLayout_10.addWidget(self.spin_bio_x_mudir, 2, 1, 1, 1)

        self.spin_bio_y_mudir = QDoubleSpinBox(self.widget_13)
        self.spin_bio_y_mudir.setObjectName(u"spin_bio_y_mudir")
        self.spin_bio_y_mudir.setMinimumSize(QSize(0, 25))
        self.spin_bio_y_mudir.setAlignment(Qt.AlignCenter)
        self.spin_bio_y_mudir.setAccelerated(True)
        self.spin_bio_y_mudir.setDecimals(1)
        self.spin_bio_y_mudir.setMinimum(-5.000000000000000)
        self.spin_bio_y_mudir.setSingleStep(0.100000000000000)

        self.gridLayout_10.addWidget(self.spin_bio_y_mudir, 2, 2, 1, 1)

        self.label_30 = QLabel(self.widget_13)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_10.addWidget(self.label_30, 2, 0, 1, 1)

        self.spin_bio_tinggi = QDoubleSpinBox(self.widget_13)
        self.spin_bio_tinggi.setObjectName(u"spin_bio_tinggi")
        self.spin_bio_tinggi.setMinimumSize(QSize(0, 25))
        self.spin_bio_tinggi.setAlignment(Qt.AlignCenter)
        self.spin_bio_tinggi.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spin_bio_tinggi.setAccelerated(True)
        self.spin_bio_tinggi.setDecimals(2)
        self.spin_bio_tinggi.setMaximum(2.000000000000000)
        self.spin_bio_tinggi.setSingleStep(0.050000000000000)
        self.spin_bio_tinggi.setValue(0.600000000000000)

        self.gridLayout_10.addWidget(self.spin_bio_tinggi, 2, 3, 1, 1)

        self.label_12 = QLabel(self.widget_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_12, 1, 3, 1, 1)


        self.gridLayout_16.addWidget(self.widget_13, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_17)


        self.gridLayout_12.addWidget(self.group_bio, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setCheckable(False)
        self.gridLayout_17 = QGridLayout(self.groupBox_4)
        self.gridLayout_17.setSpacing(5)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(5, 5, 5, 5)
        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_17.addWidget(self.label_28, 4, 0, 1, 1)

        self.label_29 = QLabel(self.groupBox_4)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_17.addWidget(self.label_29, 5, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)

        self.gridLayout_17.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_23, 3, 1, 1, 1)

        self.spin_catatan_y_walas = QDoubleSpinBox(self.groupBox_4)
        self.spin_catatan_y_walas.setObjectName(u"spin_catatan_y_walas")
        self.spin_catatan_y_walas.setMinimumSize(QSize(0, 25))
        self.spin_catatan_y_walas.setAlignment(Qt.AlignCenter)
        self.spin_catatan_y_walas.setAccelerated(True)
        self.spin_catatan_y_walas.setDecimals(1)
        self.spin_catatan_y_walas.setMinimum(-5.000000000000000)
        self.spin_catatan_y_walas.setSingleStep(0.100000000000000)

        self.gridLayout_17.addWidget(self.spin_catatan_y_walas, 4, 2, 1, 1)

        self.label_24 = QLabel(self.groupBox_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_24, 3, 2, 1, 1)

        self.spin_catatan_x_walas = QDoubleSpinBox(self.groupBox_4)
        self.spin_catatan_x_walas.setObjectName(u"spin_catatan_x_walas")
        self.spin_catatan_x_walas.setMinimumSize(QSize(0, 25))
        self.spin_catatan_x_walas.setAlignment(Qt.AlignCenter)
        self.spin_catatan_x_walas.setAccelerated(True)
        self.spin_catatan_x_walas.setDecimals(1)
        self.spin_catatan_x_walas.setMinimum(-5.000000000000000)
        self.spin_catatan_x_walas.setSingleStep(0.100000000000000)

        self.gridLayout_17.addWidget(self.spin_catatan_x_walas, 4, 1, 1, 1)

        self.spin_catatan_x_mudir = QDoubleSpinBox(self.groupBox_4)
        self.spin_catatan_x_mudir.setObjectName(u"spin_catatan_x_mudir")
        self.spin_catatan_x_mudir.setMinimumSize(QSize(0, 25))
        self.spin_catatan_x_mudir.setAlignment(Qt.AlignCenter)
        self.spin_catatan_x_mudir.setAccelerated(True)
        self.spin_catatan_x_mudir.setDecimals(1)
        self.spin_catatan_x_mudir.setMinimum(-5.000000000000000)
        self.spin_catatan_x_mudir.setSingleStep(0.100000000000000)

        self.gridLayout_17.addWidget(self.spin_catatan_x_mudir, 5, 1, 1, 1)

        self.spin_catatan_jarak = QDoubleSpinBox(self.groupBox_4)
        self.spin_catatan_jarak.setObjectName(u"spin_catatan_jarak")
        self.spin_catatan_jarak.setMinimumSize(QSize(75, 25))
        self.spin_catatan_jarak.setAlignment(Qt.AlignCenter)
        self.spin_catatan_jarak.setAccelerated(True)
        self.spin_catatan_jarak.setDecimals(0)
        self.spin_catatan_jarak.setMaximum(50.000000000000000)
        self.spin_catatan_jarak.setSingleStep(3.000000000000000)
        self.spin_catatan_jarak.setValue(12.000000000000000)

        self.gridLayout_17.addWidget(self.spin_catatan_jarak, 1, 1, 1, 1)

        self.spin_catatan_y_mudir = QDoubleSpinBox(self.groupBox_4)
        self.spin_catatan_y_mudir.setObjectName(u"spin_catatan_y_mudir")
        self.spin_catatan_y_mudir.setMinimumSize(QSize(0, 25))
        self.spin_catatan_y_mudir.setAlignment(Qt.AlignCenter)
        self.spin_catatan_y_mudir.setAccelerated(True)
        self.spin_catatan_y_mudir.setDecimals(1)
        self.spin_catatan_y_mudir.setMinimum(-5.000000000000000)
        self.spin_catatan_y_mudir.setSingleStep(0.100000000000000)

        self.gridLayout_17.addWidget(self.spin_catatan_y_mudir, 5, 2, 1, 1)

        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_20, 3, 3, 1, 1)

        self.spin_catatan_tinggi = QDoubleSpinBox(self.groupBox_4)
        self.spin_catatan_tinggi.setObjectName(u"spin_catatan_tinggi")
        self.spin_catatan_tinggi.setMinimumSize(QSize(0, 25))
        self.spin_catatan_tinggi.setAlignment(Qt.AlignCenter)
        self.spin_catatan_tinggi.setAccelerated(True)
        self.spin_catatan_tinggi.setDecimals(2)
        self.spin_catatan_tinggi.setMaximum(2.000000000000000)
        self.spin_catatan_tinggi.setSingleStep(0.100000000000000)
        self.spin_catatan_tinggi.setValue(0.600000000000000)

        self.gridLayout_17.addWidget(self.spin_catatan_tinggi, 4, 3, 1, 1)

        self.label_22 = QLabel(self.groupBox_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_17.addWidget(self.label_22, 1, 2, 1, 1)

        self.spin_catatan_size = QDoubleSpinBox(self.groupBox_4)
        self.spin_catatan_size.setObjectName(u"spin_catatan_size")
        self.spin_catatan_size.setMinimumSize(QSize(75, 25))
        self.spin_catatan_size.setAlignment(Qt.AlignCenter)
        self.spin_catatan_size.setAccelerated(True)
        self.spin_catatan_size.setDecimals(0)
        self.spin_catatan_size.setMaximum(50.000000000000000)
        self.spin_catatan_size.setSingleStep(1.000000000000000)
        self.spin_catatan_size.setValue(12.000000000000000)

        self.gridLayout_17.addWidget(self.spin_catatan_size, 1, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_2, 2, 2, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_4, 3, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setCheckable(False)
        self.gridLayout_13 = QGridLayout(self.groupBox_3)
        self.gridLayout_13.setSpacing(5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(5, 5, 5, 5)
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_17, 1, 1, 1, 1)

        self.spin_nilai_y_walas = QDoubleSpinBox(self.groupBox_3)
        self.spin_nilai_y_walas.setObjectName(u"spin_nilai_y_walas")
        self.spin_nilai_y_walas.setMinimumSize(QSize(0, 25))
        self.spin_nilai_y_walas.setAlignment(Qt.AlignCenter)
        self.spin_nilai_y_walas.setAccelerated(True)
        self.spin_nilai_y_walas.setDecimals(1)
        self.spin_nilai_y_walas.setMinimum(-5.000000000000000)
        self.spin_nilai_y_walas.setSingleStep(0.100000000000000)

        self.gridLayout_13.addWidget(self.spin_nilai_y_walas, 2, 2, 1, 1)

        self.spin_nilai_x_walas = QDoubleSpinBox(self.groupBox_3)
        self.spin_nilai_x_walas.setObjectName(u"spin_nilai_x_walas")
        self.spin_nilai_x_walas.setMinimumSize(QSize(0, 25))
        self.spin_nilai_x_walas.setAlignment(Qt.AlignCenter)
        self.spin_nilai_x_walas.setAccelerated(True)
        self.spin_nilai_x_walas.setDecimals(1)
        self.spin_nilai_x_walas.setMinimum(-5.000000000000000)
        self.spin_nilai_x_walas.setSingleStep(0.100000000000000)

        self.gridLayout_13.addWidget(self.spin_nilai_x_walas, 2, 1, 1, 1)

        self.spin_nilai_x_mudir = QDoubleSpinBox(self.groupBox_3)
        self.spin_nilai_x_mudir.setObjectName(u"spin_nilai_x_mudir")
        self.spin_nilai_x_mudir.setMinimumSize(QSize(0, 25))
        self.spin_nilai_x_mudir.setAlignment(Qt.AlignCenter)
        self.spin_nilai_x_mudir.setAccelerated(True)
        self.spin_nilai_x_mudir.setDecimals(1)
        self.spin_nilai_x_mudir.setMinimum(-5.000000000000000)
        self.spin_nilai_x_mudir.setSingleStep(0.100000000000000)

        self.gridLayout_13.addWidget(self.spin_nilai_x_mudir, 3, 1, 1, 1)

        self.spin_nilai_y_mudir = QDoubleSpinBox(self.groupBox_3)
        self.spin_nilai_y_mudir.setObjectName(u"spin_nilai_y_mudir")
        self.spin_nilai_y_mudir.setMinimumSize(QSize(0, 25))
        self.spin_nilai_y_mudir.setAlignment(Qt.AlignCenter)
        self.spin_nilai_y_mudir.setAccelerated(True)
        self.spin_nilai_y_mudir.setDecimals(1)
        self.spin_nilai_y_mudir.setMinimum(-5.000000000000000)
        self.spin_nilai_y_mudir.setSingleStep(0.100000000000000)

        self.gridLayout_13.addWidget(self.spin_nilai_y_mudir, 3, 2, 1, 1)

        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_13.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_18, 1, 2, 1, 1)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_13.addWidget(self.label_27, 3, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_13, 1, 3, 1, 1)

        self.spin_nilai_tinggi = QDoubleSpinBox(self.groupBox_3)
        self.spin_nilai_tinggi.setObjectName(u"spin_nilai_tinggi")
        self.spin_nilai_tinggi.setMinimumSize(QSize(0, 25))
        self.spin_nilai_tinggi.setAlignment(Qt.AlignCenter)
        self.spin_nilai_tinggi.setAccelerated(True)
        self.spin_nilai_tinggi.setDecimals(2)
        self.spin_nilai_tinggi.setMaximum(2.000000000000000)
        self.spin_nilai_tinggi.setSingleStep(0.100000000000000)
        self.spin_nilai_tinggi.setValue(0.600000000000000)

        self.gridLayout_13.addWidget(self.spin_nilai_tinggi, 2, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_13.addWidget(self.label_15, 0, 0, 1, 1)

        self.cbo_peringkat = QComboBox(self.groupBox_3)
        self.cbo_peringkat.addItem("")
        self.cbo_peringkat.addItem("")
        self.cbo_peringkat.addItem("")
        self.cbo_peringkat.setObjectName(u"cbo_peringkat")

        self.gridLayout_13.addWidget(self.cbo_peringkat, 0, 1, 1, 2)


        self.gridLayout_12.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 4, 0, 1, 1)

        self.groupBox = QGroupBox(self.widget_5)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_16 = QWidget(self.groupBox)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_2 = QVBoxLayout(self.widget_16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_16)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
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


        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_16)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setMinimumSize(QSize(0, 24))
        self.gridLayout_4 = QGridLayout(self.widget_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.spin_left = QDoubleSpinBox(self.widget_10)
        self.spin_left.setObjectName(u"spin_left")
        self.spin_left.setMinimumSize(QSize(0, 20))
        self.spin_left.setAlignment(Qt.AlignCenter)
        self.spin_left.setAccelerated(True)
        self.spin_left.setDecimals(1)
        self.spin_left.setSingleStep(0.100000000000000)
        self.spin_left.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_left, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_8 = QLabel(self.widget_10)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 2, 1, 1)

        self.spin_right = QDoubleSpinBox(self.widget_10)
        self.spin_right.setObjectName(u"spin_right")
        self.spin_right.setMinimumSize(QSize(0, 20))
        self.spin_right.setAlignment(Qt.AlignCenter)
        self.spin_right.setAccelerated(True)
        self.spin_right.setDecimals(1)
        self.spin_right.setSingleStep(0.100000000000000)
        self.spin_right.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_right, 1, 2, 1, 1)

        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 3, 1, 1)

        self.spin_top = QDoubleSpinBox(self.widget_10)
        self.spin_top.setObjectName(u"spin_top")
        self.spin_top.setMinimumSize(QSize(0, 20))
        self.spin_top.setAlignment(Qt.AlignCenter)
        self.spin_top.setAccelerated(True)
        self.spin_top.setDecimals(1)
        self.spin_top.setSingleStep(0.100000000000000)
        self.spin_top.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_top, 1, 3, 1, 1)

        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 4, 1, 1)

        self.spin_bottom = QDoubleSpinBox(self.widget_10)
        self.spin_bottom.setObjectName(u"spin_bottom")
        self.spin_bottom.setMinimumSize(QSize(0, 20))
        self.spin_bottom.setAlignment(Qt.AlignCenter)
        self.spin_bottom.setAccelerated(True)
        self.spin_bottom.setDecimals(1)
        self.spin_bottom.setSingleStep(0.100000000000000)
        self.spin_bottom.setValue(1.500000000000000)

        self.gridLayout_4.addWidget(self.spin_bottom, 1, 4, 1, 1)

        self.label_10 = QLabel(self.widget_10)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_10)


        self.verticalLayout.addWidget(self.widget_16)


        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)

        self.widget_15 = QWidget(self.widget_5)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.gridLayout_15 = QGridLayout(self.widget_15)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.btn_reset_setting = QPushButton(self.widget_15)
        self.btn_reset_setting.setObjectName(u"btn_reset_setting")
        self.btn_reset_setting.setMinimumSize(QSize(80, 24))

        self.gridLayout_15.addWidget(self.btn_reset_setting, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_15, 0, 0, 1, 1)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QGridLayout(self.widget_8)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cbo_halaman = QComboBox(self.widget_8)
        self.cbo_halaman.addItem("")
        self.cbo_halaman.addItem("")
        self.cbo_halaman.addItem("")
        self.cbo_halaman.addItem("")
        self.cbo_halaman.setObjectName(u"cbo_halaman")
        self.cbo_halaman.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.cbo_halaman, 2, 1, 1, 4)

        self.opsi_cover = QRadioButton(self.widget_8)
        self.opsi_cover.setObjectName(u"opsi_cover")
        self.opsi_cover.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_cover, 3, 0, 1, 1)

        self.opsi_mutasi = QRadioButton(self.widget_8)
        self.opsi_mutasi.setObjectName(u"opsi_mutasi")
        self.opsi_mutasi.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_mutasi, 3, 3, 1, 1)

        self.opsi_petunjuk = QRadioButton(self.widget_8)
        self.opsi_petunjuk.setObjectName(u"opsi_petunjuk")
        self.opsi_petunjuk.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_petunjuk, 4, 3, 1, 1)

        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_5.setFont(font)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 2)

        self.opsi_catatan = QRadioButton(self.widget_8)
        self.opsi_catatan.setObjectName(u"opsi_catatan")
        self.opsi_catatan.setChecked(True)
        self.opsi_catatan.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_catatan, 4, 2, 1, 1)

        self.opsi_nilai = QRadioButton(self.widget_8)
        self.opsi_nilai.setObjectName(u"opsi_nilai")
        self.opsi_nilai.setChecked(True)
        self.opsi_nilai.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_nilai, 3, 2, 1, 1)

        self.opsi_id_siswa = QRadioButton(self.widget_8)
        self.opsi_id_siswa.setObjectName(u"opsi_id_siswa")
        self.opsi_id_siswa.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_id_siswa, 4, 1, 1, 1)

        self.opsi_id_madrasah = QRadioButton(self.widget_8)
        self.opsi_id_madrasah.setObjectName(u"opsi_id_madrasah")
        self.opsi_id_madrasah.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.opsi_id_madrasah, 3, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_8, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_5, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget_2, 0, 2, 1, 1)

        self.gridLayout_8.setColumnStretch(1, 1)
        self.gridLayout_8.setColumnMinimumWidth(0, 350)
        self.gridLayout_8.setColumnMinimumWidth(2, 350)

        self.retranslateUi(Form)
        self.groupBox.toggled.connect(self.widget_16.setVisible)
        self.opsi_nilai.toggled.connect(self.groupBox_3.setVisible)
        self.opsi_catatan.toggled.connect(self.groupBox_4.setVisible)
        self.opsi_id_siswa.toggled.connect(self.group_bio.setVisible)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.btn_generate_pdf.setText(QCoreApplication.translate("Form", u"PDF Perkelas", None))
        self.btn_save_pdf.setText(QCoreApplication.translate("Form", u"Save PDF", None))
        self.btn_print.setText(QCoreApplication.translate("Form", u"Print", None))
        self.btn_send_whatsapp.setText(QCoreApplication.translate("Form", u"Kirim ke WA Wali Kelas", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Umum", None))
        self.radio_show_walas.setText(QCoreApplication.translate("Form", u"TTD Wali Kelas", None))
        self.radio_show_mudir.setText(QCoreApplication.translate("Form", u"TTD Mudir", None))
        self.spin_size_walas.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_size_mudir.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.group_bio.setTitle(QCoreApplication.translate("Form", u"Pengaturan Halaman Biodata Siswa", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Y", None))
        self.spin_bio_x_mudir.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_bio_y_mudir.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Mudir", None))
        self.spin_bio_tinggi.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Tinggi Baris", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Pengaturan Halaman Catatan", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Wali Kelas", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Mudir", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Jarak Catatan", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"X", None))
        self.spin_catatan_y_walas.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Y", None))
        self.spin_catatan_x_walas.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_catatan_x_mudir.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_catatan_jarak.setSuffix(QCoreApplication.translate("Form", u" pt", None))
        self.spin_catatan_y_mudir.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Tinggi Baris", None))
        self.spin_catatan_tinggi.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Ukuran Catatan", None))
        self.spin_catatan_size.setSuffix(QCoreApplication.translate("Form", u" pt", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Pengaturan Halaman Nilai", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"X", None))
        self.spin_nilai_y_walas.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_nilai_x_walas.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_nilai_x_mudir.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_nilai_y_mudir.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Wali Kelas", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Mudir", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Tinggi Baris", None))
        self.spin_nilai_tinggi.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Opsi Peringkat", None))
        self.cbo_peringkat.setItemText(0, QCoreApplication.translate("Form", u"10 Besar", None))
        self.cbo_peringkat.setItemText(1, QCoreApplication.translate("Form", u"Seluruhnya", None))
        self.cbo_peringkat.setItemText(2, QCoreApplication.translate("Form", u"Tidak Ditampilkan", None))

        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Pengaturan Kertas", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Kertas", None))
        self.cbo_kertas.setItemText(0, QCoreApplication.translate("Form", u"A4", None))
        self.cbo_kertas.setItemText(1, QCoreApplication.translate("Form", u"F4", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Orientasi", None))
        self.cbo_orientasi.setItemText(0, QCoreApplication.translate("Form", u"Portrait", None))
        self.cbo_orientasi.setItemText(1, QCoreApplication.translate("Form", u"Landscape", None))

        self.spin_left.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Left", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Right", None))
        self.spin_right.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Top", None))
        self.spin_top.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Bottom", None))
        self.spin_bottom.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Margin", None))
        self.btn_reset_setting.setText(QCoreApplication.translate("Form", u"Reset Setting", None))
        self.cbo_halaman.setItemText(0, QCoreApplication.translate("Form", u"Nilai dan Identitas", None))
        self.cbo_halaman.setItemText(1, QCoreApplication.translate("Form", u"Nilai", None))
        self.cbo_halaman.setItemText(2, QCoreApplication.translate("Form", u"Identitas", None))
        self.cbo_halaman.setItemText(3, QCoreApplication.translate("Form", u"Custom", None))

        self.opsi_cover.setText(QCoreApplication.translate("Form", u"Cover", None))
        self.opsi_mutasi.setText(QCoreApplication.translate("Form", u"Mutasi", None))
        self.opsi_petunjuk.setText(QCoreApplication.translate("Form", u"Petunjuk", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Opsi Halaman", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Halaman Rapor", None))
        self.opsi_catatan.setText(QCoreApplication.translate("Form", u"Catatan", None))
        self.opsi_nilai.setText(QCoreApplication.translate("Form", u"Nilai", None))
        self.opsi_id_siswa.setText(QCoreApplication.translate("Form", u"Identitas Siswa", None))
        self.opsi_id_madrasah.setText(QCoreApplication.translate("Form", u"Identitas Madrasah", None))
    # retranslateUi

