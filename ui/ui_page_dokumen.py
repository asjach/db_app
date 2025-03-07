# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_dokumen.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1121, 840)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_11 = QGridLayout(Form)
        self.gridLayout_11.setSpacing(3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(3, 3, 3, 3)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_tapel_aktif = QRadioButton(self.widget)
        self.radio_tapel_aktif.setObjectName(u"radio_tapel_aktif")
        self.radio_tapel_aktif.setChecked(True)
        self.radio_tapel_aktif.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.radio_tapel_aktif)

        self.radio_all = QRadioButton(self.widget)
        self.radio_all.setObjectName(u"radio_all")
        self.radio_all.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.radio_all)


        self.gridLayout_7.addWidget(self.widget, 1, 4, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setVerticalSpacing(5)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.radio_move = QRadioButton(self.frame_2)
        self.radio_move.setObjectName(u"radio_move")
        self.radio_move.setMinimumSize(QSize(80, 0))

        self.gridLayout_9.addWidget(self.radio_move, 1, 3, 1, 1)

        self.radio_input = QRadioButton(self.frame_2)
        self.radio_input.setObjectName(u"radio_input")
        self.radio_input.setMinimumSize(QSize(80, 0))
        self.radio_input.setChecked(False)

        self.gridLayout_9.addWidget(self.radio_input, 1, 0, 1, 1)

        self.radio_rename = QRadioButton(self.frame_2)
        self.radio_rename.setObjectName(u"radio_rename")
        self.radio_rename.setMinimumSize(QSize(80, 0))

        self.gridLayout_9.addWidget(self.radio_rename, 0, 1, 1, 1)

        self.radio_copy = QRadioButton(self.frame_2)
        self.radio_copy.setObjectName(u"radio_copy")
        self.radio_copy.setMinimumSize(QSize(80, 0))

        self.gridLayout_9.addWidget(self.radio_copy, 0, 3, 1, 1)

        self.radio_view = QRadioButton(self.frame_2)
        self.radio_view.setObjectName(u"radio_view")
        self.radio_view.setMinimumSize(QSize(80, 0))
        self.radio_view.setChecked(True)

        self.gridLayout_9.addWidget(self.radio_view, 0, 0, 1, 1)

        self.radio_delete = QRadioButton(self.frame_2)
        self.radio_delete.setObjectName(u"radio_delete")
        self.radio_delete.setMinimumSize(QSize(80, 0))

        self.gridLayout_9.addWidget(self.radio_delete, 0, 4, 1, 1)

        self.radio_replace = QRadioButton(self.frame_2)
        self.radio_replace.setObjectName(u"radio_replace")
        self.radio_replace.setMinimumSize(QSize(80, 0))

        self.gridLayout_9.addWidget(self.radio_replace, 1, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_2, 0, 0, 1, 6)

        self.cbo_target = QComboBox(self.frame)
        self.cbo_target.addItem("")
        self.cbo_target.addItem("")
        self.cbo_target.addItem("")
        self.cbo_target.addItem("")
        self.cbo_target.setObjectName(u"cbo_target")
        self.cbo_target.setMinimumSize(QSize(150, 24))

        self.gridLayout_7.addWidget(self.cbo_target, 1, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)

        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame, 0, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.dokumen_container = QGridLayout(self.widget_2)
        self.dokumen_container.setObjectName(u"dokumen_container")

        self.gridLayout_11.addWidget(self.widget_2, 0, 1, 2, 1)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(500, 0))
        self.scrollArea.setMaximumSize(QSize(500, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 498, 745))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_copy_move = QFrame(self.scrollAreaWidgetContents)
        self.frame_copy_move.setObjectName(u"frame_copy_move")
        self.frame_copy_move.setFrameShape(QFrame.StyledPanel)
        self.frame_copy_move.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_copy_move)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(5)
        self.gridLayout_5.setVerticalSpacing(2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_copy_move)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 0, 3, 1, 1)

        self.cbo_daftar2 = QComboBox(self.frame_copy_move)
        self.cbo_daftar2.setObjectName(u"cbo_daftar2")
        self.cbo_daftar2.setMinimumSize(QSize(0, 24))

        self.gridLayout_5.addWidget(self.cbo_daftar2, 1, 1, 1, 2)

        self.line_search2 = QLineEdit(self.frame_copy_move)
        self.line_search2.setObjectName(u"line_search2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_search2.sizePolicy().hasHeightForWidth())
        self.line_search2.setSizePolicy(sizePolicy3)
        self.line_search2.setMinimumSize(QSize(120, 24))
        self.line_search2.setMaximumSize(QSize(120, 16777215))
        self.line_search2.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.line_search2, 1, 3, 1, 1)

        self.label_17 = QLabel(self.frame_copy_move)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_28 = QLabel(self.frame_copy_move)
        self.label_28.setObjectName(u"label_28")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.label_28, 0, 0, 1, 1)

        self.line_nomor_induk2 = QLineEdit(self.frame_copy_move)
        self.line_nomor_induk2.setObjectName(u"line_nomor_induk2")
        self.line_nomor_induk2.setMinimumSize(QSize(0, 24))
        self.line_nomor_induk2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.line_nomor_induk2, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_copy_move, 5, 0, 1, 1)

        self.frame_dokumen = QFrame(self.scrollAreaWidgetContents)
        self.frame_dokumen.setObjectName(u"frame_dokumen")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_dokumen.sizePolicy().hasHeightForWidth())
        self.frame_dokumen.setSizePolicy(sizePolicy5)
        self.frame_dokumen.setFrameShape(QFrame.StyledPanel)
        self.frame_dokumen.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_dokumen)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.grup_detail_dokumen = QGroupBox(self.frame_dokumen)
        self.grup_detail_dokumen.setObjectName(u"grup_detail_dokumen")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.grup_detail_dokumen.sizePolicy().hasHeightForWidth())
        self.grup_detail_dokumen.setSizePolicy(sizePolicy6)
        self.grup_detail_dokumen.setFlat(True)
        self.grup_detail_dokumen.setCheckable(False)
        self.gridLayout_3 = QGridLayout(self.grup_detail_dokumen)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.grup_detail_dokumen)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_2 = QLabel(self.grup_detail_dokumen)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.line_nomor_induk = QLineEdit(self.grup_detail_dokumen)
        self.line_nomor_induk.setObjectName(u"line_nomor_induk")
        self.line_nomor_induk.setEnabled(False)

        self.gridLayout_3.addWidget(self.line_nomor_induk, 0, 3, 1, 1)

        self.line_id = QLineEdit(self.grup_detail_dokumen)
        self.line_id.setObjectName(u"line_id")
        self.line_id.setEnabled(False)
        self.line_id.setFrame(True)

        self.gridLayout_3.addWidget(self.line_id, 0, 1, 1, 1)

        self.label_26 = QLabel(self.grup_detail_dokumen)
        self.label_26.setObjectName(u"label_26")
        sizePolicy6.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.label_26, 3, 0, 1, 1, Qt.AlignTop)

        self.label_23 = QLabel(self.grup_detail_dokumen)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 1, 2, 1, 1)

        self.label_24 = QLabel(self.grup_detail_dokumen)
        self.label_24.setObjectName(u"label_24")
        sizePolicy6.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.label_24, 2, 0, 1, 1)

        self.line_jenis_dokumen_db = QLineEdit(self.grup_detail_dokumen)
        self.line_jenis_dokumen_db.setObjectName(u"line_jenis_dokumen_db")
        self.line_jenis_dokumen_db.setEnabled(False)

        self.gridLayout_3.addWidget(self.line_jenis_dokumen_db, 1, 1, 1, 1)

        self.line_keterangan_db = QLineEdit(self.grup_detail_dokumen)
        self.line_keterangan_db.setObjectName(u"line_keterangan_db")
        self.line_keterangan_db.setEnabled(False)

        self.gridLayout_3.addWidget(self.line_keterangan_db, 1, 3, 1, 1)

        self.line_namafile_db = QLineEdit(self.grup_detail_dokumen)
        self.line_namafile_db.setObjectName(u"line_namafile_db")
        self.line_namafile_db.setEnabled(False)

        self.gridLayout_3.addWidget(self.line_namafile_db, 2, 1, 1, 3)

        self.plain_path_db = QPlainTextEdit(self.grup_detail_dokumen)
        self.plain_path_db.setObjectName(u"plain_path_db")
        self.plain_path_db.setEnabled(False)
        self.plain_path_db.setMinimumSize(QSize(0, 60))
        self.plain_path_db.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_3.addWidget(self.plain_path_db, 3, 1, 1, 3)

        self.label_10 = QLabel(self.grup_detail_dokumen)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.grup_detail_dokumen, 3, 0, 1, 3)

        self.cbo_filter_dokumen = QComboBox(self.frame_dokumen)
        self.cbo_filter_dokumen.setObjectName(u"cbo_filter_dokumen")
        self.cbo_filter_dokumen.setMinimumSize(QSize(120, 24))
        self.cbo_filter_dokumen.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_2.addWidget(self.cbo_filter_dokumen, 1, 2, 1, 1)

        self.tbl_daftar_dokumen = QTableWidget(self.frame_dokumen)
        self.tbl_daftar_dokumen.setObjectName(u"tbl_daftar_dokumen")
        self.tbl_daftar_dokumen.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.tbl_daftar_dokumen, 2, 0, 1, 3)

        self.label_6 = QLabel(self.frame_dokumen)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1, Qt.AlignRight)

        self.label_5 = QLabel(self.frame_dokumen)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_dokumen, 1, 0, 1, 1)

        self.frame_daftar = QFrame(self.scrollAreaWidgetContents)
        self.frame_daftar.setObjectName(u"frame_daftar")
        self.frame_daftar.setFrameShape(QFrame.StyledPanel)
        self.frame_daftar.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_daftar)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_next_nama = QPushButton(self.frame_daftar)
        self.btn_next_nama.setObjectName(u"btn_next_nama")
        self.btn_next_nama.setMinimumSize(QSize(0, 24))
        self.btn_next_nama.setMaximumSize(QSize(30, 50))

        self.gridLayout.addWidget(self.btn_next_nama, 1, 2, 1, 1)

        self.cbo_daftar = QComboBox(self.frame_daftar)
        self.cbo_daftar.setObjectName(u"cbo_daftar")
        sizePolicy3.setHeightForWidth(self.cbo_daftar.sizePolicy().hasHeightForWidth())
        self.cbo_daftar.setSizePolicy(sizePolicy3)
        self.cbo_daftar.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_daftar, 1, 1, 1, 1)

        self.line_search1 = QLineEdit(self.frame_daftar)
        self.line_search1.setObjectName(u"line_search1")
        sizePolicy3.setHeightForWidth(self.line_search1.sizePolicy().hasHeightForWidth())
        self.line_search1.setSizePolicy(sizePolicy3)
        self.line_search1.setMinimumSize(QSize(120, 24))
        self.line_search1.setMaximumSize(QSize(120, 16777215))
        self.line_search1.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.line_search1, 1, 4, 1, 1)

        self.label = QLabel(self.frame_daftar)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)

        self.btn_prev_nama = QPushButton(self.frame_daftar)
        self.btn_prev_nama.setObjectName(u"btn_prev_nama")
        self.btn_prev_nama.setMinimumSize(QSize(0, 24))
        self.btn_prev_nama.setMaximumSize(QSize(30, 50))

        self.gridLayout.addWidget(self.btn_prev_nama, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.label_3 = QLabel(self.frame_daftar)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_daftar, 0, 0, 1, 1)

        self.frame_parameter = QFrame(self.scrollAreaWidgetContents)
        self.frame_parameter.setObjectName(u"frame_parameter")
        self.frame_parameter.setFrameShape(QFrame.StyledPanel)
        self.frame_parameter.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_parameter)
        self.gridLayout_10.setSpacing(5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_parameter)
        self.label_22.setObjectName(u"label_22")
        sizePolicy4.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy4)

        self.gridLayout_10.addWidget(self.label_22, 0, 0, 1, 1)

        self.cbo_jenis_dokumen = QComboBox(self.frame_parameter)
        self.cbo_jenis_dokumen.setObjectName(u"cbo_jenis_dokumen")
        self.cbo_jenis_dokumen.setMinimumSize(QSize(120, 24))

        self.gridLayout_10.addWidget(self.cbo_jenis_dokumen, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.label_27 = QLabel(self.frame_parameter)
        self.label_27.setObjectName(u"label_27")
        sizePolicy4.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy4)

        self.gridLayout_10.addWidget(self.label_27, 0, 3, 1, 1)

        self.line_input_nomor_induk = QLineEdit(self.frame_parameter)
        self.line_input_nomor_induk.setObjectName(u"line_input_nomor_induk")
        self.line_input_nomor_induk.setMinimumSize(QSize(0, 24))
        self.line_input_nomor_induk.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_10.addWidget(self.line_input_nomor_induk, 0, 4, 1, 1)

        self.label_25 = QLabel(self.frame_parameter)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_10.addWidget(self.label_25, 1, 0, 1, 1)

        self.line_input_keterangan = QLineEdit(self.frame_parameter)
        self.line_input_keterangan.setObjectName(u"line_input_keterangan")
        self.line_input_keterangan.setMinimumSize(QSize(0, 24))

        self.gridLayout_10.addWidget(self.line_input_keterangan, 1, 1, 1, 2)

        self.cbo_template_keterangan = QComboBox(self.frame_parameter)
        self.cbo_template_keterangan.setObjectName(u"cbo_template_keterangan")
        self.cbo_template_keterangan.setMinimumSize(QSize(120, 24))

        self.gridLayout_10.addWidget(self.cbo_template_keterangan, 1, 4, 1, 1)


        self.gridLayout_6.addWidget(self.frame_parameter, 3, 0, 1, 1)

        self.frame_browse = QFrame(self.scrollAreaWidgetContents)
        self.frame_browse.setObjectName(u"frame_browse")
        self.frame_browse.setFrameShape(QFrame.NoFrame)
        self.frame_browse.setFrameShadow(QFrame.Raised)
        self.frame_browse.setLineWidth(0)
        self.gridLayout_8 = QGridLayout(self.frame_browse)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_browse = QPushButton(self.frame_browse)
        self.btn_browse.setObjectName(u"btn_browse")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_browse.sizePolicy().hasHeightForWidth())
        self.btn_browse.setSizePolicy(sizePolicy7)

        self.gridLayout_8.addWidget(self.btn_browse, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 0, 0, 1, 2)

        self.plain_path_source = QPlainTextEdit(self.frame_browse)
        self.plain_path_source.setObjectName(u"plain_path_source")
        self.plain_path_source.setEnabled(False)
        self.plain_path_source.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.plain_path_source, 1, 0, 1, 3)


        self.gridLayout_6.addWidget(self.frame_browse, 4, 0, 1, 1, Qt.AlignTop)

        self.frame_eksekusi = QWidget(self.scrollAreaWidgetContents)
        self.frame_eksekusi.setObjectName(u"frame_eksekusi")
        self.gridLayout_4 = QGridLayout(self.frame_eksekusi)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_eksekusi = QPushButton(self.frame_eksekusi)
        self.btn_eksekusi.setObjectName(u"btn_eksekusi")
        self.btn_eksekusi.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.btn_eksekusi, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_eksekusi, 10, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_11.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.radio_tapel_aktif.setText(QCoreApplication.translate("Form", u"Tapel Aktif", None))
        self.radio_all.setText(QCoreApplication.translate("Form", u"Keseluruhan", None))
        self.radio_move.setText(QCoreApplication.translate("Form", u"Move", None))
        self.radio_input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.radio_rename.setText(QCoreApplication.translate("Form", u"Rename", None))
        self.radio_copy.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.radio_view.setText(QCoreApplication.translate("Form", u"View", None))
        self.radio_delete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.radio_replace.setText(QCoreApplication.translate("Form", u"Replace", None))
        self.cbo_target.setItemText(0, QCoreApplication.translate("Form", u"Siswa", None))
        self.cbo_target.setItemText(1, QCoreApplication.translate("Form", u"Guru", None))
        self.cbo_target.setItemText(2, QCoreApplication.translate("Form", u"Umum", None))
        self.cbo_target.setItemText(3, QCoreApplication.translate("Form", u"Jenjang", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Target", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"search:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Nomor Induk", None))
        self.grup_detail_dokumen.setTitle(QCoreApplication.translate("Form", u"Detail Dokumen", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Nomor Induk", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ID", None))
        self.line_id.setText("")
        self.label_26.setText(QCoreApplication.translate("Form", u"Path", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Nama File", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Jenis Dokumen", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Filter", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Daftar Dokumen", None))
        self.btn_next_nama.setText(QCoreApplication.translate("Form", u">", None))
        self.label.setText(QCoreApplication.translate("Form", u"search:", None))
        self.btn_prev_nama.setText(QCoreApplication.translate("Form", u"<", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nama:", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Jenis Dokumen", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Nomor Induk", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.btn_eksekusi.setText(QCoreApplication.translate("Form", u"Eksekusi", None))
    # retranslateUi

