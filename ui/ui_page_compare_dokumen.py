# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_compare_dokumen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSplitter, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1262, 745)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(20)
        self.widget_4 = QWidget(self.splitter)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_7 = QGridLayout(self.widget_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_prev_dok = QPushButton(self.widget_9)
        self.btn_prev_dok.setObjectName(u"btn_prev_dok")
        self.btn_prev_dok.setMinimumSize(QSize(24, 24))
        self.btn_prev_dok.setMaximumSize(QSize(24, 16777215))

        self.gridLayout_7.addWidget(self.btn_prev_dok, 0, 0, 1, 1)

        self.btn_next_dok = QPushButton(self.widget_9)
        self.btn_next_dok.setObjectName(u"btn_next_dok")
        self.btn_next_dok.setMinimumSize(QSize(24, 24))
        self.btn_next_dok.setMaximumSize(QSize(24, 16777215))

        self.gridLayout_7.addWidget(self.btn_next_dok, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget_9, 2, 5, 1, 1)

        self.widget_10 = QWidget(self.widget)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_8 = QGridLayout(self.widget_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_next_nama = QPushButton(self.widget_10)
        self.btn_next_nama.setObjectName(u"btn_next_nama")
        self.btn_next_nama.setMinimumSize(QSize(24, 24))
        self.btn_next_nama.setMaximumSize(QSize(24, 16777215))

        self.gridLayout_8.addWidget(self.btn_next_nama, 0, 2, 1, 1)

        self.btn_prev_nama = QPushButton(self.widget_10)
        self.btn_prev_nama.setObjectName(u"btn_prev_nama")
        self.btn_prev_nama.setMinimumSize(QSize(24, 24))
        self.btn_prev_nama.setMaximumSize(QSize(24, 16777215))

        self.gridLayout_8.addWidget(self.btn_prev_nama, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget_10, 1, 5, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.cbo_daftar_nama = QComboBox(self.widget)
        self.cbo_daftar_nama.setObjectName(u"cbo_daftar_nama")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbo_daftar_nama.sizePolicy().hasHeightForWidth())
        self.cbo_daftar_nama.setSizePolicy(sizePolicy1)
        self.cbo_daftar_nama.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.cbo_daftar_nama, 1, 1, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.line_search = QLineEdit(self.widget)
        self.line_search.setObjectName(u"line_search")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_search.sizePolicy().hasHeightForWidth())
        self.line_search.setSizePolicy(sizePolicy2)
        self.line_search.setMinimumSize(QSize(120, 24))
        self.line_search.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_search, 0, 4, 1, 2)

        self.cbo_daftar_dokumen = QComboBox(self.widget)
        self.cbo_daftar_dokumen.setObjectName(u"cbo_daftar_dokumen")
        self.cbo_daftar_dokumen.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.cbo_daftar_dokumen, 2, 1, 1, 4)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.radio_is_active = QRadioButton(self.widget)
        self.radio_is_active.setObjectName(u"radio_is_active")
        self.radio_is_active.setChecked(True)

        self.gridLayout_2.addWidget(self.radio_is_active, 0, 2, 1, 1)

        self.cbo_target = QComboBox(self.widget)
        self.cbo_target.setObjectName(u"cbo_target")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cbo_target.sizePolicy().hasHeightForWidth())
        self.cbo_target.setSizePolicy(sizePolicy3)
        self.cbo_target.setMinimumSize(QSize(120, 24))

        self.gridLayout_2.addWidget(self.cbo_target, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy4)
        self.viewer1_layout = QGridLayout(self.widget_5)
        self.viewer1_layout.setObjectName(u"viewer1_layout")

        self.gridLayout_3.addWidget(self.widget_5, 1, 0, 1, 1)

        self.splitter.addWidget(self.widget_4)
        self.widget_3 = QWidget(self.splitter)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy4.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy4)
        self.viewer2_layout = QGridLayout(self.widget_6)
        self.viewer2_layout.setObjectName(u"viewer2_layout")

        self.gridLayout_5.addWidget(self.widget_6, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_10 = QGridLayout(self.widget_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(15)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_9 = QGridLayout(self.widget_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label = QLabel(self.widget_11)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)

        self.cbo_jenis_dokumen = QComboBox(self.widget_11)
        self.cbo_jenis_dokumen.setObjectName(u"cbo_jenis_dokumen")
        self.cbo_jenis_dokumen.setMinimumSize(QSize(150, 24))
        self.cbo_jenis_dokumen.setMaximumSize(QSize(150, 16777215))
        self.cbo_jenis_dokumen.setEditable(False)

        self.gridLayout_9.addWidget(self.cbo_jenis_dokumen, 0, 1, 1, 1)

        self.btn_hapus = QPushButton(self.widget_11)
        self.btn_hapus.setObjectName(u"btn_hapus")
        self.btn_hapus.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.btn_hapus, 0, 2, 1, 1)

        self.label_2 = QLabel(self.widget_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.label_2, 1, 0, 1, 1)

        self.cbo_opsi_keterangan = QComboBox(self.widget_11)
        self.cbo_opsi_keterangan.setObjectName(u"cbo_opsi_keterangan")
        sizePolicy2.setHeightForWidth(self.cbo_opsi_keterangan.sizePolicy().hasHeightForWidth())
        self.cbo_opsi_keterangan.setSizePolicy(sizePolicy2)
        self.cbo_opsi_keterangan.setMinimumSize(QSize(150, 24))
        self.cbo_opsi_keterangan.setMaximumSize(QSize(150, 16777215))
        self.cbo_opsi_keterangan.setEditable(True)

        self.gridLayout_9.addWidget(self.cbo_opsi_keterangan, 1, 1, 1, 1)

        self.btn_tambah = QPushButton(self.widget_11)
        self.btn_tambah.setObjectName(u"btn_tambah")
        self.btn_tambah.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.btn_tambah, 1, 2, 1, 1)


        self.gridLayout_10.addWidget(self.widget_11, 0, 1, 1, 1)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy5)
        self.gridLayout_4 = QGridLayout(self.widget_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cbo_list_files = QComboBox(self.widget_7)
        self.cbo_list_files.setObjectName(u"cbo_list_files")
        self.cbo_list_files.setMinimumSize(QSize(0, 24))

        self.gridLayout_4.addWidget(self.cbo_list_files, 1, 2, 1, 1)

        self.label_8 = QLabel(self.widget_7)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.label_8, 1, 1, 1, 1)

        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")
        sizePolicy6.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.label_7, 0, 1, 1, 1)

        self.line_source = QLineEdit(self.widget_7)
        self.line_source.setObjectName(u"line_source")
        sizePolicy2.setHeightForWidth(self.line_source.sizePolicy().hasHeightForWidth())
        self.line_source.setSizePolicy(sizePolicy2)
        self.line_source.setMinimumSize(QSize(0, 24))

        self.gridLayout_4.addWidget(self.line_source, 0, 2, 1, 1)

        self.btn_browse = QPushButton(self.widget_7)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMinimumSize(QSize(0, 24))
        self.btn_browse.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_4.addWidget(self.btn_browse, 0, 3, 1, 1)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(80, 16777215))
        self.gridLayout_6 = QGridLayout(self.widget_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(3)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_next_file = QPushButton(self.widget_8)
        self.btn_next_file.setObjectName(u"btn_next_file")
        self.btn_next_file.setMinimumSize(QSize(24, 24))
        self.btn_next_file.setMaximumSize(QSize(24, 16777215))

        self.gridLayout_6.addWidget(self.btn_next_file, 0, 1, 1, 1)

        self.btn_prev_file = QPushButton(self.widget_8)
        self.btn_prev_file.setObjectName(u"btn_prev_file")
        self.btn_prev_file.setMinimumSize(QSize(24, 24))
        self.btn_prev_file.setMaximumSize(QSize(24, 16777215))

        self.gridLayout_6.addWidget(self.btn_prev_file, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_8, 1, 3, 1, 1, Qt.AlignLeft)


        self.gridLayout_10.addWidget(self.widget_7, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.widget_3)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_prev_dok.setText(QCoreApplication.translate("Form", u"<", None))
        self.btn_next_dok.setText(QCoreApplication.translate("Form", u">", None))
        self.btn_next_nama.setText(QCoreApplication.translate("Form", u">", None))
        self.btn_prev_nama.setText(QCoreApplication.translate("Form", u"<", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Daftar Dokumen", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.radio_is_active.setText(QCoreApplication.translate("Form", u"Siswa Aktif Saja", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Target", None))
        self.label.setText(QCoreApplication.translate("Form", u"Jenis Dokumen", None))
        self.btn_hapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.btn_tambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"File", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Folder", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Pilih File", None))
        self.btn_next_file.setText(QCoreApplication.translate("Form", u">", None))
        self.btn_prev_file.setText(QCoreApplication.translate("Form", u"<", None))
    # retranslateUi

