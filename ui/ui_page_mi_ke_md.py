# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_mi_ke_md.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1214, 696)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_7 = QGridLayout(self.widget_3)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setIndent(20)

        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)

        self.mi_tbl = QTableWidget(self.widget_3)
        self.mi_tbl.setObjectName(u"mi_tbl")
        self.mi_tbl.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_7.addWidget(self.mi_tbl, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4.setIndent(20)

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.md_tbl = QTableWidget(self.widget_2)
        self.md_tbl.setObjectName(u"md_tbl")
        self.md_tbl.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_6.addWidget(self.md_tbl, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_8 = QGridLayout(self.widget_4)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6.setIndent(20)

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)

        self.btn_update_ke_mi = QPushButton(self.widget_4)
        self.btn_update_ke_mi.setObjectName(u"btn_update_ke_mi")
        self.btn_update_ke_mi.setMinimumSize(QSize(100, 25))

        self.gridLayout_8.addWidget(self.btn_update_ke_mi, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.tbl_beda = QTableWidget(self.widget_4)
        self.tbl_beda.setObjectName(u"tbl_beda")
        self.tbl_beda.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_8.addWidget(self.tbl_beda, 1, 0, 1, 4)

        self.btn_update_ke_md = QPushButton(self.widget_4)
        self.btn_update_ke_md.setObjectName(u"btn_update_ke_md")
        self.btn_update_ke_md.setMinimumSize(QSize(100, 25))

        self.gridLayout_8.addWidget(self.btn_update_ke_md, 0, 3, 1, 1)


        self.gridLayout_2.addWidget(self.widget_4, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Daftar Siswa MI Tidak Ada di MD", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Daftar Siswa MD", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Beda Kelas Antar MI dan MD", None))
        self.btn_update_ke_mi.setText(QCoreApplication.translate("Form", u"Sesuaikan Ke MI", None))
        self.btn_update_ke_md.setText(QCoreApplication.translate("Form", u"Sesuaikan Ke MD", None))
    # retranslateUi

