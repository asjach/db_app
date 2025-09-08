# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_rename_dokumen.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1198, 740)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.viewer_layout = QGridLayout(self.widget_2)
        self.viewer_layout.setObjectName(u"viewer_layout")

        self.gridLayout_2.addWidget(self.widget_2, 0, 2, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(500, 0))
        self.widget.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.widget_3 = QWidget(self.splitter)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(333, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.cbo_target = QComboBox(self.widget_3)
        self.cbo_target.addItem("")
        self.cbo_target.addItem("")
        self.cbo_target.setObjectName(u"cbo_target")
        self.cbo_target.setMinimumSize(QSize(100, 24))

        self.gridLayout.addWidget(self.cbo_target, 0, 1, 1, 1)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tbl_daftar_nama = QTableWidget(self.widget_3)
        self.tbl_daftar_nama.setObjectName(u"tbl_daftar_nama")
        self.tbl_daftar_nama.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tbl_daftar_nama, 1, 0, 1, 3)

        self.splitter.addWidget(self.widget_3)
        self.widget_4 = QWidget(self.splitter)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.tbl_daftar_dokumen = QTableWidget(self.widget_4)
        self.tbl_daftar_dokumen.setObjectName(u"tbl_daftar_dokumen")
        self.tbl_daftar_dokumen.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_3.addWidget(self.tbl_daftar_dokumen, 1, 0, 1, 1)

        self.splitter.addWidget(self.widget_4)

        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMaximumSize(QSize(400, 16777215))
        font = QFont()
        font.setFamilies([u"Aptos Narrow"])
        font.setPointSize(10)
        self.widget_5.setFont(font)
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.gridLayout_5 = QGridLayout(self.widget_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_rename = QPushButton(self.widget_6)
        self.btn_rename.setObjectName(u"btn_rename")
        self.btn_rename.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.btn_rename, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_6, 24, 0, 1, 3)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_8 = QLabel(self.widget_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(70, 0))

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.line_id_dokumen = QLineEdit(self.widget_7)
        self.line_id_dokumen.setObjectName(u"line_id_dokumen")
        self.line_id_dokumen.setEnabled(False)
        self.line_id_dokumen.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.line_id_dokumen, 0, 1, 1, 1)

        self.line_no_induk = QLineEdit(self.widget_7)
        self.line_no_induk.setObjectName(u"line_no_induk")
        self.line_no_induk.setEnabled(False)
        self.line_no_induk.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.line_no_induk, 0, 3, 1, 1)

        self.line_nama = QLineEdit(self.widget_7)
        self.line_nama.setObjectName(u"line_nama")
        self.line_nama.setEnabled(False)
        self.line_nama.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.line_nama, 2, 1, 1, 3)


        self.gridLayout_6.addWidget(self.widget_7, 0, 0, 1, 3)

        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.label_15, 21, 0, 1, 1)

        self.plain_path_old = QPlainTextEdit(self.widget_5)
        self.plain_path_old.setObjectName(u"plain_path_old")
        self.plain_path_old.setEnabled(False)
        self.plain_path_old.setMinimumSize(QSize(0, 60))
        self.plain_path_old.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_6.addWidget(self.plain_path_old, 11, 0, 1, 2)

        self.plain_path_new = QPlainTextEdit(self.widget_5)
        self.plain_path_new.setObjectName(u"plain_path_new")
        self.plain_path_new.setEnabled(False)
        self.plain_path_new.setMinimumSize(QSize(0, 60))
        self.plain_path_new.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_6.addWidget(self.plain_path_new, 22, 0, 1, 2)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 10, 0, 1, 1)

        self.line_keterangan_old = QLineEdit(self.widget_5)
        self.line_keterangan_old.setObjectName(u"line_keterangan_old")
        self.line_keterangan_old.setEnabled(False)
        self.line_keterangan_old.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.line_keterangan_old, 6, 1, 1, 1)

        self.line_jenis_dokumen_old = QLineEdit(self.widget_5)
        self.line_jenis_dokumen_old.setObjectName(u"line_jenis_dokumen_old")
        self.line_jenis_dokumen_old.setEnabled(False)
        self.line_jenis_dokumen_old.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.line_jenis_dokumen_old, 6, 0, 1, 1)

        self.line_namafile_old = QLineEdit(self.widget_5)
        self.line_namafile_old.setObjectName(u"line_namafile_old")
        self.line_namafile_old.setEnabled(False)
        self.line_namafile_old.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.line_namafile_old, 9, 0, 1, 2)

        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 5, 1, 1, 1)

        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_9.setFont(font1)

        self.gridLayout_6.addWidget(self.label_9, 1, 0, 1, 2)

        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 8, 0, 1, 1)

        self.label_17 = QLabel(self.widget_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.label_17, 19, 0, 1, 1)

        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setFont(font1)

        self.gridLayout_6.addWidget(self.label_10, 13, 0, 1, 2)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 12, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 23, 0, 1, 3)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_8 = QGridLayout(self.widget_8)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(80, 0))

        self.gridLayout_8.addWidget(self.label_12, 0, 0, 1, 1)

        self.line_no_induk_new = QLineEdit(self.widget_8)
        self.line_no_induk_new.setObjectName(u"line_no_induk_new")
        self.line_no_induk_new.setEnabled(False)
        self.line_no_induk_new.setMinimumSize(QSize(0, 24))

        self.gridLayout_8.addWidget(self.line_no_induk_new, 0, 1, 1, 1)

        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.label_13, 2, 0, 1, 1)

        self.line_search = QLineEdit(self.widget_8)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setMinimumSize(QSize(0, 24))

        self.gridLayout_8.addWidget(self.line_search, 0, 2, 1, 1)

        self.cbo_nama_new = QComboBox(self.widget_8)
        self.cbo_nama_new.setObjectName(u"cbo_nama_new")
        self.cbo_nama_new.setMinimumSize(QSize(0, 24))

        self.gridLayout_8.addWidget(self.cbo_nama_new, 1, 1, 1, 2)

        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(70, 0))

        self.gridLayout_8.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_14 = QLabel(self.widget_8)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.label_14, 3, 0, 1, 1)

        self.cbo_jenis_dokumen_new = QComboBox(self.widget_8)
        self.cbo_jenis_dokumen_new.setObjectName(u"cbo_jenis_dokumen_new")
        self.cbo_jenis_dokumen_new.setMinimumSize(QSize(0, 24))

        self.gridLayout_8.addWidget(self.cbo_jenis_dokumen_new, 2, 1, 1, 2)

        self.cbo_keterangan_new = QComboBox(self.widget_8)
        self.cbo_keterangan_new.setObjectName(u"cbo_keterangan_new")
        self.cbo_keterangan_new.setMinimumSize(QSize(0, 24))

        self.gridLayout_8.addWidget(self.cbo_keterangan_new, 3, 1, 1, 2)


        self.gridLayout_6.addWidget(self.widget_8, 14, 0, 1, 2)

        self.label_namafile_new = QLabel(self.widget_5)
        self.label_namafile_new.setObjectName(u"label_namafile_new")
        self.label_namafile_new.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.label_namafile_new, 20, 0, 1, 2)


        self.gridLayout_2.addWidget(self.widget_5, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cbo_target.setItemText(0, QCoreApplication.translate("Form", u"Siswa", None))
        self.cbo_target.setItemText(1, QCoreApplication.translate("Form", u"Guru", None))

        self.label.setText(QCoreApplication.translate("Form", u"Target", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Daftar Dokumen", None))
        self.btn_rename.setText(QCoreApplication.translate("Form", u"Rename", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"No. Induk", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"ID Dokumen", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Path", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Path", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Lama", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Namafile", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Namafile", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Baru", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Jenis Dokumen", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"No. Induk", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Jenis Dokumen", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.label_namafile_new.setText("")
    # retranslateUi

