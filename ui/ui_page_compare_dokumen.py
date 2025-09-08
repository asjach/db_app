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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1077, 759)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.gridLayout_7 = QGridLayout(self.widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(10)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.widget_12)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radio_is_active = QRadioButton(self.widget_12)
        self.radio_is_active.setObjectName(u"radio_is_active")
        self.radio_is_active.setMinimumSize(QSize(0, 24))
        self.radio_is_active.setChecked(True)

        self.gridLayout_2.addWidget(self.radio_is_active, 0, 2, 1, 1)

        self.label_5 = QLabel(self.widget_12)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.btn_next_nama = QPushButton(self.widget_12)
        self.btn_next_nama.setObjectName(u"btn_next_nama")
        self.btn_next_nama.setMinimumSize(QSize(20, 24))
        self.btn_next_nama.setMaximumSize(QSize(24, 16777215))
        icon = QIcon()
        icon.addFile(u":/icon/resources/icon/more_than.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_next_nama.setIcon(icon)
        self.btn_next_nama.setFlat(True)

        self.gridLayout_2.addWidget(self.btn_next_nama, 0, 5, 1, 1)

        self.line_search = QLineEdit(self.widget_12)
        self.line_search.setObjectName(u"line_search")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_search.sizePolicy().hasHeightForWidth())
        self.line_search.setSizePolicy(sizePolicy2)
        self.line_search.setMinimumSize(QSize(100, 24))
        self.line_search.setMaximumSize(QSize(100, 16777215))
        self.line_search.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_search, 0, 6, 1, 1)

        self.cbo_daftar_dokumen = QComboBox(self.widget_12)
        self.cbo_daftar_dokumen.setObjectName(u"cbo_daftar_dokumen")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cbo_daftar_dokumen.sizePolicy().hasHeightForWidth())
        self.cbo_daftar_dokumen.setSizePolicy(sizePolicy3)
        self.cbo_daftar_dokumen.setMinimumSize(QSize(150, 24))
        self.cbo_daftar_dokumen.setMaximumSize(QSize(150, 16777215))
        self.cbo_daftar_dokumen.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_2.addWidget(self.cbo_daftar_dokumen, 0, 8, 1, 1)

        self.btn_prev_dok = QPushButton(self.widget_12)
        self.btn_prev_dok.setObjectName(u"btn_prev_dok")
        self.btn_prev_dok.setMinimumSize(QSize(20, 24))
        self.btn_prev_dok.setMaximumSize(QSize(24, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icon/resources/icon/less_than.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_prev_dok.setIcon(icon1)
        self.btn_prev_dok.setFlat(True)

        self.gridLayout_2.addWidget(self.btn_prev_dok, 0, 7, 1, 1)

        self.cbo_target = QComboBox(self.widget_12)
        self.cbo_target.setObjectName(u"cbo_target")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cbo_target.sizePolicy().hasHeightForWidth())
        self.cbo_target.setSizePolicy(sizePolicy4)
        self.cbo_target.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.cbo_target, 0, 1, 1, 1)

        self.btn_prev_nama = QPushButton(self.widget_12)
        self.btn_prev_nama.setObjectName(u"btn_prev_nama")
        self.btn_prev_nama.setMinimumSize(QSize(20, 24))
        self.btn_prev_nama.setMaximumSize(QSize(24, 16777215))
        self.btn_prev_nama.setIcon(icon1)
        self.btn_prev_nama.setFlat(True)

        self.gridLayout_2.addWidget(self.btn_prev_nama, 0, 3, 1, 1)

        self.cbo_daftar_nama = QComboBox(self.widget_12)
        self.cbo_daftar_nama.setObjectName(u"cbo_daftar_nama")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cbo_daftar_nama.sizePolicy().hasHeightForWidth())
        self.cbo_daftar_nama.setSizePolicy(sizePolicy5)
        self.cbo_daftar_nama.setMinimumSize(QSize(0, 24))
        self.cbo_daftar_nama.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_2.addWidget(self.cbo_daftar_nama, 0, 4, 1, 1)

        self.btn_next_dok = QPushButton(self.widget_12)
        self.btn_next_dok.setObjectName(u"btn_next_dok")
        self.btn_next_dok.setMinimumSize(QSize(20, 24))
        self.btn_next_dok.setMaximumSize(QSize(24, 16777215))
        self.btn_next_dok.setIcon(icon)
        self.btn_next_dok.setFlat(True)

        self.gridLayout_2.addWidget(self.btn_next_dok, 0, 9, 1, 1)


        self.gridLayout_7.addWidget(self.widget_12, 0, 0, 1, 1)

        self.gridLayout_7.setColumnStretch(0, 1)

        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.frame_4)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy6)
        self.viewer1_layout = QGridLayout(self.widget_5)
        self.viewer1_layout.setObjectName(u"viewer1_layout")

        self.gridLayout_3.addWidget(self.widget_5, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.frame_3)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy6.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy6)
        self.viewer2_layout = QGridLayout(self.widget_6)
        self.viewer2_layout.setObjectName(u"viewer2_layout")

        self.gridLayout_5.addWidget(self.widget_6, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.frame_3)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_10 = QGridLayout(self.widget_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(5)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_9 = QGridLayout(self.widget_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setVerticalSpacing(3)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_tambah = QPushButton(self.widget_11)
        self.btn_tambah.setObjectName(u"btn_tambah")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_tambah.sizePolicy().hasHeightForWidth())
        self.btn_tambah.setSizePolicy(sizePolicy7)
        self.btn_tambah.setMinimumSize(QSize(0, 24))
        icon2 = QIcon()
        icon2.addFile(u":/icon/resources/icon/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_tambah.setIcon(icon2)

        self.gridLayout_9.addWidget(self.btn_tambah, 0, 2, 1, 1)

        self.cbo_opsi_keterangan = QComboBox(self.widget_11)
        self.cbo_opsi_keterangan.setObjectName(u"cbo_opsi_keterangan")
        sizePolicy3.setHeightForWidth(self.cbo_opsi_keterangan.sizePolicy().hasHeightForWidth())
        self.cbo_opsi_keterangan.setSizePolicy(sizePolicy3)
        self.cbo_opsi_keterangan.setMinimumSize(QSize(100, 24))
        self.cbo_opsi_keterangan.setMaximumSize(QSize(100, 16777215))
        self.cbo_opsi_keterangan.setEditable(True)
        self.cbo_opsi_keterangan.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_9.addWidget(self.cbo_opsi_keterangan, 0, 1, 1, 1)

        self.cbo_jenis_dokumen = QComboBox(self.widget_11)
        self.cbo_jenis_dokumen.setObjectName(u"cbo_jenis_dokumen")
        self.cbo_jenis_dokumen.setMinimumSize(QSize(120, 24))
        self.cbo_jenis_dokumen.setMaximumSize(QSize(120, 16777215))
        self.cbo_jenis_dokumen.setEditable(False)
        self.cbo_jenis_dokumen.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_9.addWidget(self.cbo_jenis_dokumen, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.widget_11, 0, 1, 1, 1)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy8)
        self.gridLayout_4 = QGridLayout(self.widget_7)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMaximumSize(QSize(70, 16777215))
        self.gridLayout_6 = QGridLayout(self.widget_8)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.widget_8, 0, 6, 2, 1)

        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")
        sizePolicy7.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy7)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.btn_browse = QPushButton(self.widget_7)
        self.btn_browse.setObjectName(u"btn_browse")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.btn_browse.sizePolicy().hasHeightForWidth())
        self.btn_browse.setSizePolicy(sizePolicy9)
        self.btn_browse.setMinimumSize(QSize(0, 24))
        icon3 = QIcon()
        icon3.addFile(u":/icon/resources/icon/opened_folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_browse.setIcon(icon3)

        self.gridLayout_4.addWidget(self.btn_browse, 0, 2, 1, 1)

        self.btn_prev_file = QPushButton(self.widget_7)
        self.btn_prev_file.setObjectName(u"btn_prev_file")
        sizePolicy7.setHeightForWidth(self.btn_prev_file.sizePolicy().hasHeightForWidth())
        self.btn_prev_file.setSizePolicy(sizePolicy7)
        self.btn_prev_file.setMinimumSize(QSize(16, 24))
        self.btn_prev_file.setIcon(icon1)
        self.btn_prev_file.setFlat(True)

        self.gridLayout_4.addWidget(self.btn_prev_file, 0, 3, 1, 1)

        self.line_source = QLineEdit(self.widget_7)
        self.line_source.setObjectName(u"line_source")
        sizePolicy5.setHeightForWidth(self.line_source.sizePolicy().hasHeightForWidth())
        self.line_source.setSizePolicy(sizePolicy5)
        self.line_source.setMinimumSize(QSize(0, 24))

        self.gridLayout_4.addWidget(self.line_source, 0, 1, 1, 1)

        self.cbo_list_files = QComboBox(self.widget_7)
        self.cbo_list_files.setObjectName(u"cbo_list_files")
        sizePolicy5.setHeightForWidth(self.cbo_list_files.sizePolicy().hasHeightForWidth())
        self.cbo_list_files.setSizePolicy(sizePolicy5)
        self.cbo_list_files.setMinimumSize(QSize(0, 24))
        self.cbo_list_files.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_4.addWidget(self.cbo_list_files, 0, 4, 1, 1)

        self.btn_next_file = QPushButton(self.widget_7)
        self.btn_next_file.setObjectName(u"btn_next_file")
        sizePolicy7.setHeightForWidth(self.btn_next_file.sizePolicy().hasHeightForWidth())
        self.btn_next_file.setSizePolicy(sizePolicy7)
        self.btn_next_file.setMinimumSize(QSize(16, 24))
        self.btn_next_file.setIcon(icon)
        self.btn_next_file.setIconSize(QSize(16, 16))
        self.btn_next_file.setFlat(True)

        self.gridLayout_4.addWidget(self.btn_next_file, 0, 5, 1, 1)

        self.btn_hapus = QPushButton(self.widget_7)
        self.btn_hapus.setObjectName(u"btn_hapus")
        sizePolicy9.setHeightForWidth(self.btn_hapus.sizePolicy().hasHeightForWidth())
        self.btn_hapus.setSizePolicy(sizePolicy9)
        self.btn_hapus.setMinimumSize(QSize(0, 24))
        icon4 = QIcon()
        icon4.addFile(u":/icon/resources/icon/trash_can.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_hapus.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_hapus, 0, 7, 1, 1)


        self.gridLayout_10.addWidget(self.widget_7, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.radio_is_active.setText(QCoreApplication.translate("Form", u"Aktif", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Target", None))
        self.btn_next_nama.setText("")
        self.btn_prev_dok.setText("")
        self.btn_prev_nama.setText("")
        self.btn_next_dok.setText("")
        self.btn_tambah.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Folder", None))
        self.btn_browse.setText("")
        self.btn_prev_file.setText("")
        self.btn_next_file.setText("")
        self.btn_hapus.setText("")
    # retranslateUi

