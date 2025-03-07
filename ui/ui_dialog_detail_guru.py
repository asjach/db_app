# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_detail_guru.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1604, 991)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.line_search = QLineEdit(self.frame)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setMinimumSize(QSize(200, 24))
        self.line_search.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.line_search, 0, 3, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cbo_search_by = QComboBox(self.frame)
        self.cbo_search_by.addItem("")
        self.cbo_search_by.setObjectName(u"cbo_search_by")
        self.cbo_search_by.setMinimumSize(QSize(120, 24))

        self.gridLayout.addWidget(self.cbo_search_by, 0, 1, 1, 2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.btn_save_detail = QPushButton(self.frame)
        self.btn_save_detail.setObjectName(u"btn_save_detail")

        self.gridLayout.addWidget(self.btn_save_detail, 0, 8, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 7, 1, 1)

        self.cbo_daftar_guru = QComboBox(self.frame)
        self.cbo_daftar_guru.setObjectName(u"cbo_daftar_guru")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbo_daftar_guru.sizePolicy().hasHeightForWidth())
        self.cbo_daftar_guru.setSizePolicy(sizePolicy2)
        self.cbo_daftar_guru.setMinimumSize(QSize(400, 24))
        self.cbo_daftar_guru.setMaximumSize(QSize(400, 16777215))

        self.gridLayout.addWidget(self.cbo_daftar_guru, 0, 6, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.frame_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.gridLayout_12 = QGridLayout(self.tab1)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(10)
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.tab1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(600, 0))
        self.scrollArea.setMaximumSize(QSize(600, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 598, 925))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.frame_datadiri = QFrame(self.scrollAreaWidgetContents)
        self.frame_datadiri.setObjectName(u"frame_datadiri")
        self.frame_datadiri.setStyleSheet(u"")
        self.frame_datadiri.setFrameShape(QFrame.StyledPanel)
        self.frame_datadiri.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_datadiri)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.frame_datadiri)
        self.widget.setObjectName(u"widget")

        self.gridLayout_5.addWidget(self.widget, 3, 2, 1, 1)

        self.label_62 = QLabel(self.frame_datadiri)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_5.addWidget(self.label_62, 2, 0, 1, 1)

        self.line_tgl_lahir = QLineEdit(self.frame_datadiri)
        self.line_tgl_lahir.setObjectName(u"line_tgl_lahir")

        self.gridLayout_5.addWidget(self.line_tgl_lahir, 5, 1, 1, 1)

        self.cbo_jk = QComboBox(self.frame_datadiri)
        self.cbo_jk.setObjectName(u"cbo_jk")

        self.gridLayout_5.addWidget(self.cbo_jk, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_datadiri)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_4 = QLabel(self.frame_datadiri)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_3 = QLabel(self.frame_datadiri)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 3, 0, 1, 1)

        self.line_tmp_lahir = QLineEdit(self.frame_datadiri)
        self.line_tmp_lahir.setObjectName(u"line_tmp_lahir")

        self.gridLayout_5.addWidget(self.line_tmp_lahir, 4, 1, 1, 1)

        self.label_6 = QLabel(self.frame_datadiri)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 3, 3, 1, 1)

        self.line_nik = QLineEdit(self.frame_datadiri)
        self.line_nik.setObjectName(u"line_nik")

        self.gridLayout_5.addWidget(self.line_nik, 3, 4, 1, 1)

        self.label_40 = QLabel(self.frame_datadiri)
        self.label_40.setObjectName(u"label_40")
        font = QFont()
        font.setBold(True)
        self.label_40.setFont(font)

        self.gridLayout_5.addWidget(self.label_40, 0, 0, 1, 2)

        self.label_8 = QLabel(self.frame_datadiri)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 7, 0, 1, 1)

        self.cbo_agama = QComboBox(self.frame_datadiri)
        self.cbo_agama.setObjectName(u"cbo_agama")

        self.gridLayout_5.addWidget(self.cbo_agama, 6, 4, 1, 1)

        self.line_nama_lengkap = QLineEdit(self.frame_datadiri)
        self.line_nama_lengkap.setObjectName(u"line_nama_lengkap")

        self.gridLayout_5.addWidget(self.line_nama_lengkap, 2, 1, 1, 4)

        self.label_9 = QLabel(self.frame_datadiri)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 6, 3, 1, 1)

        self.line_no_kk = QLineEdit(self.frame_datadiri)
        self.line_no_kk.setObjectName(u"line_no_kk")

        self.gridLayout_5.addWidget(self.line_no_kk, 5, 4, 1, 1)

        self.label_7 = QLabel(self.frame_datadiri)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 5, 3, 1, 1)

        self.line_niat_npa = QLineEdit(self.frame_datadiri)
        self.line_niat_npa.setObjectName(u"line_niat_npa")

        self.gridLayout_5.addWidget(self.line_niat_npa, 4, 4, 1, 1)

        self.label_76 = QLabel(self.frame_datadiri)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_5.addWidget(self.label_76, 4, 3, 1, 1)

        self.line_ayah = QLineEdit(self.frame_datadiri)
        self.line_ayah.setObjectName(u"line_ayah")

        self.gridLayout_5.addWidget(self.line_ayah, 6, 1, 1, 1)

        self.line_ibu_kandung = QLineEdit(self.frame_datadiri)
        self.line_ibu_kandung.setObjectName(u"line_ibu_kandung")

        self.gridLayout_5.addWidget(self.line_ibu_kandung, 7, 1, 1, 1)

        self.label_78 = QLabel(self.frame_datadiri)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_5.addWidget(self.label_78, 6, 0, 1, 1)

        self.label_79 = QLabel(self.frame_datadiri)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_5.addWidget(self.label_79, 1, 0, 1, 1)

        self.line_id_guru = QLineEdit(self.frame_datadiri)
        self.line_id_guru.setObjectName(u"line_id_guru")

        self.gridLayout_5.addWidget(self.line_id_guru, 1, 1, 1, 1)

        self.gridLayout_5.setColumnMinimumWidth(0, 120)
        self.gridLayout_5.setColumnMinimumWidth(2, 20)
        self.gridLayout_5.setColumnMinimumWidth(3, 80)

        self.gridLayout_4.addWidget(self.frame_datadiri, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_7.addWidget(self.label_23, 1, 3, 1, 1)

        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_7.addWidget(self.label_24, 2, 3, 1, 1)

        self.line_nama_pemilik_rekening = QLineEdit(self.frame_6)
        self.line_nama_pemilik_rekening.setObjectName(u"line_nama_pemilik_rekening")

        self.gridLayout_7.addWidget(self.line_nama_pemilik_rekening, 3, 4, 1, 1)

        self.line_npwp = QLineEdit(self.frame_6)
        self.line_npwp.setObjectName(u"line_npwp")

        self.gridLayout_7.addWidget(self.line_npwp, 1, 4, 1, 1)

        self.cbo_goldar = QComboBox(self.frame_6)
        self.cbo_goldar.setObjectName(u"cbo_goldar")

        self.gridLayout_7.addWidget(self.cbo_goldar, 2, 4, 1, 1)

        self.line_nama_bank = QLineEdit(self.frame_6)
        self.line_nama_bank.setObjectName(u"line_nama_bank")

        self.gridLayout_7.addWidget(self.line_nama_bank, 5, 4, 1, 1)

        self.line_norek = QLineEdit(self.frame_6)
        self.line_norek.setObjectName(u"line_norek")

        self.gridLayout_7.addWidget(self.line_norek, 4, 4, 1, 1)

        self.label_26 = QLabel(self.frame_6)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_7.addWidget(self.label_26, 4, 3, 1, 1)

        self.label_27 = QLabel(self.frame_6)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_7.addWidget(self.label_27, 5, 3, 1, 1)

        self.label_25 = QLabel(self.frame_6)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_7.addWidget(self.label_25, 3, 3, 1, 1)

        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_7.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_7.addWidget(self.label_16, 2, 0, 1, 1)

        self.line_no_hp = QLineEdit(self.frame_6)
        self.line_no_hp.setObjectName(u"line_no_hp")

        self.gridLayout_7.addWidget(self.line_no_hp, 1, 1, 1, 1)

        self.line_email_pribadi = QLineEdit(self.frame_6)
        self.line_email_pribadi.setObjectName(u"line_email_pribadi")

        self.gridLayout_7.addWidget(self.line_email_pribadi, 2, 1, 1, 1)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_7.addWidget(self.label_18, 4, 0, 1, 1)

        self.line_password_hebat = QLineEdit(self.frame_6)
        self.line_password_hebat.setObjectName(u"line_password_hebat")

        self.gridLayout_7.addWidget(self.line_password_hebat, 4, 1, 1, 1)

        self.line_email_hebat = QLineEdit(self.frame_6)
        self.line_email_hebat.setObjectName(u"line_email_hebat")

        self.gridLayout_7.addWidget(self.line_email_hebat, 3, 1, 1, 1)

        self.line_bpjs = QLineEdit(self.frame_6)
        self.line_bpjs.setObjectName(u"line_bpjs")

        self.gridLayout_7.addWidget(self.line_bpjs, 5, 1, 1, 1)

        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 5, 0, 1, 1)

        self.label_42 = QLabel(self.frame_6)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font)

        self.gridLayout_7.addWidget(self.label_42, 0, 0, 1, 2)

        self.widget_4 = QWidget(self.frame_6)
        self.widget_4.setObjectName(u"widget_4")

        self.gridLayout_7.addWidget(self.widget_4, 1, 2, 1, 1)

        self.gridLayout_7.setColumnMinimumWidth(0, 120)
        self.gridLayout_7.setColumnMinimumWidth(2, 20)
        self.gridLayout_7.setColumnMinimumWidth(3, 80)

        self.gridLayout_4.addWidget(self.frame_6, 3, 0, 1, 1)

        self.frame_alamat = QFrame(self.scrollAreaWidgetContents)
        self.frame_alamat.setObjectName(u"frame_alamat")
        self.frame_alamat.setStyleSheet(u"")
        self.frame_alamat.setFrameShape(QFrame.StyledPanel)
        self.frame_alamat.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_alamat)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_32 = QLabel(self.frame_alamat)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_8.addWidget(self.label_32, 1, 3, 1, 1)

        self.label_63 = QLabel(self.frame_alamat)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_8.addWidget(self.label_63, 3, 0, 1, 1)

        self.line_kodepos = QLineEdit(self.frame_alamat)
        self.line_kodepos.setObjectName(u"line_kodepos")

        self.gridLayout_8.addWidget(self.line_kodepos, 3, 1, 1, 1)

        self.cbo_jarak = QComboBox(self.frame_alamat)
        self.cbo_jarak.setObjectName(u"cbo_jarak")

        self.gridLayout_8.addWidget(self.cbo_jarak, 4, 4, 1, 1)

        self.line_provinsi = QLineEdit(self.frame_alamat)
        self.line_provinsi.setObjectName(u"line_provinsi")

        self.gridLayout_8.addWidget(self.line_provinsi, 3, 4, 1, 1)

        self.cbo_waktu_tempuh = QComboBox(self.frame_alamat)
        self.cbo_waktu_tempuh.setObjectName(u"cbo_waktu_tempuh")

        self.gridLayout_8.addWidget(self.cbo_waktu_tempuh, 7, 4, 1, 1)

        self.label_34 = QLabel(self.frame_alamat)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_8.addWidget(self.label_34, 3, 3, 1, 1)

        self.label_36 = QLabel(self.frame_alamat)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_8.addWidget(self.label_36, 5, 3, 1, 1)

        self.label_37 = QLabel(self.frame_alamat)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_8.addWidget(self.label_37, 7, 3, 1, 1)

        self.line_kecamatan = QLineEdit(self.frame_alamat)
        self.line_kecamatan.setObjectName(u"line_kecamatan")

        self.gridLayout_8.addWidget(self.line_kecamatan, 1, 4, 1, 1)

        self.label_33 = QLabel(self.frame_alamat)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_8.addWidget(self.label_33, 2, 3, 1, 1)

        self.label_35 = QLabel(self.frame_alamat)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_8.addWidget(self.label_35, 4, 3, 1, 1)

        self.cbo_transportasi = QComboBox(self.frame_alamat)
        self.cbo_transportasi.setObjectName(u"cbo_transportasi")

        self.gridLayout_8.addWidget(self.cbo_transportasi, 5, 4, 1, 1)

        self.line_kab_kota = QLineEdit(self.frame_alamat)
        self.line_kab_kota.setObjectName(u"line_kab_kota")

        self.gridLayout_8.addWidget(self.line_kab_kota, 2, 4, 1, 1)

        self.label_29 = QLabel(self.frame_alamat)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_8.addWidget(self.label_29, 4, 0, 1, 1)

        self.cbo_status_tmp_tinggal = QComboBox(self.frame_alamat)
        self.cbo_status_tmp_tinggal.setObjectName(u"cbo_status_tmp_tinggal")

        self.gridLayout_8.addWidget(self.cbo_status_tmp_tinggal, 1, 1, 1, 1)

        self.line_alamat = QLineEdit(self.frame_alamat)
        self.line_alamat.setObjectName(u"line_alamat")

        self.gridLayout_8.addWidget(self.line_alamat, 2, 1, 1, 1)

        self.label_22 = QLabel(self.frame_alamat)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_8.addWidget(self.label_22, 1, 0, 1, 1)

        self.label_28 = QLabel(self.frame_alamat)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_8.addWidget(self.label_28, 2, 0, 1, 1)

        self.line_kel_desa = QLineEdit(self.frame_alamat)
        self.line_kel_desa.setObjectName(u"line_kel_desa")

        self.gridLayout_8.addWidget(self.line_kel_desa, 7, 1, 1, 1)

        self.line_rw = QLineEdit(self.frame_alamat)
        self.line_rw.setObjectName(u"line_rw")

        self.gridLayout_8.addWidget(self.line_rw, 5, 1, 1, 1)

        self.label_31 = QLabel(self.frame_alamat)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_8.addWidget(self.label_31, 7, 0, 1, 1)

        self.line_rt = QLineEdit(self.frame_alamat)
        self.line_rt.setObjectName(u"line_rt")

        self.gridLayout_8.addWidget(self.line_rt, 4, 1, 1, 1)

        self.label_30 = QLabel(self.frame_alamat)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_8.addWidget(self.label_30, 5, 0, 1, 1)

        self.label_41 = QLabel(self.frame_alamat)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)

        self.gridLayout_8.addWidget(self.label_41, 0, 0, 1, 2)

        self.widget_2 = QWidget(self.frame_alamat)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_8.addWidget(self.widget_2, 1, 2, 1, 1)

        self.gridLayout_8.setColumnMinimumWidth(0, 120)
        self.gridLayout_8.setColumnMinimumWidth(2, 20)
        self.gridLayout_8.setColumnMinimumWidth(3, 80)

        self.gridLayout_4.addWidget(self.frame_alamat, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 1, 3, 1, 1)

        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 2, 3, 1, 1)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 3, 3, 1, 1)

        self.line_tmt_pegawai = QLineEdit(self.frame_5)
        self.line_tmt_pegawai.setObjectName(u"line_tmt_pegawai")

        self.gridLayout_6.addWidget(self.line_tmt_pegawai, 3, 4, 1, 1)

        self.line_tmt_guru = QLineEdit(self.frame_5)
        self.line_tmt_guru.setObjectName(u"line_tmt_guru")

        self.gridLayout_6.addWidget(self.line_tmt_guru, 2, 4, 1, 1)

        self.line_peg_id = QLineEdit(self.frame_5)
        self.line_peg_id.setObjectName(u"line_peg_id")

        self.gridLayout_6.addWidget(self.line_peg_id, 1, 4, 1, 1)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)

        self.cbo_status_kepegawaian = QComboBox(self.frame_5)
        self.cbo_status_kepegawaian.addItem("")
        self.cbo_status_kepegawaian.addItem("")
        self.cbo_status_kepegawaian.setObjectName(u"cbo_status_kepegawaian")

        self.gridLayout_6.addWidget(self.cbo_status_kepegawaian, 1, 1, 1, 1)

        self.line_nuptk = QLineEdit(self.frame_5)
        self.line_nuptk.setObjectName(u"line_nuptk")

        self.gridLayout_6.addWidget(self.line_nuptk, 2, 1, 1, 1)

        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 3, 0, 1, 1)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 2, 0, 1, 1)

        self.line_npk = QLineEdit(self.frame_5)
        self.line_npk.setObjectName(u"line_npk")

        self.gridLayout_6.addWidget(self.line_npk, 3, 1, 1, 1)

        self.label_43 = QLabel(self.frame_5)
        self.label_43.setObjectName(u"label_43")
        sizePolicy1.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy1)
        self.label_43.setFont(font)

        self.gridLayout_6.addWidget(self.label_43, 0, 0, 1, 2)

        self.widget_3 = QWidget(self.frame_5)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout_6.addWidget(self.widget_3, 1, 2, 1, 1)

        self.gridLayout_6.setColumnMinimumWidth(0, 120)
        self.gridLayout_6.setColumnMinimumWidth(2, 20)
        self.gridLayout_6.setColumnMinimumWidth(3, 80)

        self.gridLayout_4.addWidget(self.frame_5, 2, 0, 1, 1)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_7)
        self.gridLayout_14.setSpacing(5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(5, 5, 5, 5)
        self.line_model_sertifikasi = QLineEdit(self.frame_7)
        self.line_model_sertifikasi.setObjectName(u"line_model_sertifikasi")

        self.gridLayout_14.addWidget(self.line_model_sertifikasi, 4, 4, 1, 1)

        self.line_naungan_sertifikasi = QLineEdit(self.frame_7)
        self.line_naungan_sertifikasi.setObjectName(u"line_naungan_sertifikasi")

        self.gridLayout_14.addWidget(self.line_naungan_sertifikasi, 6, 4, 1, 1)

        self.line_jalur_sertifikasi = QLineEdit(self.frame_7)
        self.line_jalur_sertifikasi.setObjectName(u"line_jalur_sertifikasi")

        self.gridLayout_14.addWidget(self.line_jalur_sertifikasi, 5, 4, 1, 1)

        self.label_75 = QLabel(self.frame_7)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_14.addWidget(self.label_75, 6, 3, 1, 1)

        self.label_74 = QLabel(self.frame_7)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_14.addWidget(self.label_74, 5, 3, 1, 1)

        self.label_64 = QLabel(self.frame_7)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_14.addWidget(self.label_64, 6, 0, 1, 1)

        self.label_65 = QLabel(self.frame_7)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_14.addWidget(self.label_65, 1, 3, 1, 1)

        self.label_66 = QLabel(self.frame_7)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_14.addWidget(self.label_66, 3, 3, 1, 1)

        self.label_67 = QLabel(self.frame_7)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_14.addWidget(self.label_67, 4, 3, 1, 1)

        self.label_68 = QLabel(self.frame_7)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_14.addWidget(self.label_68, 2, 3, 1, 1)

        self.label_69 = QLabel(self.frame_7)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_14.addWidget(self.label_69, 1, 0, 1, 1)

        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_14.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_70 = QLabel(self.frame_7)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_14.addWidget(self.label_70, 2, 0, 1, 1)

        self.line_lptk_sertifikasi = QLineEdit(self.frame_7)
        self.line_lptk_sertifikasi.setObjectName(u"line_lptk_sertifikasi")

        self.gridLayout_14.addWidget(self.line_lptk_sertifikasi, 6, 1, 1, 1)

        self.line_tgl_lulus_sertifikasi = QLineEdit(self.frame_7)
        self.line_tgl_lulus_sertifikasi.setObjectName(u"line_tgl_lulus_sertifikasi")

        self.gridLayout_14.addWidget(self.line_tgl_lulus_sertifikasi, 2, 4, 1, 1)

        self.label_71 = QLabel(self.frame_7)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_14.addWidget(self.label_71, 4, 0, 1, 1)

        self.line_kode_mapel_sertifikasi = QLineEdit(self.frame_7)
        self.line_kode_mapel_sertifikasi.setObjectName(u"line_kode_mapel_sertifikasi")

        self.gridLayout_14.addWidget(self.line_kode_mapel_sertifikasi, 4, 1, 1, 1)

        self.line_nopes_sertifikasi = QLineEdit(self.frame_7)
        self.line_nopes_sertifikasi.setObjectName(u"line_nopes_sertifikasi")

        self.gridLayout_14.addWidget(self.line_nopes_sertifikasi, 5, 1, 1, 1)

        self.line_mapel_sertifikasi = QLineEdit(self.frame_7)
        self.line_mapel_sertifikasi.setObjectName(u"line_mapel_sertifikasi")

        self.gridLayout_14.addWidget(self.line_mapel_sertifikasi, 3, 1, 1, 1)

        self.label_72 = QLabel(self.frame_7)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_14.addWidget(self.label_72, 5, 0, 1, 1)

        self.label_73 = QLabel(self.frame_7)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font)

        self.gridLayout_14.addWidget(self.label_73, 0, 0, 1, 2)

        self.line_tahun_sertifikasi = QLineEdit(self.frame_7)
        self.line_tahun_sertifikasi.setObjectName(u"line_tahun_sertifikasi")

        self.gridLayout_14.addWidget(self.line_tahun_sertifikasi, 3, 4, 1, 1)

        self.cbo_status_sertifikasi = QComboBox(self.frame_7)
        self.cbo_status_sertifikasi.setObjectName(u"cbo_status_sertifikasi")

        self.gridLayout_14.addWidget(self.cbo_status_sertifikasi, 1, 1, 1, 1)

        self.cbo_jenjang_sertifikasi = QComboBox(self.frame_7)
        self.cbo_jenjang_sertifikasi.setObjectName(u"cbo_jenjang_sertifikasi")

        self.gridLayout_14.addWidget(self.cbo_jenjang_sertifikasi, 2, 1, 1, 1)

        self.widget_5 = QWidget(self.frame_7)
        self.widget_5.setObjectName(u"widget_5")

        self.gridLayout_14.addWidget(self.widget_5, 1, 2, 1, 1)

        self.line_no_sertifikasi = QLineEdit(self.frame_7)
        self.line_no_sertifikasi.setObjectName(u"line_no_sertifikasi")

        self.gridLayout_14.addWidget(self.line_no_sertifikasi, 1, 4, 1, 1)

        self.gridLayout_14.setColumnMinimumWidth(0, 120)
        self.gridLayout_14.setColumnMinimumWidth(2, 20)
        self.gridLayout_14.setColumnMinimumWidth(3, 80)

        self.gridLayout_4.addWidget(self.frame_7, 4, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_12.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.frame3 = QFrame(self.tab1)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(0)
        self.gridLayout_16.setVerticalSpacing(20)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_10)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_10)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)

        self.gridLayout_11.addWidget(self.label_52, 0, 0, 1, 2)

        self.tbl_pendidikan_formal = QTableWidget(self.frame_10)
        self.tbl_pendidikan_formal.setObjectName(u"tbl_pendidikan_formal")

        self.gridLayout_11.addWidget(self.tbl_pendidikan_formal, 1, 0, 1, 5)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_11)
        self.gridLayout_13.setSpacing(5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(5, 5, 5, 5)
        self.line_nem_ipk = QLineEdit(self.frame_11)
        self.line_nem_ipk.setObjectName(u"line_nem_ipk")
        self.line_nem_ipk.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_13.addWidget(self.line_nem_ipk, 6, 5, 1, 1)

        self.label_61 = QLabel(self.frame_11)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_13.addWidget(self.label_61, 5, 5, 1, 1)

        self.line_alamat_sekolah = QLineEdit(self.frame_11)
        self.line_alamat_sekolah.setObjectName(u"line_alamat_sekolah")

        self.gridLayout_13.addWidget(self.line_alamat_sekolah, 1, 3, 1, 3)

        self.line_nomor_ijazah = QLineEdit(self.frame_11)
        self.line_nomor_ijazah.setObjectName(u"line_nomor_ijazah")
        self.line_nomor_ijazah.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_13.addWidget(self.line_nomor_ijazah, 6, 4, 1, 1)

        self.label_58 = QLabel(self.frame_11)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_13.addWidget(self.label_58, 5, 1, 1, 1)

        self.label_60 = QLabel(self.frame_11)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_13.addWidget(self.label_60, 5, 4, 1, 1)

        self.line_tahun_lulus = QLineEdit(self.frame_11)
        self.line_tahun_lulus.setObjectName(u"line_tahun_lulus")
        self.line_tahun_lulus.setMinimumSize(QSize(80, 0))
        self.line_tahun_lulus.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_13.addWidget(self.line_tahun_lulus, 6, 2, 1, 1)

        self.cbo_status_sekolah = QComboBox(self.frame_11)
        self.cbo_status_sekolah.addItem("")
        self.cbo_status_sekolah.addItem("")
        self.cbo_status_sekolah.setObjectName(u"cbo_status_sekolah")
        self.cbo_status_sekolah.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_13.addWidget(self.cbo_status_sekolah, 6, 0, 1, 1)

        self.label_53 = QLabel(self.frame_11)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_13.addWidget(self.label_53, 0, 0, 1, 1)

        self.cbo_jenjang_sekolah = QComboBox(self.frame_11)
        self.cbo_jenjang_sekolah.setObjectName(u"cbo_jenjang_sekolah")
        self.cbo_jenjang_sekolah.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_13.addWidget(self.cbo_jenjang_sekolah, 1, 0, 1, 1)

        self.label_56 = QLabel(self.frame_11)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_13.addWidget(self.label_56, 0, 3, 1, 1)

        self.label_54 = QLabel(self.frame_11)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_13.addWidget(self.label_54, 0, 1, 1, 1)

        self.label_59 = QLabel(self.frame_11)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_13.addWidget(self.label_59, 5, 3, 1, 1)

        self.label_55 = QLabel(self.frame_11)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_13.addWidget(self.label_55, 5, 0, 1, 1)

        self.line_tgl_ijazah = QLineEdit(self.frame_11)
        self.line_tgl_ijazah.setObjectName(u"line_tgl_ijazah")
        self.line_tgl_ijazah.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_13.addWidget(self.line_tgl_ijazah, 6, 3, 1, 1)

        self.label_57 = QLabel(self.frame_11)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_13.addWidget(self.label_57, 5, 2, 1, 1)

        self.line_tahun_masuk = QLineEdit(self.frame_11)
        self.line_tahun_masuk.setObjectName(u"line_tahun_masuk")
        self.line_tahun_masuk.setMinimumSize(QSize(80, 0))
        self.line_tahun_masuk.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_13.addWidget(self.line_tahun_masuk, 6, 1, 1, 1)

        self.line_nama_sekolah = QLineEdit(self.frame_11)
        self.line_nama_sekolah.setObjectName(u"line_nama_sekolah")

        self.gridLayout_13.addWidget(self.line_nama_sekolah, 1, 1, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_4, 0, 6, 8, 1)

        self.btn_tambah_sekolah = QPushButton(self.frame_11)
        self.btn_tambah_sekolah.setObjectName(u"btn_tambah_sekolah")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_tambah_sekolah.sizePolicy().hasHeightForWidth())
        self.btn_tambah_sekolah.setSizePolicy(sizePolicy3)
        self.btn_tambah_sekolah.setMinimumSize(QSize(60, 0))
        self.btn_tambah_sekolah.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_13.addWidget(self.btn_tambah_sekolah, 0, 7, 7, 1)


        self.gridLayout_11.addWidget(self.frame_11, 2, 0, 1, 5)


        self.gridLayout_16.addWidget(self.frame_10, 1, 0, 1, 1)

        self.frame_8 = QFrame(self.frame3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_8)
        self.gridLayout_9.setSpacing(5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_9)
        self.gridLayout_10.setSpacing(5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 1, 8, 1, 1)

        self.label_46 = QLabel(self.frame_9)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_10.addWidget(self.label_46, 2, 0, 1, 1)

        self.label_45 = QLabel(self.frame_9)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_10.addWidget(self.label_45, 0, 0, 1, 1)

        self.cbo_pendidikan_anak = QComboBox(self.frame_9)
        self.cbo_pendidikan_anak.setObjectName(u"cbo_pendidikan_anak")
        self.cbo_pendidikan_anak.setMinimumSize(QSize(80, 24))

        self.gridLayout_10.addWidget(self.cbo_pendidikan_anak, 1, 4, 1, 1)

        self.label_51 = QLabel(self.frame_9)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_10.addWidget(self.label_51, 0, 5, 1, 1)

        self.label_49 = QLabel(self.frame_9)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_10.addWidget(self.label_49, 0, 4, 1, 1)

        self.cbo_jk_anak = QComboBox(self.frame_9)
        self.cbo_jk_anak.setObjectName(u"cbo_jk_anak")
        self.cbo_jk_anak.setMinimumSize(QSize(50, 24))

        self.gridLayout_10.addWidget(self.cbo_jk_anak, 1, 5, 1, 1)

        self.line_tmp_lahir_anak = QLineEdit(self.frame_9)
        self.line_tmp_lahir_anak.setObjectName(u"line_tmp_lahir_anak")
        self.line_tmp_lahir_anak.setMinimumSize(QSize(100, 24))

        self.gridLayout_10.addWidget(self.line_tmp_lahir_anak, 3, 0, 1, 1)

        self.line_tgl_lahir_anak = QLineEdit(self.frame_9)
        self.line_tgl_lahir_anak.setObjectName(u"line_tgl_lahir_anak")
        self.line_tgl_lahir_anak.setMinimumSize(QSize(80, 24))

        self.gridLayout_10.addWidget(self.line_tgl_lahir_anak, 3, 1, 1, 1)

        self.label_47 = QLabel(self.frame_9)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_10.addWidget(self.label_47, 2, 1, 1, 1)

        self.label_50 = QLabel(self.frame_9)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_10.addWidget(self.label_50, 2, 4, 1, 1)

        self.cbo_pekerjaan_anak = QComboBox(self.frame_9)
        self.cbo_pekerjaan_anak.setObjectName(u"cbo_pekerjaan_anak")
        self.cbo_pekerjaan_anak.setMinimumSize(QSize(120, 24))

        self.gridLayout_10.addWidget(self.cbo_pekerjaan_anak, 3, 4, 1, 1)

        self.label_48 = QLabel(self.frame_9)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_10.addWidget(self.label_48, 2, 5, 1, 1)

        self.cbo_status_anak = QComboBox(self.frame_9)
        self.cbo_status_anak.setObjectName(u"cbo_status_anak")
        self.cbo_status_anak.setMinimumSize(QSize(80, 24))

        self.gridLayout_10.addWidget(self.cbo_status_anak, 3, 5, 1, 1)

        self.btn_tambah_anak = QPushButton(self.frame_9)
        self.btn_tambah_anak.setObjectName(u"btn_tambah_anak")
        sizePolicy3.setHeightForWidth(self.btn_tambah_anak.sizePolicy().hasHeightForWidth())
        self.btn_tambah_anak.setSizePolicy(sizePolicy3)
        self.btn_tambah_anak.setMinimumSize(QSize(60, 0))
        self.btn_tambah_anak.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_10.addWidget(self.btn_tambah_anak, 0, 9, 4, 1)

        self.label_80 = QLabel(self.frame_9)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_10.addWidget(self.label_80, 0, 1, 1, 1)

        self.line_nama_anak = QLineEdit(self.frame_9)
        self.line_nama_anak.setObjectName(u"line_nama_anak")
        self.line_nama_anak.setMinimumSize(QSize(200, 24))

        self.gridLayout_10.addWidget(self.line_nama_anak, 1, 0, 1, 1)

        self.line_nik_anak = QLineEdit(self.frame_9)
        self.line_nik_anak.setObjectName(u"line_nik_anak")
        self.line_nik_anak.setMinimumSize(QSize(200, 24))

        self.gridLayout_10.addWidget(self.line_nik_anak, 1, 1, 1, 1)


        self.gridLayout_9.addWidget(self.frame_9, 6, 0, 1, 5)

        self.label_44 = QLabel(self.frame_8)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)

        self.gridLayout_9.addWidget(self.label_44, 0, 0, 1, 1)

        self.tbl_daftar_keluarga = QTableWidget(self.frame_8)
        self.tbl_daftar_keluarga.setObjectName(u"tbl_daftar_keluarga")

        self.gridLayout_9.addWidget(self.tbl_daftar_keluarga, 5, 0, 1, 5)

        self.label_38 = QLabel(self.frame_8)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_9.addWidget(self.label_38, 1, 0, 1, 1)

        self.cbo_status_kawin = QComboBox(self.frame_8)
        self.cbo_status_kawin.setObjectName(u"cbo_status_kawin")
        self.cbo_status_kawin.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.cbo_status_kawin, 2, 0, 1, 1)

        self.label_39 = QLabel(self.frame_8)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_9.addWidget(self.label_39, 1, 1, 1, 1)

        self.line_nama_istri_suami = QLineEdit(self.frame_8)
        self.line_nama_istri_suami.setObjectName(u"line_nama_istri_suami")
        self.line_nama_istri_suami.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.line_nama_istri_suami, 2, 1, 1, 1)

        self.label_77 = QLabel(self.frame_8)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_9.addWidget(self.label_77, 1, 2, 1, 1)

        self.line_jumlah_anak = QLineEdit(self.frame_8)
        self.line_jumlah_anak.setObjectName(u"line_jumlah_anak")
        self.line_jumlah_anak.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.line_jumlah_anak, 2, 2, 1, 1)


        self.gridLayout_16.addWidget(self.frame_8, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame3, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Search By:", None))
        self.cbo_search_by.setItemText(0, QCoreApplication.translate("Form", u"nama_lengkap", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"Daftar Guru", None))
        self.btn_save_detail.setText(QCoreApplication.translate("Form", u"Save", None))
        self.label_62.setText(QCoreApplication.translate("Form", u"Nama Lengkap", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Tanggal Lahir", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Tempat Lahir", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"NIK", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"DATA DIRI", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Nama Ibu", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Agama", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Nomor KK", None))
        self.label_76.setText(QCoreApplication.translate("Form", u"NIAT/NPA", None))
        self.label_78.setText(QCoreApplication.translate("Form", u"Nama Ayah", None))
        self.label_79.setText(QCoreApplication.translate("Form", u"ID GURU", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"NPWP", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Golongan Darah", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Nomor Rekening", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Nama Bank", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Rekening a.n.", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"No. Handphone", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Email Madrasah Hebat", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Email Pribadi", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Password Email MH", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Nomor BPJS Kesehatan", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"DATA LAINNYA", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Kecamatan", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"Kodepos", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Provinsi", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Transportasi", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Waktu Tempuh", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Kabupaten/Kota", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Jarak", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"RT", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Status Tempat Tinggal", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Kelurahan/Desa", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"RW", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"DATA ALAMAT", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Peg ID", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"TMT Guru", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"TMT Pegawai", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Status Kepegawaian", None))
        self.cbo_status_kepegawaian.setItemText(0, QCoreApplication.translate("Form", u"Non-PNS", None))
        self.cbo_status_kepegawaian.setItemText(1, QCoreApplication.translate("Form", u"PNS", None))

        self.label_12.setText(QCoreApplication.translate("Form", u"NPK", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"NUPTK", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"DATA KEPEGAWAIAN", None))
        self.label_75.setText(QCoreApplication.translate("Form", u"Naungan Sertifikasi", None))
        self.label_74.setText(QCoreApplication.translate("Form", u"Jalur Sertifikasi", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"LPTK Penyelenggara", None))
        self.label_65.setText(QCoreApplication.translate("Form", u"Nomor Sertifikat", None))
        self.label_66.setText(QCoreApplication.translate("Form", u"Tahun Sertifikasi", None))
        self.label_67.setText(QCoreApplication.translate("Form", u"Model Sertifikasi", None))
        self.label_68.setText(QCoreApplication.translate("Form", u"Tanggal Lulus", None))
        self.label_69.setText(QCoreApplication.translate("Form", u"Status Sertifikasi", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Mapel", None))
        self.label_70.setText(QCoreApplication.translate("Form", u"Jenjang Sertifikasi", None))
        self.label_71.setText(QCoreApplication.translate("Form", u"Kode Mapel", None))
        self.label_72.setText(QCoreApplication.translate("Form", u"Nomor Peserta", None))
        self.label_73.setText(QCoreApplication.translate("Form", u"DATA SERTIFIKASI", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"PENDIDIKAN FORMAL", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"NEM/IPK", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"Tahun Masuk", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"Nomor Ijazah", None))
        self.cbo_status_sekolah.setItemText(0, QCoreApplication.translate("Form", u"Negeri", None))
        self.cbo_status_sekolah.setItemText(1, QCoreApplication.translate("Form", u"Swasta", None))

        self.label_53.setText(QCoreApplication.translate("Form", u"Jenjang", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"Nama Sekolah", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"Tanggal Ijazah", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"Status", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"Tahun Keluar", None))
        self.btn_tambah_sekolah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"Tempat Lahir", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"Nama Anak", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"JK", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"Pendidikan", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"Tanggal Lahir", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"Pekerjaan", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"Status", None))
        self.btn_tambah_anak.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.label_80.setText(QCoreApplication.translate("Form", u"NIK", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"DATA KELUARGA", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Status Perkawinan", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Nama Suami/Istri", None))
        self.label_77.setText(QCoreApplication.translate("Form", u"Jumlah Anak", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("Form", u"Biodata", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Keaktifan", None))
    # retranslateUi

