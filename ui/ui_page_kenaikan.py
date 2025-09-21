# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_kenaikan.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(925, 617)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.tbl_siswa_naik = QTableWidget(Form)
        self.tbl_siswa_naik.setObjectName(u"tbl_siswa_naik")

        self.gridLayout.addWidget(self.tbl_siswa_naik, 0, 1, 1, 1)

        self.tbl_siswa_tidak_naik = QTableWidget(Form)
        self.tbl_siswa_tidak_naik.setObjectName(u"tbl_siswa_tidak_naik")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_siswa_tidak_naik.sizePolicy().hasHeightForWidth())
        self.tbl_siswa_tidak_naik.setSizePolicy(sizePolicy)
        self.tbl_siswa_tidak_naik.setMinimumSize(QSize(0, 200))
        self.tbl_siswa_tidak_naik.setMaximumSize(QSize(16777215, 200))

        self.gridLayout.addWidget(self.tbl_siswa_tidak_naik, 1, 1, 1, 1)

        self.widget_kiri = QWidget(Form)
        self.widget_kiri.setObjectName(u"widget_kiri")
        self.widget_kiri.setMinimumSize(QSize(500, 0))
        self.widget_kiri.setMaximumSize(QSize(500, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget_kiri)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_kiri)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.btn_naikkan = QPushButton(self.widget_kiri)
        self.btn_naikkan.setObjectName(u"btn_naikkan")
        self.btn_naikkan.setMinimumSize(QSize(100, 24))
        self.btn_naikkan.setMaximumSize(QSize(100, 24))

        self.gridLayout_2.addWidget(self.btn_naikkan, 0, 2, 1, 1)

        self.tbl_list_siswa_kenaikan = QTableWidget(self.widget_kiri)
        self.tbl_list_siswa_kenaikan.setObjectName(u"tbl_list_siswa_kenaikan")

        self.gridLayout_2.addWidget(self.tbl_list_siswa_kenaikan, 1, 0, 1, 3)

        self.date_tgl_naik = QDateEdit(self.widget_kiri)
        self.date_tgl_naik.setObjectName(u"date_tgl_naik")
        self.date_tgl_naik.setMinimumSize(QSize(150, 24))
        self.date_tgl_naik.setMaximumSize(QSize(150, 16777215))
        self.date_tgl_naik.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.date_tgl_naik.setAlignment(Qt.AlignCenter)
        self.date_tgl_naik.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.date_tgl_naik, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_kiri, 0, 0, 2, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tanggal Kenaikan", None))
        self.btn_naikkan.setText(QCoreApplication.translate("Form", u"Naikkan", None))
        self.date_tgl_naik.setDisplayFormat(QCoreApplication.translate("Form", u"dd MMMM yyyy", None))
    # retranslateUi

