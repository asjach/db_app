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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QListView, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSplitter, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from scripts.widgets.custom import DropPlainTextEdit

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1105, 738)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.tbl_widget = QTableWidget(self.splitter)
        self.tbl_widget.setObjectName(u"tbl_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_widget.sizePolicy().hasHeightForWidth())
        self.tbl_widget.setSizePolicy(sizePolicy)
        self.tbl_widget.setLineWidth(0)
        self.tbl_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_widget.setShowGrid(True)
        self.splitter.addWidget(self.tbl_widget)
        self.tbl_widget.verticalHeader().setMinimumSectionSize(24)
        self.tbl_widget.verticalHeader().setDefaultSectionSize(24)
        self.widget_custom = QWidget(self.splitter)
        self.widget_custom.setObjectName(u"widget_custom")
        self.widget_custom.setMinimumSize(QSize(300, 0))
        self.verticalLayout = QVBoxLayout(self.widget_custom)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.list_kolom = QListWidget(self.widget_custom)
        self.list_kolom.setObjectName(u"list_kolom")
        self.list_kolom.setAcceptDrops(False)
        self.list_kolom.setDragEnabled(True)
        self.list_kolom.setDragDropOverwriteMode(False)
        self.list_kolom.setDragDropMode(QAbstractItemView.DragDrop)
        self.list_kolom.setDefaultDropAction(Qt.MoveAction)
        self.list_kolom.setResizeMode(QListView.Adjust)
        self.list_kolom.setLayoutMode(QListView.Batched)
        self.list_kolom.setSpacing(0)
        self.list_kolom.setViewMode(QListView.IconMode)
        self.list_kolom.setWordWrap(False)
        self.list_kolom.setSelectionRectVisible(False)

        self.verticalLayout.addWidget(self.list_kolom)

        self.plain_custom = DropPlainTextEdit(self.widget_custom)
        self.plain_custom.setObjectName(u"plain_custom")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plain_custom.sizePolicy().hasHeightForWidth())
        self.plain_custom.setSizePolicy(sizePolicy1)
        self.plain_custom.setAcceptDrops(True)
        self.plain_custom.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.plain_custom)

        self.btn_preview = QPushButton(self.widget_custom)
        self.btn_preview.setObjectName(u"btn_preview")
        self.btn_preview.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.btn_preview)

        self.splitter.addWidget(self.widget_custom)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.plain_custom.setPlainText("")
        self.btn_preview.setText(QCoreApplication.translate("Form", u"Preview", None))
    # retranslateUi

