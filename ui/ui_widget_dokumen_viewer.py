# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_dokumen_viewer.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)
import resources_rc

class Ui_Dokumen_Viewer(object):
    def setupUi(self, Dokumen_Viewer):
        if not Dokumen_Viewer.objectName():
            Dokumen_Viewer.setObjectName(u"Dokumen_Viewer")
        Dokumen_Viewer.resize(771, 840)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dokumen_Viewer.sizePolicy().hasHeightForWidth())
        Dokumen_Viewer.setSizePolicy(sizePolicy)
        Dokumen_Viewer.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(Dokumen_Viewer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dokumen_Viewer)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.btn_1x = QPushButton(self.widget)
        self.btn_1x.setObjectName(u"btn_1x")
        self.btn_1x.setMinimumSize(QSize(24, 24))
        self.btn_1x.setMaximumSize(QSize(24, 24))
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(10)
        self.btn_1x.setFont(font)

        self.horizontalLayout.addWidget(self.btn_1x)

        self.btn_2x = QPushButton(self.widget)
        self.btn_2x.setObjectName(u"btn_2x")
        self.btn_2x.setMinimumSize(QSize(24, 24))
        self.btn_2x.setMaximumSize(QSize(24, 24))
        self.btn_2x.setFont(font)

        self.horizontalLayout.addWidget(self.btn_2x)

        self.btn_3x = QPushButton(self.widget)
        self.btn_3x.setObjectName(u"btn_3x")
        self.btn_3x.setMinimumSize(QSize(24, 24))
        self.btn_3x.setMaximumSize(QSize(24, 24))
        self.btn_3x.setFont(font)

        self.horizontalLayout.addWidget(self.btn_3x)

        self.btn_4x = QPushButton(self.widget)
        self.btn_4x.setObjectName(u"btn_4x")
        self.btn_4x.setMinimumSize(QSize(24, 24))
        self.btn_4x.setMaximumSize(QSize(24, 24))
        self.btn_4x.setFont(font)

        self.horizontalLayout.addWidget(self.btn_4x)

        self.btn_5x = QPushButton(self.widget)
        self.btn_5x.setObjectName(u"btn_5x")
        self.btn_5x.setMinimumSize(QSize(24, 24))
        self.btn_5x.setMaximumSize(QSize(24, 24))
        self.btn_5x.setFont(font)

        self.horizontalLayout.addWidget(self.btn_5x)

        self.btn_rotate_left = QPushButton(self.widget)
        self.btn_rotate_left.setObjectName(u"btn_rotate_left")
        self.btn_rotate_left.setMinimumSize(QSize(24, 24))
        self.btn_rotate_left.setMaximumSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u":/icon/resources/icon/rotate_left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_rotate_left.setIcon(icon)
        self.btn_rotate_left.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_rotate_left)

        self.btn_rotate_right = QPushButton(self.widget)
        self.btn_rotate_right.setObjectName(u"btn_rotate_right")
        self.btn_rotate_right.setMinimumSize(QSize(24, 24))
        self.btn_rotate_right.setMaximumSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u":/icon/resources/icon/rotate_right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_rotate_right.setIcon(icon1)
        self.btn_rotate_right.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_rotate_right)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.page_control = QWidget(self.widget)
        self.page_control.setObjectName(u"page_control")
        self.gridLayout_3 = QGridLayout(self.page_control)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 1, 0, 1)
        self.btn_next_page = QPushButton(self.page_control)
        self.btn_next_page.setObjectName(u"btn_next_page")
        self.btn_next_page.setMinimumSize(QSize(24, 24))
        self.btn_next_page.setMaximumSize(QSize(24, 24))
        icon2 = QIcon()
        icon2.addFile(u":/dark/resources/icon/dark/more_than.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_next_page.setIcon(icon2)

        self.gridLayout_3.addWidget(self.btn_next_page, 0, 2, 1, 1)

        self.spin_page = QSpinBox(self.page_control)
        self.spin_page.setObjectName(u"spin_page")
        self.spin_page.setMinimumSize(QSize(50, 22))
        self.spin_page.setMaximumSize(QSize(50, 22))
        self.spin_page.setAlignment(Qt.AlignCenter)
        self.spin_page.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spin_page.setMinimum(1)
        self.spin_page.setMaximum(99999)
        self.spin_page.setValue(1)

        self.gridLayout_3.addWidget(self.spin_page, 0, 1, 1, 1)

        self.btn_prev_page = QPushButton(self.page_control)
        self.btn_prev_page.setObjectName(u"btn_prev_page")
        self.btn_prev_page.setMinimumSize(QSize(24, 24))
        self.btn_prev_page.setMaximumSize(QSize(24, 24))
        icon3 = QIcon()
        icon3.addFile(u":/dark/resources/icon/dark/less_than.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_prev_page.setIcon(icon3)

        self.gridLayout_3.addWidget(self.btn_prev_page, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.page_control)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_open = QPushButton(self.widget)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(36, 24))
        icon4 = QIcon()
        icon4.addFile(u":/icon/resources/icon/image.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_open.setIcon(icon4)
        self.btn_open.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btn_open)

        self.btn_explorer = QPushButton(self.widget)
        self.btn_explorer.setObjectName(u"btn_explorer")
        self.btn_explorer.setMinimumSize(QSize(36, 24))
        icon5 = QIcon()
        icon5.addFile(u":/icon/resources/icon/opened_folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_explorer.setIcon(icon5)
        self.btn_explorer.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btn_explorer)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.viewer_widget = QWidget(Dokumen_Viewer)
        self.viewer_widget.setObjectName(u"viewer_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.viewer_widget.sizePolicy().hasHeightForWidth())
        self.viewer_widget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.viewer_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.image_viwer_label = QLabel(self.viewer_widget)
        self.image_viwer_label.setObjectName(u"image_viwer_label")
        sizePolicy1.setHeightForWidth(self.image_viwer_label.sizePolicy().hasHeightForWidth())
        self.image_viwer_label.setSizePolicy(sizePolicy1)
        self.image_viwer_label.setStyleSheet(u"")
        self.image_viwer_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.image_viwer_label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.viewer_widget, 1, 0, 1, 1)


        self.retranslateUi(Dokumen_Viewer)

        QMetaObject.connectSlotsByName(Dokumen_Viewer)
    # setupUi

    def retranslateUi(self, Dokumen_Viewer):
        Dokumen_Viewer.setWindowTitle(QCoreApplication.translate("Dokumen_Viewer", u"Form", None))
        self.btn_1x.setText(QCoreApplication.translate("Dokumen_Viewer", u"1", None))
        self.btn_2x.setText(QCoreApplication.translate("Dokumen_Viewer", u"2", None))
        self.btn_3x.setText(QCoreApplication.translate("Dokumen_Viewer", u"3", None))
        self.btn_4x.setText(QCoreApplication.translate("Dokumen_Viewer", u"4", None))
        self.btn_5x.setText(QCoreApplication.translate("Dokumen_Viewer", u"5", None))
        self.btn_rotate_left.setText("")
        self.btn_rotate_right.setText("")
        self.btn_next_page.setText("")
        self.spin_page.setPrefix("")
        self.btn_prev_page.setText("")
#if QT_CONFIG(statustip)
        self.btn_open.setStatusTip(QCoreApplication.translate("Dokumen_Viewer", u"Open File", None))
#endif // QT_CONFIG(statustip)
        self.btn_open.setText("")
#if QT_CONFIG(statustip)
        self.btn_explorer.setStatusTip(QCoreApplication.translate("Dokumen_Viewer", u"Open In Explorer", None))
#endif // QT_CONFIG(statustip)
        self.btn_explorer.setText("")
        self.image_viwer_label.setText("")
    # retranslateUi

