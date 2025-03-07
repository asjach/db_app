# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_rekap_siswa.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1256, 700)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tbl_rekap_tingkat = QTableWidget(self.frame_2)
        self.tbl_rekap_tingkat.setObjectName(u"tbl_rekap_tingkat")

        self.gridLayout_4.addWidget(self.tbl_rekap_tingkat, 0, 0, 1, 1)

        self.tbl_rekap_rombel = QTableWidget(self.frame_2)
        self.tbl_rekap_rombel.setObjectName(u"tbl_rekap_rombel")

        self.gridLayout_4.addWidget(self.tbl_rekap_rombel, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 350))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tbl_rekap_umur = QTableWidget(self.frame_3)
        self.tbl_rekap_umur.setObjectName(u"tbl_rekap_umur")

        self.gridLayout_3.addWidget(self.tbl_rekap_umur, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(350, 0))
        self.frame.setMaximumSize(QSize(350, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tbl_rekap_all = QTableWidget(self.frame)
        self.tbl_rekap_all.setObjectName(u"tbl_rekap_all")

        self.gridLayout_2.addWidget(self.tbl_rekap_all, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 2, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

