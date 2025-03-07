# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_pengaturan_kegiatan.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1234, 835)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 5, 0, 5)
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.clear_peserta_btn = QPushButton(self.widget_3)
        self.clear_peserta_btn.setObjectName(u"clear_peserta_btn")
        self.clear_peserta_btn.setMinimumSize(QSize(0, 24))
        self.clear_peserta_btn.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_4.addWidget(self.clear_peserta_btn, 0, 2, 1, 1)

        self.generate_peserta_btn = QPushButton(self.widget_3)
        self.generate_peserta_btn.setObjectName(u"generate_peserta_btn")
        self.generate_peserta_btn.setMinimumSize(QSize(0, 24))
        self.generate_peserta_btn.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_4.addWidget(self.generate_peserta_btn, 0, 1, 1, 1)

        self.peserta_tbl = QTableWidget(self.widget_3)
        self.peserta_tbl.setObjectName(u"peserta_tbl")
        self.peserta_tbl.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_4.addWidget(self.peserta_tbl, 1, 0, 1, 3)


        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.kelas_tbl = QTableWidget(self.widget)
        self.kelas_tbl.setObjectName(u"kelas_tbl")
        self.kelas_tbl.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.kelas_tbl, 8, 0, 1, 6)

        self.id_kelas_line = QLineEdit(self.widget)
        self.id_kelas_line.setObjectName(u"id_kelas_line")
        self.id_kelas_line.setMinimumSize(QSize(0, 24))
        self.id_kelas_line.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.id_kelas_line, 6, 5, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.wali_kelas_cbo = QComboBox(self.widget)
        self.wali_kelas_cbo.setObjectName(u"wali_kelas_cbo")
        self.wali_kelas_cbo.setMinimumSize(QSize(240, 24))

        self.gridLayout_2.addWidget(self.wali_kelas_cbo, 6, 3, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 6, 4, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.label, 6, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 6, 1, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 6, 2, 1, 1)

        self.id_kegiatan_line = QLineEdit(self.widget)
        self.id_kegiatan_line.setObjectName(u"id_kegiatan_line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.id_kegiatan_line.sizePolicy().hasHeightForWidth())
        self.id_kegiatan_line.setSizePolicy(sizePolicy2)
        self.id_kegiatan_line.setMinimumSize(QSize(0, 24))
        self.id_kegiatan_line.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.id_kegiatan_line, 3, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 1, 1, 3)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 4, 1, 1)

        self.kegiatan_tbl = QTableWidget(self.widget)
        self.kegiatan_tbl.setObjectName(u"kegiatan_tbl")
        self.kegiatan_tbl.setMaximumSize(QSize(16777215, 250))
        self.kegiatan_tbl.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.kegiatan_tbl, 4, 0, 1, 6)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_8 = QGridLayout(self.widget_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, -1, -1, 8)
        self.tujuan_cbo = QComboBox(self.widget_7)
        self.tujuan_cbo.addItem("")
        self.tujuan_cbo.addItem("")
        self.tujuan_cbo.setObjectName(u"tujuan_cbo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tujuan_cbo.sizePolicy().hasHeightForWidth())
        self.tujuan_cbo.setSizePolicy(sizePolicy4)

        self.gridLayout_8.addWidget(self.tujuan_cbo, 3, 0, 1, 1)

        self.label_15 = QLabel(self.widget_7)
        self.label_15.setObjectName(u"label_15")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy5)

        self.gridLayout_8.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_16 = QLabel(self.widget_7)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_8.addWidget(self.label_16, 2, 1, 1, 1)

        self.kegiatan_cbo = QComboBox(self.widget_7)
        self.kegiatan_cbo.addItem("")
        self.kegiatan_cbo.addItem("")
        self.kegiatan_cbo.addItem("")
        self.kegiatan_cbo.addItem("")
        self.kegiatan_cbo.setObjectName(u"kegiatan_cbo")
        sizePolicy4.setHeightForWidth(self.kegiatan_cbo.sizePolicy().hasHeightForWidth())
        self.kegiatan_cbo.setSizePolicy(sizePolicy4)

        self.gridLayout_8.addWidget(self.kegiatan_cbo, 3, 1, 1, 1)

        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setColumnStretch(1, 1)

        self.gridLayout_3.addWidget(self.widget_7, 2, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.label_10, 1, 3, 1, 1)

        self.clear_mapel_btn = QPushButton(self.widget_5)
        self.clear_mapel_btn.setObjectName(u"clear_mapel_btn")
        sizePolicy4.setHeightForWidth(self.clear_mapel_btn.sizePolicy().hasHeightForWidth())
        self.clear_mapel_btn.setSizePolicy(sizePolicy4)
        self.clear_mapel_btn.setMinimumSize(QSize(125, 0))
        self.clear_mapel_btn.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_6.addWidget(self.clear_mapel_btn, 0, 4, 1, 1)

        self.id_mapel_line = QLineEdit(self.widget_5)
        self.id_mapel_line.setObjectName(u"id_mapel_line")
        self.id_mapel_line.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.id_mapel_line, 1, 4, 1, 1)

        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.label_8, 1, 0, 1, 1)

        self.guru_cbo = QComboBox(self.widget_5)
        self.guru_cbo.setObjectName(u"guru_cbo")
        sizePolicy4.setHeightForWidth(self.guru_cbo.sizePolicy().hasHeightForWidth())
        self.guru_cbo.setSizePolicy(sizePolicy4)
        self.guru_cbo.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.guru_cbo, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.mapel_tbl = QTableWidget(self.widget_5)
        self.mapel_tbl.setObjectName(u"mapel_tbl")
        self.mapel_tbl.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_6.addWidget(self.mapel_tbl, 2, 0, 1, 5)

        self.label_12 = QLabel(self.widget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 4)


        self.gridLayout_3.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)

        self.opsi_insert_cbo = QComboBox(self.widget_4)
        self.opsi_insert_cbo.addItem("")
        self.opsi_insert_cbo.addItem("")
        self.opsi_insert_cbo.addItem("")
        self.opsi_insert_cbo.setObjectName(u"opsi_insert_cbo")
        sizePolicy4.setHeightForWidth(self.opsi_insert_cbo.sizePolicy().hasHeightForWidth())
        self.opsi_insert_cbo.setSizePolicy(sizePolicy4)
        self.opsi_insert_cbo.setMinimumSize(QSize(0, 24))

        self.gridLayout_5.addWidget(self.opsi_insert_cbo, 1, 1, 1, 1)

        self.preview_tbl = QTableWidget(self.widget_4)
        self.preview_tbl.setObjectName(u"preview_tbl")

        self.gridLayout_5.addWidget(self.preview_tbl, 0, 0, 1, 3)

        self.input_line = QLineEdit(self.widget_4)
        self.input_line.setObjectName(u"input_line")
        self.input_line.setMinimumSize(QSize(0, 24))

        self.gridLayout_5.addWidget(self.input_line, 2, 0, 1, 2)

        self.execute_insert_btn = QPushButton(self.widget_4)
        self.execute_insert_btn.setObjectName(u"execute_insert_btn")
        self.execute_insert_btn.setMinimumSize(QSize(24, 24))
        self.execute_insert_btn.setMaximumSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.execute_insert_btn, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 3, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_14 = QLabel(self.widget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.label_14, 1, 3, 1, 1)

        self.id_ekskul_line = QLineEdit(self.widget_6)
        self.id_ekskul_line.setObjectName(u"id_ekskul_line")
        self.id_ekskul_line.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.id_ekskul_line, 1, 4, 1, 1)

        self.ekskul_tbl = QTableWidget(self.widget_6)
        self.ekskul_tbl.setObjectName(u"ekskul_tbl")
        self.ekskul_tbl.setMaximumSize(QSize(16777215, 150))
        self.ekskul_tbl.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_7.addWidget(self.ekskul_tbl, 2, 0, 1, 5)

        self.pembimbing_cbo = QComboBox(self.widget_6)
        self.pembimbing_cbo.setObjectName(u"pembimbing_cbo")
        self.pembimbing_cbo.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.pembimbing_cbo, 1, 1, 1, 1)

        self.label_13 = QLabel(self.widget_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.label_13, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.clear_ekskul_btn = QPushButton(self.widget_6)
        self.clear_ekskul_btn.setObjectName(u"clear_ekskul_btn")
        sizePolicy4.setHeightForWidth(self.clear_ekskul_btn.sizePolicy().hasHeightForWidth())
        self.clear_ekskul_btn.setSizePolicy(sizePolicy4)
        self.clear_ekskul_btn.setMinimumSize(QSize(125, 0))
        self.clear_ekskul_btn.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_7.addWidget(self.clear_ekskul_btn, 0, 4, 1, 1)

        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 4)


        self.gridLayout_3.addWidget(self.widget_6, 1, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)

        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 35)
        self.gridLayout.setColumnStretch(1, 40)
        self.gridLayout.setColumnStretch(2, 25)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Kegiatan Peserta", None))
        self.clear_peserta_btn.setText(QCoreApplication.translate("Form", u"Clear Peserta", None))
        self.generate_peserta_btn.setText(QCoreApplication.translate("Form", u"Generate Peserta", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Kegiatan Riwayat", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"ID Kelas", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kelas Riwayat", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Wali Kelas", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"ID Kegiatan", None))
        self.tujuan_cbo.setItemText(0, QCoreApplication.translate("Form", u"Mapel", None))
        self.tujuan_cbo.setItemText(1, QCoreApplication.translate("Form", u"Ekskul", None))

        self.label_15.setText(QCoreApplication.translate("Form", u"Tujuan Input", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.kegiatan_cbo.setItemText(0, QCoreApplication.translate("Form", u"PAS", None))
        self.kegiatan_cbo.setItemText(1, QCoreApplication.translate("Form", u"PAT", None))
        self.kegiatan_cbo.setItemText(2, QCoreApplication.translate("Form", u"UAP", None))
        self.kegiatan_cbo.setItemText(3, QCoreApplication.translate("Form", u"AM", None))

        self.label_10.setText(QCoreApplication.translate("Form", u"id_mapel", None))
        self.clear_mapel_btn.setText(QCoreApplication.translate("Form", u"Clear Mapel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Pilih Guru", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Riwayat Mapel", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Opsi Insert", None))
        self.opsi_insert_cbo.setItemText(0, QCoreApplication.translate("Form", u"List", None))
        self.opsi_insert_cbo.setItemText(1, QCoreApplication.translate("Form", u"Kegiatan", None))
        self.opsi_insert_cbo.setItemText(2, QCoreApplication.translate("Form", u"Terisi", None))

        self.execute_insert_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"id_ekskul", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Pilih Pembimbing", None))
        self.clear_ekskul_btn.setText(QCoreApplication.translate("Form", u"Clear Ekskul", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Riwayat Ekstrakurikuler", None))
    # retranslateUi

