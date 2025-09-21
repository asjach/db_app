# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_tambah_dokumen.ui'
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
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(787, 606)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(600, 0))
        self.widget.setMaximumSize(QSize(600, 16777215))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.plain_destination = QPlainTextEdit(self.widget_4)
        self.plain_destination.setObjectName(u"plain_destination")
        self.plain_destination.setEnabled(False)
        self.plain_destination.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_5.addWidget(self.plain_destination, 12, 0, 1, 3)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.widget_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_5.addWidget(self.widget_6, 10, 0, 1, 1)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_8 = QGridLayout(self.widget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.radio_cycle = QRadioButton(self.widget_8)
        self.radio_cycle.setObjectName(u"radio_cycle")
        self.radio_cycle.setChecked(True)
        self.radio_cycle.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.radio_cycle, 3, 2, 1, 1)

        self.label_10 = QLabel(self.widget_8)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setBold(True)
        self.label_10.setFont(font)

        self.gridLayout_8.addWidget(self.label_10, 1, 0, 1, 1)

        self.radio_move_sudah = QRadioButton(self.widget_8)
        self.radio_move_sudah.setObjectName(u"radio_move_sudah")
        self.radio_move_sudah.setChecked(True)
        self.radio_move_sudah.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.radio_move_sudah, 3, 1, 1, 1)

        self.btn_tambah = QPushButton(self.widget_8)
        self.btn_tambah.setObjectName(u"btn_tambah")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_tambah.sizePolicy().hasHeightForWidth())
        self.btn_tambah.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.btn_tambah, 1, 3, 3, 1)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_6 = QGridLayout(self.widget_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.radio_mode_copy = QRadioButton(self.widget_9)
        self.radio_mode_copy.setObjectName(u"radio_mode_copy")
        self.radio_mode_copy.setChecked(True)
        self.radio_mode_copy.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.radio_mode_copy, 0, 0, 1, 1)

        self.radio_mode_move = QRadioButton(self.widget_9)
        self.radio_mode_move.setObjectName(u"radio_mode_move")
        self.radio_mode_move.setChecked(False)
        self.radio_mode_move.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.radio_mode_move, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.widget_9, 2, 1, 1, 2)


        self.gridLayout_5.addWidget(self.widget_8, 13, 0, 1, 3)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy2.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy2)
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_clear_source = QPushButton(self.widget_7)
        self.btn_clear_source.setObjectName(u"btn_clear_source")
        self.btn_clear_source.setMinimumSize(QSize(24, 24))
        self.btn_clear_source.setMaximumSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.btn_clear_source, 0, 1, 1, 1)

        self.btn_browse = QPushButton(self.widget_7)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.btn_browse, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_7, 0, 2, 1, 1)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.line_jenis_dokumen = QLineEdit(self.widget_4)
        self.line_jenis_dokumen.setObjectName(u"line_jenis_dokumen")
        self.line_jenis_dokumen.setMinimumSize(QSize(0, 24))
        self.line_jenis_dokumen.setMaximumSize(QSize(150, 16777215))
        self.line_jenis_dokumen.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.line_jenis_dokumen, 4, 1, 1, 1)

        self.line_nama = QLineEdit(self.widget_4)
        self.line_nama.setObjectName(u"line_nama")
        self.line_nama.setEnabled(False)
        self.line_nama.setMinimumSize(QSize(0, 24))

        self.gridLayout_5.addWidget(self.line_nama, 4, 0, 1, 1)

        self.line_keterangan = QLineEdit(self.widget_4)
        self.line_keterangan.setObjectName(u"line_keterangan")
        self.line_keterangan.setMinimumSize(QSize(0, 24))
        self.line_keterangan.setMaximumSize(QSize(150, 16777215))
        self.line_keterangan.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.line_keterangan, 4, 2, 1, 1)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 3, 1, 1, 1)

        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_3, 3, 2, 1, 1)

        self.line_no_induk = QLineEdit(self.widget_4)
        self.line_no_induk.setObjectName(u"line_no_induk")
        self.line_no_induk.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_no_induk.sizePolicy().hasHeightForWidth())
        self.line_no_induk.setSizePolicy(sizePolicy3)
        self.line_no_induk.setMinimumSize(QSize(0, 24))

        self.gridLayout_5.addWidget(self.line_no_induk, 7, 0, 1, 1)

        self.list_jenis_dokumen = QListWidget(self.widget_4)
        self.list_jenis_dokumen.setObjectName(u"list_jenis_dokumen")
        sizePolicy1.setHeightForWidth(self.list_jenis_dokumen.sizePolicy().hasHeightForWidth())
        self.list_jenis_dokumen.setSizePolicy(sizePolicy1)
        self.list_jenis_dokumen.setMaximumSize(QSize(150, 300))
        self.list_jenis_dokumen.setAutoScroll(True)
        self.list_jenis_dokumen.setAutoScrollMargin(16)
        self.list_jenis_dokumen.setBatchSize(100)

        self.gridLayout_5.addWidget(self.list_jenis_dokumen, 5, 1, 5, 1)

        self.list_keterangan = QListWidget(self.widget_4)
        self.list_keterangan.setObjectName(u"list_keterangan")
        sizePolicy1.setHeightForWidth(self.list_keterangan.sizePolicy().hasHeightForWidth())
        self.list_keterangan.setSizePolicy(sizePolicy1)
        self.list_keterangan.setMaximumSize(QSize(150, 300))

        self.gridLayout_5.addWidget(self.list_keterangan, 5, 2, 5, 1)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 11, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy4)
        self.widget_5.setMinimumSize(QSize(0, 24))

        self.gridLayout_5.addWidget(self.widget_5, 8, 0, 1, 1)

        self.plain_source = QPlainTextEdit(self.widget_4)
        self.plain_source.setObjectName(u"plain_source")
        self.plain_source.setEnabled(False)
        self.plain_source.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_5.addWidget(self.plain_source, 1, 0, 1, 3)

        self.gridLayout_5.setColumnStretch(0, 1)

        self.gridLayout.addWidget(self.widget_4, 2, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(297, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.cbo_target = QComboBox(self.widget_3)
        self.cbo_target.addItem("")
        self.cbo_target.addItem("")
        self.cbo_target.setObjectName(u"cbo_target")
        self.cbo_target.setMinimumSize(QSize(120, 24))

        self.gridLayout_2.addWidget(self.cbo_target, 0, 1, 1, 1)

        self.tbl_daftar_nama = QTableWidget(self.widget_3)
        self.tbl_daftar_nama.setObjectName(u"tbl_daftar_nama")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tbl_daftar_nama.sizePolicy().hasHeightForWidth())
        self.tbl_daftar_nama.setSizePolicy(sizePolicy5)
        self.tbl_daftar_nama.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_daftar_nama.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tbl_daftar_nama, 1, 0, 1, 3)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy6)
        self.viewer_layout = QGridLayout(self.widget_2)
        self.viewer_layout.setObjectName(u"viewer_layout")

        self.gridLayout_3.addWidget(self.widget_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.radio_cycle.setText(QCoreApplication.translate("Form", u"Input berulang", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"MODE:", None))
        self.radio_move_sudah.setText(QCoreApplication.translate("Form", u"Pindahkan ke folder 'sudah'", None))
        self.btn_tambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.radio_mode_copy.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.radio_mode_move.setText(QCoreApplication.translate("Form", u"Move", None))
        self.btn_clear_source.setText(QCoreApplication.translate("Form", u"X", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Pilih File", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Pilih File", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Nomor Induk", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Jenis Dokumen", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Nama File Input", None))
        self.label.setText(QCoreApplication.translate("Form", u"Target", None))
        self.cbo_target.setItemText(0, QCoreApplication.translate("Form", u"Siswa", None))
        self.cbo_target.setItemText(1, QCoreApplication.translate("Form", u"Guru", None))

    # retranslateUi

