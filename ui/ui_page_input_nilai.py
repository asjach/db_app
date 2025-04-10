# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_input_nilai.ui'
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
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)
import resources_rc

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
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 5, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(379, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.btn_save = QPushButton(self.widget_2)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 50))

        self.gridLayout_5.addWidget(self.btn_save, 6, 0, 1, 3)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pte_excel_path = QPlainTextEdit(self.widget_3)
        self.pte_excel_path.setObjectName(u"pte_excel_path")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pte_excel_path.sizePolicy().hasHeightForWidth())
        self.pte_excel_path.setSizePolicy(sizePolicy)
        self.pte_excel_path.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_4.addWidget(self.pte_excel_path, 1, 0, 1, 4)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 3)

        self.btn_open_file = QPushButton(self.widget_3)
        self.btn_open_file.setObjectName(u"btn_open_file")
        self.btn_open_file.setMinimumSize(QSize(80, 0))

        self.gridLayout_4.addWidget(self.btn_open_file, 2, 0, 1, 1)

        self.btn_browse = QPushButton(self.widget_3)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMinimumSize(QSize(80, 24))

        self.gridLayout_4.addWidget(self.btn_browse, 2, 3, 1, 1)

        self.btn_clear = QPushButton(self.widget_3)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(80, 0))

        self.gridLayout_4.addWidget(self.btn_clear, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.widget_3, 3, 0, 1, 3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_new_default_path = QPushButton(self.widget_4)
        self.btn_new_default_path.setObjectName(u"btn_new_default_path")
        self.btn_new_default_path.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.btn_new_default_path, 0, 2, 1, 1)

        self.open_default_folder = QPushButton(self.widget_4)
        self.open_default_folder.setObjectName(u"open_default_folder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.open_default_folder.sizePolicy().hasHeightForWidth())
        self.open_default_folder.setSizePolicy(sizePolicy1)
        self.open_default_folder.setMinimumSize(QSize(0, 24))
        self.open_default_folder.setMaximumSize(QSize(30, 16777215))
        icon = QIcon()
        icon.addFile(u":/icon/resources/icon/icons8_opened_folder.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_default_folder.setIcon(icon)

        self.gridLayout_3.addWidget(self.open_default_folder, 0, 3, 1, 1)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.pte_default_path = QPlainTextEdit(self.widget_4)
        self.pte_default_path.setObjectName(u"pte_default_path")
        self.pte_default_path.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_3.addWidget(self.pte_default_path, 1, 0, 1, 4)

        self.line_nilai = QLineEdit(self.widget_4)
        self.line_nilai.setObjectName(u"line_nilai")
        self.line_nilai.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.line_nilai, 2, 0, 1, 2)

        self.line_walas = QLineEdit(self.widget_4)
        self.line_walas.setObjectName(u"line_walas")
        self.line_walas.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.line_walas, 3, 0, 1, 2)

        self.line_rekap = QLineEdit(self.widget_4)
        self.line_rekap.setObjectName(u"line_rekap")
        self.line_rekap.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.line_rekap, 4, 0, 1, 2)

        self.btn_template_rekap = QPushButton(self.widget_4)
        self.btn_template_rekap.setObjectName(u"btn_template_rekap")
        sizePolicy1.setHeightForWidth(self.btn_template_rekap.sizePolicy().hasHeightForWidth())
        self.btn_template_rekap.setSizePolicy(sizePolicy1)
        self.btn_template_rekap.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.btn_template_rekap, 4, 2, 1, 2)

        self.btn_template_walas = QPushButton(self.widget_4)
        self.btn_template_walas.setObjectName(u"btn_template_walas")
        sizePolicy1.setHeightForWidth(self.btn_template_walas.sizePolicy().hasHeightForWidth())
        self.btn_template_walas.setSizePolicy(sizePolicy1)
        self.btn_template_walas.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.btn_template_walas, 3, 2, 1, 2)

        self.btn_template_nilai = QPushButton(self.widget_4)
        self.btn_template_nilai.setObjectName(u"btn_template_nilai")
        sizePolicy1.setHeightForWidth(self.btn_template_nilai.sizePolicy().hasHeightForWidth())
        self.btn_template_nilai.setSizePolicy(sizePolicy1)
        self.btn_template_nilai.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.btn_template_nilai, 2, 2, 1, 2)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnMinimumWidth(2, 100)

        self.gridLayout_5.addWidget(self.widget_4, 0, 0, 2, 3)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radio_nilai_excel = QRadioButton(self.widget_5)
        self.radio_nilai_excel.setObjectName(u"radio_nilai_excel")

        self.gridLayout_6.addWidget(self.radio_nilai_excel, 5, 0, 1, 1)

        self.radio_nilai_catatan_db = QRadioButton(self.widget_5)
        self.radio_nilai_catatan_db.setObjectName(u"radio_nilai_catatan_db")
        self.radio_nilai_catatan_db.setChecked(False)

        self.gridLayout_6.addWidget(self.radio_nilai_catatan_db, 2, 0, 1, 1)

        self.radio_nilai_db = QRadioButton(self.widget_5)
        self.radio_nilai_db.setObjectName(u"radio_nilai_db")
        self.radio_nilai_db.setChecked(True)

        self.gridLayout_6.addWidget(self.radio_nilai_db, 0, 0, 1, 1)

        self.radio_catatan_db = QRadioButton(self.widget_5)
        self.radio_catatan_db.setObjectName(u"radio_catatan_db")

        self.gridLayout_6.addWidget(self.radio_catatan_db, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_5, 4, 0, 1, 3)


        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"SAVE", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"INPUT DARI FILE REKAP NILAI", None))
        self.btn_open_file.setText(QCoreApplication.translate("Form", u"Open File", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.btn_clear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.btn_new_default_path.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.open_default_folder.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"TEMPLATE EXCEL", None))
        self.btn_template_rekap.setText(QCoreApplication.translate("Form", u"REKAP", None))
        self.btn_template_walas.setText(QCoreApplication.translate("Form", u"WALI KELAS", None))
        self.btn_template_nilai.setText(QCoreApplication.translate("Form", u" NILAI", None))
        self.radio_nilai_excel.setText(QCoreApplication.translate("Form", u"Rekap Nilai di File Excel", None))
        self.radio_nilai_catatan_db.setText(QCoreApplication.translate("Form", u"Rekap Nilai dan Catatan di Database", None))
        self.radio_nilai_db.setText(QCoreApplication.translate("Form", u"Rekap Nilai di Database", None))
        self.radio_catatan_db.setText(QCoreApplication.translate("Form", u"Rekap Catatan di Database", None))
    # retranslateUi

