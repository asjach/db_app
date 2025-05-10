# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_input_excel.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(815, 343)
        self.gridLayout_12 = QGridLayout(Form)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(15)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(400, 0))
        font = QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        font1 = QFont()
        font1.setBold(False)
        self.widget_3.setFont(font1)
        self.gridLayout_6 = QGridLayout(self.widget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.widget_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_6.addWidget(self.label_27, 0, 0, 1, 1)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)

        self.cbo_db = QComboBox(self.widget_3)
        self.cbo_db.setObjectName(u"cbo_db")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo_db.sizePolicy().hasHeightForWidth())
        self.cbo_db.setSizePolicy(sizePolicy)
        self.cbo_db.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.cbo_db, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 1, 3, 1, 1)

        self.cbo_table = QComboBox(self.widget_3)
        self.cbo_table.setObjectName(u"cbo_table")
        sizePolicy.setHeightForWidth(self.cbo_table.sizePolicy().hasHeightForWidth())
        self.cbo_table.setSizePolicy(sizePolicy)
        self.cbo_table.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.cbo_table, 1, 4, 1, 1)

        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)

        self.radio_filled = QRadioButton(self.widget_3)
        self.radio_filled.setObjectName(u"radio_filled")
        self.radio_filled.setChecked(True)

        self.gridLayout_6.addWidget(self.radio_filled, 0, 1, 1, 4)

        self.line_filename_nofilter = QLineEdit(self.widget_3)
        self.line_filename_nofilter.setObjectName(u"line_filename_nofilter")
        self.line_filename_nofilter.setMinimumSize(QSize(0, 24))

        self.gridLayout_6.addWidget(self.line_filename_nofilter, 2, 1, 1, 4)

        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnStretch(4, 1)
        self.gridLayout_6.setColumnMinimumWidth(0, 80)
        self.gridLayout_6.setColumnMinimumWidth(3, 80)

        self.gridLayout_4.addWidget(self.widget_3, 0, 0, 1, 2)

        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setFont(font1)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cbo_kelas = QComboBox(self.widget_2)
        self.cbo_kelas.setObjectName(u"cbo_kelas")
        sizePolicy.setHeightForWidth(self.cbo_kelas.sizePolicy().hasHeightForWidth())
        self.cbo_kelas.setSizePolicy(sizePolicy)
        self.cbo_kelas.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_kelas, 6, 1, 1, 1)

        self.cbo_tingkat = QComboBox(self.widget_2)
        self.cbo_tingkat.setObjectName(u"cbo_tingkat")
        sizePolicy.setHeightForWidth(self.cbo_tingkat.sizePolicy().hasHeightForWidth())
        self.cbo_tingkat.setSizePolicy(sizePolicy)
        self.cbo_tingkat.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_tingkat, 5, 1, 1, 1)

        self.cbo_jenjang = QComboBox(self.widget_2)
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.addItem("")
        self.cbo_jenjang.setObjectName(u"cbo_jenjang")
        sizePolicy.setHeightForWidth(self.cbo_jenjang.sizePolicy().hasHeightForWidth())
        self.cbo_jenjang.setSizePolicy(sizePolicy)
        self.cbo_jenjang.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_jenjang, 1, 1, 1, 1)

        self.cbo_semester = QComboBox(self.widget_2)
        self.cbo_semester.setObjectName(u"cbo_semester")
        sizePolicy.setHeightForWidth(self.cbo_semester.sizePolicy().hasHeightForWidth())
        self.cbo_semester.setSizePolicy(sizePolicy)
        self.cbo_semester.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_semester, 3, 1, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.cbo_kegiatan = QComboBox(self.widget_2)
        self.cbo_kegiatan.setObjectName(u"cbo_kegiatan")
        sizePolicy.setHeightForWidth(self.cbo_kegiatan.sizePolicy().hasHeightForWidth())
        self.cbo_kegiatan.setSizePolicy(sizePolicy)
        self.cbo_kegiatan.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_kegiatan, 3, 4, 1, 1)

        self.cbo_tapel = QComboBox(self.widget_2)
        self.cbo_tapel.setObjectName(u"cbo_tapel")
        sizePolicy.setHeightForWidth(self.cbo_tapel.sizePolicy().hasHeightForWidth())
        self.cbo_tapel.setSizePolicy(sizePolicy)
        self.cbo_tapel.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_tapel, 1, 4, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 5, 3, 1, 1)

        self.cbo_status = QComboBox(self.widget_2)
        self.cbo_status.setObjectName(u"cbo_status")
        sizePolicy.setHeightForWidth(self.cbo_status.sizePolicy().hasHeightForWidth())
        self.cbo_status.setSizePolicy(sizePolicy)
        self.cbo_status.setMinimumSize(QSize(0, 24))

        self.gridLayout.addWidget(self.cbo_status, 5, 4, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnMinimumWidth(0, 80)
        self.gridLayout.setColumnMinimumWidth(3, 80)

        self.gridLayout_4.addWidget(self.widget_2, 3, 0, 1, 2)

        self.widget_5 = QWidget(self.groupBox)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_8 = QGridLayout(self.widget_5)
        self.gridLayout_8.setSpacing(3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_with__filter = QPushButton(self.widget_5)
        self.btn_with__filter.setObjectName(u"btn_with__filter")
        self.btn_with__filter.setMinimumSize(QSize(0, 40))
        self.btn_with__filter.setAutoDefault(False)

        self.gridLayout_8.addWidget(self.btn_with__filter, 0, 1, 1, 1)

        self.btn_no_filter = QPushButton(self.widget_5)
        self.btn_no_filter.setObjectName(u"btn_no_filter")
        self.btn_no_filter.setMinimumSize(QSize(0, 40))
        self.btn_no_filter.setFont(font)
        self.btn_no_filter.setAutoDefault(False)

        self.gridLayout_8.addWidget(self.btn_no_filter, 0, 0, 1, 1)

        self.progress_filter = QProgressBar(self.widget_5)
        self.progress_filter.setObjectName(u"progress_filter")
        self.progress_filter.setMinimumSize(QSize(0, 10))
        self.progress_filter.setMaximumSize(QSize(16777215, 10))
        self.progress_filter.setValue(0)
        self.progress_filter.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progress_filter.setTextVisible(False)

        self.gridLayout_8.addWidget(self.progress_filter, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.widget_5, 5, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(400, 0))
        self.groupBox_3.setFont(font)
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.cbo_sheet = QComboBox(self.groupBox_3)
        self.cbo_sheet.setObjectName(u"cbo_sheet")
        self.cbo_sheet.setMinimumSize(QSize(0, 24))
        self.cbo_sheet.setFont(font1)

        self.gridLayout_7.addWidget(self.cbo_sheet, 4, 1, 1, 1)

        self.cbo_save_to_db = QComboBox(self.groupBox_3)
        self.cbo_save_to_db.setObjectName(u"cbo_save_to_db")
        self.cbo_save_to_db.setMinimumSize(QSize(0, 24))

        self.gridLayout_7.addWidget(self.cbo_save_to_db, 6, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 6, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_7.addWidget(self.label_12, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_7.addWidget(self.label_13, 5, 0, 1, 1)

        self.widget_8 = QWidget(self.groupBox_3)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_5 = QGridLayout(self.widget_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.line_source = QLineEdit(self.widget_8)
        self.line_source.setObjectName(u"line_source")
        self.line_source.setMinimumSize(QSize(0, 24))
        self.line_source.setFont(font1)

        self.gridLayout_5.addWidget(self.line_source, 0, 0, 1, 1)

        self.btn_browse = QPushButton(self.widget_8)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMinimumSize(QSize(0, 24))
        self.btn_browse.setFont(font1)
        self.btn_browse.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.btn_browse, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.widget_8, 0, 0, 1, 2)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_7.addWidget(self.label_10, 2, 0, 1, 1)

        self.line_namafile = QLineEdit(self.groupBox_3)
        self.line_namafile.setObjectName(u"line_namafile")
        self.line_namafile.setMinimumSize(QSize(0, 24))
        self.line_namafile.setFont(font1)

        self.gridLayout_7.addWidget(self.line_namafile, 2, 1, 1, 1)

        self.widget = QWidget(self.groupBox_3)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.insert_btn = QPushButton(self.widget)
        self.insert_btn.setObjectName(u"insert_btn")
        self.insert_btn.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        self.insert_btn.setFont(font2)
        self.insert_btn.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.insert_btn, 0, 0, 1, 1)

        self.insert_btn_2 = QPushButton(self.widget)
        self.insert_btn_2.setObjectName(u"insert_btn_2")
        self.insert_btn_2.setMinimumSize(QSize(0, 40))
        self.insert_btn_2.setFont(font2)
        self.insert_btn_2.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.insert_btn_2, 0, 1, 1, 1)

        self.progress_save = QProgressBar(self.widget)
        self.progress_save.setObjectName(u"progress_save")
        self.progress_save.setMinimumSize(QSize(0, 10))
        self.progress_save.setMaximumSize(QSize(16777215, 10))
        self.progress_save.setValue(0)
        self.progress_save.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progress_save.setTextVisible(False)

        self.gridLayout_3.addWidget(self.progress_save, 1, 0, 1, 2)


        self.gridLayout_7.addWidget(self.widget, 8, 0, 1, 2)

        self.cbo_key = QComboBox(self.groupBox_3)
        self.cbo_key.setObjectName(u"cbo_key")
        self.cbo_key.setMinimumSize(QSize(0, 24))
        self.cbo_key.setFont(font1)

        self.gridLayout_7.addWidget(self.cbo_key, 5, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 3, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_3, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"TEMPLATE", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Data", None))
        self.label.setText(QCoreApplication.translate("Form", u"Database", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nama Tabel", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Nama Template", None))
        self.radio_filled.setText(QCoreApplication.translate("Form", u"Isi Data", None))
        self.cbo_jenjang.setItemText(0, "")
        self.cbo_jenjang.setItemText(1, QCoreApplication.translate("Form", u"MI", None))
        self.cbo_jenjang.setItemText(2, QCoreApplication.translate("Form", u"MD", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Jenjang", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Tingkat", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"FILTER", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Kegiatan", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Semester", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Tapel", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Kelas", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Status", None))
        self.btn_with__filter.setText(QCoreApplication.translate("Form", u"Template dengan Filter", None))
        self.btn_no_filter.setText(QCoreApplication.translate("Form", u"Template tanpa filter", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"INSERT/UPDATE", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Pilih Database", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Sheet", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Kolom Kunci", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Nama File", None))
        self.insert_btn.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.insert_btn_2.setText(QCoreApplication.translate("Form", u"Update", None))
    # retranslateUi

