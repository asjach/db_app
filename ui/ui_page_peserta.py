# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_peserta.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(928, 616)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(492, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.cbo_kegiatan = QComboBox(self.widget)
        self.cbo_kegiatan.setObjectName(u"cbo_kegiatan")
        self.cbo_kegiatan.setMinimumSize(QSize(80, 24))

        self.gridLayout.addWidget(self.cbo_kegiatan, 0, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btn_generate = QPushButton(self.widget)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setMinimumSize(QSize(150, 24))

        self.gridLayout.addWidget(self.btn_generate, 0, 3, 1, 1)

        self.btn_clear = QPushButton(self.widget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(82, 24))

        self.gridLayout.addWidget(self.btn_clear, 0, 4, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tbl_widget = QTableWidget(self.widget_2)
        self.tbl_widget.setObjectName(u"tbl_widget")
        self.tbl_widget.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.gridLayout_4.addWidget(self.tbl_widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tbl_siswa_aktif_belum_masuk = QTableWidget(self.widget_3)
        self.tbl_siswa_aktif_belum_masuk.setObjectName(u"tbl_siswa_aktif_belum_masuk")
        self.tbl_siswa_aktif_belum_masuk.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.gridLayout_3.addWidget(self.tbl_siswa_aktif_belum_masuk, 1, 0, 1, 1)

        self.tbl_peserta_tidak_aktif = QTableWidget(self.widget_3)
        self.tbl_peserta_tidak_aktif.setObjectName(u"tbl_peserta_tidak_aktif")
        self.tbl_peserta_tidak_aktif.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.gridLayout_3.addWidget(self.tbl_peserta_tidak_aktif, 3, 0, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_3, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kegiatan Evaluatif", None))
        self.btn_generate.setText(QCoreApplication.translate("Form", u"Generate Peserta", None))
        self.btn_clear.setText(QCoreApplication.translate("Form", u"Clear Peserta", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Peserta Belum Masuk", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Peserta Tidak Aktif", None))
    # retranslateUi

