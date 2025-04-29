# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_kartu_peserta.ui'
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
        Form.resize(1024, 816)
        self.gridLayout_6 = QGridLayout(Form)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(400, 0))
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cbo_kegiatan = QComboBox(self.widget_3)
        self.cbo_kegiatan.setObjectName(u"cbo_kegiatan")
        self.cbo_kegiatan.setMinimumSize(QSize(100, 24))

        self.gridLayout.addWidget(self.cbo_kegiatan, 1, 2, 1, 1)

        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.tbl_daftar_peserta = QTableWidget(self.widget_3)
        self.tbl_daftar_peserta.setObjectName(u"tbl_daftar_peserta")
        self.tbl_daftar_peserta.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tbl_daftar_peserta, 2, 0, 1, 3)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)


        self.gridLayout_6.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.viewer_layout = QGridLayout(self.widget)
        self.viewer_layout.setObjectName(u"viewer_layout")

        self.gridLayout_6.addWidget(self.widget, 0, 1, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 9, 0, 9)
        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_8 = QGridLayout(self.widget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.btn_generate_selected = QPushButton(self.widget_8)
        self.btn_generate_selected.setObjectName(u"btn_generate_selected")
        self.btn_generate_selected.setMinimumSize(QSize(0, 30))

        self.gridLayout_8.addWidget(self.btn_generate_selected, 0, 0, 1, 1)

        self.btn_generate_all = QPushButton(self.widget_8)
        self.btn_generate_all.setObjectName(u"btn_generate_all")
        self.btn_generate_all.setMinimumSize(QSize(0, 30))

        self.gridLayout_8.addWidget(self.btn_generate_all, 0, 1, 1, 1)

        self.btn_print = QPushButton(self.widget_8)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setMinimumSize(QSize(0, 30))

        self.gridLayout_8.addWidget(self.btn_print, 1, 1, 1, 1)

        self.btn_save_pdf = QPushButton(self.widget_8)
        self.btn_save_pdf.setObjectName(u"btn_save_pdf")
        self.btn_save_pdf.setMinimumSize(QSize(0, 30))

        self.gridLayout_8.addWidget(self.btn_save_pdf, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_8, 13, 0, 1, 1)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_4 = QGridLayout(self.widget_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.widget_7)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setBold(False)
        self.label_8.setFont(font1)

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)

        self.spin_margin_top = QDoubleSpinBox(self.widget_7)
        self.spin_margin_top.setObjectName(u"spin_margin_top")
        self.spin_margin_top.setMinimumSize(QSize(0, 24))
        self.spin_margin_top.setDecimals(2)
        self.spin_margin_top.setMinimum(0.500000000000000)
        self.spin_margin_top.setMaximum(30.000000000000000)
        self.spin_margin_top.setSingleStep(0.100000000000000)
        self.spin_margin_top.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.spin_margin_top, 1, 4, 1, 1)

        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.spin_margin_left = QDoubleSpinBox(self.widget_7)
        self.spin_margin_left.setObjectName(u"spin_margin_left")
        self.spin_margin_left.setMinimumSize(QSize(0, 24))
        self.spin_margin_left.setDecimals(2)
        self.spin_margin_left.setMinimum(0.500000000000000)
        self.spin_margin_left.setMaximum(30.000000000000000)
        self.spin_margin_left.setSingleStep(0.100000000000000)
        self.spin_margin_left.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.spin_margin_left, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_7, 3, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_2)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.widget_10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.widget_10)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 3, 3, 1, 1)

        self.y_nama = QDoubleSpinBox(self.widget_10)
        self.y_nama.setObjectName(u"y_nama")
        self.y_nama.setMinimumSize(QSize(0, 24))
        self.y_nama.setAlignment(Qt.AlignCenter)
        self.y_nama.setDecimals(2)
        self.y_nama.setMinimum(-100.000000000000000)
        self.y_nama.setMaximum(100.000000000000000)
        self.y_nama.setSingleStep(0.100000000000000)
        self.y_nama.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.y_nama, 4, 2, 1, 1)

        self.y_no_induk = QDoubleSpinBox(self.widget_10)
        self.y_no_induk.setObjectName(u"y_no_induk")
        self.y_no_induk.setMinimumSize(QSize(0, 24))
        self.y_no_induk.setAlignment(Qt.AlignCenter)
        self.y_no_induk.setDecimals(2)
        self.y_no_induk.setMinimum(-100.000000000000000)
        self.y_no_induk.setMaximum(100.000000000000000)
        self.y_no_induk.setSingleStep(0.100000000000000)
        self.y_no_induk.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.y_no_induk, 9, 2, 1, 1)

        self.y_ttl = QDoubleSpinBox(self.widget_10)
        self.y_ttl.setObjectName(u"y_ttl")
        self.y_ttl.setMinimumSize(QSize(0, 24))
        self.y_ttl.setAlignment(Qt.AlignCenter)
        self.y_ttl.setDecimals(2)
        self.y_ttl.setMinimum(-100.000000000000000)
        self.y_ttl.setMaximum(100.000000000000000)
        self.y_ttl.setSingleStep(0.100000000000000)
        self.y_ttl.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.y_ttl, 5, 2, 1, 1)

        self.label_19 = QLabel(self.widget_10)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 3, 2, 1, 1)

        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.radio_nama = QRadioButton(self.widget_10)
        self.radio_nama.setObjectName(u"radio_nama")
        self.radio_nama.setChecked(True)
        self.radio_nama.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.radio_nama, 4, 0, 1, 1)

        self.radio_ttl = QRadioButton(self.widget_10)
        self.radio_ttl.setObjectName(u"radio_ttl")
        self.radio_ttl.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.radio_ttl, 5, 0, 1, 1)

        self.x_no_induk = QDoubleSpinBox(self.widget_10)
        self.x_no_induk.setObjectName(u"x_no_induk")
        self.x_no_induk.setMinimumSize(QSize(0, 24))
        self.x_no_induk.setAlignment(Qt.AlignCenter)
        self.x_no_induk.setDecimals(2)
        self.x_no_induk.setMinimum(-100.000000000000000)
        self.x_no_induk.setMaximum(100.000000000000000)
        self.x_no_induk.setSingleStep(0.100000000000000)
        self.x_no_induk.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.x_no_induk, 9, 1, 1, 1)

        self.label_17 = QLabel(self.widget_10)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 3, 1, 1, 1)

        self.radio_no_induk = QRadioButton(self.widget_10)
        self.radio_no_induk.setObjectName(u"radio_no_induk")
        self.radio_no_induk.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.radio_no_induk, 9, 0, 1, 1)

        self.x_ttl = QDoubleSpinBox(self.widget_10)
        self.x_ttl.setObjectName(u"x_ttl")
        self.x_ttl.setMinimumSize(QSize(0, 24))
        self.x_ttl.setAlignment(Qt.AlignCenter)
        self.x_ttl.setDecimals(2)
        self.x_ttl.setMinimum(-100.000000000000000)
        self.x_ttl.setMaximum(100.000000000000000)
        self.x_ttl.setSingleStep(0.100000000000000)
        self.x_ttl.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.x_ttl, 5, 1, 1, 1)

        self.x_nama = QDoubleSpinBox(self.widget_10)
        self.x_nama.setObjectName(u"x_nama")
        self.x_nama.setMinimumSize(QSize(0, 24))
        self.x_nama.setAlignment(Qt.AlignCenter)
        self.x_nama.setDecimals(2)
        self.x_nama.setMinimum(-100.000000000000000)
        self.x_nama.setMaximum(100.000000000000000)
        self.x_nama.setSingleStep(0.100000000000000)
        self.x_nama.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.x_nama, 4, 1, 1, 1)

        self.size_nama = QDoubleSpinBox(self.widget_10)
        self.size_nama.setObjectName(u"size_nama")
        self.size_nama.setMinimumSize(QSize(0, 24))
        self.size_nama.setAlignment(Qt.AlignCenter)
        self.size_nama.setDecimals(1)
        self.size_nama.setMinimum(6.000000000000000)
        self.size_nama.setMaximum(100.000000000000000)
        self.size_nama.setSingleStep(1.000000000000000)
        self.size_nama.setValue(12.000000000000000)

        self.gridLayout_3.addWidget(self.size_nama, 4, 3, 1, 1)

        self.size_no_induk = QDoubleSpinBox(self.widget_10)
        self.size_no_induk.setObjectName(u"size_no_induk")
        self.size_no_induk.setMinimumSize(QSize(0, 24))
        self.size_no_induk.setAlignment(Qt.AlignCenter)
        self.size_no_induk.setDecimals(1)
        self.size_no_induk.setMinimum(6.000000000000000)
        self.size_no_induk.setMaximum(100.000000000000000)
        self.size_no_induk.setSingleStep(1.000000000000000)
        self.size_no_induk.setValue(12.000000000000000)

        self.gridLayout_3.addWidget(self.size_no_induk, 9, 3, 1, 1)

        self.radio_nisn = QRadioButton(self.widget_10)
        self.radio_nisn.setObjectName(u"radio_nisn")
        self.radio_nisn.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.radio_nisn, 10, 0, 1, 1)

        self.size_nisn = QDoubleSpinBox(self.widget_10)
        self.size_nisn.setObjectName(u"size_nisn")
        self.size_nisn.setMinimumSize(QSize(0, 24))
        self.size_nisn.setAlignment(Qt.AlignCenter)
        self.size_nisn.setDecimals(1)
        self.size_nisn.setMinimum(6.000000000000000)
        self.size_nisn.setMaximum(100.000000000000000)
        self.size_nisn.setSingleStep(1.000000000000000)
        self.size_nisn.setValue(12.000000000000000)

        self.gridLayout_3.addWidget(self.size_nisn, 10, 3, 1, 1)

        self.y_nisn = QDoubleSpinBox(self.widget_10)
        self.y_nisn.setObjectName(u"y_nisn")
        self.y_nisn.setMinimumSize(QSize(0, 24))
        self.y_nisn.setAlignment(Qt.AlignCenter)
        self.y_nisn.setDecimals(2)
        self.y_nisn.setMinimum(-100.000000000000000)
        self.y_nisn.setMaximum(100.000000000000000)
        self.y_nisn.setSingleStep(0.100000000000000)
        self.y_nisn.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.y_nisn, 10, 2, 1, 1)

        self.x_nisn = QDoubleSpinBox(self.widget_10)
        self.x_nisn.setObjectName(u"x_nisn")
        self.x_nisn.setMinimumSize(QSize(0, 24))
        self.x_nisn.setAlignment(Qt.AlignCenter)
        self.x_nisn.setDecimals(2)
        self.x_nisn.setMinimum(-100.000000000000000)
        self.x_nisn.setMaximum(100.000000000000000)
        self.x_nisn.setSingleStep(0.100000000000000)
        self.x_nisn.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.x_nisn, 10, 1, 1, 1)

        self.radio_kelas = QRadioButton(self.widget_10)
        self.radio_kelas.setObjectName(u"radio_kelas")
        self.radio_kelas.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.radio_kelas, 7, 0, 1, 1)

        self.y_kelas = QDoubleSpinBox(self.widget_10)
        self.y_kelas.setObjectName(u"y_kelas")
        self.y_kelas.setMinimumSize(QSize(0, 24))
        self.y_kelas.setAlignment(Qt.AlignCenter)
        self.y_kelas.setDecimals(2)
        self.y_kelas.setMinimum(-100.000000000000000)
        self.y_kelas.setMaximum(100.000000000000000)
        self.y_kelas.setSingleStep(0.100000000000000)
        self.y_kelas.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.y_kelas, 7, 2, 1, 1)

        self.x_kelas = QDoubleSpinBox(self.widget_10)
        self.x_kelas.setObjectName(u"x_kelas")
        self.x_kelas.setMinimumSize(QSize(0, 24))
        self.x_kelas.setAlignment(Qt.AlignCenter)
        self.x_kelas.setDecimals(2)
        self.x_kelas.setMinimum(-100.000000000000000)
        self.x_kelas.setMaximum(100.000000000000000)
        self.x_kelas.setSingleStep(0.100000000000000)
        self.x_kelas.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.x_kelas, 7, 1, 1, 1)

        self.x_nopes = QDoubleSpinBox(self.widget_10)
        self.x_nopes.setObjectName(u"x_nopes")
        self.x_nopes.setMinimumSize(QSize(0, 24))
        self.x_nopes.setAlignment(Qt.AlignCenter)
        self.x_nopes.setDecimals(2)
        self.x_nopes.setMinimum(-100.000000000000000)
        self.x_nopes.setMaximum(100.000000000000000)
        self.x_nopes.setSingleStep(0.100000000000000)
        self.x_nopes.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.x_nopes, 6, 1, 1, 1)

        self.size_ttl = QDoubleSpinBox(self.widget_10)
        self.size_ttl.setObjectName(u"size_ttl")
        self.size_ttl.setMinimumSize(QSize(0, 24))
        self.size_ttl.setAlignment(Qt.AlignCenter)
        self.size_ttl.setDecimals(1)
        self.size_ttl.setMinimum(6.000000000000000)
        self.size_ttl.setMaximum(100.000000000000000)
        self.size_ttl.setSingleStep(1.000000000000000)
        self.size_ttl.setValue(12.000000000000000)

        self.gridLayout_3.addWidget(self.size_ttl, 5, 3, 1, 1)

        self.size_kelas = QDoubleSpinBox(self.widget_10)
        self.size_kelas.setObjectName(u"size_kelas")
        self.size_kelas.setMinimumSize(QSize(0, 24))
        self.size_kelas.setAlignment(Qt.AlignCenter)
        self.size_kelas.setDecimals(1)
        self.size_kelas.setMinimum(6.000000000000000)
        self.size_kelas.setMaximum(100.000000000000000)
        self.size_kelas.setSingleStep(1.000000000000000)
        self.size_kelas.setValue(12.000000000000000)

        self.gridLayout_3.addWidget(self.size_kelas, 7, 3, 1, 1)

        self.radio_nopes = QRadioButton(self.widget_10)
        self.radio_nopes.setObjectName(u"radio_nopes")
        self.radio_nopes.setChecked(True)
        self.radio_nopes.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.radio_nopes, 6, 0, 1, 1)

        self.y_nopes = QDoubleSpinBox(self.widget_10)
        self.y_nopes.setObjectName(u"y_nopes")
        self.y_nopes.setMinimumSize(QSize(0, 24))
        self.y_nopes.setAlignment(Qt.AlignCenter)
        self.y_nopes.setDecimals(2)
        self.y_nopes.setMinimum(-100.000000000000000)
        self.y_nopes.setMaximum(100.000000000000000)
        self.y_nopes.setSingleStep(0.100000000000000)
        self.y_nopes.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.y_nopes, 6, 2, 1, 1)

        self.size_nopes = QDoubleSpinBox(self.widget_10)
        self.size_nopes.setObjectName(u"size_nopes")
        self.size_nopes.setMinimumSize(QSize(0, 24))
        self.size_nopes.setAlignment(Qt.AlignCenter)
        self.size_nopes.setDecimals(1)
        self.size_nopes.setMinimum(6.000000000000000)
        self.size_nopes.setMaximum(100.000000000000000)
        self.size_nopes.setSingleStep(1.000000000000000)
        self.size_nopes.setValue(12.000000000000000)

        self.gridLayout_3.addWidget(self.size_nopes, 6, 3, 1, 1)

        self.cbo_fonts = QComboBox(self.widget_10)
        self.cbo_fonts.setObjectName(u"cbo_fonts")
        self.cbo_fonts.setMinimumSize(QSize(0, 24))
        self.cbo_fonts.setEditable(False)

        self.gridLayout_3.addWidget(self.cbo_fonts, 1, 1, 1, 3)

        self.label_25 = QLabel(self.widget_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(80, 16777215))
        self.label_25.setFont(font)

        self.gridLayout_3.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_26 = QLabel(self.widget_10)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.gridLayout_3.addWidget(self.label_26, 2, 0, 1, 1)

        self.spin_presisi = QDoubleSpinBox(self.widget_10)
        self.spin_presisi.setObjectName(u"spin_presisi")
        self.spin_presisi.setMinimumSize(QSize(80, 24))
        self.spin_presisi.setDecimals(2)
        self.spin_presisi.setMinimum(0.000000000000000)
        self.spin_presisi.setMaximum(28.000000000000000)
        self.spin_presisi.setSingleStep(0.100000000000000)
        self.spin_presisi.setValue(0.100000000000000)

        self.gridLayout_3.addWidget(self.spin_presisi, 2, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_10, 7, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(3)
        self.gridLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.spin_vertikal = QDoubleSpinBox(self.widget_6)
        self.spin_vertikal.setObjectName(u"spin_vertikal")
        self.spin_vertikal.setMinimumSize(QSize(0, 24))
        self.spin_vertikal.setDecimals(2)
        self.spin_vertikal.setMinimum(0.000000000000000)
        self.spin_vertikal.setMaximum(1.000000000000000)
        self.spin_vertikal.setSingleStep(0.010000000000000)
        self.spin_vertikal.setValue(0.050000000000000)

        self.gridLayout_7.addWidget(self.spin_vertikal, 4, 4, 1, 1)

        self.label_12 = QLabel(self.widget_6)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 1)

        self.spin_lebar = QDoubleSpinBox(self.widget_6)
        self.spin_lebar.setObjectName(u"spin_lebar")
        self.spin_lebar.setMinimumSize(QSize(0, 24))
        self.spin_lebar.setDecimals(2)
        self.spin_lebar.setMinimum(0.500000000000000)
        self.spin_lebar.setMaximum(30.000000000000000)
        self.spin_lebar.setSingleStep(0.100000000000000)
        self.spin_lebar.setValue(10.000000000000000)

        self.gridLayout_7.addWidget(self.spin_lebar, 1, 1, 1, 1)

        self.spin_horizontal = QDoubleSpinBox(self.widget_6)
        self.spin_horizontal.setObjectName(u"spin_horizontal")
        self.spin_horizontal.setMinimumSize(QSize(0, 24))
        self.spin_horizontal.setDecimals(2)
        self.spin_horizontal.setMinimum(0.000000000000000)
        self.spin_horizontal.setMaximum(1.000000000000000)
        self.spin_horizontal.setSingleStep(0.010000000000000)
        self.spin_horizontal.setValue(0.050000000000000)

        self.gridLayout_7.addWidget(self.spin_horizontal, 4, 1, 1, 1)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 1, 3, 1, 1)

        self.spin_tinggi = QDoubleSpinBox(self.widget_6)
        self.spin_tinggi.setObjectName(u"spin_tinggi")
        self.spin_tinggi.setMinimumSize(QSize(0, 24))
        self.spin_tinggi.setDecimals(2)
        self.spin_tinggi.setMinimum(0.500000000000000)
        self.spin_tinggi.setMaximum(30.000000000000000)
        self.spin_tinggi.setSingleStep(0.100000000000000)
        self.spin_tinggi.setValue(5.000000000000000)

        self.gridLayout_7.addWidget(self.spin_tinggi, 1, 4, 1, 1)

        self.label_13 = QLabel(self.widget_6)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 4, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 2)


        self.gridLayout_5.addWidget(self.widget_6, 4, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_11 = QGridLayout(self.widget_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_24 = QLabel(self.widget_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(80, 0))
        self.label_24.setFont(font)

        self.gridLayout_11.addWidget(self.label_24, 0, 0, 1, 1)

        self.cbo_jenis = QComboBox(self.widget_11)
        self.cbo_jenis.addItem("")
        self.cbo_jenis.addItem("")
        self.cbo_jenis.setObjectName(u"cbo_jenis")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbo_jenis.sizePolicy().hasHeightForWidth())
        self.cbo_jenis.setSizePolicy(sizePolicy1)
        self.cbo_jenis.setMinimumSize(QSize(0, 24))
        self.cbo_jenis.setEditable(False)

        self.gridLayout_11.addWidget(self.cbo_jenis, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget_11, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_10 = QGridLayout(self.widget_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setVerticalSpacing(3)
        self.gridLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.x_foto = QDoubleSpinBox(self.widget_5)
        self.x_foto.setObjectName(u"x_foto")
        self.x_foto.setMinimumSize(QSize(0, 24))
        self.x_foto.setAlignment(Qt.AlignCenter)
        self.x_foto.setDecimals(2)
        self.x_foto.setMinimum(-100.000000000000000)
        self.x_foto.setMaximum(100.000000000000000)
        self.x_foto.setSingleStep(0.100000000000000)
        self.x_foto.setValue(1.000000000000000)

        self.gridLayout_10.addWidget(self.x_foto, 1, 3, 1, 1)

        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_10.addWidget(self.label_15, 1, 1, 1, 1)

        self.y_foto = QDoubleSpinBox(self.widget_5)
        self.y_foto.setObjectName(u"y_foto")
        self.y_foto.setMinimumSize(QSize(0, 24))
        self.y_foto.setAlignment(Qt.AlignCenter)
        self.y_foto.setDecimals(2)
        self.y_foto.setMinimum(-100.000000000000000)
        self.y_foto.setMaximum(100.000000000000000)
        self.y_foto.setSingleStep(0.100000000000000)
        self.y_foto.setValue(1.000000000000000)

        self.gridLayout_10.addWidget(self.y_foto, 1, 5, 1, 1)

        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_20, 1, 2, 1, 1)

        self.w_foto = QDoubleSpinBox(self.widget_5)
        self.w_foto.setObjectName(u"w_foto")
        self.w_foto.setMinimumSize(QSize(0, 24))
        self.w_foto.setAlignment(Qt.AlignCenter)
        self.w_foto.setDecimals(2)
        self.w_foto.setMinimum(0.500000000000000)
        self.w_foto.setMaximum(30.000000000000000)
        self.w_foto.setSingleStep(0.100000000000000)
        self.w_foto.setValue(1.000000000000000)

        self.gridLayout_10.addWidget(self.w_foto, 2, 3, 1, 1)

        self.h_foto = QDoubleSpinBox(self.widget_5)
        self.h_foto.setObjectName(u"h_foto")
        self.h_foto.setMinimumSize(QSize(0, 24))
        self.h_foto.setAlignment(Qt.AlignCenter)
        self.h_foto.setDecimals(2)
        self.h_foto.setMinimum(0.500000000000000)
        self.h_foto.setMaximum(30.000000000000000)
        self.h_foto.setSingleStep(0.100000000000000)
        self.h_foto.setValue(1.000000000000000)

        self.gridLayout_10.addWidget(self.h_foto, 2, 5, 1, 1)

        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_10.addWidget(self.label_16, 2, 1, 1, 1)

        self.label_21 = QLabel(self.widget_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_21, 1, 4, 1, 1)

        self.label_23 = QLabel(self.widget_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_23, 2, 4, 1, 1)

        self.label_22 = QLabel(self.widget_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_22, 2, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.radio_foto = QRadioButton(self.widget_5)
        self.radio_foto.setObjectName(u"radio_foto")
        self.radio_foto.setAutoExclusive(False)

        self.gridLayout_10.addWidget(self.radio_foto, 0, 0, 1, 2)


        self.gridLayout_5.addWidget(self.widget_5, 9, 0, 1, 1)

        self.widget_12 = QWidget(self.widget_2)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_12 = QGridLayout(self.widget_12)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.btn_reset = QPushButton(self.widget_12)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(0, 30))
        self.btn_reset.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_12.addWidget(self.btn_reset, 0, 1, 1, 1)

        self.btn_save_setting = QPushButton(self.widget_12)
        self.btn_save_setting.setObjectName(u"btn_save_setting")
        self.btn_save_setting.setMinimumSize(QSize(0, 30))

        self.gridLayout_12.addWidget(self.btn_save_setting, 0, 0, 1, 1)

        self.btn_clear = QPushButton(self.widget_12)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(0, 30))
        self.btn_clear.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_12.addWidget(self.btn_clear, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.widget_12, 10, 0, 1, 1)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.cbo_kertas = QComboBox(self.widget_4)
        self.cbo_kertas.addItem("")
        self.cbo_kertas.addItem("")
        self.cbo_kertas.setObjectName(u"cbo_kertas")
        self.cbo_kertas.setMinimumSize(QSize(0, 24))
        self.cbo_kertas.setEditable(False)

        self.gridLayout_2.addWidget(self.cbo_kertas, 0, 1, 1, 1)

        self.cbo_orientasi = QComboBox(self.widget_4)
        self.cbo_orientasi.addItem("")
        self.cbo_orientasi.addItem("")
        self.cbo_orientasi.setObjectName(u"cbo_orientasi")
        self.cbo_orientasi.setMinimumSize(QSize(0, 24))
        self.cbo_orientasi.setEditable(False)

        self.gridLayout_2.addWidget(self.cbo_orientasi, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.widget_4, 2, 0, 1, 1)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.gridLayout_9 = QGridLayout(self.widget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.btn_browse = QPushButton(self.widget_9)
        self.btn_browse.setObjectName(u"btn_browse")

        self.gridLayout_9.addWidget(self.btn_browse, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)

        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.plain_background = QPlainTextEdit(self.widget_9)
        self.plain_background.setObjectName(u"plain_background")
        self.plain_background.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_9.addWidget(self.plain_background, 2, 0, 1, 2)


        self.gridLayout_5.addWidget(self.widget_9, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.widget_13 = QWidget(self.widget_2)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_13 = QGridLayout(self.widget_13)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, 0, -1, 0)

        self.gridLayout_5.addWidget(self.widget_13, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_2, 0, 2, 1, 1)

        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnMinimumWidth(2, 400)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.label.setText(QCoreApplication.translate("Form", u"DAFTAR PESERTA", None))
        self.btn_generate_selected.setText(QCoreApplication.translate("Form", u"Generate Selected", None))
        self.btn_generate_all.setText(QCoreApplication.translate("Form", u"Generate All", None))
        self.btn_print.setText(QCoreApplication.translate("Form", u"Print", None))
        self.btn_save_pdf.setText(QCoreApplication.translate("Form", u"Save PDF", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Left", None))
        self.spin_margin_top.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Top", None))
        self.spin_margin_left.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Margin", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Size", None))
        self.y_nama.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.y_no_induk.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.y_ttl.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Variabel-Variabel", None))
        self.radio_nama.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.radio_ttl.setText(QCoreApplication.translate("Form", u"TTL", None))
        self.x_no_induk.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"X", None))
        self.radio_no_induk.setText(QCoreApplication.translate("Form", u"Nomor Induk", None))
        self.x_ttl.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.x_nama.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.size_nama.setSuffix(QCoreApplication.translate("Form", u" pt", None))
        self.size_no_induk.setSuffix(QCoreApplication.translate("Form", u" pt", None))
        self.radio_nisn.setText(QCoreApplication.translate("Form", u"NISN", None))
        self.size_nisn.setSuffix(QCoreApplication.translate("Form", u" pt", None))
        self.y_nisn.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.x_nisn.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.radio_kelas.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.y_kelas.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.x_kelas.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.x_nopes.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.size_ttl.setSuffix(QCoreApplication.translate("Form", u" pt", None))
        self.size_kelas.setSuffix(QCoreApplication.translate("Form", u" pt", None))
        self.radio_nopes.setText(QCoreApplication.translate("Form", u"Nomor Peserta", None))
        self.y_nopes.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.size_nopes.setSuffix(QCoreApplication.translate("Form", u" pt", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"FONT", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Tingkat Presisi", None))
        self.spin_presisi.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_vertikal.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Horizontal Gap", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Lebar", None))
        self.spin_lebar.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.spin_horizontal.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Tinggi", None))
        self.spin_tinggi.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Vertical Gap", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Pengaturan Kartu", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Jenis Kartu", None))
        self.cbo_jenis.setItemText(0, QCoreApplication.translate("Form", u"Kartu Peserta", None))
        self.cbo_jenis.setItemText(1, QCoreApplication.translate("Form", u"Tempelan Bangku", None))

        self.x_foto.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Posisi", None))
        self.y_foto.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"X", None))
        self.w_foto.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.h_foto.setSuffix(QCoreApplication.translate("Form", u" cm", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Ukuran", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Tinggi", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Lebar", None))
        self.radio_foto.setText(QCoreApplication.translate("Form", u"Foto", None))
        self.btn_reset.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.btn_save_setting.setText(QCoreApplication.translate("Form", u"Simpan Setting Kartu", None))
        self.btn_clear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Kertas", None))
        self.cbo_kertas.setItemText(0, QCoreApplication.translate("Form", u"A4", None))
        self.cbo_kertas.setItemText(1, QCoreApplication.translate("Form", u"F4", None))

        self.cbo_orientasi.setItemText(0, QCoreApplication.translate("Form", u"Portrait", None))
        self.cbo_orientasi.setItemText(1, QCoreApplication.translate("Form", u"Landscape", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"Orientasi", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Background", None))
    # retranslateUi

