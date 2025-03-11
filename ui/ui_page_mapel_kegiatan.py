# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_mapel_kegiatan.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1142, 588)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.cbo_guru = QComboBox(self.widget_4)
        self.cbo_guru.setObjectName(u"cbo_guru")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbo_guru.sizePolicy().hasHeightForWidth())
        self.cbo_guru.setSizePolicy(sizePolicy1)
        self.cbo_guru.setMinimumSize(QSize(80, 24))
        self.cbo_guru.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_3.addWidget(self.cbo_guru, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.list_input_pelajaran = QLineEdit(self.widget_4)
        self.list_input_pelajaran.setObjectName(u"list_input_pelajaran")
        self.list_input_pelajaran.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.list_input_pelajaran, 0, 6, 1, 1)

        self.btn_tambah = QPushButton(self.widget_4)
        self.btn_tambah.setObjectName(u"btn_tambah")
        self.btn_tambah.setMinimumSize(QSize(80, 24))

        self.gridLayout_3.addWidget(self.btn_tambah, 0, 7, 1, 1)

        self.cbo_kegiatan = QComboBox(self.widget_4)
        self.cbo_kegiatan.setObjectName(u"cbo_kegiatan")
        self.cbo_kegiatan.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.cbo_kegiatan, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 3, 1, 1)

        self.btn_hapus = QPushButton(self.widget_4)
        self.btn_hapus.setObjectName(u"btn_hapus")
        self.btn_hapus.setMinimumSize(QSize(80, 24))

        self.gridLayout_3.addWidget(self.btn_hapus, 0, 8, 1, 1)


        self.gridLayout_4.addWidget(self.widget_4, 0, 0, 1, 1)

        self.tbl_mapel = QTableWidget(self.widget_3)
        self.tbl_mapel.setObjectName(u"tbl_mapel")
        self.tbl_mapel.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_4.addWidget(self.tbl_mapel, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 2, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_salin = QPushButton(self.widget_2)
        self.btn_salin.setObjectName(u"btn_salin")
        self.btn_salin.setMinimumSize(QSize(80, 24))

        self.gridLayout.addWidget(self.btn_salin, 0, 0, 1, 1)

        self.btn_clear_mapel = QPushButton(self.widget_2)
        self.btn_clear_mapel.setObjectName(u"btn_clear_mapel")
        self.btn_clear_mapel.setMinimumSize(QSize(80, 24))
        self.btn_clear_mapel.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.btn_clear_mapel, 0, 1, 1, 1)

        self.tbl_list_mapel = QTableWidget(self.widget_2)
        self.tbl_list_mapel.setObjectName(u"tbl_list_mapel")
        self.tbl_list_mapel.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tbl_list_mapel, 1, 0, 1, 2)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 2, 1)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.btn_tambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Guru Pengampu", None))
        self.btn_hapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btn_salin.setText(QCoreApplication.translate("Form", u"Salin Data Semester Sebelumnya", None))
        self.btn_clear_mapel.setText(QCoreApplication.translate("Form", u"Clear Mapel Kelas", None))
    # retranslateUi

