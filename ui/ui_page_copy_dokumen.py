# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_copy_dokumen.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1129, 824)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_keterangan = QLineEdit(self.widget)
        self.line_keterangan.setObjectName(u"line_keterangan")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_keterangan.sizePolicy().hasHeightForWidth())
        self.line_keterangan.setSizePolicy(sizePolicy1)
        self.line_keterangan.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.line_keterangan, 2, 1, 1, 1)

        self.line_jenis_dokumen = QLineEdit(self.widget)
        self.line_jenis_dokumen.setObjectName(u"line_jenis_dokumen")
        sizePolicy1.setHeightForWidth(self.line_jenis_dokumen.sizePolicy().hasHeightForWidth())
        self.line_jenis_dokumen.setSizePolicy(sizePolicy1)
        self.line_jenis_dokumen.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.line_jenis_dokumen, 1, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.cbo_filter_keterangan = QComboBox(self.widget)
        self.cbo_filter_keterangan.setObjectName(u"cbo_filter_keterangan")
        self.cbo_filter_keterangan.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.cbo_filter_keterangan, 2, 2, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.tbl_daftar_nama = QTableWidget(self.widget)
        self.tbl_daftar_nama.setObjectName(u"tbl_daftar_nama")
        self.tbl_daftar_nama.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.tbl_daftar_nama, 3, 0, 1, 3)

        self.cbo_filter_jenis_dokumen = QComboBox(self.widget)
        self.cbo_filter_jenis_dokumen.setObjectName(u"cbo_filter_jenis_dokumen")
        self.cbo_filter_jenis_dokumen.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.cbo_filter_jenis_dokumen, 1, 2, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.cbo_target = QComboBox(self.widget)
        self.cbo_target.addItem("")
        self.cbo_target.addItem("")
        self.cbo_target.setObjectName(u"cbo_target")
        self.cbo_target.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.cbo_target, 0, 1, 1, 1)

        self.radio_active_only = QRadioButton(self.widget)
        self.radio_active_only.setObjectName(u"radio_active_only")
        self.radio_active_only.setChecked(True)

        self.gridLayout_2.addWidget(self.radio_active_only, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(450, 0))
        self.widget_2.setMaximumSize(QSize(450, 16777215))
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.btn_browse = QPushButton(self.widget_3)
        self.btn_browse.setObjectName(u"btn_browse")

        self.gridLayout_3.addWidget(self.btn_browse, 0, 1, 1, 1)

        self.line_tujuan = QLineEdit(self.widget_3)
        self.line_tujuan.setObjectName(u"line_tujuan")
        self.line_tujuan.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.line_tujuan, 1, 0, 1, 2)


        self.gridLayout_6.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.cbo_opsi_namafile = QComboBox(self.widget_4)
        self.cbo_opsi_namafile.addItem("")
        self.cbo_opsi_namafile.addItem("")
        self.cbo_opsi_namafile.setObjectName(u"cbo_opsi_namafile")
        self.cbo_opsi_namafile.setMinimumSize(QSize(0, 24))

        self.gridLayout_4.addWidget(self.cbo_opsi_namafile, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_4, 1, 0, 1, 1)

        self.plain_log = QPlainTextEdit(self.widget_2)
        self.plain_log.setObjectName(u"plain_log")

        self.gridLayout_6.addWidget(self.plain_log, 2, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_copy = QPushButton(self.widget_5)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.btn_copy, 0, 0, 1, 1)

        self.btn_clear_log = QPushButton(self.widget_5)
        self.btn_clear_log.setObjectName(u"btn_clear_log")
        self.btn_clear_log.setMinimumSize(QSize(0, 40))
        self.btn_clear_log.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_5.addWidget(self.btn_clear_log, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.widget_5, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Jenis Dokumen", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Target", None))
        self.cbo_target.setItemText(0, QCoreApplication.translate("Form", u"Siswa", None))
        self.cbo_target.setItemText(1, QCoreApplication.translate("Form", u"Guru", None))

        self.radio_active_only.setText(QCoreApplication.translate("Form", u"Siswa Aktif Saja", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pilih Folder Tujuan", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Format Nama File", None))
        self.cbo_opsi_namafile.setItemText(0, QCoreApplication.translate("Form", u"NISN", None))
        self.cbo_opsi_namafile.setItemText(1, "")

        self.btn_copy.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.btn_clear_log.setText(QCoreApplication.translate("Form", u"Clear Log", None))
    # retranslateUi

