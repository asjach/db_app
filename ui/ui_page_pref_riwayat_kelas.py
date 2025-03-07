# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_pref_riwayat_kelas.ui'
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
        Form.resize(905, 532)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 24))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.tbl_jenjang = QTableWidget(self.widget_3)
        self.tbl_jenjang.setObjectName(u"tbl_jenjang")
        self.tbl_jenjang.setMaximumSize(QSize(16777215, 200))
        self.tbl_jenjang.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.tbl_jenjang, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_3, 0, 0, 2, 2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.tbl_tapel = QTableWidget(self.widget_4)
        self.tbl_tapel.setObjectName(u"tbl_tapel")
        self.tbl_tapel.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_3.addWidget(self.tbl_tapel, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_4, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cbo_wali_kelas = QComboBox(self.widget_2)
        self.cbo_wali_kelas.setObjectName(u"cbo_wali_kelas")
        self.cbo_wali_kelas.setMinimumSize(QSize(200, 24))

        self.gridLayout_5.addWidget(self.cbo_wali_kelas, 0, 6, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 24))

        self.gridLayout_5.addWidget(self.label_4, 0, 5, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 24))

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.tbl_kelas = QTableWidget(self.widget_2)
        self.tbl_kelas.setObjectName(u"tbl_kelas")
        self.tbl_kelas.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_5.addWidget(self.tbl_kelas, 1, 0, 1, 7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.line_tambah_kelas = QLineEdit(self.widget_2)
        self.line_tambah_kelas.setObjectName(u"line_tambah_kelas")

        self.gridLayout_5.addWidget(self.line_tambah_kelas, 0, 2, 1, 1)

        self.btn_tambah_kelas = QPushButton(self.widget_2)
        self.btn_tambah_kelas.setObjectName(u"btn_tambah_kelas")
        self.btn_tambah_kelas.setMinimumSize(QSize(100, 0))

        self.gridLayout_5.addWidget(self.btn_tambah_kelas, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Jenjang", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Tapel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Pilih Wali Kelas", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Riwayat Kelas", None))
        self.btn_tambah_kelas.setText(QCoreApplication.translate("Form", u"Tambah Kelas", None))
    # retranslateUi

