# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_2.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QGridLayout, QHBoxLayout, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1129, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.window_dragger = QWidget(self.centralwidget)
        self.window_dragger.setObjectName(u"window_dragger")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_dragger.sizePolicy().hasHeightForWidth())
        self.window_dragger.setSizePolicy(sizePolicy)
        self.window_dragger.setMinimumSize(QSize(0, 32))
        self.window_dragger.setMaximumSize(QSize(16777215, 32))
        self.gridLayout_2 = QGridLayout(self.window_dragger)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.widget_5 = QWidget(self.window_dragger)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setMinimumSize(QSize(80, 30))
        self.widget_5.setMaximumSize(QSize(16777215, 30))
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.widget_5)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy1.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.toolButton)


        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.window_dragger)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QSize(0, 30))
        self.widget_4.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_3 = QGridLayout(self.widget_6)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_6)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(30, 0))
        self.pushButton.setMaximumSize(QSize(30, 16777215))
        font = QFont()
        font.setFamilies([u"Aptos"])
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(30, 0))
        self.pushButton_2.setMaximumSize(QSize(30, 16777215))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_4 = QGridLayout(self.widget_7)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.widget_7)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(90, 0))
        self.comboBox.setFont(font)

        self.gridLayout_4.addWidget(self.comboBox, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_7)

        self.widget_11 = QWidget(self.widget_4)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_10 = QGridLayout(self.widget_11)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.list_tingkat = QListWidget(self.widget_11)
        QListWidgetItem(self.list_tingkat)
        QListWidgetItem(self.list_tingkat)
        QListWidgetItem(self.list_tingkat)
        QListWidgetItem(self.list_tingkat)
        QListWidgetItem(self.list_tingkat)
        QListWidgetItem(self.list_tingkat)
        self.list_tingkat.setObjectName(u"list_tingkat")
        sizePolicy1.setHeightForWidth(self.list_tingkat.sizePolicy().hasHeightForWidth())
        self.list_tingkat.setSizePolicy(sizePolicy1)
        self.list_tingkat.setMinimumSize(QSize(110, 28))
        font1 = QFont()
        font1.setFamilies([u"Aptos Narrow"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.list_tingkat.setFont(font1)
        self.list_tingkat.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_tingkat.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_tingkat.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.list_tingkat.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_tingkat.setFlow(QListView.LeftToRight)
        self.list_tingkat.setProperty(u"isWrapping", False)
        self.list_tingkat.setResizeMode(QListView.Fixed)
        self.list_tingkat.setLayoutMode(QListView.Batched)
        self.list_tingkat.setSpacing(0)
        self.list_tingkat.setViewMode(QListView.ListMode)

        self.gridLayout_10.addWidget(self.list_tingkat, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_4)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_11 = QGridLayout(self.widget_12)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.list_kelas = QListWidget(self.widget_12)
        self.list_kelas.setObjectName(u"list_kelas")
        sizePolicy1.setHeightForWidth(self.list_kelas.sizePolicy().hasHeightForWidth())
        self.list_kelas.setSizePolicy(sizePolicy1)
        self.list_kelas.setMinimumSize(QSize(0, 28))
        self.list_kelas.setMaximumSize(QSize(300, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Aptos Narrow"])
        font2.setPointSize(10)
        self.list_kelas.setFont(font2)
        self.list_kelas.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_kelas.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_kelas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.list_kelas.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_kelas.setFlow(QListView.LeftToRight)
        self.list_kelas.setProperty(u"isWrapping", False)
        self.list_kelas.setResizeMode(QListView.Fixed)
        self.list_kelas.setLayoutMode(QListView.SinglePass)
        self.list_kelas.setSpacing(0)
        self.list_kelas.setViewMode(QListView.ListMode)

        self.gridLayout_11.addWidget(self.list_kelas, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_12)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_5 = QGridLayout(self.widget_8)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.widget_8)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy1.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy1)
        self.comboBox_2.setMinimumSize(QSize(100, 0))
        self.comboBox_2.setMaximumSize(QSize(16777215, 28))
        self.comboBox_2.setFont(font)

        self.gridLayout_5.addWidget(self.comboBox_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_6 = QGridLayout(self.widget_9)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.comboBox_3 = QComboBox(self.widget_9)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.setMinimumSize(QSize(100, 0))
        self.comboBox_3.setMaximumSize(QSize(16777215, 28))
        self.comboBox_3.setFont(font)

        self.gridLayout_6.addWidget(self.comboBox_3, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_9)

        self.horizontalSpacer = QSpacerItem(793, 9, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_10 = QWidget(self.widget_4)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_8 = QGridLayout(self.widget_10)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget_10)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(100, 0))
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout_8.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.widget_10)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy1.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy1)
        self.comboBox_4.setMinimumSize(QSize(100, 0))
        self.comboBox_4.setMaximumSize(QSize(16777215, 28))
        self.comboBox_4.setFont(font)

        self.gridLayout_8.addWidget(self.comboBox_4, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.widget_10)


        self.gridLayout_2.addWidget(self.widget_4, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.window_dragger)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 30))
        self.widget_3.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_7 = QGridLayout(self.widget_3)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.widget_3)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(30, 0))
        self.btn_minimize.setMaximumSize(QSize(30, 16777215))
        self.btn_minimize.setCheckable(True)
        self.btn_minimize.setAutoExclusive(True)

        self.gridLayout_7.addWidget(self.btn_minimize, 0, 0, 1, 1)

        self.btn_close = QPushButton(self.widget_3)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(30, 0))
        self.btn_close.setMaximumSize(QSize(30, 16777215))
        self.btn_close.setCheckable(True)
        self.btn_close.setAutoExclusive(True)

        self.gridLayout_7.addWidget(self.btn_close, 0, 3, 1, 1)

        self.btn_restore = QPushButton(self.widget_3)
        self.btn_restore.setObjectName(u"btn_restore")
        sizePolicy2.setHeightForWidth(self.btn_restore.sizePolicy().hasHeightForWidth())
        self.btn_restore.setSizePolicy(sizePolicy2)
        self.btn_restore.setMinimumSize(QSize(30, 0))
        self.btn_restore.setMaximumSize(QSize(30, 16777215))
        self.btn_restore.setCheckable(True)
        self.btn_restore.setAutoExclusive(True)

        self.gridLayout_7.addWidget(self.btn_restore, 0, 1, 1, 1)

        self.btn_maximize = QPushButton(self.widget_3)
        self.btn_maximize.setObjectName(u"btn_maximize")
        sizePolicy2.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy2)
        self.btn_maximize.setMinimumSize(QSize(30, 0))
        self.btn_maximize.setMaximumSize(QSize(30, 16777215))
        self.btn_maximize.setCheckable(True)
        self.btn_maximize.setAutoExclusive(True)

        self.gridLayout_7.addWidget(self.btn_maximize, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.window_dragger, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 60))
        self.gridLayout_9 = QGridLayout(self.widget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(5)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"MI", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"MD", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"2024-2025", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2025-2026", None))


        __sortingEnabled = self.list_tingkat.isSortingEnabled()
        self.list_tingkat.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_tingkat.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u" 1 ", None));
        ___qlistwidgetitem1 = self.list_tingkat.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u" 2 ", None));
        ___qlistwidgetitem2 = self.list_tingkat.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u" 3 ", None));
        ___qlistwidgetitem3 = self.list_tingkat.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u" 4 ", None));
        ___qlistwidgetitem4 = self.list_tingkat.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u" 5 ", None));
        ___qlistwidgetitem5 = self.list_tingkat.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u" 6 ", None));
        self.list_tingkat.setSortingEnabled(__sortingEnabled)

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"ORDER", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"KOLOM", None))

        self.comboBox_3.setCurrentText(QCoreApplication.translate("MainWindow", u"KOLOM", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"SEARCH", None))

        self.comboBox_4.setCurrentText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.btn_minimize.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.btn_restore.setText(QCoreApplication.translate("MainWindow", u"[ ]", None))
        self.btn_maximize.setText(QCoreApplication.translate("MainWindow", u"[[]]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

