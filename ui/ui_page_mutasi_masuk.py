# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_mutasi_masuk.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1138, 582)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(450, 0))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)

        self.line_no_urut = QLineEdit(self.tab_3)
        self.line_no_urut.setObjectName(u"line_no_urut")
        self.line_no_urut.setMinimumSize(QSize(50, 24))
        self.line_no_urut.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_6.addWidget(self.line_no_urut, 0, 1, 1, 2)

        self.cbo_jk = QComboBox(self.tab_3)
        self.cbo_jk.addItem("")
        self.cbo_jk.addItem("")
        self.cbo_jk.setObjectName(u"cbo_jk")
        self.cbo_jk.setMinimumSize(QSize(50, 24))
        self.cbo_jk.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_6.addWidget(self.cbo_jk, 2, 1, 1, 1)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 2, 0, 1, 1)

        self.cbo_kelas = QComboBox(self.tab_3)
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItem("")
        self.cbo_kelas.setObjectName(u"cbo_kelas")
        self.cbo_kelas.setMinimumSize(QSize(50, 24))
        self.cbo_kelas.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_6.addWidget(self.cbo_kelas, 3, 1, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 3, 0, 1, 1)

        self.btn_tambah = QPushButton(self.tab_3)
        self.btn_tambah.setObjectName(u"btn_tambah")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tambah.sizePolicy().hasHeightForWidth())
        self.btn_tambah.setSizePolicy(sizePolicy)
        self.btn_tambah.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.btn_tambah, 4, 0, 1, 3)

        self.line_nama_lengkap = QLineEdit(self.tab_3)
        self.line_nama_lengkap.setObjectName(u"line_nama_lengkap")
        self.line_nama_lengkap.setMinimumSize(QSize(240, 24))

        self.gridLayout_6.addWidget(self.line_nama_lengkap, 1, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(328, 392, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 5, 1, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tbl_diterima = QTableWidget(self.tab)
        self.tbl_diterima.setObjectName(u"tbl_diterima")
        self.tbl_diterima.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tbl_diterima, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tbl_calon_belum = QTableWidget(self.tab_2)
        self.tbl_calon_belum.setObjectName(u"tbl_calon_belum")
        self.tbl_calon_belum.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_5.addWidget(self.tbl_calon_belum, 0, 0, 1, 1)

        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(450, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.date_tgl_masuk = QDateEdit(self.frame)
        self.date_tgl_masuk.setObjectName(u"date_tgl_masuk")
        self.date_tgl_masuk.setMinimumSize(QSize(0, 24))
        self.date_tgl_masuk.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.date_tgl_masuk.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.date_tgl_masuk, 0, 1, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.btn_terima = QPushButton(self.frame)
        self.btn_terima.setObjectName(u"btn_terima")
        self.btn_terima.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.btn_terima, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 3, 1)

        self.tbl_daftar_calon_siswa = QTableWidget(Form)
        self.tbl_daftar_calon_siswa.setObjectName(u"tbl_daftar_calon_siswa")
        self.tbl_daftar_calon_siswa.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_3.addWidget(self.tbl_daftar_calon_siswa, 0, 0, 3, 1)

        self.gridLayout_3.setColumnStretch(0, 1)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"No Urut", None))
        self.cbo_jk.setItemText(0, QCoreApplication.translate("Form", u"L", None))
        self.cbo_jk.setItemText(1, QCoreApplication.translate("Form", u"P", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Nama Lengkap", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"JK", None))
        self.cbo_kelas.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.cbo_kelas.setItemText(1, QCoreApplication.translate("Form", u"2", None))
        self.cbo_kelas.setItemText(2, QCoreApplication.translate("Form", u"3", None))
        self.cbo_kelas.setItemText(3, QCoreApplication.translate("Form", u"4", None))
        self.cbo_kelas.setItemText(4, QCoreApplication.translate("Form", u"5", None))
        self.cbo_kelas.setItemText(5, QCoreApplication.translate("Form", u"6", None))

        self.label_8.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.btn_tambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Input Baru", None))
#if QT_CONFIG(tooltip)
        self.tbl_diterima.setToolTip(QCoreApplication.translate("Form", u"Tekan tombol silang untuk membatalkan", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Sudah Diterima", None))
        self.date_tgl_masuk.setDisplayFormat(QCoreApplication.translate("Form", u"dd MMMM yyyy", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None))
#if QT_CONFIG(tooltip)
        self.btn_terima.setToolTip(QCoreApplication.translate("Form", u"Menerima semua calon siswa yang tercantum di tabel", None))
#endif // QT_CONFIG(tooltip)
        self.btn_terima.setText(QCoreApplication.translate("Form", u"Terima Semua", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Belum Diterima", None))
    # retranslateUi

