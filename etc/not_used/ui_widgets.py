# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgets.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1308, 367)
        self.frame_search = QWidget(Form)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setGeometry(QRect(10, 90, 225, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_search.sizePolicy().hasHeightForWidth())
        self.frame_search.setSizePolicy(sizePolicy)
        self.frame_search.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.frame_search.setFont(font)
        self.frame_search.setInputMethodHints(Qt.ImhHiddenText)
        self.gridLayout_6 = QGridLayout(self.frame_search)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(5)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line_search = QLineEdit(self.frame_search)
        self.line_search.setObjectName(u"line_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_search.sizePolicy().hasHeightForWidth())
        self.line_search.setSizePolicy(sizePolicy1)
        self.line_search.setMinimumSize(QSize(120, 28))
        self.line_search.setMaximumSize(QSize(120, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        self.line_search.setFont(font1)
        self.line_search.setFrame(True)
        self.line_search.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.line_search, 0, 0, 1, 2, Qt.AlignRight)

        self.cbo_search_by = QComboBox(self.frame_search)
        self.cbo_search_by.setObjectName(u"cbo_search_by")
        self.cbo_search_by.setMinimumSize(QSize(100, 28))
        self.cbo_search_by.setMaximumSize(QSize(120, 16777215))
        self.cbo_search_by.setFont(font1)
        self.cbo_search_by.setEditable(False)
        self.cbo_search_by.setFrame(False)

        self.gridLayout_6.addWidget(self.cbo_search_by, 0, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

