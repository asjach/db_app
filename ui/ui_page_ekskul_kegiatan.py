# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_ekskul_kegiatan.ui'
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
        self.cbo_pembimbing = QComboBox(self.widget_4)
        self.cbo_pembimbing.setObjectName(u"cbo_pembimbing")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbo_pembimbing.sizePolicy().hasHeightForWidth())
        self.cbo_pembimbing.setSizePolicy(sizePolicy1)
        self.cbo_pembimbing.setMinimumSize(QSize(80, 24))
        self.cbo_pembimbing.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_3.addWidget(self.cbo_pembimbing, 0, 4, 1, 1)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.btn_tambah = QPushButton(self.widget_4)
        self.btn_tambah.setObjectName(u"btn_tambah")
        self.btn_tambah.setMinimumSize(QSize(80, 24))

        self.gridLayout_3.addWidget(self.btn_tambah, 0, 7, 1, 1)

        self.list_input_ekskul = QLineEdit(self.widget_4)
        self.list_input_ekskul.setObjectName(u"list_input_ekskul")
        self.list_input_ekskul.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.list_input_ekskul, 0, 6, 1, 1)

        self.cbo_kegiatan = QComboBox(self.widget_4)
        self.cbo_kegiatan.setObjectName(u"cbo_kegiatan")
        self.cbo_kegiatan.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.cbo_kegiatan, 0, 1, 1, 1)

        self.btn_hapus = QPushButton(self.widget_4)
        self.btn_hapus.setObjectName(u"btn_hapus")
        self.btn_hapus.setMinimumSize(QSize(80, 24))

        self.gridLayout_3.addWidget(self.btn_hapus, 0, 8, 1, 1)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.widget_4, 0, 0, 1, 1)

        self.tbl_riwayat_ekskul = QTableWidget(self.widget_3)
        self.tbl_riwayat_ekskul.setObjectName(u"tbl_riwayat_ekskul")
        self.tbl_riwayat_ekskul.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_4.addWidget(self.tbl_riwayat_ekskul, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 2, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(300, 0))
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tbl_ekskul = QTableWidget(self.widget_2)
        self.tbl_ekskul.setObjectName(u"tbl_ekskul")
        self.tbl_ekskul.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.tbl_ekskul, 1, 0, 1, 2)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 2, 1)

        self.gridLayout_2.setColumnStretch(0, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.btn_tambah.setText(QCoreApplication.translate("Form", u"Tambah", None))
        self.btn_hapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Pembimbing Ekskul", None))
        self.label.setText(QCoreApplication.translate("Form", u"EKSTRAKURIKULER", None))
    # retranslateUi

