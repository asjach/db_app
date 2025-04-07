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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1503, 623)
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(400, 0))
        self.widget_2.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.radio_siswa_aktif = QRadioButton(self.widget_3)
        self.radio_siswa_aktif.setObjectName(u"radio_siswa_aktif")
        self.radio_siswa_aktif.setChecked(True)

        self.gridLayout.addWidget(self.radio_siswa_aktif, 1, 0, 1, 1)

        self.radio_buku_induk = QRadioButton(self.widget_3)
        self.radio_buku_induk.setObjectName(u"radio_buku_induk")

        self.gridLayout.addWidget(self.radio_buku_induk, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.tbl_siswa = QTableWidget(self.widget_3)
        self.tbl_siswa.setObjectName(u"tbl_siswa")
        self.tbl_siswa.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tbl_siswa, 2, 0, 1, 3)


        self.gridLayout_3.addWidget(self.widget_3, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 4, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tbl_transaksi = QTableWidget(self.widget)
        self.tbl_transaksi.setObjectName(u"tbl_transaksi")
        self.tbl_transaksi.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_4.addWidget(self.tbl_transaksi, 1, 0, 1, 2)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.gridLayout_9 = QGridLayout(self.widget_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_12 = QGridLayout(self.widget_11)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(0)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.date_awal = QDateEdit(self.widget_11)
        self.date_awal.setObjectName(u"date_awal")
        self.date_awal.setMinimumSize(QSize(0, 24))
        self.date_awal.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.date_awal.setProperty(u"showGroupSeparator", True)
        self.date_awal.setCalendarPopup(True)
        self.date_awal.setTimeSpec(Qt.LocalTime)

        self.gridLayout_12.addWidget(self.date_awal, 1, 2, 1, 1)

        self.label_16 = QLabel(self.widget_11)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_12.addWidget(self.label_16, 1, 0, 1, 1)

        self.date_akhir = QDateEdit(self.widget_11)
        self.date_akhir.setObjectName(u"date_akhir")
        self.date_akhir.setMinimumSize(QSize(0, 24))
        self.date_akhir.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.date_akhir.setProperty(u"showGroupSeparator", True)
        self.date_akhir.setCalendarPopup(True)
        self.date_akhir.setTimeSpec(Qt.LocalTime)

        self.gridLayout_12.addWidget(self.date_akhir, 2, 2, 1, 1)

        self.label_17 = QLabel(self.widget_11)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_12.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_21 = QLabel(self.widget_11)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_12.addWidget(self.label_21, 0, 0, 1, 3)

        self.btn_tgl_awal_prev = QPushButton(self.widget_11)
        self.btn_tgl_awal_prev.setObjectName(u"btn_tgl_awal_prev")
        self.btn_tgl_awal_prev.setMinimumSize(QSize(0, 24))
        self.btn_tgl_awal_prev.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_12.addWidget(self.btn_tgl_awal_prev, 1, 1, 1, 1)

        self.btn_tgl_awal_next = QPushButton(self.widget_11)
        self.btn_tgl_awal_next.setObjectName(u"btn_tgl_awal_next")
        self.btn_tgl_awal_next.setMinimumSize(QSize(0, 24))
        self.btn_tgl_awal_next.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_12.addWidget(self.btn_tgl_awal_next, 1, 3, 1, 1)

        self.btn_tgl_akhir_prev = QPushButton(self.widget_11)
        self.btn_tgl_akhir_prev.setObjectName(u"btn_tgl_akhir_prev")
        self.btn_tgl_akhir_prev.setMinimumSize(QSize(0, 24))
        self.btn_tgl_akhir_prev.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_12.addWidget(self.btn_tgl_akhir_prev, 2, 1, 1, 1)

        self.btn_tgl_akhir_next = QPushButton(self.widget_11)
        self.btn_tgl_akhir_next.setObjectName(u"btn_tgl_akhir_next")
        self.btn_tgl_akhir_next.setMinimumSize(QSize(0, 24))
        self.btn_tgl_akhir_next.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_12.addWidget(self.btn_tgl_akhir_next, 2, 3, 1, 1)

        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_13 = QGridLayout(self.widget_12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_clear_biaya = QPushButton(self.widget_12)
        self.btn_clear_biaya.setObjectName(u"btn_clear_biaya")
        self.btn_clear_biaya.setMinimumSize(QSize(0, 24))
        self.btn_clear_biaya.setMaximumSize(QSize(20, 24))

        self.gridLayout_13.addWidget(self.btn_clear_biaya, 0, 2, 1, 1)

        self.label_24 = QLabel(self.widget_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(60, 0))
        self.label_24.setMaximumSize(QSize(65, 16777215))

        self.gridLayout_13.addWidget(self.label_24, 0, 0, 1, 1)

        self.cbo_filter_biaya = QComboBox(self.widget_12)
        self.cbo_filter_biaya.setObjectName(u"cbo_filter_biaya")
        self.cbo_filter_biaya.setMinimumSize(QSize(120, 24))

        self.gridLayout_13.addWidget(self.cbo_filter_biaya, 0, 1, 1, 1)


        self.gridLayout_12.addWidget(self.widget_12, 4, 0, 1, 4)

        self.gridLayout_12.setColumnStretch(1, 1)
        self.gridLayout_12.setColumnMinimumWidth(0, 60)

        self.gridLayout_9.addWidget(self.widget_11, 0, 2, 1, 1)

        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_11 = QGridLayout(self.widget_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_20 = QLabel(self.widget_10)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_11.addWidget(self.label_20, 0, 0, 1, 1)

        self.radio_bulan = QRadioButton(self.widget_10)
        self.radio_bulan.setObjectName(u"radio_bulan")

        self.gridLayout_11.addWidget(self.radio_bulan, 2, 0, 1, 1)

        self.radio_tahun = QRadioButton(self.widget_10)
        self.radio_tahun.setObjectName(u"radio_tahun")

        self.gridLayout_11.addWidget(self.radio_tahun, 3, 0, 1, 1)

        self.radio_hari = QRadioButton(self.widget_10)
        self.radio_hari.setObjectName(u"radio_hari")
        self.radio_hari.setChecked(True)

        self.gridLayout_11.addWidget(self.radio_hari, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_10, 0, 0, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_8, 0, 0, 1, 2)

        self.gridLayout_4.setColumnStretch(0, 1)

        self.gridLayout_5.addWidget(self.widget, 0, 2, 4, 1)

        self.widget_9 = QWidget(Form)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setMinimumSize(QSize(500, 0))
        self.gridLayout_10 = QGridLayout(self.widget_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setVerticalSpacing(30)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_9)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_8 = QGridLayout(self.widget_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(6)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_id_tagihan = QLabel(self.widget_7)
        self.label_id_tagihan.setObjectName(u"label_id_tagihan")
        self.label_id_tagihan.setMinimumSize(QSize(120, 0))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_id_tagihan.setFont(font)
        self.label_id_tagihan.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.label_id_tagihan, 0, 1, 1, 1)

        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_nama_biaya = QLabel(self.widget_7)
        self.label_nama_biaya.setObjectName(u"label_nama_biaya")
        self.label_nama_biaya.setMinimumSize(QSize(120, 0))
        self.label_nama_biaya.setFont(font)
        self.label_nama_biaya.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.label_nama_biaya, 1, 1, 1, 1)

        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_8.addWidget(self.label_11, 4, 0, 1, 1)

        self.label_status = QLabel(self.widget_7)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(120, 0))
        self.label_status.setFont(font)
        self.label_status.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.label_status, 4, 1, 1, 1)

        self.label_15 = QLabel(self.widget_7)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_8.addWidget(self.label_15, 0, 2, 1, 1)

        self.label_periode = QLabel(self.widget_7)
        self.label_periode.setObjectName(u"label_periode")
        self.label_periode.setMinimumSize(QSize(120, 0))
        self.label_periode.setFont(font)
        self.label_periode.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.label_periode, 0, 3, 1, 1)

        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_8.addWidget(self.label_13, 4, 2, 1, 1)

        self.label_sudah_bayar = QLabel(self.widget_7)
        self.label_sudah_bayar.setObjectName(u"label_sudah_bayar")
        self.label_sudah_bayar.setMinimumSize(QSize(120, 0))
        self.label_sudah_bayar.setFont(font)
        self.label_sudah_bayar.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.label_sudah_bayar, 4, 3, 1, 1)

        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_8.addWidget(self.label_10, 1, 2, 1, 1)

        self.label_nominal_tagihan = QLabel(self.widget_7)
        self.label_nominal_tagihan.setObjectName(u"label_nominal_tagihan")
        self.label_nominal_tagihan.setMinimumSize(QSize(120, 0))
        self.label_nominal_tagihan.setFont(font)
        self.label_nominal_tagihan.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_8.addWidget(self.label_nominal_tagihan, 1, 3, 1, 1)

        self.gridLayout_8.setColumnStretch(1, 1)
        self.gridLayout_8.setColumnStretch(3, 1)
        self.gridLayout_8.setColumnMinimumWidth(0, 80)
        self.gridLayout_8.setColumnMinimumWidth(2, 80)

        self.gridLayout_10.addWidget(self.widget_7, 2, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_9)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(150, 0))
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_bayar = QPushButton(self.widget_6)
        self.btn_bayar.setObjectName(u"btn_bayar")
        self.btn_bayar.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_bayar.setFont(font1)

        self.gridLayout_7.addWidget(self.btn_bayar, 8, 0, 1, 2)

        self.label_terbilang = QLabel(self.widget_6)
        self.label_terbilang.setObjectName(u"label_terbilang")
        self.label_terbilang.setMinimumSize(QSize(120, 24))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(True)
        self.label_terbilang.setFont(font2)
        self.label_terbilang.setFrameShape(QFrame.StyledPanel)
        self.label_terbilang.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_terbilang, 5, 0, 1, 2)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_14 = QLabel(self.widget_6)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 3, 1, 1, 1)

        self.label_18 = QLabel(self.widget_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_7.addWidget(self.label_18, 1, 0, 1, 1)

        self.cbo_petugas = QComboBox(self.widget_6)
        self.cbo_petugas.setObjectName(u"cbo_petugas")
        self.cbo_petugas.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.cbo_petugas, 1, 1, 1, 1)

        self.line_nominal_bayar = QLineEdit(self.widget_6)
        self.line_nominal_bayar.setObjectName(u"line_nominal_bayar")
        self.line_nominal_bayar.setMinimumSize(QSize(0, 30))
        self.line_nominal_bayar.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setPointSize(16)
        self.line_nominal_bayar.setFont(font3)
        self.line_nominal_bayar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_nominal_bayar.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.line_nominal_bayar, 4, 1, 1, 1)

        self.date_bayar = QDateEdit(self.widget_6)
        self.date_bayar.setObjectName(u"date_bayar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.date_bayar.sizePolicy().hasHeightForWidth())
        self.date_bayar.setSizePolicy(sizePolicy2)
        self.date_bayar.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setPointSize(10)
        self.date_bayar.setFont(font4)
        self.date_bayar.setAlignment(Qt.AlignCenter)
        self.date_bayar.setCalendarPopup(True)
        self.date_bayar.setTimeSpec(Qt.LocalTime)

        self.gridLayout_7.addWidget(self.date_bayar, 4, 0, 1, 1)

        self.label_19 = QLabel(self.widget_6)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 2, 0, 1, 1)

        self.cbo_metode = QComboBox(self.widget_6)
        self.cbo_metode.addItem("")
        self.cbo_metode.addItem("")
        self.cbo_metode.setObjectName(u"cbo_metode")
        self.cbo_metode.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.cbo_metode, 2, 1, 1, 1)

        self.gridLayout_7.setColumnStretch(1, 1)

        self.gridLayout_10.addWidget(self.widget_6, 5, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_9)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_nis_lokal = QLabel(self.widget_5)
        self.label_nis_lokal.setObjectName(u"label_nis_lokal")
        self.label_nis_lokal.setMinimumSize(QSize(120, 0))
        self.label_nis_lokal.setFont(font)
        self.label_nis_lokal.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_6.addWidget(self.label_nis_lokal, 0, 1, 1, 1)

        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_kelas = QLabel(self.widget_5)
        self.label_kelas.setObjectName(u"label_kelas")
        self.label_kelas.setMinimumSize(QSize(60, 0))
        self.label_kelas.setFont(font)
        self.label_kelas.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_6.addWidget(self.label_kelas, 0, 3, 1, 1)

        self.label_ortu = QLabel(self.widget_5)
        self.label_ortu.setObjectName(u"label_ortu")
        self.label_ortu.setMinimumSize(QSize(0, 0))
        self.label_ortu.setFont(font)
        self.label_ortu.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_6.addWidget(self.label_ortu, 2, 1, 1, 3)

        self.label_nama = QLabel(self.widget_5)
        self.label_nama.setObjectName(u"label_nama")
        self.label_nama.setMinimumSize(QSize(0, 0))
        self.label_nama.setFont(font)
        self.label_nama.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_6.addWidget(self.label_nama, 1, 1, 1, 3)

        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnStretch(3, 1)
        self.gridLayout_6.setColumnMinimumWidth(0, 80)
        self.gridLayout_6.setColumnMinimumWidth(2, 80)

        self.gridLayout_10.addWidget(self.widget_5, 1, 0, 1, 1)

        self.widget_4 = QWidget(self.widget_9)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.tbl_tagihan = QTableWidget(self.widget_4)
        self.tbl_tagihan.setObjectName(u"tbl_tagihan")
        self.tbl_tagihan.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.tbl_tagihan, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.widget_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_9, 0, 1, 4, 1)

        self.gridLayout_5.setColumnStretch(2, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Daftar Santri", None))
        self.radio_siswa_aktif.setText(QCoreApplication.translate("Form", u"Siswa Aktif", None))
        self.radio_buku_induk.setText(QCoreApplication.translate("Form", u"Buku Induk", None))
        self.date_awal.setDisplayFormat(QCoreApplication.translate("Form", u"dd MMMM yyyy", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Tgl Awal", None))
        self.date_akhir.setDisplayFormat(QCoreApplication.translate("Form", u"dd MMMM yyyy", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Tgll Akhir", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Rentang Tanggal", None))
        self.btn_tgl_awal_prev.setText(QCoreApplication.translate("Form", u"<", None))
        self.btn_tgl_awal_next.setText(QCoreApplication.translate("Form", u">", None))
        self.btn_tgl_akhir_prev.setText(QCoreApplication.translate("Form", u"<", None))
        self.btn_tgl_akhir_next.setText(QCoreApplication.translate("Form", u">", None))
        self.btn_clear_biaya.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Jenis Biaya", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Rentang Tanggal:", None))
        self.radio_bulan.setText(QCoreApplication.translate("Form", u"Bulan Ini", None))
        self.radio_tahun.setText(QCoreApplication.translate("Form", u"Tahun Berjalan", None))
        self.radio_hari.setText(QCoreApplication.translate("Form", u"Hari ini", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ID Tagihan", None))
        self.label_id_tagihan.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"Nama Tagihan", None))
        self.label_nama_biaya.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Status Tagihan", None))
        self.label_status.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"Periode", None))
        self.label_periode.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"Sudah Bayar", None))
        self.label_sudah_bayar.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"Nominal Tagihan", None))
        self.label_nominal_tagihan.setText("")
        self.btn_bayar.setText(QCoreApplication.translate("Form", u"BAYAR", None))
        self.label_terbilang.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Tanggal Bayar", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Nominal Pembayaran", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Petugas", None))
        self.date_bayar.setDisplayFormat(QCoreApplication.translate("Form", u"dd MMMM yyyy", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Metode Pembayaran", None))
        self.cbo_metode.setItemText(0, QCoreApplication.translate("Form", u"Tunai", None))
        self.cbo_metode.setItemText(1, QCoreApplication.translate("Form", u"Transfer", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"Nama Siswa", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"NIS Lokal", None))
        self.label_nis_lokal.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"Orang Tua", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.label_kelas.setText("")
        self.label_ortu.setText("")
        self.label_nama.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Daftar Tagihan/Tunggakan", None))
    # retranslateUi

