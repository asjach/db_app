# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_kelulusan.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1003, 596)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_show_bottom = QPushButton(self.widget)
        self.btn_show_bottom.setObjectName(u"btn_show_bottom")
        self.btn_show_bottom.setMinimumSize(QSize(24, 24))
        self.btn_show_bottom.setMaximumSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.btn_show_bottom, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.tbl_siswa_lulus = QTableWidget(self.widget)
        self.tbl_siswa_lulus.setObjectName(u"tbl_siswa_lulus")

        self.gridLayout_3.addWidget(self.tbl_siswa_lulus, 1, 0, 1, 2)

        self.tbl_siswa_tidak_lulus = QTableWidget(self.widget)
        self.tbl_siswa_tidak_lulus.setObjectName(u"tbl_siswa_tidak_lulus")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_siswa_tidak_lulus.sizePolicy().hasHeightForWidth())
        self.tbl_siswa_tidak_lulus.setSizePolicy(sizePolicy)
        self.tbl_siswa_tidak_lulus.setMinimumSize(QSize(0, 200))
        self.tbl_siswa_tidak_lulus.setMaximumSize(QSize(16777215, 200))

        self.gridLayout_3.addWidget(self.tbl_siswa_tidak_lulus, 2, 0, 1, 2)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.widget_kiri = QWidget(Form)
        self.widget_kiri.setObjectName(u"widget_kiri")
        self.widget_kiri.setMinimumSize(QSize(500, 0))
        self.widget_kiri.setMaximumSize(QSize(500, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget_kiri)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_kiri)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.btn_luluskan = QPushButton(self.widget_kiri)
        self.btn_luluskan.setObjectName(u"btn_luluskan")
        self.btn_luluskan.setMinimumSize(QSize(100, 24))
        self.btn_luluskan.setMaximumSize(QSize(100, 24))

        self.gridLayout_2.addWidget(self.btn_luluskan, 0, 2, 1, 1)

        self.tbl_list_siswa = QTableWidget(self.widget_kiri)
        self.tbl_list_siswa.setObjectName(u"tbl_list_siswa")

        self.gridLayout_2.addWidget(self.tbl_list_siswa, 1, 0, 1, 3)

        self.date_tgl_lulus = QDateEdit(self.widget_kiri)
        self.date_tgl_lulus.setObjectName(u"date_tgl_lulus")
        self.date_tgl_lulus.setMinimumSize(QSize(150, 24))
        self.date_tgl_lulus.setMaximumSize(QSize(150, 16777215))
        self.date_tgl_lulus.setLocale(QLocale(QLocale.Indonesian, QLocale.Indonesia))
        self.date_tgl_lulus.setAlignment(Qt.AlignCenter)
        self.date_tgl_lulus.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.date_tgl_lulus, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_kiri, 0, 0, 2, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_show_bottom.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Tanggal Kelulusan", None))
        self.btn_luluskan.setText(QCoreApplication.translate("Form", u"Luluskan", None))
        self.date_tgl_lulus.setDisplayFormat(QCoreApplication.translate("Form", u"dd MMMM yyyy", None))
    # retranslateUi

