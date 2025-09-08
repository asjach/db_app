# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_export_excel.ui'
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
    QHeaderView, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1172, 698)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(80, 0))
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.cbo_opsi_data = QComboBox(self.widget_3)
        self.cbo_opsi_data.addItem("")
        self.cbo_opsi_data.addItem("")
        self.cbo_opsi_data.setObjectName(u"cbo_opsi_data")
        self.cbo_opsi_data.setMinimumSize(QSize(80, 28))

        self.gridLayout_2.addWidget(self.cbo_opsi_data, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_3, 0, 0, 1, 1)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_kelas = QWidget(self.frame)
        self.frame_kelas.setObjectName(u"frame_kelas")
        self.gridLayout_8 = QGridLayout(self.frame_kelas)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_kelas)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)

        self.cbo_kelas = QComboBox(self.frame_kelas)
        self.cbo_kelas.setObjectName(u"cbo_kelas")
        self.cbo_kelas.setMinimumSize(QSize(80, 28))

        self.gridLayout_8.addWidget(self.cbo_kelas, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_kelas, 0, 2, 1, 1)

        self.frame_tingkat = QWidget(self.frame)
        self.frame_tingkat.setObjectName(u"frame_tingkat")
        self.gridLayout_7 = QGridLayout(self.frame_tingkat)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_tingkat)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)

        self.cbo_tingkat = QComboBox(self.frame_tingkat)
        self.cbo_tingkat.addItem("")
        self.cbo_tingkat.addItem("")
        self.cbo_tingkat.addItem("")
        self.cbo_tingkat.addItem("")
        self.cbo_tingkat.addItem("")
        self.cbo_tingkat.addItem("")
        self.cbo_tingkat.addItem("")
        self.cbo_tingkat.setObjectName(u"cbo_tingkat")
        self.cbo_tingkat.setMinimumSize(QSize(80, 28))

        self.gridLayout_7.addWidget(self.cbo_tingkat, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_tingkat, 0, 1, 1, 1)

        self.frame_order = QWidget(self.frame)
        self.frame_order.setObjectName(u"frame_order")
        self.gridLayout_12 = QGridLayout(self.frame_order)
        self.gridLayout_12.setSpacing(5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_order)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_12.addWidget(self.label_7, 0, 0, 1, 1)

        self.cbo_order = QComboBox(self.frame_order)
        self.cbo_order.setObjectName(u"cbo_order")
        self.cbo_order.setMinimumSize(QSize(70, 28))

        self.gridLayout_12.addWidget(self.cbo_order, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_order, 0, 6, 1, 1)

        self.frame_export = QFrame(self.frame)
        self.frame_export.setObjectName(u"frame_export")
        self.frame_export.setFrameShape(QFrame.StyledPanel)
        self.frame_export.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_export)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_preview = QPushButton(self.frame_export)
        self.btn_preview.setObjectName(u"btn_preview")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_preview.sizePolicy().hasHeightForWidth())
        self.btn_preview.setSizePolicy(sizePolicy1)
        self.btn_preview.setMinimumSize(QSize(0, 28))
        font = QFont()
        font.setPointSize(10)
        self.btn_preview.setFont(font)

        self.gridLayout_3.addWidget(self.btn_preview, 0, 0, 1, 1)

        self.btn_export = QPushButton(self.frame_export)
        self.btn_export.setObjectName(u"btn_export")
        sizePolicy1.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy1)
        self.btn_export.setMinimumSize(QSize(0, 28))
        self.btn_export.setFont(font)

        self.gridLayout_3.addWidget(self.btn_export, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_export, 0, 8, 1, 1)

        self.frame_status = QWidget(self.frame)
        self.frame_status.setObjectName(u"frame_status")
        self.gridLayout_9 = QGridLayout(self.frame_status)
        self.gridLayout_9.setSpacing(5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_status)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)

        self.cbo_status = QComboBox(self.frame_status)
        self.cbo_status.setObjectName(u"cbo_status")
        self.cbo_status.setMinimumSize(QSize(70, 28))

        self.gridLayout_9.addWidget(self.cbo_status, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_status, 0, 5, 1, 1)

        self.frame_jenjang = QWidget(self.frame)
        self.frame_jenjang.setObjectName(u"frame_jenjang")
        self.gridLayout_5 = QGridLayout(self.frame_jenjang)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_jenjang)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.cbo_jenjang = QComboBox(self.frame_jenjang)
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.setObjectName(u"cbo_jenjang")
        self.cbo_jenjang.setMinimumSize(QSize(80, 28))

        self.gridLayout_5.addWidget(self.cbo_jenjang, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_jenjang, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 7, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 1, 1, 1)

        self.widget_10 = QWidget(self.widget)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.gridLayout_13 = QGridLayout(self.widget_10)
        self.gridLayout_13.setSpacing(5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(5, 5, 5, 5)
        self.widget_8 = QWidget(self.widget_10)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy2)
        self.gridLayout_10 = QGridLayout(self.widget_8)
        self.gridLayout_10.setSpacing(5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_save = QPushButton(self.widget_8)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 28))

        self.gridLayout_10.addWidget(self.btn_save, 1, 2, 1, 1)

        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_10.addWidget(self.label_6, 1, 5, 1, 1)

        self.cbo_kolom = QComboBox(self.widget_8)
        self.cbo_kolom.setObjectName(u"cbo_kolom")
        self.cbo_kolom.setMinimumSize(QSize(120, 28))

        self.gridLayout_10.addWidget(self.cbo_kolom, 1, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.label_8 = QLabel(self.widget_8)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_10.addWidget(self.label_8, 1, 0, 1, 1)

        self.cbo_nama_data_kolom = QComboBox(self.widget_8)
        self.cbo_nama_data_kolom.setObjectName(u"cbo_nama_data_kolom")
        self.cbo_nama_data_kolom.setMinimumSize(QSize(200, 28))
        self.cbo_nama_data_kolom.setEditable(True)

        self.gridLayout_10.addWidget(self.cbo_nama_data_kolom, 1, 1, 1, 1)


        self.gridLayout_13.addWidget(self.widget_8, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.widget_10)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_15 = QGridLayout(self.widget_4)
        self.gridLayout_15.setSpacing(5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.plain_filter_tambahan = QPlainTextEdit(self.widget_4)
        self.plain_filter_tambahan.setObjectName(u"plain_filter_tambahan")
        sizePolicy2.setHeightForWidth(self.plain_filter_tambahan.sizePolicy().hasHeightForWidth())
        self.plain_filter_tambahan.setSizePolicy(sizePolicy2)
        self.plain_filter_tambahan.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_15.addWidget(self.plain_filter_tambahan, 1, 0, 1, 1)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_15.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_4, 0, 1, 2, 1)

        self.plain_kolom_kolom = QPlainTextEdit(self.widget_10)
        self.plain_kolom_kolom.setObjectName(u"plain_kolom_kolom")
        sizePolicy.setHeightForWidth(self.plain_kolom_kolom.sizePolicy().hasHeightForWidth())
        self.plain_kolom_kolom.setSizePolicy(sizePolicy)
        self.plain_kolom_kolom.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_13.addWidget(self.plain_kolom_kolom, 1, 0, 1, 1)

        self.gridLayout_13.setColumnStretch(0, 2)
        self.gridLayout_13.setColumnStretch(1, 1)

        self.gridLayout_4.addWidget(self.widget_10, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.gridLayout_11 = QGridLayout(self.widget_2)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.widget_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_11.addWidget(self.tableWidget, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Data", None))
        self.cbo_opsi_data.setItemText(0, QCoreApplication.translate("Form", u"Siswa", None))
        self.cbo_opsi_data.setItemText(1, QCoreApplication.translate("Form", u"Guru", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Tingkat", None))
        self.cbo_tingkat.setItemText(0, QCoreApplication.translate("Form", u"--Semua--", None))
        self.cbo_tingkat.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.cbo_tingkat.setItemText(2, QCoreApplication.translate("Form", u"2", None))
        self.cbo_tingkat.setItemText(3, QCoreApplication.translate("Form", u"3", None))
        self.cbo_tingkat.setItemText(4, QCoreApplication.translate("Form", u"4", None))
        self.cbo_tingkat.setItemText(5, QCoreApplication.translate("Form", u"5", None))
        self.cbo_tingkat.setItemText(6, QCoreApplication.translate("Form", u"6", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"Order", None))
        self.btn_preview.setText(QCoreApplication.translate("Form", u"Preview", None))
        self.btn_export.setText(QCoreApplication.translate("Form", u"Export", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Status", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Jenjang", None))
        self.cbo_jenjang.setItemText(0, QCoreApplication.translate("Form", u"--Semua--", None))
        self.cbo_jenjang.setItemText(1, QCoreApplication.translate("Form", u"MI", None))
        self.cbo_jenjang.setItemText(2, QCoreApplication.translate("Form", u"MD", None))
        self.cbo_jenjang.setItemText(3, QCoreApplication.translate("Form", u"MI-MD", None))
        self.cbo_jenjang.setItemText(4, QCoreApplication.translate("Form", u"MI Saja", None))
        self.cbo_jenjang.setItemText(5, QCoreApplication.translate("Form", u"MD Saja", None))
        self.cbo_jenjang.setItemText(6, QCoreApplication.translate("Form", u"MI Saja/MD Saja", None))

        self.btn_save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Kolom", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Nama Data Kolom", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Filter Tambahan (Spesifik)", None))
    # retranslateUi

