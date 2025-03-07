# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_input_excel.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPlainTextEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSplitter, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(962, 777)
        self.gridLayout_7 = QGridLayout(Form)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget_4 = QWidget(self.splitter)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.plainTextEdit = QPlainTextEdit(self.widget_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.widget_4)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.gridLayout_2.addWidget(self.plainTextEdit_2, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowMinimumHeight(0, 200)
        self.splitter.addWidget(self.widget_4)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(400, 0))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(15)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.widget_5 = QWidget(self.groupBox)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_8 = QGridLayout(self.widget_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.btn_with__filter = QPushButton(self.widget_5)
        self.btn_with__filter.setObjectName(u"btn_with__filter")
        self.btn_with__filter.setMinimumSize(QSize(0, 40))

        self.gridLayout_8.addWidget(self.btn_with__filter, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_5, 4, 0, 1, 2)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        font1 = QFont()
        font1.setBold(False)
        self.widget_3.setFont(font1)
        self.gridLayout_6 = QGridLayout(self.widget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 2, 0, 1, 1)

        self.radio_filled = QRadioButton(self.widget_3)
        self.radio_filled.setObjectName(u"radio_filled")
        self.radio_filled.setChecked(True)

        self.gridLayout_6.addWidget(self.radio_filled, 1, 0, 1, 1)

        self.cbo_db = QComboBox(self.widget_3)
        self.cbo_db.setObjectName(u"cbo_db")
        self.cbo_db.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.cbo_db, 3, 0, 1, 1)

        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 4, 0, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 2, 1, 1, 1)

        self.cbo_table = QComboBox(self.widget_3)
        self.cbo_table.setObjectName(u"cbo_table")
        self.cbo_table.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.cbo_table, 3, 1, 1, 1)

        self.line_filename_nofilter = QLineEdit(self.widget_3)
        self.line_filename_nofilter.setObjectName(u"line_filename_nofilter")
        self.line_filename_nofilter.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.line_filename_nofilter, 5, 0, 1, 2)

        self.btn_no_filter = QPushButton(self.widget_3)
        self.btn_no_filter.setObjectName(u"btn_no_filter")
        self.btn_no_filter.setMinimumSize(QSize(0, 40))
        self.btn_no_filter.setFont(font)

        self.gridLayout_6.addWidget(self.btn_no_filter, 6, 0, 1, 2)


        self.gridLayout_4.addWidget(self.widget_3, 0, 0, 1, 2)

        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setFont(font1)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.cbo_jenjang = QComboBox(self.widget_2)
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.setObjectName(u"cbo_jenjang")
        self.cbo_jenjang.setMinimumSize(QSize(0, 24))
        self.cbo_jenjang.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.cbo_jenjang, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.cbo_kelas = QComboBox(self.widget_2)
        self.cbo_kelas.setObjectName(u"cbo_kelas")
        self.cbo_kelas.setMinimumSize(QSize(0, 24))
        self.cbo_kelas.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.cbo_kelas, 1, 3, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.cbo_tapel = QComboBox(self.widget_2)
        self.cbo_tapel.setObjectName(u"cbo_tapel")
        self.cbo_tapel.setMinimumSize(QSize(0, 24))
        self.cbo_tapel.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.cbo_tapel, 2, 1, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.cbo_tingkat = QComboBox(self.widget_2)
        self.cbo_tingkat.setObjectName(u"cbo_tingkat")
        self.cbo_tingkat.setMinimumSize(QSize(0, 24))
        self.cbo_tingkat.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.cbo_tingkat, 2, 3, 1, 1)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.cbo_semester = QComboBox(self.widget_2)
        self.cbo_semester.setObjectName(u"cbo_semester")
        self.cbo_semester.setMinimumSize(QSize(0, 24))
        self.cbo_semester.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.cbo_semester, 3, 1, 1, 1)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)

        self.cbo_status = QComboBox(self.widget_2)
        self.cbo_status.setObjectName(u"cbo_status")
        self.cbo_status.setMinimumSize(QSize(0, 24))
        self.cbo_status.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.cbo_status, 3, 3, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.cbo_kegiatan = QComboBox(self.widget_2)
        self.cbo_kegiatan.setObjectName(u"cbo_kegiatan")
        self.cbo_kegiatan.setMinimumSize(QSize(0, 24))
        self.cbo_kegiatan.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.cbo_kegiatan, 4, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnMinimumWidth(0, 60)
        self.gridLayout.setColumnMinimumWidth(2, 60)

        self.gridLayout_4.addWidget(self.widget_2, 3, 0, 1, 2)

        self.progress_filter = QProgressBar(self.groupBox)
        self.progress_filter.setObjectName(u"progress_filter")
        self.progress_filter.setMinimumSize(QSize(0, 10))
        self.progress_filter.setMaximumSize(QSize(16777215, 10))
        self.progress_filter.setValue(0)
        self.progress_filter.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progress_filter.setTextVisible(False)

        self.gridLayout_4.addWidget(self.progress_filter, 5, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_5.addWidget(self.label_13, 4, 0, 1, 1)

        self.line_namafile = QLineEdit(self.groupBox_2)
        self.line_namafile.setObjectName(u"line_namafile")
        self.line_namafile.setMinimumSize(QSize(0, 24))
        self.line_namafile.setFont(font1)

        self.gridLayout_5.addWidget(self.line_namafile, 2, 1, 1, 3)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_5.addWidget(self.label_12, 3, 0, 1, 1)

        self.cbo_sheet = QComboBox(self.groupBox_2)
        self.cbo_sheet.setObjectName(u"cbo_sheet")
        self.cbo_sheet.setMinimumSize(QSize(0, 24))
        self.cbo_sheet.setFont(font1)

        self.gridLayout_5.addWidget(self.cbo_sheet, 3, 1, 1, 3)

        self.cbo_key = QComboBox(self.groupBox_2)
        self.cbo_key.setObjectName(u"cbo_key")
        self.cbo_key.setMinimumSize(QSize(0, 24))
        self.cbo_key.setFont(font1)

        self.gridLayout_5.addWidget(self.cbo_key, 4, 1, 1, 3)

        self.btn_browse = QPushButton(self.groupBox_2)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMinimumSize(QSize(0, 24))
        self.btn_browse.setFont(font1)

        self.gridLayout_5.addWidget(self.btn_browse, 1, 3, 1, 1)

        self.line_source = QLineEdit(self.groupBox_2)
        self.line_source.setObjectName(u"line_source")
        self.line_source.setMinimumSize(QSize(0, 24))
        self.line_source.setFont(font1)

        self.gridLayout_5.addWidget(self.line_source, 1, 0, 1, 3)

        self.progress_load_excel = QProgressBar(self.groupBox_2)
        self.progress_load_excel.setObjectName(u"progress_load_excel")
        self.progress_load_excel.setMinimumSize(QSize(0, 10))
        self.progress_load_excel.setMaximumSize(QSize(16777215, 10))
        self.progress_load_excel.setValue(0)
        self.progress_load_excel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progress_load_excel.setTextVisible(False)

        self.gridLayout_5.addWidget(self.progress_load_excel, 6, 0, 1, 4)

        self.btn_cek_sql = QPushButton(self.groupBox_2)
        self.btn_cek_sql.setObjectName(u"btn_cek_sql")
        self.btn_cek_sql.setMinimumSize(QSize(0, 30))

        self.gridLayout_5.addWidget(self.btn_cek_sql, 5, 0, 1, 4)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 2)

        self.cbo_save_to_db = QComboBox(self.widget)
        self.cbo_save_to_db.setObjectName(u"cbo_save_to_db")
        self.cbo_save_to_db.setMinimumSize(QSize(0, 24))

        self.gridLayout_3.addWidget(self.cbo_save_to_db, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.progress_save = QProgressBar(self.widget)
        self.progress_save.setObjectName(u"progress_save")
        self.progress_save.setMinimumSize(QSize(0, 10))
        self.progress_save.setMaximumSize(QSize(16777215, 10))
        self.progress_save.setValue(0)
        self.progress_save.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progress_save.setTextVisible(False)

        self.gridLayout_3.addWidget(self.progress_save, 8, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 5, 0, 1, 1)

        self.insert_btn = QPushButton(self.widget)
        self.insert_btn.setObjectName(u"insert_btn")
        self.insert_btn.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        self.insert_btn.setFont(font2)

        self.gridLayout_3.addWidget(self.insert_btn, 7, 0, 1, 2)

        self.splitter.addWidget(self.widget)

        self.gridLayout_7.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"TEMPLATE", None))
        self.btn_with__filter.setText(QCoreApplication.translate("Form", u"Template dengan Filter", None))
        self.label.setText(QCoreApplication.translate("Form", u"Database", None))
        self.radio_filled.setText(QCoreApplication.translate("Form", u"Isi Data", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Nama Template", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Tabel", None))
        self.btn_no_filter.setText(QCoreApplication.translate("Form", u"Template tanpa filter", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"FILTER", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Jenjang", None))
        self.cbo_jenjang.setItemText(0, "")
        self.cbo_jenjang.setItemText(1, QCoreApplication.translate("Form", u"MI", None))
        self.cbo_jenjang.setItemText(2, QCoreApplication.translate("Form", u"MD", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Tapel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Tingkat", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Semester", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Status", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"INPUT/UPDATE DARI EXCEL", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Nama File", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Kolom Kunci", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Sheet", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.btn_cek_sql.setText(QCoreApplication.translate("Form", u"CEK SQL", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Pilih Database", None))
        self.insert_btn.setText(QCoreApplication.translate("Form", u"Insert", None))
    # retranslateUi

