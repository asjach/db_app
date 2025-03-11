# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_detail_siswa.ui'
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
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1232, 557)
        Form.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame_utama = QFrame(self.splitter)
        self.frame_utama.setObjectName(u"frame_utama")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_utama.sizePolicy().hasHeightForWidth())
        self.frame_utama.setSizePolicy(sizePolicy)
        self.frame_utama.setMinimumSize(QSize(650, 0))
        self.frame_utama.setFrameShape(QFrame.StyledPanel)
        self.frame_utama.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_utama)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_49 = QWidget(self.frame_utama)
        self.widget_49.setObjectName(u"widget_49")
        self.gridLayout_45 = QGridLayout(self.widget_49)
        self.gridLayout_45.setSpacing(2)
        self.gridLayout_45.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 2, 2, 2)
        self.label_145 = QLabel(self.widget_49)
        self.label_145.setObjectName(u"label_145")

        self.gridLayout_45.addWidget(self.label_145, 0, 0, 1, 1)

        self.cbo_search_by = QComboBox(self.widget_49)
        self.cbo_search_by.addItem("")
        self.cbo_search_by.addItem("")
        self.cbo_search_by.addItem("")
        self.cbo_search_by.addItem("")
        self.cbo_search_by.addItem("")
        self.cbo_search_by.setObjectName(u"cbo_search_by")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbo_search_by.sizePolicy().hasHeightForWidth())
        self.cbo_search_by.setSizePolicy(sizePolicy1)
        self.cbo_search_by.setMinimumSize(QSize(0, 24))
        self.cbo_search_by.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_45.addWidget(self.cbo_search_by, 0, 1, 1, 1)

        self.btn_sidebar = QPushButton(self.widget_49)
        self.btn_sidebar.setObjectName(u"btn_sidebar")
        self.btn_sidebar.setMinimumSize(QSize(30, 24))
        self.btn_sidebar.setMaximumSize(QSize(30, 25))

        self.gridLayout_45.addWidget(self.btn_sidebar, 0, 8, 1, 1)

        self.save_btn = QPushButton(self.widget_49)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(75, 24))
        self.save_btn.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_45.addWidget(self.save_btn, 1, 7, 1, 1)

        self.prev_btn = QPushButton(self.widget_49)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setMinimumSize(QSize(30, 24))
        self.prev_btn.setMaximumSize(QSize(30, 25))

        self.gridLayout_45.addWidget(self.prev_btn, 1, 5, 1, 1)

        self.copy_nama_lengkap = QPushButton(self.widget_49)
        self.copy_nama_lengkap.setObjectName(u"copy_nama_lengkap")
        self.copy_nama_lengkap.setMinimumSize(QSize(25, 25))
        self.copy_nama_lengkap.setMaximumSize(QSize(25, 25))
        self.copy_nama_lengkap.setStyleSheet(u"")
        self.copy_nama_lengkap.setFlat(False)

        self.gridLayout_45.addWidget(self.copy_nama_lengkap, 1, 4, 1, 1)

        self.label_131 = QLabel(self.widget_49)
        self.label_131.setObjectName(u"label_131")

        self.gridLayout_45.addWidget(self.label_131, 1, 0, 1, 1)

        self.next_btn = QPushButton(self.widget_49)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setMinimumSize(QSize(30, 24))
        self.next_btn.setMaximumSize(QSize(30, 25))

        self.gridLayout_45.addWidget(self.next_btn, 1, 8, 1, 1)

        self.line_search = QLineEdit(self.widget_49)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setMinimumSize(QSize(0, 24))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.line_search.setFont(font)

        self.gridLayout_45.addWidget(self.line_search, 0, 3, 1, 1)

        self.cbo_nama_lengkap = QComboBox(self.widget_49)
        self.cbo_nama_lengkap.setObjectName(u"cbo_nama_lengkap")
        sizePolicy1.setHeightForWidth(self.cbo_nama_lengkap.sizePolicy().hasHeightForWidth())
        self.cbo_nama_lengkap.setSizePolicy(sizePolicy1)
        self.cbo_nama_lengkap.setMinimumSize(QSize(0, 24))

        self.gridLayout_45.addWidget(self.cbo_nama_lengkap, 1, 1, 1, 3)


        self.gridLayout_2.addWidget(self.widget_49, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.frame_utama)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(500, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(10)
        self.tabWidget.setFont(font1)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tab_biodata = QWidget()
        self.tab_biodata.setObjectName(u"tab_biodata")
        self.tab_biodata.setMinimumSize(QSize(500, 0))
        self.gridLayout = QGridLayout(self.tab_biodata)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_edit = QWidget(self.tab_biodata)
        self.frame_edit.setObjectName(u"frame_edit")
        self.frame_edit.setMinimumSize(QSize(500, 0))
        self.gridLayout_29 = QGridLayout(self.frame_edit)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(2, 2, 2, 2)
        self.scrollArea = QScrollArea(self.frame_edit)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -1017, 619, 1629))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_datadiri = QWidget(self.scrollAreaWidgetContents)
        self.frame_datadiri.setObjectName(u"frame_datadiri")
        self.gridLayout_16 = QGridLayout(self.frame_datadiri)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_datadiri)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_2.setFont(font2)

        self.gridLayout_16.addWidget(self.label_2, 0, 0, 1, 1)

        self.frame_biodata = QWidget(self.frame_datadiri)
        self.frame_biodata.setObjectName(u"frame_biodata")
        self.gridLayout_37 = QGridLayout(self.frame_biodata)
        self.gridLayout_37.setSpacing(5)
        self.gridLayout_37.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setHorizontalSpacing(10)
        self.gridLayout_37.setVerticalSpacing(0)
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.frame_biodata)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_38 = QGridLayout(self.widget_19)
        self.gridLayout_38.setSpacing(5)
        self.gridLayout_38.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setHorizontalSpacing(10)
        self.gridLayout_38.setVerticalSpacing(0)
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        self.gridLayout_20 = QGridLayout(self.widget_20)
        self.gridLayout_20.setSpacing(5)
        self.gridLayout_20.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setHorizontalSpacing(0)
        self.gridLayout_20.setVerticalSpacing(5)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.nis_lokal_le = QLineEdit(self.widget_20)
        self.nis_lokal_le.setObjectName(u"nis_lokal_le")
        self.nis_lokal_le.setMinimumSize(QSize(150, 25))
        self.nis_lokal_le.setMaximumSize(QSize(16777215, 25))
        self.nis_lokal_le.setFont(font)
        self.nis_lokal_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.nis_lokal_le, 0, 2, 1, 1)

        self.label_94 = QLabel(self.widget_20)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout_20.addWidget(self.label_94, 0, 0, 1, 1)

        self.label_92 = QLabel(self.widget_20)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_20.addWidget(self.label_92, 1, 0, 1, 1)

        self.nisn_le = QLineEdit(self.widget_20)
        self.nisn_le.setObjectName(u"nisn_le")
        self.nisn_le.setMinimumSize(QSize(150, 25))
        self.nisn_le.setMaximumSize(QSize(16777215, 25))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.nisn_le.setFont(font3)
        self.nisn_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.nisn_le, 1, 2, 1, 1)

        self.label_nisn = QLabel(self.widget_20)
        self.label_nisn.setObjectName(u"label_nisn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_nisn.sizePolicy().hasHeightForWidth())
        self.label_nisn.setSizePolicy(sizePolicy2)
        self.label_nisn.setMinimumSize(QSize(20, 25))
        self.label_nisn.setMaximumSize(QSize(20, 25))

        self.gridLayout_20.addWidget(self.label_nisn, 1, 1, 1, 1)

        self.label_93 = QLabel(self.widget_20)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_20.addWidget(self.label_93, 2, 0, 1, 1)

        self.nik_le = QLineEdit(self.widget_20)
        self.nik_le.setObjectName(u"nik_le")
        self.nik_le.setMinimumSize(QSize(150, 25))
        self.nik_le.setMaximumSize(QSize(16777215, 25))
        self.nik_le.setFont(font)
        self.nik_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.nik_le, 2, 2, 1, 1)

        self.label_98 = QLabel(self.widget_20)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_20.addWidget(self.label_98, 3, 0, 1, 1)

        self.label_nik = QLabel(self.widget_20)
        self.label_nik.setObjectName(u"label_nik")
        sizePolicy2.setHeightForWidth(self.label_nik.sizePolicy().hasHeightForWidth())
        self.label_nik.setSizePolicy(sizePolicy2)
        self.label_nik.setMinimumSize(QSize(20, 25))

        self.gridLayout_20.addWidget(self.label_nik, 2, 1, 1, 1)

        self.jk_cbo = QComboBox(self.widget_20)
        self.jk_cbo.setObjectName(u"jk_cbo")
        self.jk_cbo.setMinimumSize(QSize(150, 25))
        self.jk_cbo.setMaximumSize(QSize(16777215, 25))
        self.jk_cbo.setFont(font)
        self.jk_cbo.setMouseTracking(False)
        self.jk_cbo.setFocusPolicy(Qt.TabFocus)
        self.jk_cbo.setEditable(True)

        self.gridLayout_20.addWidget(self.jk_cbo, 3, 2, 1, 1)

        self.tmp_lahir_le = QLineEdit(self.widget_20)
        self.tmp_lahir_le.setObjectName(u"tmp_lahir_le")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tmp_lahir_le.sizePolicy().hasHeightForWidth())
        self.tmp_lahir_le.setSizePolicy(sizePolicy3)
        self.tmp_lahir_le.setMinimumSize(QSize(150, 25))
        self.tmp_lahir_le.setMaximumSize(QSize(16777215, 25))
        self.tmp_lahir_le.setFont(font)
        self.tmp_lahir_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.tmp_lahir_le, 4, 2, 1, 1)

        self.label_96 = QLabel(self.widget_20)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_20.addWidget(self.label_96, 4, 0, 1, 1)

        self.label_97 = QLabel(self.widget_20)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_20.addWidget(self.label_97, 6, 0, 1, 1)

        self.tgl_lahir_le = QLineEdit(self.widget_20)
        self.tgl_lahir_le.setObjectName(u"tgl_lahir_le")
        sizePolicy3.setHeightForWidth(self.tgl_lahir_le.sizePolicy().hasHeightForWidth())
        self.tgl_lahir_le.setSizePolicy(sizePolicy3)
        self.tgl_lahir_le.setMinimumSize(QSize(150, 25))
        self.tgl_lahir_le.setMaximumSize(QSize(16777215, 25))
        self.tgl_lahir_le.setFont(font)
        self.tgl_lahir_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.tgl_lahir_le, 5, 2, 1, 1)

        self.label_95 = QLabel(self.widget_20)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_20.addWidget(self.label_95, 5, 0, 1, 1)

        self.label_99 = QLabel(self.widget_20)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout_20.addWidget(self.label_99, 7, 0, 1, 1)

        self.jumlah_saudara_le = QLineEdit(self.widget_20)
        self.jumlah_saudara_le.setObjectName(u"jumlah_saudara_le")
        self.jumlah_saudara_le.setMinimumSize(QSize(150, 25))
        self.jumlah_saudara_le.setMaximumSize(QSize(16777215, 25))
        self.jumlah_saudara_le.setFont(font)
        self.jumlah_saudara_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.jumlah_saudara_le, 7, 2, 1, 1)

        self.anak_ke_le = QLineEdit(self.widget_20)
        self.anak_ke_le.setObjectName(u"anak_ke_le")
        self.anak_ke_le.setMinimumSize(QSize(150, 25))
        self.anak_ke_le.setMaximumSize(QSize(16777215, 25))
        self.anak_ke_le.setFont(font)
        self.anak_ke_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.anak_ke_le, 6, 2, 1, 1)

        self.copy_nis_lokal = QPushButton(self.widget_20)
        self.copy_nis_lokal.setObjectName(u"copy_nis_lokal")
        self.copy_nis_lokal.setMinimumSize(QSize(25, 25))
        self.copy_nis_lokal.setMaximumSize(QSize(25, 25))
        self.copy_nis_lokal.setFlat(False)

        self.gridLayout_20.addWidget(self.copy_nis_lokal, 0, 3, 1, 1)

        self.copy_nisn = QPushButton(self.widget_20)
        self.copy_nisn.setObjectName(u"copy_nisn")
        self.copy_nisn.setMinimumSize(QSize(25, 25))
        self.copy_nisn.setMaximumSize(QSize(25, 25))
        self.copy_nisn.setFlat(False)

        self.gridLayout_20.addWidget(self.copy_nisn, 1, 3, 1, 1)

        self.copy_nik = QPushButton(self.widget_20)
        self.copy_nik.setObjectName(u"copy_nik")
        self.copy_nik.setMinimumSize(QSize(25, 25))
        self.copy_nik.setMaximumSize(QSize(25, 25))
        self.copy_nik.setFlat(False)

        self.gridLayout_20.addWidget(self.copy_nik, 2, 3, 1, 1)

        self.copy_tmp = QPushButton(self.widget_20)
        self.copy_tmp.setObjectName(u"copy_tmp")
        self.copy_tmp.setMinimumSize(QSize(25, 25))
        self.copy_tmp.setMaximumSize(QSize(25, 25))
        self.copy_tmp.setFlat(False)

        self.gridLayout_20.addWidget(self.copy_tmp, 4, 3, 1, 1)

        self.copy_anak_ke = QPushButton(self.widget_20)
        self.copy_anak_ke.setObjectName(u"copy_anak_ke")
        self.copy_anak_ke.setMinimumSize(QSize(25, 25))
        self.copy_anak_ke.setMaximumSize(QSize(25, 25))
        self.copy_anak_ke.setFlat(False)

        self.gridLayout_20.addWidget(self.copy_anak_ke, 6, 3, 1, 1)

        self.copy_saudara = QPushButton(self.widget_20)
        self.copy_saudara.setObjectName(u"copy_saudara")
        self.copy_saudara.setMinimumSize(QSize(25, 25))
        self.copy_saudara.setMaximumSize(QSize(25, 25))
        self.copy_saudara.setFlat(False)

        self.gridLayout_20.addWidget(self.copy_saudara, 7, 3, 1, 1)

        self.gridLayout_20.setColumnMinimumWidth(0, 80)

        self.gridLayout_38.addWidget(self.widget_20, 0, 0, 1, 1)

        self.widget_28 = QWidget(self.widget_19)
        self.widget_28.setObjectName(u"widget_28")
        self.gridLayout_21 = QGridLayout(self.widget_28)
        self.gridLayout_21.setSpacing(5)
        self.gridLayout_21.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setHorizontalSpacing(0)
        self.gridLayout_21.setVerticalSpacing(5)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_101 = QLabel(self.widget_28)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_21.addWidget(self.label_101, 1, 0, 1, 1)

        self.label_100 = QLabel(self.widget_28)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_21.addWidget(self.label_100, 0, 0, 1, 1)

        self.nis_kemenag_le = QLineEdit(self.widget_28)
        self.nis_kemenag_le.setObjectName(u"nis_kemenag_le")
        self.nis_kemenag_le.setMinimumSize(QSize(150, 25))
        self.nis_kemenag_le.setMaximumSize(QSize(16777215, 25))
        self.nis_kemenag_le.setFont(font3)
        self.nis_kemenag_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.nis_kemenag_le, 0, 2, 1, 1)

        self.cita_cita_cbo = QComboBox(self.widget_28)
        self.cita_cita_cbo.setObjectName(u"cita_cita_cbo")
        self.cita_cita_cbo.setMinimumSize(QSize(150, 25))
        self.cita_cita_cbo.setMaximumSize(QSize(16777215, 25))
        self.cita_cita_cbo.setFont(font)
        self.cita_cita_cbo.setMouseTracking(False)
        self.cita_cita_cbo.setFocusPolicy(Qt.TabFocus)
        self.cita_cita_cbo.setEditable(True)

        self.gridLayout_21.addWidget(self.cita_cita_cbo, 1, 2, 1, 1)

        self.label_103 = QLabel(self.widget_28)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_21.addWidget(self.label_103, 2, 0, 1, 1)

        self.hobi_cbo = QComboBox(self.widget_28)
        self.hobi_cbo.setObjectName(u"hobi_cbo")
        self.hobi_cbo.setMinimumSize(QSize(150, 25))
        self.hobi_cbo.setMaximumSize(QSize(16777215, 25))
        self.hobi_cbo.setFont(font)
        self.hobi_cbo.setMouseTracking(False)
        self.hobi_cbo.setFocusPolicy(Qt.TabFocus)
        self.hobi_cbo.setEditable(True)

        self.gridLayout_21.addWidget(self.hobi_cbo, 2, 2, 1, 1)

        self.label_104 = QLabel(self.widget_28)
        self.label_104.setObjectName(u"label_104")

        self.gridLayout_21.addWidget(self.label_104, 3, 0, 1, 1)

        self.agama_cbo = QComboBox(self.widget_28)
        self.agama_cbo.setObjectName(u"agama_cbo")
        self.agama_cbo.setMinimumSize(QSize(150, 25))
        self.agama_cbo.setMaximumSize(QSize(16777215, 25))
        self.agama_cbo.setFont(font)
        self.agama_cbo.setMouseTracking(False)
        self.agama_cbo.setFocusPolicy(Qt.TabFocus)
        self.agama_cbo.setEditable(True)

        self.gridLayout_21.addWidget(self.agama_cbo, 3, 2, 1, 1)

        self.label_181 = QLabel(self.widget_28)
        self.label_181.setObjectName(u"label_181")

        self.gridLayout_21.addWidget(self.label_181, 4, 0, 1, 1)

        self.keb_khusus_cbo = QComboBox(self.widget_28)
        self.keb_khusus_cbo.setObjectName(u"keb_khusus_cbo")
        self.keb_khusus_cbo.setMinimumSize(QSize(150, 25))
        self.keb_khusus_cbo.setMaximumSize(QSize(16777215, 25))
        self.keb_khusus_cbo.setFont(font)
        self.keb_khusus_cbo.setMouseTracking(False)
        self.keb_khusus_cbo.setFocusPolicy(Qt.TabFocus)
        self.keb_khusus_cbo.setEditable(True)

        self.gridLayout_21.addWidget(self.keb_khusus_cbo, 4, 2, 1, 1)

        self.label_105 = QLabel(self.widget_28)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_21.addWidget(self.label_105, 5, 0, 1, 1)

        self.label_183 = QLabel(self.widget_28)
        self.label_183.setObjectName(u"label_183")

        self.gridLayout_21.addWidget(self.label_183, 6, 0, 1, 1)

        self.no_kip_le = QLineEdit(self.widget_28)
        self.no_kip_le.setObjectName(u"no_kip_le")
        self.no_kip_le.setMinimumSize(QSize(150, 25))
        self.no_kip_le.setMaximumSize(QSize(16777215, 25))
        self.no_kip_le.setFont(font)
        self.no_kip_le.setFrame(True)
        self.no_kip_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.no_kip_le, 6, 2, 1, 1)

        self.pembiayaan_cbo = QComboBox(self.widget_28)
        self.pembiayaan_cbo.setObjectName(u"pembiayaan_cbo")
        self.pembiayaan_cbo.setMinimumSize(QSize(150, 25))
        self.pembiayaan_cbo.setMaximumSize(QSize(16777215, 25))
        self.pembiayaan_cbo.setFont(font)
        self.pembiayaan_cbo.setMouseTracking(False)
        self.pembiayaan_cbo.setFocusPolicy(Qt.TabFocus)
        self.pembiayaan_cbo.setEditable(True)

        self.gridLayout_21.addWidget(self.pembiayaan_cbo, 5, 2, 1, 1)

        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMinimumSize(QSize(0, 25))
        self.widget_29.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_21.addWidget(self.widget_29, 7, 2, 1, 1)

        self.widget_15 = QWidget(self.widget_28)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(20, 0))

        self.gridLayout_21.addWidget(self.widget_15, 7, 1, 1, 1)

        self.copy_nis_kemenag = QPushButton(self.widget_28)
        self.copy_nis_kemenag.setObjectName(u"copy_nis_kemenag")
        self.copy_nis_kemenag.setMinimumSize(QSize(25, 25))
        self.copy_nis_kemenag.setMaximumSize(QSize(25, 25))
        self.copy_nis_kemenag.setFlat(False)

        self.gridLayout_21.addWidget(self.copy_nis_kemenag, 0, 3, 1, 1)

        self.btn_nis_kemenag = QPushButton(self.widget_28)
        self.btn_nis_kemenag.setObjectName(u"btn_nis_kemenag")
        self.btn_nis_kemenag.setMinimumSize(QSize(22, 25))
        self.btn_nis_kemenag.setMaximumSize(QSize(20, 25))
        self.btn_nis_kemenag.setStyleSheet(u"")
        self.btn_nis_kemenag.setFlat(True)

        self.gridLayout_21.addWidget(self.btn_nis_kemenag, 0, 1, 1, 1)

        self.gridLayout_21.setColumnMinimumWidth(0, 80)

        self.gridLayout_38.addWidget(self.widget_28, 0, 1, 1, 1)

        self.gridLayout_38.setColumnStretch(0, 1)
        self.gridLayout_38.setColumnStretch(1, 1)

        self.gridLayout_37.addWidget(self.widget_19, 3, 0, 1, 2)

        self.widget_30 = QWidget(self.frame_biodata)
        self.widget_30.setObjectName(u"widget_30")
        self.gridLayout_47 = QGridLayout(self.widget_30)
        self.gridLayout_47.setSpacing(5)
        self.gridLayout_47.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setHorizontalSpacing(0)
        self.gridLayout_47.setVerticalSpacing(5)
        self.gridLayout_47.setContentsMargins(0, 0, 0, 5)
        self.label_128 = QLabel(self.widget_30)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMaximumSize(QSize(85, 16777215))

        self.gridLayout_47.addWidget(self.label_128, 1, 0, 1, 1)

        self.nama_singkat_le = QLineEdit(self.widget_30)
        self.nama_singkat_le.setObjectName(u"nama_singkat_le")
        self.nama_singkat_le.setMinimumSize(QSize(0, 25))
        self.nama_singkat_le.setFont(font)

        self.gridLayout_47.addWidget(self.nama_singkat_le, 1, 1, 1, 1)

        self.btn_singkat_nama = QPushButton(self.widget_30)
        self.btn_singkat_nama.setObjectName(u"btn_singkat_nama")
        self.btn_singkat_nama.setMinimumSize(QSize(22, 25))
        self.btn_singkat_nama.setMaximumSize(QSize(20, 25))
        self.btn_singkat_nama.setStyleSheet(u"")
        self.btn_singkat_nama.setFlat(False)

        self.gridLayout_47.addWidget(self.btn_singkat_nama, 1, 2, 1, 1)

        self.label_129 = QLabel(self.widget_30)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMaximumSize(QSize(85, 16777215))

        self.gridLayout_47.addWidget(self.label_129, 0, 0, 1, 1)

        self.nama_lengkap_le = QLineEdit(self.widget_30)
        self.nama_lengkap_le.setObjectName(u"nama_lengkap_le")
        self.nama_lengkap_le.setMinimumSize(QSize(0, 25))
        self.nama_lengkap_le.setFont(font)

        self.gridLayout_47.addWidget(self.nama_lengkap_le, 0, 1, 1, 1)

        self.gridLayout_47.setColumnMinimumWidth(0, 100)

        self.gridLayout_37.addWidget(self.widget_30, 0, 0, 1, 2)

        self.gridLayout_37.setColumnStretch(0, 1)
        self.gridLayout_37.setColumnStretch(1, 1)

        self.gridLayout_16.addWidget(self.frame_biodata, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_datadiri)

        self.frame_alamat = QWidget(self.scrollAreaWidgetContents)
        self.frame_alamat.setObjectName(u"frame_alamat")
        self.gridLayout_22 = QGridLayout(self.frame_alamat)
        self.gridLayout_22.setSpacing(5)
        self.gridLayout_22.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(0)
        self.gridLayout_22.setVerticalSpacing(5)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.frame_alamat)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_6 = QGridLayout(self.widget_4)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_4)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_23 = QGridLayout(self.widget_16)
        self.gridLayout_23.setSpacing(5)
        self.gridLayout_23.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setHorizontalSpacing(0)
        self.gridLayout_23.setVerticalSpacing(5)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.alamat_cbo = QComboBox(self.widget_16)
        self.alamat_cbo.setObjectName(u"alamat_cbo")
        sizePolicy1.setHeightForWidth(self.alamat_cbo.sizePolicy().hasHeightForWidth())
        self.alamat_cbo.setSizePolicy(sizePolicy1)
        self.alamat_cbo.setMinimumSize(QSize(175, 25))
        self.alamat_cbo.setMaximumSize(QSize(175, 16777215))
        self.alamat_cbo.setFont(font3)
        self.alamat_cbo.setFocusPolicy(Qt.TabFocus)

        self.gridLayout_23.addWidget(self.alamat_cbo, 1, 1, 1, 1)

        self.label_130 = QLabel(self.widget_16)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(100, 0))
        font4 = QFont()
        font4.setItalic(True)
        self.label_130.setFont(font4)

        self.gridLayout_23.addWidget(self.label_130, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.gridLayout_6.addWidget(self.widget_16, 1, 1, 1, 1)

        self.widget_12 = QWidget(self.widget_4)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_17 = QGridLayout(self.widget_12)
        self.gridLayout_17.setSpacing(5)
        self.gridLayout_17.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(10)
        self.gridLayout_17.setVerticalSpacing(0)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_18 = QGridLayout(self.widget_13)
        self.gridLayout_18.setSpacing(5)
        self.gridLayout_18.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(0)
        self.gridLayout_18.setVerticalSpacing(5)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_138 = QLabel(self.widget_13)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setFont(font4)

        self.gridLayout_18.addWidget(self.label_138, 2, 0, 1, 1)

        self.provinsi_le = QLineEdit(self.widget_13)
        self.provinsi_le.setObjectName(u"provinsi_le")
        self.provinsi_le.setMinimumSize(QSize(0, 25))
        self.provinsi_le.setFont(font)
        self.provinsi_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.provinsi_le, 2, 1, 1, 1)

        self.label_139 = QLabel(self.widget_13)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setFont(font4)

        self.gridLayout_18.addWidget(self.label_139, 3, 0, 1, 1)

        self.label_143 = QLabel(self.widget_13)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setFont(font4)

        self.gridLayout_18.addWidget(self.label_143, 4, 0, 1, 1)

        self.label_144 = QLabel(self.widget_13)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setFont(font4)

        self.gridLayout_18.addWidget(self.label_144, 5, 0, 1, 1)

        self.jalan_le = QLineEdit(self.widget_13)
        self.jalan_le.setObjectName(u"jalan_le")
        self.jalan_le.setMinimumSize(QSize(0, 25))
        self.jalan_le.setFont(font)
        self.jalan_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.jalan_le, 0, 1, 1, 1)

        self.kodepos_le = QLineEdit(self.widget_13)
        self.kodepos_le.setObjectName(u"kodepos_le")
        self.kodepos_le.setMinimumSize(QSize(0, 25))
        self.kodepos_le.setFont(font)
        self.kodepos_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_18.addWidget(self.kodepos_le, 3, 1, 1, 1)

        self.jarak_cbo = QComboBox(self.widget_13)
        self.jarak_cbo.setObjectName(u"jarak_cbo")
        self.jarak_cbo.setMinimumSize(QSize(0, 25))
        self.jarak_cbo.setFont(font)
        self.jarak_cbo.setFocusPolicy(Qt.TabFocus)
        self.jarak_cbo.setEditable(True)

        self.gridLayout_18.addWidget(self.jarak_cbo, 4, 1, 1, 1)

        self.transportasi_cbo = QComboBox(self.widget_13)
        self.transportasi_cbo.setObjectName(u"transportasi_cbo")
        self.transportasi_cbo.setMinimumSize(QSize(0, 25))
        self.transportasi_cbo.setFont(font)
        self.transportasi_cbo.setFocusPolicy(Qt.TabFocus)
        self.transportasi_cbo.setEditable(True)

        self.gridLayout_18.addWidget(self.transportasi_cbo, 5, 1, 1, 1)

        self.label_185 = QLabel(self.widget_13)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setFont(font4)

        self.gridLayout_18.addWidget(self.label_185, 0, 0, 1, 1)

        self.label_142 = QLabel(self.widget_13)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setFont(font4)

        self.gridLayout_18.addWidget(self.label_142, 6, 0, 1, 1)

        self.waktu_cbo = QComboBox(self.widget_13)
        self.waktu_cbo.setObjectName(u"waktu_cbo")
        self.waktu_cbo.setMinimumSize(QSize(0, 25))
        self.waktu_cbo.setFont(font)
        self.waktu_cbo.setFocusPolicy(Qt.TabFocus)
        self.waktu_cbo.setEditable(True)

        self.gridLayout_18.addWidget(self.waktu_cbo, 6, 1, 1, 1)

        self.copy_kodepos = QPushButton(self.widget_13)
        self.copy_kodepos.setObjectName(u"copy_kodepos")
        self.copy_kodepos.setMinimumSize(QSize(25, 25))
        self.copy_kodepos.setMaximumSize(QSize(25, 25))
        self.copy_kodepos.setFlat(False)

        self.gridLayout_18.addWidget(self.copy_kodepos, 3, 2, 1, 1)

        self.gridLayout_18.setColumnMinimumWidth(0, 100)

        self.gridLayout_17.addWidget(self.widget_13, 0, 1, 1, 1)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_19 = QGridLayout(self.widget_14)
        self.gridLayout_19.setSpacing(5)
        self.gridLayout_19.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(0)
        self.gridLayout_19.setVerticalSpacing(5)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.kab_kota_le = QLineEdit(self.widget_14)
        self.kab_kota_le.setObjectName(u"kab_kota_le")
        self.kab_kota_le.setMinimumSize(QSize(0, 25))
        self.kab_kota_le.setFont(font)
        self.kab_kota_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.kab_kota_le, 6, 1, 1, 1)

        self.label_135 = QLabel(self.widget_14)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setFont(font4)

        self.gridLayout_19.addWidget(self.label_135, 6, 0, 1, 1)

        self.label_132 = QLabel(self.widget_14)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setFont(font4)

        self.gridLayout_19.addWidget(self.label_132, 1, 0, 1, 1)

        self.label_133 = QLabel(self.widget_14)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font4)

        self.gridLayout_19.addWidget(self.label_133, 3, 0, 1, 1)

        self.label_134 = QLabel(self.widget_14)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setFont(font4)

        self.gridLayout_19.addWidget(self.label_134, 2, 0, 1, 1)

        self.rt_le = QLineEdit(self.widget_14)
        self.rt_le.setObjectName(u"rt_le")
        self.rt_le.setMinimumSize(QSize(0, 25))
        self.rt_le.setFont(font)
        self.rt_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.rt_le, 2, 1, 1, 1)

        self.kecamatan_le = QLineEdit(self.widget_14)
        self.kecamatan_le.setObjectName(u"kecamatan_le")
        self.kecamatan_le.setMinimumSize(QSize(0, 25))
        self.kecamatan_le.setFont(font)
        self.kecamatan_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.kecamatan_le, 5, 1, 1, 1)

        self.kel_desa_le = QLineEdit(self.widget_14)
        self.kel_desa_le.setObjectName(u"kel_desa_le")
        self.kel_desa_le.setMinimumSize(QSize(0, 25))
        self.kel_desa_le.setFont(font)
        self.kel_desa_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.kel_desa_le, 4, 1, 1, 1)

        self.label_136 = QLabel(self.widget_14)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setFont(font4)

        self.gridLayout_19.addWidget(self.label_136, 5, 0, 1, 1)

        self.rw_le = QLineEdit(self.widget_14)
        self.rw_le.setObjectName(u"rw_le")
        self.rw_le.setMinimumSize(QSize(0, 25))
        self.rw_le.setFont(font)
        self.rw_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.rw_le, 3, 1, 1, 1)

        self.kampung_le = QLineEdit(self.widget_14)
        self.kampung_le.setObjectName(u"kampung_le")
        self.kampung_le.setMinimumSize(QSize(0, 25))
        self.kampung_le.setFont(font)
        self.kampung_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.kampung_le, 1, 1, 1, 1)

        self.label_137 = QLabel(self.widget_14)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setFont(font4)

        self.gridLayout_19.addWidget(self.label_137, 4, 0, 1, 1)

        self.copy_kampung = QPushButton(self.widget_14)
        self.copy_kampung.setObjectName(u"copy_kampung")
        self.copy_kampung.setMinimumSize(QSize(25, 25))
        self.copy_kampung.setMaximumSize(QSize(25, 25))
        self.copy_kampung.setFlat(False)

        self.gridLayout_19.addWidget(self.copy_kampung, 1, 2, 1, 1)

        self.gridLayout_19.setColumnMinimumWidth(0, 100)

        self.gridLayout_17.addWidget(self.widget_14, 0, 0, 1, 1)

        self.gridLayout_17.setColumnStretch(0, 1)
        self.gridLayout_17.setColumnStretch(1, 1)

        self.gridLayout_6.addWidget(self.widget_12, 2, 0, 1, 2)

        self.widget_17 = QWidget(self.widget_4)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_24 = QGridLayout(self.widget_17)
        self.gridLayout_24.setSpacing(5)
        self.gridLayout_24.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(0)
        self.gridLayout_24.setVerticalSpacing(5)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_141 = QLabel(self.widget_17)
        self.label_141.setObjectName(u"label_141")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_141.sizePolicy().hasHeightForWidth())
        self.label_141.setSizePolicy(sizePolicy4)
        self.label_141.setFont(font4)

        self.gridLayout_24.addWidget(self.label_141, 1, 0, 1, 1, Qt.AlignTop)

        self.alamat_le = QLineEdit(self.widget_17)
        self.alamat_le.setObjectName(u"alamat_le")
        self.alamat_le.setMinimumSize(QSize(0, 25))
        self.alamat_le.setFont(font)
        self.alamat_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.alamat_le.setReadOnly(True)

        self.gridLayout_24.addWidget(self.alamat_le, 0, 1, 1, 1)

        self.label_140 = QLabel(self.widget_17)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setFont(font4)

        self.gridLayout_24.addWidget(self.label_140, 0, 0, 1, 1)

        self.alamat_full_pte = QPlainTextEdit(self.widget_17)
        self.alamat_full_pte.setObjectName(u"alamat_full_pte")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.alamat_full_pte.sizePolicy().hasHeightForWidth())
        self.alamat_full_pte.setSizePolicy(sizePolicy5)
        self.alamat_full_pte.setMinimumSize(QSize(0, 50))
        self.alamat_full_pte.setMaximumSize(QSize(16777215, 50))
        self.alamat_full_pte.setFont(font3)
        self.alamat_full_pte.setFocusPolicy(Qt.TabFocus)
        self.alamat_full_pte.setTabChangesFocus(True)
        self.alamat_full_pte.setReadOnly(True)

        self.gridLayout_24.addWidget(self.alamat_full_pte, 1, 1, 1, 1)

        self.copy_alamat = QPushButton(self.widget_17)
        self.copy_alamat.setObjectName(u"copy_alamat")
        self.copy_alamat.setMinimumSize(QSize(25, 25))
        self.copy_alamat.setMaximumSize(QSize(25, 25))
        self.copy_alamat.setFlat(False)

        self.gridLayout_24.addWidget(self.copy_alamat, 0, 2, 1, 1)

        self.copy_alamat_full = QPushButton(self.widget_17)
        self.copy_alamat_full.setObjectName(u"copy_alamat_full")
        self.copy_alamat_full.setMinimumSize(QSize(25, 25))
        self.copy_alamat_full.setMaximumSize(QSize(25, 25))
        self.copy_alamat_full.setFlat(False)

        self.gridLayout_24.addWidget(self.copy_alamat_full, 1, 2, 1, 1)

        self.gridLayout_24.setColumnMinimumWidth(0, 100)

        self.gridLayout_6.addWidget(self.widget_17, 3, 0, 1, 2)


        self.gridLayout_22.addWidget(self.widget_4, 1, 0, 1, 1)

        self.label = QLabel(self.frame_alamat)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 24))
        self.label.setFont(font2)

        self.gridLayout_22.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_alamat)

        self.frame_kk = QWidget(self.scrollAreaWidgetContents)
        self.frame_kk.setObjectName(u"frame_kk")
        self.gridLayout_33 = QGridLayout(self.frame_kk)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.widget_43 = QWidget(self.frame_kk)
        self.widget_43.setObjectName(u"widget_43")
        self.gridLayout_9 = QGridLayout(self.widget_43)
        self.gridLayout_9.setSpacing(5)
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(5)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_kepala_ibu = QPushButton(self.widget_43)
        self.btn_kepala_ibu.setObjectName(u"btn_kepala_ibu")
        self.btn_kepala_ibu.setMinimumSize(QSize(0, 25))
        self.btn_kepala_ibu.setMaximumSize(QSize(50, 16777215))
        self.btn_kepala_ibu.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.btn_kepala_ibu, 0, 2, 1, 1)

        self.kepala_kk_le = QLineEdit(self.widget_43)
        self.kepala_kk_le.setObjectName(u"kepala_kk_le")
        self.kepala_kk_le.setMinimumSize(QSize(0, 25))
        self.kepala_kk_le.setFont(font)

        self.gridLayout_9.addWidget(self.kepala_kk_le, 1, 0, 1, 3)

        self.label_187 = QLabel(self.widget_43)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setFont(font4)

        self.gridLayout_9.addWidget(self.label_187, 0, 6, 1, 1)

        self.nomor_kk_le = QLineEdit(self.widget_43)
        self.nomor_kk_le.setObjectName(u"nomor_kk_le")
        self.nomor_kk_le.setMinimumSize(QSize(160, 25))
        self.nomor_kk_le.setFont(font)

        self.gridLayout_9.addWidget(self.nomor_kk_le, 1, 3, 1, 3)

        self.label_146 = QLabel(self.widget_43)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setFont(font4)

        self.gridLayout_9.addWidget(self.label_146, 0, 0, 1, 1)

        self.label_189 = QLabel(self.widget_43)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setFont(font4)

        self.gridLayout_9.addWidget(self.label_189, 0, 3, 1, 1)

        self.label_no_kk = QLabel(self.widget_43)
        self.label_no_kk.setObjectName(u"label_no_kk")

        self.gridLayout_9.addWidget(self.label_no_kk, 0, 5, 1, 1)

        self.tgl_kk_le = QLineEdit(self.widget_43)
        self.tgl_kk_le.setObjectName(u"tgl_kk_le")
        self.tgl_kk_le.setMinimumSize(QSize(0, 25))
        self.tgl_kk_le.setFont(font)

        self.gridLayout_9.addWidget(self.tgl_kk_le, 1, 6, 1, 1)

        self.btn_kepala_ayah = QPushButton(self.widget_43)
        self.btn_kepala_ayah.setObjectName(u"btn_kepala_ayah")
        self.btn_kepala_ayah.setMinimumSize(QSize(0, 25))
        self.btn_kepala_ayah.setMaximumSize(QSize(50, 16777215))
        self.btn_kepala_ayah.setStyleSheet(u"image: none;")

        self.gridLayout_9.addWidget(self.btn_kepala_ayah, 0, 1, 1, 1)

        self.copy_no_kk = QPushButton(self.widget_43)
        self.copy_no_kk.setObjectName(u"copy_no_kk")
        self.copy_no_kk.setMinimumSize(QSize(25, 25))
        self.copy_no_kk.setMaximumSize(QSize(25, 25))
        self.copy_no_kk.setFlat(False)

        self.gridLayout_9.addWidget(self.copy_no_kk, 0, 4, 1, 1)

        self.gridLayout_9.setColumnStretch(0, 4)
        self.gridLayout_9.setColumnStretch(1, 1)
        self.gridLayout_9.setColumnStretch(2, 1)
        self.gridLayout_9.setColumnStretch(3, 2)

        self.gridLayout_33.addWidget(self.widget_43, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_kk)

        self.frame_ortu = QWidget(self.scrollAreaWidgetContents)
        self.frame_ortu.setObjectName(u"frame_ortu")
        self.gridLayout_3 = QGridLayout(self.frame_ortu)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_ortu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setFont(font2)

        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_ortu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))
        self.label_3.setFont(font2)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_ortu)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 2)

        self.widget_3 = QWidget(self.frame_ortu)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_10 = QGridLayout(self.widget_3)
        self.gridLayout_10.setSpacing(5)
        self.gridLayout_10.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(10)
        self.gridLayout_10.setVerticalSpacing(5)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_32 = QWidget(self.widget_3)
        self.widget_32.setObjectName(u"widget_32")
        self.gridLayout_7 = QGridLayout(self.widget_32)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(5)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_113 = QLabel(self.widget_32)
        self.label_113.setObjectName(u"label_113")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy6)
        self.label_113.setFont(font4)

        self.gridLayout_7.addWidget(self.label_113, 6, 0, 1, 1)

        self.ayah_nama_le = QLineEdit(self.widget_32)
        self.ayah_nama_le.setObjectName(u"ayah_nama_le")
        sizePolicy1.setHeightForWidth(self.ayah_nama_le.sizePolicy().hasHeightForWidth())
        self.ayah_nama_le.setSizePolicy(sizePolicy1)
        self.ayah_nama_le.setMinimumSize(QSize(0, 25))
        self.ayah_nama_le.setFont(font)
        self.ayah_nama_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.ayah_nama_le, 0, 2, 1, 1)

        self.label_121 = QLabel(self.widget_32)
        self.label_121.setObjectName(u"label_121")
        sizePolicy6.setHeightForWidth(self.label_121.sizePolicy().hasHeightForWidth())
        self.label_121.setSizePolicy(sizePolicy6)
        self.label_121.setFont(font4)

        self.gridLayout_7.addWidget(self.label_121, 0, 0, 1, 1)

        self.label_107 = QLabel(self.widget_32)
        self.label_107.setObjectName(u"label_107")
        sizePolicy6.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy6)
        self.label_107.setFont(font4)

        self.gridLayout_7.addWidget(self.label_107, 1, 0, 1, 1)

        self.label_108 = QLabel(self.widget_32)
        self.label_108.setObjectName(u"label_108")
        sizePolicy6.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy6)
        self.label_108.setFont(font4)

        self.gridLayout_7.addWidget(self.label_108, 2, 0, 1, 1)

        self.label_nik_ayah = QLabel(self.widget_32)
        self.label_nik_ayah.setObjectName(u"label_nik_ayah")
        sizePolicy6.setHeightForWidth(self.label_nik_ayah.sizePolicy().hasHeightForWidth())
        self.label_nik_ayah.setSizePolicy(sizePolicy6)
        self.label_nik_ayah.setMinimumSize(QSize(20, 0))

        self.gridLayout_7.addWidget(self.label_nik_ayah, 2, 1, 1, 1)

        self.ayah_status_cbo = QComboBox(self.widget_32)
        self.ayah_status_cbo.setObjectName(u"ayah_status_cbo")
        sizePolicy1.setHeightForWidth(self.ayah_status_cbo.sizePolicy().hasHeightForWidth())
        self.ayah_status_cbo.setSizePolicy(sizePolicy1)
        self.ayah_status_cbo.setMinimumSize(QSize(0, 25))
        self.ayah_status_cbo.setFont(font)
        self.ayah_status_cbo.setFocusPolicy(Qt.TabFocus)
        self.ayah_status_cbo.setEditable(True)

        self.gridLayout_7.addWidget(self.ayah_status_cbo, 1, 2, 1, 1)

        self.ayah_tmp_lahir_le = QLineEdit(self.widget_32)
        self.ayah_tmp_lahir_le.setObjectName(u"ayah_tmp_lahir_le")
        sizePolicy1.setHeightForWidth(self.ayah_tmp_lahir_le.sizePolicy().hasHeightForWidth())
        self.ayah_tmp_lahir_le.setSizePolicy(sizePolicy1)
        self.ayah_tmp_lahir_le.setMinimumSize(QSize(0, 25))
        self.ayah_tmp_lahir_le.setFont(font)
        self.ayah_tmp_lahir_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.ayah_tmp_lahir_le, 3, 2, 1, 1)

        self.ayah_nik_le = QLineEdit(self.widget_32)
        self.ayah_nik_le.setObjectName(u"ayah_nik_le")
        sizePolicy1.setHeightForWidth(self.ayah_nik_le.sizePolicy().hasHeightForWidth())
        self.ayah_nik_le.setSizePolicy(sizePolicy1)
        self.ayah_nik_le.setMinimumSize(QSize(0, 25))
        self.ayah_nik_le.setFont(font)
        self.ayah_nik_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.ayah_nik_le, 2, 2, 1, 1)

        self.label_110 = QLabel(self.widget_32)
        self.label_110.setObjectName(u"label_110")
        sizePolicy6.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy6)
        self.label_110.setFont(font4)

        self.gridLayout_7.addWidget(self.label_110, 3, 0, 1, 1)

        self.ayah_tgl_lahir_le = QLineEdit(self.widget_32)
        self.ayah_tgl_lahir_le.setObjectName(u"ayah_tgl_lahir_le")
        sizePolicy1.setHeightForWidth(self.ayah_tgl_lahir_le.sizePolicy().hasHeightForWidth())
        self.ayah_tgl_lahir_le.setSizePolicy(sizePolicy1)
        self.ayah_tgl_lahir_le.setMinimumSize(QSize(0, 25))
        self.ayah_tgl_lahir_le.setFont(font)
        self.ayah_tgl_lahir_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.ayah_tgl_lahir_le, 4, 2, 1, 1)

        self.label_114 = QLabel(self.widget_32)
        self.label_114.setObjectName(u"label_114")
        sizePolicy6.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy6)
        self.label_114.setFont(font4)

        self.gridLayout_7.addWidget(self.label_114, 5, 0, 1, 1)

        self.label_112 = QLabel(self.widget_32)
        self.label_112.setObjectName(u"label_112")
        sizePolicy6.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy6)
        self.label_112.setFont(font4)

        self.gridLayout_7.addWidget(self.label_112, 4, 0, 1, 1)

        self.ayah_pendidikan_cbo = QComboBox(self.widget_32)
        self.ayah_pendidikan_cbo.setObjectName(u"ayah_pendidikan_cbo")
        sizePolicy1.setHeightForWidth(self.ayah_pendidikan_cbo.sizePolicy().hasHeightForWidth())
        self.ayah_pendidikan_cbo.setSizePolicy(sizePolicy1)
        self.ayah_pendidikan_cbo.setMinimumSize(QSize(0, 25))
        self.ayah_pendidikan_cbo.setFont(font)
        self.ayah_pendidikan_cbo.setFocusPolicy(Qt.TabFocus)
        self.ayah_pendidikan_cbo.setEditable(True)

        self.gridLayout_7.addWidget(self.ayah_pendidikan_cbo, 5, 2, 1, 1)

        self.ayah_pekerjaan_cbo = QComboBox(self.widget_32)
        self.ayah_pekerjaan_cbo.setObjectName(u"ayah_pekerjaan_cbo")
        sizePolicy1.setHeightForWidth(self.ayah_pekerjaan_cbo.sizePolicy().hasHeightForWidth())
        self.ayah_pekerjaan_cbo.setSizePolicy(sizePolicy1)
        self.ayah_pekerjaan_cbo.setMinimumSize(QSize(0, 25))
        self.ayah_pekerjaan_cbo.setFont(font)
        self.ayah_pekerjaan_cbo.setFocusPolicy(Qt.TabFocus)
        self.ayah_pekerjaan_cbo.setEditable(True)

        self.gridLayout_7.addWidget(self.ayah_pekerjaan_cbo, 6, 2, 1, 1)

        self.label_115 = QLabel(self.widget_32)
        self.label_115.setObjectName(u"label_115")
        sizePolicy6.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy6)
        self.label_115.setFont(font4)

        self.gridLayout_7.addWidget(self.label_115, 7, 0, 1, 1)

        self.ayah_telp_le = QLineEdit(self.widget_32)
        self.ayah_telp_le.setObjectName(u"ayah_telp_le")
        sizePolicy1.setHeightForWidth(self.ayah_telp_le.sizePolicy().hasHeightForWidth())
        self.ayah_telp_le.setSizePolicy(sizePolicy1)
        self.ayah_telp_le.setMinimumSize(QSize(0, 25))
        self.ayah_telp_le.setFont(font)
        self.ayah_telp_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.ayah_telp_le, 8, 2, 1, 1)

        self.ayah_penghasilan_cbo = QComboBox(self.widget_32)
        self.ayah_penghasilan_cbo.setObjectName(u"ayah_penghasilan_cbo")
        sizePolicy1.setHeightForWidth(self.ayah_penghasilan_cbo.sizePolicy().hasHeightForWidth())
        self.ayah_penghasilan_cbo.setSizePolicy(sizePolicy1)
        self.ayah_penghasilan_cbo.setMinimumSize(QSize(0, 25))
        self.ayah_penghasilan_cbo.setFont(font)
        self.ayah_penghasilan_cbo.setFocusPolicy(Qt.TabFocus)
        self.ayah_penghasilan_cbo.setEditable(True)

        self.gridLayout_7.addWidget(self.ayah_penghasilan_cbo, 7, 2, 1, 1)

        self.label_116 = QLabel(self.widget_32)
        self.label_116.setObjectName(u"label_116")
        sizePolicy6.setHeightForWidth(self.label_116.sizePolicy().hasHeightForWidth())
        self.label_116.setSizePolicy(sizePolicy6)
        self.label_116.setFont(font4)

        self.gridLayout_7.addWidget(self.label_116, 8, 0, 1, 1)

        self.copy_ayah = QPushButton(self.widget_32)
        self.copy_ayah.setObjectName(u"copy_ayah")
        self.copy_ayah.setMinimumSize(QSize(25, 25))
        self.copy_ayah.setMaximumSize(QSize(25, 25))
        self.copy_ayah.setFlat(False)

        self.gridLayout_7.addWidget(self.copy_ayah, 0, 3, 1, 1)

        self.copy_nik_ayah = QPushButton(self.widget_32)
        self.copy_nik_ayah.setObjectName(u"copy_nik_ayah")
        self.copy_nik_ayah.setMinimumSize(QSize(25, 25))
        self.copy_nik_ayah.setMaximumSize(QSize(25, 25))
        self.copy_nik_ayah.setFlat(False)

        self.gridLayout_7.addWidget(self.copy_nik_ayah, 2, 3, 1, 1)

        self.copy_tmp_ayah = QPushButton(self.widget_32)
        self.copy_tmp_ayah.setObjectName(u"copy_tmp_ayah")
        self.copy_tmp_ayah.setMinimumSize(QSize(25, 25))
        self.copy_tmp_ayah.setMaximumSize(QSize(25, 25))
        self.copy_tmp_ayah.setFlat(False)

        self.gridLayout_7.addWidget(self.copy_tmp_ayah, 3, 3, 1, 1)

        self.copy_telp_ayah = QPushButton(self.widget_32)
        self.copy_telp_ayah.setObjectName(u"copy_telp_ayah")
        self.copy_telp_ayah.setMinimumSize(QSize(25, 25))
        self.copy_telp_ayah.setMaximumSize(QSize(25, 25))
        self.copy_telp_ayah.setFlat(False)

        self.gridLayout_7.addWidget(self.copy_telp_ayah, 8, 3, 1, 1)

        self.copy_telp_ayah62 = QPushButton(self.widget_32)
        self.copy_telp_ayah62.setObjectName(u"copy_telp_ayah62")
        self.copy_telp_ayah62.setMinimumSize(QSize(25, 25))
        self.copy_telp_ayah62.setMaximumSize(QSize(25, 25))
        self.copy_telp_ayah62.setFlat(False)

        self.gridLayout_7.addWidget(self.copy_telp_ayah62, 9, 3, 1, 1)

        self.label_ayah62 = QLabel(self.widget_32)
        self.label_ayah62.setObjectName(u"label_ayah62")
        sizePolicy.setHeightForWidth(self.label_ayah62.sizePolicy().hasHeightForWidth())
        self.label_ayah62.setSizePolicy(sizePolicy)
        self.label_ayah62.setMinimumSize(QSize(0, 25))
        self.label_ayah62.setFont(font4)

        self.gridLayout_7.addWidget(self.label_ayah62, 9, 2, 1, 1)

        self.label_117 = QLabel(self.widget_32)
        self.label_117.setObjectName(u"label_117")
        sizePolicy6.setHeightForWidth(self.label_117.sizePolicy().hasHeightForWidth())
        self.label_117.setSizePolicy(sizePolicy6)
        self.label_117.setFont(font4)

        self.gridLayout_7.addWidget(self.label_117, 9, 0, 1, 1)


        self.gridLayout_10.addWidget(self.widget_32, 0, 0, 1, 1)

        self.widget_40 = QWidget(self.widget_3)
        self.widget_40.setObjectName(u"widget_40")
        self.gridLayout_25 = QGridLayout(self.widget_40)
        self.gridLayout_25.setSpacing(5)
        self.gridLayout_25.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(0)
        self.gridLayout_25.setVerticalSpacing(5)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_174 = QLabel(self.widget_40)
        self.label_174.setObjectName(u"label_174")
        sizePolicy6.setHeightForWidth(self.label_174.sizePolicy().hasHeightForWidth())
        self.label_174.setSizePolicy(sizePolicy6)
        self.label_174.setFont(font4)

        self.gridLayout_25.addWidget(self.label_174, 0, 0, 1, 1)

        self.ibu_nama_le = QLineEdit(self.widget_40)
        self.ibu_nama_le.setObjectName(u"ibu_nama_le")
        sizePolicy1.setHeightForWidth(self.ibu_nama_le.sizePolicy().hasHeightForWidth())
        self.ibu_nama_le.setSizePolicy(sizePolicy1)
        self.ibu_nama_le.setMinimumSize(QSize(0, 25))
        self.ibu_nama_le.setFont(font)
        self.ibu_nama_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.ibu_nama_le, 0, 2, 1, 1)

        self.label_172 = QLabel(self.widget_40)
        self.label_172.setObjectName(u"label_172")
        sizePolicy6.setHeightForWidth(self.label_172.sizePolicy().hasHeightForWidth())
        self.label_172.setSizePolicy(sizePolicy6)
        self.label_172.setFont(font4)

        self.gridLayout_25.addWidget(self.label_172, 1, 0, 1, 1)

        self.label_173 = QLabel(self.widget_40)
        self.label_173.setObjectName(u"label_173")
        sizePolicy6.setHeightForWidth(self.label_173.sizePolicy().hasHeightForWidth())
        self.label_173.setSizePolicy(sizePolicy6)
        self.label_173.setFont(font4)

        self.gridLayout_25.addWidget(self.label_173, 2, 0, 1, 1)

        self.ibu_status_cbo = QComboBox(self.widget_40)
        self.ibu_status_cbo.setObjectName(u"ibu_status_cbo")
        sizePolicy1.setHeightForWidth(self.ibu_status_cbo.sizePolicy().hasHeightForWidth())
        self.ibu_status_cbo.setSizePolicy(sizePolicy1)
        self.ibu_status_cbo.setMinimumSize(QSize(0, 25))
        self.ibu_status_cbo.setFont(font)
        self.ibu_status_cbo.setFocusPolicy(Qt.TabFocus)
        self.ibu_status_cbo.setEditable(True)

        self.gridLayout_25.addWidget(self.ibu_status_cbo, 1, 2, 1, 1)

        self.label_nik_ibu = QLabel(self.widget_40)
        self.label_nik_ibu.setObjectName(u"label_nik_ibu")
        sizePolicy6.setHeightForWidth(self.label_nik_ibu.sizePolicy().hasHeightForWidth())
        self.label_nik_ibu.setSizePolicy(sizePolicy6)
        self.label_nik_ibu.setMinimumSize(QSize(20, 0))

        self.gridLayout_25.addWidget(self.label_nik_ibu, 2, 1, 1, 1)

        self.ibu_nik_le = QLineEdit(self.widget_40)
        self.ibu_nik_le.setObjectName(u"ibu_nik_le")
        sizePolicy1.setHeightForWidth(self.ibu_nik_le.sizePolicy().hasHeightForWidth())
        self.ibu_nik_le.setSizePolicy(sizePolicy1)
        self.ibu_nik_le.setMinimumSize(QSize(0, 25))
        self.ibu_nik_le.setFont(font)
        self.ibu_nik_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.ibu_nik_le, 2, 2, 1, 1)

        self.label_170 = QLabel(self.widget_40)
        self.label_170.setObjectName(u"label_170")
        sizePolicy6.setHeightForWidth(self.label_170.sizePolicy().hasHeightForWidth())
        self.label_170.setSizePolicy(sizePolicy6)
        self.label_170.setFont(font4)

        self.gridLayout_25.addWidget(self.label_170, 3, 0, 1, 1)

        self.ibu_tmp_lahir_le = QLineEdit(self.widget_40)
        self.ibu_tmp_lahir_le.setObjectName(u"ibu_tmp_lahir_le")
        sizePolicy1.setHeightForWidth(self.ibu_tmp_lahir_le.sizePolicy().hasHeightForWidth())
        self.ibu_tmp_lahir_le.setSizePolicy(sizePolicy1)
        self.ibu_tmp_lahir_le.setMinimumSize(QSize(0, 25))
        self.ibu_tmp_lahir_le.setFont(font)
        self.ibu_tmp_lahir_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.ibu_tmp_lahir_le, 3, 2, 1, 1)

        self.label_171 = QLabel(self.widget_40)
        self.label_171.setObjectName(u"label_171")
        sizePolicy6.setHeightForWidth(self.label_171.sizePolicy().hasHeightForWidth())
        self.label_171.setSizePolicy(sizePolicy6)
        self.label_171.setFont(font4)

        self.gridLayout_25.addWidget(self.label_171, 4, 0, 1, 1)

        self.label_175 = QLabel(self.widget_40)
        self.label_175.setObjectName(u"label_175")
        sizePolicy6.setHeightForWidth(self.label_175.sizePolicy().hasHeightForWidth())
        self.label_175.setSizePolicy(sizePolicy6)
        self.label_175.setFont(font4)

        self.gridLayout_25.addWidget(self.label_175, 5, 0, 1, 1)

        self.ibu_tgl_lahir_le = QLineEdit(self.widget_40)
        self.ibu_tgl_lahir_le.setObjectName(u"ibu_tgl_lahir_le")
        sizePolicy1.setHeightForWidth(self.ibu_tgl_lahir_le.sizePolicy().hasHeightForWidth())
        self.ibu_tgl_lahir_le.setSizePolicy(sizePolicy1)
        self.ibu_tgl_lahir_le.setMinimumSize(QSize(0, 25))
        self.ibu_tgl_lahir_le.setFont(font)
        self.ibu_tgl_lahir_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.ibu_tgl_lahir_le, 4, 2, 1, 1)

        self.ibu_pendidikan_cbo = QComboBox(self.widget_40)
        self.ibu_pendidikan_cbo.setObjectName(u"ibu_pendidikan_cbo")
        sizePolicy1.setHeightForWidth(self.ibu_pendidikan_cbo.sizePolicy().hasHeightForWidth())
        self.ibu_pendidikan_cbo.setSizePolicy(sizePolicy1)
        self.ibu_pendidikan_cbo.setMinimumSize(QSize(0, 25))
        self.ibu_pendidikan_cbo.setFont(font)
        self.ibu_pendidikan_cbo.setFocusPolicy(Qt.TabFocus)
        self.ibu_pendidikan_cbo.setEditable(True)

        self.gridLayout_25.addWidget(self.ibu_pendidikan_cbo, 5, 2, 1, 1)

        self.label_176 = QLabel(self.widget_40)
        self.label_176.setObjectName(u"label_176")
        sizePolicy6.setHeightForWidth(self.label_176.sizePolicy().hasHeightForWidth())
        self.label_176.setSizePolicy(sizePolicy6)
        self.label_176.setFont(font4)

        self.gridLayout_25.addWidget(self.label_176, 6, 0, 1, 1)

        self.ibu_pekerjaan_cbo = QComboBox(self.widget_40)
        self.ibu_pekerjaan_cbo.setObjectName(u"ibu_pekerjaan_cbo")
        sizePolicy1.setHeightForWidth(self.ibu_pekerjaan_cbo.sizePolicy().hasHeightForWidth())
        self.ibu_pekerjaan_cbo.setSizePolicy(sizePolicy1)
        self.ibu_pekerjaan_cbo.setMinimumSize(QSize(0, 25))
        self.ibu_pekerjaan_cbo.setFont(font)
        self.ibu_pekerjaan_cbo.setFocusPolicy(Qt.TabFocus)
        self.ibu_pekerjaan_cbo.setEditable(True)

        self.gridLayout_25.addWidget(self.ibu_pekerjaan_cbo, 6, 2, 1, 1)

        self.label_168 = QLabel(self.widget_40)
        self.label_168.setObjectName(u"label_168")
        sizePolicy6.setHeightForWidth(self.label_168.sizePolicy().hasHeightForWidth())
        self.label_168.setSizePolicy(sizePolicy6)
        self.label_168.setFont(font4)

        self.gridLayout_25.addWidget(self.label_168, 7, 0, 1, 1)

        self.ibu_penghasilan_cbo = QComboBox(self.widget_40)
        self.ibu_penghasilan_cbo.setObjectName(u"ibu_penghasilan_cbo")
        sizePolicy1.setHeightForWidth(self.ibu_penghasilan_cbo.sizePolicy().hasHeightForWidth())
        self.ibu_penghasilan_cbo.setSizePolicy(sizePolicy1)
        self.ibu_penghasilan_cbo.setMinimumSize(QSize(0, 25))
        self.ibu_penghasilan_cbo.setFont(font)
        self.ibu_penghasilan_cbo.setFocusPolicy(Qt.TabFocus)
        self.ibu_penghasilan_cbo.setEditable(True)

        self.gridLayout_25.addWidget(self.ibu_penghasilan_cbo, 7, 2, 1, 1)

        self.ibu_telp_le = QLineEdit(self.widget_40)
        self.ibu_telp_le.setObjectName(u"ibu_telp_le")
        sizePolicy1.setHeightForWidth(self.ibu_telp_le.sizePolicy().hasHeightForWidth())
        self.ibu_telp_le.setSizePolicy(sizePolicy1)
        self.ibu_telp_le.setMinimumSize(QSize(0, 25))
        self.ibu_telp_le.setFont(font)
        self.ibu_telp_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.ibu_telp_le, 8, 2, 1, 1)

        self.label_169 = QLabel(self.widget_40)
        self.label_169.setObjectName(u"label_169")
        sizePolicy6.setHeightForWidth(self.label_169.sizePolicy().hasHeightForWidth())
        self.label_169.setSizePolicy(sizePolicy6)
        self.label_169.setFont(font4)

        self.gridLayout_25.addWidget(self.label_169, 8, 0, 1, 1)

        self.copy_ibu = QPushButton(self.widget_40)
        self.copy_ibu.setObjectName(u"copy_ibu")
        self.copy_ibu.setMinimumSize(QSize(25, 25))
        self.copy_ibu.setMaximumSize(QSize(25, 25))
        self.copy_ibu.setFlat(False)

        self.gridLayout_25.addWidget(self.copy_ibu, 0, 3, 1, 1)

        self.copy_tmp_ibu = QPushButton(self.widget_40)
        self.copy_tmp_ibu.setObjectName(u"copy_tmp_ibu")
        self.copy_tmp_ibu.setMinimumSize(QSize(25, 25))
        self.copy_tmp_ibu.setMaximumSize(QSize(25, 25))
        self.copy_tmp_ibu.setFlat(False)

        self.gridLayout_25.addWidget(self.copy_tmp_ibu, 3, 3, 1, 1)

        self.copy_nik_ibu = QPushButton(self.widget_40)
        self.copy_nik_ibu.setObjectName(u"copy_nik_ibu")
        self.copy_nik_ibu.setMinimumSize(QSize(25, 25))
        self.copy_nik_ibu.setMaximumSize(QSize(25, 25))
        self.copy_nik_ibu.setFlat(False)

        self.gridLayout_25.addWidget(self.copy_nik_ibu, 2, 3, 1, 1)

        self.label_119 = QLabel(self.widget_40)
        self.label_119.setObjectName(u"label_119")
        sizePolicy6.setHeightForWidth(self.label_119.sizePolicy().hasHeightForWidth())
        self.label_119.setSizePolicy(sizePolicy6)
        self.label_119.setFont(font4)

        self.gridLayout_25.addWidget(self.label_119, 9, 0, 1, 1)

        self.copy_telp_ibu62 = QPushButton(self.widget_40)
        self.copy_telp_ibu62.setObjectName(u"copy_telp_ibu62")
        self.copy_telp_ibu62.setMinimumSize(QSize(25, 25))
        self.copy_telp_ibu62.setMaximumSize(QSize(25, 25))
        self.copy_telp_ibu62.setFlat(False)

        self.gridLayout_25.addWidget(self.copy_telp_ibu62, 9, 3, 1, 1)

        self.label_ibu62 = QLabel(self.widget_40)
        self.label_ibu62.setObjectName(u"label_ibu62")
        sizePolicy.setHeightForWidth(self.label_ibu62.sizePolicy().hasHeightForWidth())
        self.label_ibu62.setSizePolicy(sizePolicy)
        self.label_ibu62.setMinimumSize(QSize(0, 25))
        self.label_ibu62.setFont(font4)

        self.gridLayout_25.addWidget(self.label_ibu62, 9, 2, 1, 1)

        self.copy_telp_ibu = QPushButton(self.widget_40)
        self.copy_telp_ibu.setObjectName(u"copy_telp_ibu")
        self.copy_telp_ibu.setMinimumSize(QSize(25, 25))
        self.copy_telp_ibu.setMaximumSize(QSize(25, 25))
        self.copy_telp_ibu.setFlat(False)

        self.gridLayout_25.addWidget(self.copy_telp_ibu, 8, 3, 1, 1)

        self.gridLayout_25.setColumnMinimumWidth(0, 80)

        self.gridLayout_10.addWidget(self.widget_40, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_3, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_ortu)

        self.frame_wali = QWidget(self.scrollAreaWidgetContents)
        self.frame_wali.setObjectName(u"frame_wali")
        self.gridLayout_34 = QGridLayout(self.frame_wali)
        self.gridLayout_34.setSpacing(5)
        self.gridLayout_34.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setHorizontalSpacing(10)
        self.gridLayout_34.setVerticalSpacing(0)
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.frame_wali)
        self.widget_18.setObjectName(u"widget_18")
        self.gridLayout_26 = QGridLayout(self.widget_18)
        self.gridLayout_26.setSpacing(5)
        self.gridLayout_26.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setHorizontalSpacing(0)
        self.gridLayout_26.setVerticalSpacing(5)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_154 = QLabel(self.widget_18)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setFont(font4)

        self.gridLayout_26.addWidget(self.label_154, 6, 0, 1, 1)

        self.wali_pendidikan_cbo = QComboBox(self.widget_18)
        self.wali_pendidikan_cbo.setObjectName(u"wali_pendidikan_cbo")
        self.wali_pendidikan_cbo.setMinimumSize(QSize(0, 25))
        self.wali_pendidikan_cbo.setFont(font)
        self.wali_pendidikan_cbo.setFocusPolicy(Qt.TabFocus)
        self.wali_pendidikan_cbo.setEditable(True)

        self.gridLayout_26.addWidget(self.wali_pendidikan_cbo, 5, 1, 1, 1)

        self.wali_nama_le = QLineEdit(self.widget_18)
        self.wali_nama_le.setObjectName(u"wali_nama_le")
        self.wali_nama_le.setMinimumSize(QSize(0, 25))
        self.wali_nama_le.setFont(font)
        self.wali_nama_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.wali_nama_le, 1, 1, 1, 1)

        self.label_153 = QLabel(self.widget_18)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setFont(font4)

        self.gridLayout_26.addWidget(self.label_153, 3, 0, 1, 1)

        self.wali_tmp_lahir_le = QLineEdit(self.widget_18)
        self.wali_tmp_lahir_le.setObjectName(u"wali_tmp_lahir_le")
        self.wali_tmp_lahir_le.setMinimumSize(QSize(0, 25))
        self.wali_tmp_lahir_le.setFont(font)
        self.wali_tmp_lahir_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.wali_tmp_lahir_le, 3, 1, 1, 1)

        self.label_155 = QLabel(self.widget_18)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setFont(font4)

        self.gridLayout_26.addWidget(self.label_155, 5, 0, 1, 1)

        self.wali_tgl_lahir_le = QLineEdit(self.widget_18)
        self.wali_tgl_lahir_le.setObjectName(u"wali_tgl_lahir_le")
        self.wali_tgl_lahir_le.setMinimumSize(QSize(0, 25))
        self.wali_tgl_lahir_le.setFont(font)
        self.wali_tgl_lahir_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.wali_tgl_lahir_le, 4, 1, 1, 1)

        self.label_151 = QLabel(self.widget_18)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font4)

        self.gridLayout_26.addWidget(self.label_151, 4, 0, 1, 1)

        self.wali_pekerjaan_cbo = QComboBox(self.widget_18)
        self.wali_pekerjaan_cbo.setObjectName(u"wali_pekerjaan_cbo")
        self.wali_pekerjaan_cbo.setMinimumSize(QSize(0, 25))
        self.wali_pekerjaan_cbo.setFont(font)
        self.wali_pekerjaan_cbo.setFocusPolicy(Qt.TabFocus)
        self.wali_pekerjaan_cbo.setEditable(True)

        self.gridLayout_26.addWidget(self.wali_pekerjaan_cbo, 6, 1, 1, 1)

        self.label_150 = QLabel(self.widget_18)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setFont(font4)

        self.gridLayout_26.addWidget(self.label_150, 0, 0, 1, 1)

        self.wali_status_cbo = QComboBox(self.widget_18)
        self.wali_status_cbo.setObjectName(u"wali_status_cbo")
        self.wali_status_cbo.setMinimumSize(QSize(0, 25))
        self.wali_status_cbo.setFont(font)
        self.wali_status_cbo.setFocusPolicy(Qt.TabFocus)
        self.wali_status_cbo.setEditable(True)

        self.gridLayout_26.addWidget(self.wali_status_cbo, 0, 1, 1, 1)

        self.label_149 = QLabel(self.widget_18)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setFont(font4)

        self.gridLayout_26.addWidget(self.label_149, 2, 0, 1, 1)

        self.label_152 = QLabel(self.widget_18)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setFont(font4)

        self.gridLayout_26.addWidget(self.label_152, 1, 0, 1, 1)

        self.label_188 = QLabel(self.widget_18)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setFont(font4)

        self.gridLayout_26.addWidget(self.label_188, 7, 0, 1, 1)

        self.wali_nik_le = QLineEdit(self.widget_18)
        self.wali_nik_le.setObjectName(u"wali_nik_le")
        sizePolicy3.setHeightForWidth(self.wali_nik_le.sizePolicy().hasHeightForWidth())
        self.wali_nik_le.setSizePolicy(sizePolicy3)
        self.wali_nik_le.setMinimumSize(QSize(0, 25))
        self.wali_nik_le.setFont(font)
        self.wali_nik_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.wali_nik_le, 2, 1, 1, 1)

        self.wali_telp_le = QLineEdit(self.widget_18)
        self.wali_telp_le.setObjectName(u"wali_telp_le")
        self.wali_telp_le.setMinimumSize(QSize(0, 25))
        self.wali_telp_le.setFont(font)
        self.wali_telp_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_26.addWidget(self.wali_telp_le, 7, 1, 1, 1)


        self.gridLayout_34.addWidget(self.widget_18, 1, 0, 1, 1)

        self.widget_21 = QWidget(self.frame_wali)
        self.widget_21.setObjectName(u"widget_21")
        self.gridLayout_27 = QGridLayout(self.widget_21)
        self.gridLayout_27.setSpacing(5)
        self.gridLayout_27.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setHorizontalSpacing(0)
        self.gridLayout_27.setVerticalSpacing(5)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.widget_21)
        self.widget_22.setObjectName(u"widget_22")

        self.gridLayout_27.addWidget(self.widget_22, 7, 0, 1, 1)

        self.label_159 = QLabel(self.widget_21)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setFont(font4)

        self.gridLayout_27.addWidget(self.label_159, 0, 0, 1, 1)

        self.tgl_masuk_le = QLineEdit(self.widget_21)
        self.tgl_masuk_le.setObjectName(u"tgl_masuk_le")
        sizePolicy1.setHeightForWidth(self.tgl_masuk_le.sizePolicy().hasHeightForWidth())
        self.tgl_masuk_le.setSizePolicy(sizePolicy1)
        self.tgl_masuk_le.setMinimumSize(QSize(0, 25))
        self.tgl_masuk_le.setFont(font)
        self.tgl_masuk_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.tgl_masuk_le, 0, 1, 1, 1)

        self.label_158 = QLabel(self.widget_21)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setFont(font4)

        self.gridLayout_27.addWidget(self.label_158, 1, 0, 1, 1)

        self.tapel_masuk_le = QLineEdit(self.widget_21)
        self.tapel_masuk_le.setObjectName(u"tapel_masuk_le")
        sizePolicy1.setHeightForWidth(self.tapel_masuk_le.sizePolicy().hasHeightForWidth())
        self.tapel_masuk_le.setSizePolicy(sizePolicy1)
        self.tapel_masuk_le.setMinimumSize(QSize(0, 25))
        self.tapel_masuk_le.setFont(font)
        self.tapel_masuk_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.tapel_masuk_le, 1, 1, 1, 1)

        self.kls_masuk_le = QLineEdit(self.widget_21)
        self.kls_masuk_le.setObjectName(u"kls_masuk_le")
        sizePolicy1.setHeightForWidth(self.kls_masuk_le.sizePolicy().hasHeightForWidth())
        self.kls_masuk_le.setSizePolicy(sizePolicy1)
        self.kls_masuk_le.setMinimumSize(QSize(0, 25))
        self.kls_masuk_le.setFont(font)
        self.kls_masuk_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.kls_masuk_le, 2, 1, 1, 1)

        self.label_193 = QLabel(self.widget_21)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setFont(font4)

        self.gridLayout_27.addWidget(self.label_193, 3, 0, 1, 1)

        self.label_190 = QLabel(self.widget_21)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setFont(font4)

        self.gridLayout_27.addWidget(self.label_190, 2, 0, 1, 1)

        self.label_162 = QLabel(self.widget_21)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setFont(font4)

        self.gridLayout_27.addWidget(self.label_162, 4, 0, 1, 1)

        self.label_161 = QLabel(self.widget_21)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setFont(font4)

        self.gridLayout_27.addWidget(self.label_161, 5, 0, 1, 1)

        self.no_urut_le = QLineEdit(self.widget_21)
        self.no_urut_le.setObjectName(u"no_urut_le")
        sizePolicy1.setHeightForWidth(self.no_urut_le.sizePolicy().hasHeightForWidth())
        self.no_urut_le.setSizePolicy(sizePolicy1)
        self.no_urut_le.setMinimumSize(QSize(0, 25))
        self.no_urut_le.setFont(font)
        self.no_urut_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.no_urut_le, 3, 1, 1, 1)

        self.pilihan_jenjang_cbo = QComboBox(self.widget_21)
        self.pilihan_jenjang_cbo.setObjectName(u"pilihan_jenjang_cbo")
        sizePolicy1.setHeightForWidth(self.pilihan_jenjang_cbo.sizePolicy().hasHeightForWidth())
        self.pilihan_jenjang_cbo.setSizePolicy(sizePolicy1)
        self.pilihan_jenjang_cbo.setMinimumSize(QSize(0, 25))
        self.pilihan_jenjang_cbo.setFont(font)
        self.pilihan_jenjang_cbo.setFocusPolicy(Qt.TabFocus)
        self.pilihan_jenjang_cbo.setEditable(True)

        self.gridLayout_27.addWidget(self.pilihan_jenjang_cbo, 4, 1, 1, 1)

        self.jenis_sekolah_cbo = QComboBox(self.widget_21)
        self.jenis_sekolah_cbo.setObjectName(u"jenis_sekolah_cbo")
        sizePolicy1.setHeightForWidth(self.jenis_sekolah_cbo.sizePolicy().hasHeightForWidth())
        self.jenis_sekolah_cbo.setSizePolicy(sizePolicy1)
        self.jenis_sekolah_cbo.setMinimumSize(QSize(0, 25))
        self.jenis_sekolah_cbo.setFont(font)
        self.jenis_sekolah_cbo.setFocusPolicy(Qt.TabFocus)
        self.jenis_sekolah_cbo.setEditable(True)

        self.gridLayout_27.addWidget(self.jenis_sekolah_cbo, 5, 1, 1, 1)

        self.widget_23 = QWidget(self.widget_21)
        self.widget_23.setObjectName(u"widget_23")

        self.gridLayout_27.addWidget(self.widget_23, 6, 0, 1, 1)

        self.widget_24 = QWidget(self.widget_21)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(0, 25))

        self.gridLayout_27.addWidget(self.widget_24, 6, 1, 1, 1)

        self.widget_27 = QWidget(self.widget_21)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(0, 25))

        self.gridLayout_27.addWidget(self.widget_27, 7, 1, 1, 1)

        self.gridLayout_27.setColumnMinimumWidth(0, 100)

        self.gridLayout_34.addWidget(self.widget_21, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame_wali)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.gridLayout_34.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame_wali)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setFont(font4)

        self.gridLayout_34.addWidget(self.label_6, 0, 1, 1, 1)

        self.gridLayout_34.setColumnStretch(0, 1)
        self.gridLayout_34.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_wali)

        self.frame_psb = QWidget(self.scrollAreaWidgetContents)
        self.frame_psb.setObjectName(u"frame_psb")
        self.gridLayout_8 = QGridLayout(self.frame_psb)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.frame_psb)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_12 = QGridLayout(self.widget_7)
        self.gridLayout_12.setSpacing(5)
        self.gridLayout_12.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(5)
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_163 = QLabel(self.widget_7)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setFont(font4)

        self.gridLayout_12.addWidget(self.label_163, 2, 2, 1, 1)

        self.cbo_daftar_sekolah = QComboBox(self.widget_7)
        self.cbo_daftar_sekolah.setObjectName(u"cbo_daftar_sekolah")
        self.cbo_daftar_sekolah.setMinimumSize(QSize(0, 25))
        self.cbo_daftar_sekolah.setFont(font3)
        self.cbo_daftar_sekolah.setEditable(False)

        self.gridLayout_12.addWidget(self.cbo_daftar_sekolah, 1, 0, 1, 2)

        self.nama_sekolah_le = QLineEdit(self.widget_7)
        self.nama_sekolah_le.setObjectName(u"nama_sekolah_le")
        self.nama_sekolah_le.setMinimumSize(QSize(0, 25))
        self.nama_sekolah_le.setFont(font)
        self.nama_sekolah_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.nama_sekolah_le, 3, 2, 1, 1)

        self.label_164 = QLabel(self.widget_7)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setFont(font4)

        self.gridLayout_12.addWidget(self.label_164, 2, 0, 1, 1)

        self.label_167 = QLabel(self.widget_7)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setFont(font4)

        self.gridLayout_12.addWidget(self.label_167, 0, 0, 1, 1)

        self.label_165 = QLabel(self.widget_7)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setFont(font4)

        self.gridLayout_12.addWidget(self.label_165, 2, 1, 1, 1)

        self.nss_le = QLineEdit(self.widget_7)
        self.nss_le.setObjectName(u"nss_le")
        sizePolicy3.setHeightForWidth(self.nss_le.sizePolicy().hasHeightForWidth())
        self.nss_le.setSizePolicy(sizePolicy3)
        self.nss_le.setMinimumSize(QSize(80, 25))
        self.nss_le.setFont(font)
        self.nss_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.nss_le, 3, 0, 1, 1)

        self.npsn_le = QLineEdit(self.widget_7)
        self.npsn_le.setObjectName(u"npsn_le")
        sizePolicy3.setHeightForWidth(self.npsn_le.sizePolicy().hasHeightForWidth())
        self.npsn_le.setSizePolicy(sizePolicy3)
        self.npsn_le.setMinimumSize(QSize(0, 25))
        self.npsn_le.setFont(font)
        self.npsn_le.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.npsn_le, 3, 1, 1, 1)

        self.label_166 = QLabel(self.widget_7)
        self.label_166.setObjectName(u"label_166")
        sizePolicy4.setHeightForWidth(self.label_166.sizePolicy().hasHeightForWidth())
        self.label_166.setSizePolicy(sizePolicy4)
        self.label_166.setFont(font4)

        self.gridLayout_12.addWidget(self.label_166, 5, 0, 1, 1)

        self.plain_alamat_sekolah = QPlainTextEdit(self.widget_7)
        self.plain_alamat_sekolah.setObjectName(u"plain_alamat_sekolah")
        self.plain_alamat_sekolah.setMinimumSize(QSize(0, 50))
        self.plain_alamat_sekolah.setMaximumSize(QSize(16777215, 50))
        self.plain_alamat_sekolah.setTabChangesFocus(True)

        self.gridLayout_12.addWidget(self.plain_alamat_sekolah, 6, 0, 1, 3)

        self.widget_6 = QWidget(self.widget_7)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_13 = QGridLayout(self.widget_6)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_tambah_sekolah = QPushButton(self.widget_6)
        self.btn_tambah_sekolah.setObjectName(u"btn_tambah_sekolah")
        self.btn_tambah_sekolah.setMinimumSize(QSize(22, 25))
        self.btn_tambah_sekolah.setMaximumSize(QSize(22, 25))
        self.btn_tambah_sekolah.setStyleSheet(u"")

        self.gridLayout_13.addWidget(self.btn_tambah_sekolah, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)


        self.gridLayout_12.addWidget(self.widget_6, 1, 2, 1, 1)


        self.gridLayout_8.addWidget(self.widget_7, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_psb)

        self.frame_pendataan = QWidget(self.scrollAreaWidgetContents)
        self.frame_pendataan.setObjectName(u"frame_pendataan")
        self.gridLayout_28 = QGridLayout(self.frame_pendataan)
        self.gridLayout_28.setSpacing(5)
        self.gridLayout_28.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setHorizontalSpacing(10)
        self.gridLayout_28.setVerticalSpacing(5)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.frame_pendataan)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_30 = QGridLayout(self.widget_9)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_156 = QLabel(self.widget_9)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setFont(font4)

        self.gridLayout_30.addWidget(self.label_156, 0, 0, 1, 1)

        self.emis_cbo = QComboBox(self.widget_9)
        self.emis_cbo.addItem("")
        self.emis_cbo.addItem("")
        self.emis_cbo.addItem("")
        self.emis_cbo.setObjectName(u"emis_cbo")
        self.emis_cbo.setMinimumSize(QSize(0, 25))
        self.emis_cbo.setFont(font)
        self.emis_cbo.setFocusPolicy(Qt.TabFocus)
        self.emis_cbo.setEditable(True)

        self.gridLayout_30.addWidget(self.emis_cbo, 0, 1, 1, 1)


        self.gridLayout_28.addWidget(self.widget_9, 1, 0, 1, 1, Qt.AlignTop)

        self.widget_10 = QWidget(self.frame_pendataan)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_31 = QGridLayout(self.widget_10)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_157 = QLabel(self.widget_10)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setFont(font4)

        self.gridLayout_31.addWidget(self.label_157, 0, 0, 2, 2)

        self.vervalpd_cbo = QComboBox(self.widget_10)
        self.vervalpd_cbo.addItem("")
        self.vervalpd_cbo.addItem("")
        self.vervalpd_cbo.addItem("")
        self.vervalpd_cbo.setObjectName(u"vervalpd_cbo")
        self.vervalpd_cbo.setMinimumSize(QSize(0, 25))
        self.vervalpd_cbo.setFont(font)
        self.vervalpd_cbo.setFocusPolicy(Qt.TabFocus)
        self.vervalpd_cbo.setEditable(True)

        self.gridLayout_31.addWidget(self.vervalpd_cbo, 1, 1, 1, 1)


        self.gridLayout_28.addWidget(self.widget_10, 1, 1, 1, 1)

        self.label_11 = QLabel(self.frame_pendataan)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.gridLayout_28.addWidget(self.label_11, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_pendataan, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_29.addWidget(self.scrollArea, 0, 0, 3, 1)


        self.gridLayout.addWidget(self.frame_edit, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_biodata, "")
        self.tab_riwayat = QWidget()
        self.tab_riwayat.setObjectName(u"tab_riwayat")
        self.gridLayout_36 = QGridLayout(self.tab_riwayat)
        self.gridLayout_36.setSpacing(5)
        self.gridLayout_36.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(5, 5, 5, 5)
        self.tbl_riwayat = QTableWidget(self.tab_riwayat)
        self.tbl_riwayat.setObjectName(u"tbl_riwayat")

        self.gridLayout_36.addWidget(self.tbl_riwayat, 1, 0, 1, 1)

        self.widget_50 = QWidget(self.tab_riwayat)
        self.widget_50.setObjectName(u"widget_50")
        self.gridLayout_46 = QGridLayout(self.widget_50)
        self.gridLayout_46.setSpacing(5)
        self.gridLayout_46.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setHorizontalSpacing(5)
        self.gridLayout_46.setVerticalSpacing(0)
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.pilihan_jenjang_cbo2 = QComboBox(self.widget_50)
        self.pilihan_jenjang_cbo2.setObjectName(u"pilihan_jenjang_cbo2")
        self.pilihan_jenjang_cbo2.setMinimumSize(QSize(120, 0))
        self.pilihan_jenjang_cbo2.setEditable(True)

        self.gridLayout_46.addWidget(self.pilihan_jenjang_cbo2, 0, 1, 1, 1)

        self.label_10 = QLabel(self.widget_50)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_46.addWidget(self.label_10, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.gridLayout_36.addWidget(self.widget_50, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_riwayat, "")
        self.tab_nilai = QWidget()
        self.tab_nilai.setObjectName(u"tab_nilai")
        self.gridLayout_44 = QGridLayout(self.tab_nilai)
        self.gridLayout_44.setSpacing(5)
        self.gridLayout_44.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(5, 5, 5, 5)
        self.widget_47 = QWidget(self.tab_nilai)
        self.widget_47.setObjectName(u"widget_47")
        self.gridLayout_43 = QGridLayout(self.widget_47)
        self.gridLayout_43.setSpacing(5)
        self.gridLayout_43.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.label_5 = QLabel(self.widget_47)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.gridLayout_43.addWidget(self.label_5, 0, 0, 1, 1)

        self.tbl_nilai_mi = QTableWidget(self.widget_47)
        self.tbl_nilai_mi.setObjectName(u"tbl_nilai_mi")

        self.gridLayout_43.addWidget(self.tbl_nilai_mi, 1, 0, 1, 1)


        self.gridLayout_44.addWidget(self.widget_47, 0, 0, 1, 1)

        self.widget_48 = QWidget(self.tab_nilai)
        self.widget_48.setObjectName(u"widget_48")
        self.gridLayout_42 = QGridLayout(self.widget_48)
        self.gridLayout_42.setSpacing(5)
        self.gridLayout_42.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.label_9 = QLabel(self.widget_48)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.gridLayout_42.addWidget(self.label_9, 0, 0, 1, 1)

        self.tbl_nilai_md = QTableWidget(self.widget_48)
        self.tbl_nilai_md.setObjectName(u"tbl_nilai_md")

        self.gridLayout_42.addWidget(self.tbl_nilai_md, 1, 0, 1, 1)


        self.gridLayout_44.addWidget(self.widget_48, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_nilai, "")
        self.tab_profil = QWidget()
        self.tab_profil.setObjectName(u"tab_profil")
        self.gridLayout_11 = QGridLayout(self.tab_profil)
        self.gridLayout_11.setSpacing(5)
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pdf_viewer = QPdfView(self.tab_profil)
        self.pdf_viewer.setObjectName(u"pdf_viewer")

        self.gridLayout_11.addWidget(self.pdf_viewer, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_profil, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.splitter.addWidget(self.frame_utama)
        self.frame_preview = QFrame(self.splitter)
        self.frame_preview.setObjectName(u"frame_preview")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_preview.sizePolicy().hasHeightForWidth())
        self.frame_preview.setSizePolicy(sizePolicy7)
        self.gridLayout_41 = QGridLayout(self.frame_preview)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 5)
        self.header_frame = QWidget(self.frame_preview)
        self.header_frame.setObjectName(u"header_frame")
        self.gridLayout_5 = QGridLayout(self.header_frame)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(3)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.btn_next_dok = QPushButton(self.header_frame)
        self.btn_next_dok.setObjectName(u"btn_next_dok")
        self.btn_next_dok.setMinimumSize(QSize(0, 25))
        self.btn_next_dok.setMaximumSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.btn_next_dok, 0, 3, 1, 1)

        self.copy_filepath = QPushButton(self.header_frame)
        self.copy_filepath.setObjectName(u"copy_filepath")
        self.copy_filepath.setMinimumSize(QSize(0, 25))
        self.copy_filepath.setMaximumSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.copy_filepath, 0, 4, 1, 1)

        self.btn_prev_dok = QPushButton(self.header_frame)
        self.btn_prev_dok.setObjectName(u"btn_prev_dok")
        self.btn_prev_dok.setMinimumSize(QSize(0, 25))
        self.btn_prev_dok.setMaximumSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.btn_prev_dok, 0, 1, 1, 1)

        self.cbo_daftar_dokumen = QComboBox(self.header_frame)
        self.cbo_daftar_dokumen.setObjectName(u"cbo_daftar_dokumen")
        sizePolicy3.setHeightForWidth(self.cbo_daftar_dokumen.sizePolicy().hasHeightForWidth())
        self.cbo_daftar_dokumen.setSizePolicy(sizePolicy3)
        self.cbo_daftar_dokumen.setMinimumSize(QSize(120, 25))

        self.gridLayout_5.addWidget(self.cbo_daftar_dokumen, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.pushButton = QPushButton(self.header_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(30, 24))
        self.pushButton.setCheckable(True)

        self.gridLayout_5.addWidget(self.pushButton, 0, 6, 1, 1)


        self.gridLayout_41.addWidget(self.header_frame, 0, 0, 1, 1)

        self.widget_viewer = QWidget(self.frame_preview)
        self.widget_viewer.setObjectName(u"widget_viewer")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_viewer.sizePolicy().hasHeightForWidth())
        self.widget_viewer.setSizePolicy(sizePolicy8)
        self.grid_viewer = QGridLayout(self.widget_viewer)
        self.grid_viewer.setSpacing(5)
        self.grid_viewer.setContentsMargins(5, 5, 5, 5)
        self.grid_viewer.setObjectName(u"grid_viewer")
        self.grid_viewer.setContentsMargins(5, 5, 5, 5)

        self.gridLayout_41.addWidget(self.widget_viewer, 2, 0, 1, 1)

        self.splitter.addWidget(self.frame_preview)

        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_145.setText(QCoreApplication.translate("Form", u"Search By", None))
        self.cbo_search_by.setItemText(0, QCoreApplication.translate("Form", u"nama_lengkap", None))
        self.cbo_search_by.setItemText(1, QCoreApplication.translate("Form", u"ayah_nama", None))
        self.cbo_search_by.setItemText(2, QCoreApplication.translate("Form", u"ibu_nama", None))
        self.cbo_search_by.setItemText(3, QCoreApplication.translate("Form", u"nis_lokal", None))
        self.cbo_search_by.setItemText(4, QCoreApplication.translate("Form", u"nisn", None))

        self.btn_sidebar.setText(QCoreApplication.translate("Form", u"[   ]", None))
        self.save_btn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.prev_btn.setText(QCoreApplication.translate("Form", u"<", None))
        self.copy_nama_lengkap.setText("")
        self.label_131.setText(QCoreApplication.translate("Form", u"Nama Lengkap", None))
        self.next_btn.setText(QCoreApplication.translate("Form", u">", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"DATA DIRI SISWA", None))
        self.label_94.setText(QCoreApplication.translate("Form", u"NIS Lokal", None))
        self.label_92.setText(QCoreApplication.translate("Form", u"NISN", None))
        self.label_nisn.setText("")
        self.label_93.setText(QCoreApplication.translate("Form", u"NIK", None))
        self.label_98.setText(QCoreApplication.translate("Form", u"JK", None))
        self.label_nik.setText("")
        self.label_96.setText(QCoreApplication.translate("Form", u"Tempat Lahir", None))
        self.label_97.setText(QCoreApplication.translate("Form", u"Anak Ke-", None))
        self.label_95.setText(QCoreApplication.translate("Form", u"Tanggal Lahir", None))
        self.label_99.setText(QCoreApplication.translate("Form", u"Saudara", None))
        self.copy_nis_lokal.setText("")
        self.copy_nisn.setText("")
        self.copy_nik.setText("")
        self.copy_tmp.setText("")
        self.copy_anak_ke.setText("")
        self.copy_saudara.setText("")
        self.label_101.setText(QCoreApplication.translate("Form", u"Cita-Cita", None))
        self.label_100.setText(QCoreApplication.translate("Form", u"NIS Kemenag", None))
        self.label_103.setText(QCoreApplication.translate("Form", u"Hobi", None))
        self.label_104.setText(QCoreApplication.translate("Form", u"Agama", None))
        self.label_181.setText(QCoreApplication.translate("Form", u"Keb. Khusus", None))
        self.label_105.setText(QCoreApplication.translate("Form", u"Pembiayaan", None))
        self.label_183.setText(QCoreApplication.translate("Form", u"Nomor KIP", None))
        self.copy_nis_kemenag.setText("")
        self.btn_nis_kemenag.setText("")
        self.label_128.setText(QCoreApplication.translate("Form", u"Nama Singkat", None))
        self.nama_singkat_le.setInputMask("")
        self.btn_singkat_nama.setText("")
        self.label_129.setText(QCoreApplication.translate("Form", u"Nama Lengkap", None))
        self.nama_lengkap_le.setInputMask("")
        self.label_130.setText(QCoreApplication.translate("Form", u"Pilih Alamat", None))
        self.label_138.setText(QCoreApplication.translate("Form", u"Provinsi", None))
        self.label_139.setText(QCoreApplication.translate("Form", u"Kode Pos", None))
        self.label_143.setText(QCoreApplication.translate("Form", u"Jarak", None))
        self.label_144.setText(QCoreApplication.translate("Form", u"Transportasi", None))
        self.label_185.setText(QCoreApplication.translate("Form", u"Jalan", None))
        self.label_142.setText(QCoreApplication.translate("Form", u"Waktu Tempuh", None))
        self.copy_kodepos.setText("")
        self.label_135.setText(QCoreApplication.translate("Form", u"Kab/Kota", None))
        self.label_132.setText(QCoreApplication.translate("Form", u"Kampung", None))
        self.label_133.setText(QCoreApplication.translate("Form", u"RW", None))
        self.label_134.setText(QCoreApplication.translate("Form", u"RT", None))
        self.label_136.setText(QCoreApplication.translate("Form", u"Kecamatan", None))
        self.label_137.setText(QCoreApplication.translate("Form", u"Desa", None))
        self.copy_kampung.setText("")
        self.label_141.setText(QCoreApplication.translate("Form", u"Alamat Lengkap", None))
        self.label_140.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.copy_alamat.setText("")
        self.copy_alamat_full.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"DATA ALAMAT", None))
        self.btn_kepala_ibu.setText(QCoreApplication.translate("Form", u"Ibu", None))
        self.label_187.setText(QCoreApplication.translate("Form", u"Tanggal KK", None))
        self.label_146.setText(QCoreApplication.translate("Form", u"Kepala KK", None))
        self.label_189.setText(QCoreApplication.translate("Form", u"Nomor KK", None))
        self.label_no_kk.setText("")
        self.btn_kepala_ayah.setText(QCoreApplication.translate("Form", u"Ayah", None))
        self.copy_no_kk.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"DATA IBU", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"DATA AYAH", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"DATA KELUARGA", None))
        self.label_113.setText(QCoreApplication.translate("Form", u"Pekerjaan", None))
        self.label_121.setText(QCoreApplication.translate("Form", u"Nama Ayah", None))
        self.label_107.setText(QCoreApplication.translate("Form", u"Status", None))
        self.label_108.setText(QCoreApplication.translate("Form", u"NIK", None))
        self.label_nik_ayah.setText("")
        self.label_110.setText(QCoreApplication.translate("Form", u"Tempat Lahir", None))
        self.label_114.setText(QCoreApplication.translate("Form", u"Pendidikan", None))
        self.label_112.setText(QCoreApplication.translate("Form", u"Tanggal Lahir", None))
        self.label_115.setText(QCoreApplication.translate("Form", u"Penghasilan", None))
        self.label_116.setText(QCoreApplication.translate("Form", u"No Telpon/HP", None))
        self.copy_ayah.setText("")
        self.copy_nik_ayah.setText("")
        self.copy_tmp_ayah.setText("")
        self.copy_telp_ayah.setText("")
        self.copy_telp_ayah62.setText("")
        self.label_ayah62.setText("")
        self.label_117.setText(QCoreApplication.translate("Form", u"Format 62", None))
        self.label_174.setText(QCoreApplication.translate("Form", u"Nama Ibu", None))
        self.label_172.setText(QCoreApplication.translate("Form", u"Status", None))
        self.label_173.setText(QCoreApplication.translate("Form", u"NIK", None))
        self.label_nik_ibu.setText("")
        self.label_170.setText(QCoreApplication.translate("Form", u"Tempat Lahir", None))
        self.label_171.setText(QCoreApplication.translate("Form", u"Tanggal Lahir", None))
        self.label_175.setText(QCoreApplication.translate("Form", u"Pendidikan", None))
        self.label_176.setText(QCoreApplication.translate("Form", u"Pekerjaan", None))
        self.label_168.setText(QCoreApplication.translate("Form", u"Penghasilan", None))
        self.label_169.setText(QCoreApplication.translate("Form", u"No Telpon/HP", None))
        self.copy_ibu.setText("")
        self.copy_tmp_ibu.setText("")
        self.copy_nik_ibu.setText("")
        self.label_119.setText(QCoreApplication.translate("Form", u"Format 62", None))
        self.copy_telp_ibu62.setText("")
        self.label_ibu62.setText("")
        self.copy_telp_ibu.setText("")
        self.label_154.setText(QCoreApplication.translate("Form", u"Pekerjaan", None))
        self.label_153.setText(QCoreApplication.translate("Form", u"Tempat Lahir", None))
        self.label_155.setText(QCoreApplication.translate("Form", u"Pendidikan", None))
        self.label_151.setText(QCoreApplication.translate("Form", u"Tanggal Lahir", None))
        self.label_150.setText(QCoreApplication.translate("Form", u"Status Wali", None))
        self.label_149.setText(QCoreApplication.translate("Form", u"NIK", None))
        self.label_152.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.label_188.setText(QCoreApplication.translate("Form", u"No. Telp", None))
        self.label_159.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None))
        self.label_158.setText(QCoreApplication.translate("Form", u"Tapel Masuk", None))
        self.label_193.setText(QCoreApplication.translate("Form", u"Nomor Urut", None))
        self.label_190.setText(QCoreApplication.translate("Form", u"Kelas Masuk", None))
        self.label_162.setText(QCoreApplication.translate("Form", u"Pilihan Jenjang", None))
        self.label_161.setText(QCoreApplication.translate("Form", u"Jenis Sekolah", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"DATA WALI SANTRI", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"PENDAFTARAN", None))
        self.label_163.setText(QCoreApplication.translate("Form", u"Nama Sekolah Asal", None))
        self.label_164.setText(QCoreApplication.translate("Form", u"NSS/NSM", None))
        self.label_167.setText(QCoreApplication.translate("Form", u"Pilih Salah Satu Sekolah", None))
        self.label_165.setText(QCoreApplication.translate("Form", u"NPSN", None))
        self.label_166.setText(QCoreApplication.translate("Form", u"Alamat Sekolah", None))
        self.btn_tambah_sekolah.setText("")
        self.label_156.setText(QCoreApplication.translate("Form", u"Status di EMIS", None))
        self.emis_cbo.setItemText(0, "")
        self.emis_cbo.setItemText(1, QCoreApplication.translate("Form", u"Ya", None))
        self.emis_cbo.setItemText(2, QCoreApplication.translate("Form", u"Tidak", None))

        self.label_157.setText(QCoreApplication.translate("Form", u"Status di VervalPD", None))
        self.vervalpd_cbo.setItemText(0, "")
        self.vervalpd_cbo.setItemText(1, QCoreApplication.translate("Form", u"Ya", None))
        self.vervalpd_cbo.setItemText(2, QCoreApplication.translate("Form", u"Tidak", None))

        self.label_11.setText(QCoreApplication.translate("Form", u"PENDATAAN", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_biodata), QCoreApplication.translate("Form", u"Biodata Siswa", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Pilihan Jenjang", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_riwayat), QCoreApplication.translate("Form", u"Riwayat Belajar", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Nilai Rapor MI", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Nilai Rapor MD", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nilai), QCoreApplication.translate("Form", u"Nilai Rapor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_profil), QCoreApplication.translate("Form", u"Profil (PDF)", None))
        self.btn_next_dok.setText(QCoreApplication.translate("Form", u">", None))
        self.copy_filepath.setText("")
        self.btn_prev_dok.setText(QCoreApplication.translate("Form", u"<", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u">", None))
    # retranslateUi

