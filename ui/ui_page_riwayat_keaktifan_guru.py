# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_riwayat_keaktifan_guru.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

from scripts.widgets.custom import DropPlainTextEdit

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1060, 654)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 5, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btn_tapel_sebelumnya = QPushButton(Form)
        self.btn_tapel_sebelumnya.setObjectName(u"btn_tapel_sebelumnya")
        self.btn_tapel_sebelumnya.setMinimumSize(QSize(250, 24))

        self.gridLayout.addWidget(self.btn_tapel_sebelumnya, 0, 5, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.cbo_guru = QComboBox(Form)
        self.cbo_guru.setObjectName(u"cbo_guru")
        self.cbo_guru.setMinimumSize(QSize(200, 24))

        self.gridLayout.addWidget(self.cbo_guru, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.btn_preview = QPushButton(Form)
        self.btn_preview.setObjectName(u"btn_preview")
        self.btn_preview.setMinimumSize(QSize(80, 24))

        self.gridLayout.addWidget(self.btn_preview, 0, 6, 1, 1)

        self.tbl_keaktifan = QTableWidget(Form)
        self.tbl_keaktifan.setObjectName(u"tbl_keaktifan")

        self.gridLayout.addWidget(self.tbl_keaktifan, 2, 0, 1, 7)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 80))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.list_nama_kolom = QListWidget(self.widget)
        self.list_nama_kolom.setObjectName(u"list_nama_kolom")
        self.list_nama_kolom.setStyleSheet(u"")
        self.list_nama_kolom.setDragEnabled(True)
        self.list_nama_kolom.setFlow(QListView.LeftToRight)
        self.list_nama_kolom.setResizeMode(QListView.Adjust)
        self.list_nama_kolom.setLayoutMode(QListView.Batched)
        self.list_nama_kolom.setViewMode(QListView.IconMode)

        self.gridLayout_2.addWidget(self.list_nama_kolom, 0, 1, 1, 1)

        self.plain_custom = DropPlainTextEdit(self.widget)
        self.plain_custom.setObjectName(u"plain_custom")
        self.plain_custom.setMinimumSize(QSize(0, 60))

        self.gridLayout_2.addWidget(self.plain_custom, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Riwayat Keaktifan Guru", None))
        self.btn_tapel_sebelumnya.setText(QCoreApplication.translate("Form", u"Aktifkan Guru dari Tapel Sebelumnya", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Tambah Manual", None))
#if QT_CONFIG(tooltip)
        self.cbo_guru.setToolTip(QCoreApplication.translate("Form", u"Pilih guru yang akan ditambahkan", None))
#endif // QT_CONFIG(tooltip)
        self.btn_preview.setText(QCoreApplication.translate("Form", u"Preview", None))
    # retranslateUi

