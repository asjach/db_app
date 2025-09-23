# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_daftar_kelas.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1105, 677)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tbl_widget = QTableWidget(Form)
        self.tbl_widget.setObjectName(u"tbl_widget")
        self.tbl_widget.setLineWidth(0)
        self.tbl_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_widget.setShowGrid(True)
        self.tbl_widget.verticalHeader().setMinimumSectionSize(24)
        self.tbl_widget.verticalHeader().setDefaultSectionSize(24)

        self.gridLayout.addWidget(self.tbl_widget, 1, 0, 1, 1)

        self.widget_custom = QWidget(Form)
        self.widget_custom.setObjectName(u"widget_custom")
        self.widget_custom.setMinimumSize(QSize(0, 60))
        self.widget_custom.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout = QHBoxLayout(self.widget_custom)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.plain_custom = QPlainTextEdit(self.widget_custom)
        self.plain_custom.setObjectName(u"plain_custom")

        self.horizontalLayout.addWidget(self.plain_custom)

        self.btn_preview = QPushButton(self.widget_custom)
        self.btn_preview.setObjectName(u"btn_preview")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_preview.sizePolicy().hasHeightForWidth())
        self.btn_preview.setSizePolicy(sizePolicy)
        self.btn_preview.setMinimumSize(QSize(80, 0))
        self.btn_preview.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.btn_preview)


        self.gridLayout.addWidget(self.widget_custom, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_preview.setText(QCoreApplication.translate("Form", u"preview", None))
    # retranslateUi

