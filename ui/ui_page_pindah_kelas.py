# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_pindah_kelas.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1056, 800)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_b = QLabel(self.widget_2)
        self.lbl_b.setObjectName(u"lbl_b")
        self.lbl_b.setMinimumSize(QSize(0, 24))
        self.lbl_b.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_3.addWidget(self.lbl_b, 0, 0, 1, 1)

        self.tbl_b = QTableWidget(self.widget_2)
        self.tbl_b.setObjectName(u"tbl_b")

        self.gridLayout_3.addWidget(self.tbl_b, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_c = QLabel(self.widget_3)
        self.lbl_c.setObjectName(u"lbl_c")
        self.lbl_c.setMinimumSize(QSize(0, 24))
        self.lbl_c.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_4.addWidget(self.lbl_c, 0, 0, 1, 1)

        self.tbl_c = QTableWidget(self.widget_3)
        self.tbl_c.setObjectName(u"tbl_c")

        self.gridLayout_4.addWidget(self.tbl_c, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_a = QLabel(self.widget)
        self.lbl_a.setObjectName(u"lbl_a")
        self.lbl_a.setMinimumSize(QSize(0, 24))
        self.lbl_a.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_2.addWidget(self.lbl_a, 0, 0, 1, 1)

        self.tbl_a = QTableWidget(self.widget)
        self.tbl_a.setObjectName(u"tbl_a")

        self.gridLayout_2.addWidget(self.tbl_a, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_b.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_c.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_a.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

