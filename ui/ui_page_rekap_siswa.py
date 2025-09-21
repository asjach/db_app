# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_rekap_siswa.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1256, 700)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tbl_rekap_tingkat = QTableWidget(self.widget_2)
        self.tbl_rekap_tingkat.setObjectName(u"tbl_rekap_tingkat")
        self.tbl_rekap_tingkat.setLineWidth(0)

        self.gridLayout_4.addWidget(self.tbl_rekap_tingkat, 0, 0, 1, 1)

        self.tbl_rekap_rombel = QTableWidget(self.widget_2)
        self.tbl_rekap_rombel.setObjectName(u"tbl_rekap_rombel")
        self.tbl_rekap_rombel.setLineWidth(0)

        self.gridLayout_4.addWidget(self.tbl_rekap_rombel, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(350, 0))
        self.widget.setMaximumSize(QSize(350, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tbl_rekap_all = QTableWidget(self.widget)
        self.tbl_rekap_all.setObjectName(u"tbl_rekap_all")
        self.tbl_rekap_all.setLineWidth(0)

        self.gridLayout_2.addWidget(self.tbl_rekap_all, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 1, 2, 1)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(0, 350))
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tbl_rekap_umur = QTableWidget(self.widget_3)
        self.tbl_rekap_umur.setObjectName(u"tbl_rekap_umur")
        self.tbl_rekap_umur.setLineWidth(0)

        self.gridLayout_3.addWidget(self.tbl_rekap_umur, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 1, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

