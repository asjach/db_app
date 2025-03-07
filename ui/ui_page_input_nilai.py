# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_input_nilai.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1208, 810)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cbo_kegiatan = QComboBox(self.widget)
        self.cbo_kegiatan.setObjectName(u"cbo_kegiatan")
        self.cbo_kegiatan.setMinimumSize(QSize(120, 24))

        self.gridLayout_2.addWidget(self.cbo_kegiatan, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(1015, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)

        self.input_tbl = QTableWidget(Form)
        self.input_tbl.setObjectName(u"input_tbl")

        self.gridLayout.addWidget(self.input_tbl, 1, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(400, 0))
        self.widget_2.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pte_default_path = QPlainTextEdit(self.widget_2)
        self.pte_default_path.setObjectName(u"pte_default_path")
        self.pte_default_path.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_3.addWidget(self.pte_default_path, 2, 0, 1, 2)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_reload = QPushButton(self.widget_3)
        self.btn_reload.setObjectName(u"btn_reload")
        self.btn_reload.setMinimumSize(QSize(80, 0))

        self.gridLayout_4.addWidget(self.btn_reload, 2, 2, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.pte_excel_path = QPlainTextEdit(self.widget_3)
        self.pte_excel_path.setObjectName(u"pte_excel_path")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pte_excel_path.sizePolicy().hasHeightForWidth())
        self.pte_excel_path.setSizePolicy(sizePolicy)
        self.pte_excel_path.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_4.addWidget(self.pte_excel_path, 1, 0, 1, 4)

        self.btn_browse = QPushButton(self.widget_3)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMinimumSize(QSize(80, 24))

        self.gridLayout_4.addWidget(self.btn_browse, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.btn_open = QPushButton(self.widget_3)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(80, 0))

        self.gridLayout_4.addWidget(self.btn_open, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_3, 9, 0, 1, 2)

        self.btn_template_rekap = QPushButton(self.widget_2)
        self.btn_template_rekap.setObjectName(u"btn_template_rekap")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_template_rekap.sizePolicy().hasHeightForWidth())
        self.btn_template_rekap.setSizePolicy(sizePolicy1)
        self.btn_template_rekap.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.btn_template_rekap, 5, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(379, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 7, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.btn_template_walas = QPushButton(self.widget_2)
        self.btn_template_walas.setObjectName(u"btn_template_walas")
        sizePolicy1.setHeightForWidth(self.btn_template_walas.sizePolicy().hasHeightForWidth())
        self.btn_template_walas.setSizePolicy(sizePolicy1)
        self.btn_template_walas.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.btn_template_walas, 4, 0, 1, 2)

        self.btn_save = QPushButton(self.widget_2)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 50))

        self.gridLayout_3.addWidget(self.btn_save, 13, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 11, 0, 1, 2)

        self.btn_template_nilai = QPushButton(self.widget_2)
        self.btn_template_nilai.setObjectName(u"btn_template_nilai")
        sizePolicy1.setHeightForWidth(self.btn_template_nilai.sizePolicy().hasHeightForWidth())
        self.btn_template_nilai.setSizePolicy(sizePolicy1)
        self.btn_template_nilai.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.btn_template_nilai, 3, 0, 1, 2)

        self.btn_new_default_path = QPushButton(self.widget_2)
        self.btn_new_default_path.setObjectName(u"btn_new_default_path")
        self.btn_new_default_path.setMinimumSize(QSize(120, 24))

        self.gridLayout_3.addWidget(self.btn_new_default_path, 1, 1, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.btn_reload.setText(QCoreApplication.translate("Form", u"Reload", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"INPUT NILAI DARI EXCEL", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.btn_open.setText(QCoreApplication.translate("Form", u"Open File", None))
        self.btn_template_rekap.setText(QCoreApplication.translate("Form", u"TEMPLATE REKAP", None))
        self.btn_template_walas.setText(QCoreApplication.translate("Form", u"TEMPLATE WALI KELAS", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"SAVE", None))
        self.btn_template_nilai.setText(QCoreApplication.translate("Form", u"TEMPLATE NILAI", None))
        self.btn_new_default_path.setText(QCoreApplication.translate("Form", u"Default Folder", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TEMPLATE EXCEL", None))
    # retranslateUi

