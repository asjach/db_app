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
        Form.resize(1140, 810)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.radio_nilai_excel = QRadioButton(self.widget)
        self.radio_nilai_excel.setObjectName(u"radio_nilai_excel")

        self.gridLayout_2.addWidget(self.radio_nilai_excel, 0, 9, 1, 1)

        self.radio_nilai_db = QRadioButton(self.widget)
        self.radio_nilai_db.setObjectName(u"radio_nilai_db")
        self.radio_nilai_db.setChecked(True)

        self.gridLayout_2.addWidget(self.radio_nilai_db, 0, 3, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.cbo_kegiatan = QComboBox(self.widget)
        self.cbo_kegiatan.setObjectName(u"cbo_kegiatan")
        self.cbo_kegiatan.setMinimumSize(QSize(120, 24))

        self.gridLayout_2.addWidget(self.cbo_kegiatan, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(1015, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 10, 1, 1)

        self.radio_nilai_catatan_db = QRadioButton(self.widget)
        self.radio_nilai_catatan_db.setObjectName(u"radio_nilai_catatan_db")
        self.radio_nilai_catatan_db.setChecked(False)

        self.gridLayout_2.addWidget(self.radio_nilai_catatan_db, 0, 7, 1, 1)

        self.radio_catatan_db = QRadioButton(self.widget)
        self.radio_catatan_db.setObjectName(u"radio_catatan_db")

        self.gridLayout_2.addWidget(self.radio_catatan_db, 0, 5, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 6, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 0, 8, 1, 1)


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
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(40)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_template_nilai = QPushButton(self.widget_6)
        self.btn_template_nilai.setObjectName(u"btn_template_nilai")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_template_nilai.sizePolicy().hasHeightForWidth())
        self.btn_template_nilai.setSizePolicy(sizePolicy)
        self.btn_template_nilai.setMinimumSize(QSize(60, 24))

        self.gridLayout_7.addWidget(self.btn_template_nilai, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        self.label_4.setFont(font)

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_7.addWidget(self.label_5, 1, 0, 1, 1)

        self.btn_template_walas = QPushButton(self.widget_6)
        self.btn_template_walas.setObjectName(u"btn_template_walas")
        sizePolicy.setHeightForWidth(self.btn_template_walas.sizePolicy().hasHeightForWidth())
        self.btn_template_walas.setSizePolicy(sizePolicy)
        self.btn_template_walas.setMinimumSize(QSize(60, 24))

        self.gridLayout_7.addWidget(self.btn_template_walas, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_6, 2, 0, 1, 2)

        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_6 = QGridLayout(self.widget_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pte_default_path = QPlainTextEdit(self.widget_9)
        self.pte_default_path.setObjectName(u"pte_default_path")
        self.pte_default_path.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_6.addWidget(self.pte_default_path, 1, 0, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 2, 0, 1, 1)

        self.open_default_folder = QPushButton(self.widget_9)
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

        self.gridLayout_6.addWidget(self.open_default_folder, 0, 1, 1, 1, Qt.AlignRight)

        self.btn_new_default_path = QPushButton(self.widget_9)
        self.btn_new_default_path.setObjectName(u"btn_new_default_path")
        self.btn_new_default_path.setMinimumSize(QSize(60, 24))

        self.gridLayout_6.addWidget(self.btn_new_default_path, 2, 1, 1, 1)

        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_9, 1, 0, 1, 2)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_9 = QGridLayout(self.widget_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 2)

        self.btn_template_rekap = QPushButton(self.widget_8)
        self.btn_template_rekap.setObjectName(u"btn_template_rekap")
        sizePolicy.setHeightForWidth(self.btn_template_rekap.sizePolicy().hasHeightForWidth())
        self.btn_template_rekap.setSizePolicy(sizePolicy)
        self.btn_template_rekap.setMinimumSize(QSize(60, 24))

        self.gridLayout_9.addWidget(self.btn_template_rekap, 1, 1, 1, 1)

        self.line_rekap = QLineEdit(self.widget_8)
        self.line_rekap.setObjectName(u"line_rekap")
        self.line_rekap.setMinimumSize(QSize(0, 24))

        self.gridLayout_9.addWidget(self.line_rekap, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_8, 4, 0, 1, 2)

        self.gridLayout_3.setColumnStretch(0, 1)

        self.gridLayout_5.addWidget(self.widget_4, 0, 0, 2, 2)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pte_excel_path = QPlainTextEdit(self.widget_3)
        self.pte_excel_path.setObjectName(u"pte_excel_path")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pte_excel_path.sizePolicy().hasHeightForWidth())
        self.pte_excel_path.setSizePolicy(sizePolicy2)
        self.pte_excel_path.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_4.addWidget(self.pte_excel_path, 1, 0, 1, 4)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
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
        self.btn_clear.setMinimumSize(QSize(50, 0))
        self.btn_clear.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_4.addWidget(self.btn_clear, 0, 3, 1, 1, Qt.AlignRight)


        self.gridLayout_5.addWidget(self.widget_3, 3, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 4, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(379, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_10 = QGridLayout(self.widget_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_save = QPushButton(self.widget_5)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 50))

        self.gridLayout_10.addWidget(self.btn_save, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_5, 5, 0, 1, 2)


        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.radio_nilai_excel.setText(QCoreApplication.translate("Form", u"Rekap Nilai di File Excel", None))
        self.radio_nilai_db.setText(QCoreApplication.translate("Form", u"Rekap Nilai di Database", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.radio_nilai_catatan_db.setText(QCoreApplication.translate("Form", u"Rekap Nilai dan Catatan di Database", None))
        self.radio_catatan_db.setText(QCoreApplication.translate("Form", u"Rekap Catatan di Database", None))
        self.btn_template_nilai.setText(QCoreApplication.translate("Form", u"Create", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Template Blanko Nilai", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Template Blanko Catatan Wali Kelas", None))
        self.btn_template_walas.setText(QCoreApplication.translate("Form", u"Create", None))
        self.open_default_folder.setText("")
        self.btn_new_default_path.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Simpan di", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Template Blanko Catatan Wali Kelas", None))
        self.btn_template_rekap.setText(QCoreApplication.translate("Form", u"Create", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"INPUT DARI FILE REKAP NILAI", None))
        self.btn_open_file.setText(QCoreApplication.translate("Form", u"Open File", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.btn_clear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"INSERT", None))
    # retranslateUi

