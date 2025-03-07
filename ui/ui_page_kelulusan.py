# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_kelulusan.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(925, 617)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tbl_siswa_lulus = QTableWidget(Form)
        self.tbl_siswa_lulus.setObjectName(u"tbl_siswa_lulus")

        self.gridLayout.addWidget(self.tbl_siswa_lulus, 0, 1, 1, 1)

        self.tbl_siswa_tidak_lulus = QTableWidget(Form)
        self.tbl_siswa_tidak_lulus.setObjectName(u"tbl_siswa_tidak_lulus")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_siswa_tidak_lulus.sizePolicy().hasHeightForWidth())
        self.tbl_siswa_tidak_lulus.setSizePolicy(sizePolicy)
        self.tbl_siswa_tidak_lulus.setMinimumSize(QSize(0, 200))
        self.tbl_siswa_tidak_lulus.setMaximumSize(QSize(16777215, 200))

        self.gridLayout.addWidget(self.tbl_siswa_tidak_lulus, 1, 1, 1, 1)

        self.frame_kiri = QFrame(Form)
        self.frame_kiri.setObjectName(u"frame_kiri")
        self.frame_kiri.setMinimumSize(QSize(400, 0))
        self.frame_kiri.setMaximumSize(QSize(400, 16777215))
        self.frame_kiri.setFrameShape(QFrame.StyledPanel)
        self.frame_kiri.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_kiri)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(0, 5, 0, 9)
        self.label = QLabel(self.frame_kiri)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.line_tgl_lulus = QLineEdit(self.frame_kiri)
        self.line_tgl_lulus.setObjectName(u"line_tgl_lulus")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_tgl_lulus.sizePolicy().hasHeightForWidth())
        self.line_tgl_lulus.setSizePolicy(sizePolicy1)
        self.line_tgl_lulus.setMinimumSize(QSize(120, 24))

        self.gridLayout_2.addWidget(self.line_tgl_lulus, 0, 1, 1, 1)

        self.btn_luluskan = QPushButton(self.frame_kiri)
        self.btn_luluskan.setObjectName(u"btn_luluskan")
        self.btn_luluskan.setMinimumSize(QSize(100, 24))
        self.btn_luluskan.setMaximumSize(QSize(100, 24))

        self.gridLayout_2.addWidget(self.btn_luluskan, 0, 2, 1, 1)

        self.tbl_list_siswa = QTableWidget(self.frame_kiri)
        self.tbl_list_siswa.setObjectName(u"tbl_list_siswa")

        self.gridLayout_2.addWidget(self.tbl_list_siswa, 1, 0, 1, 3)


        self.gridLayout.addWidget(self.frame_kiri, 0, 0, 2, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tanggal Kelulusan", None))
        self.btn_luluskan.setText(QCoreApplication.translate("Form", u"Luluskan", None))
    # retranslateUi

