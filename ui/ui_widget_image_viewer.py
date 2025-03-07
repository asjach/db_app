# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_image_viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import resources_rc

class Ui_Image_Viewer_Form(object):
    def setupUi(self, Image_Viewer_Form):
        if not Image_Viewer_Form.objectName():
            Image_Viewer_Form.setObjectName(u"Image_Viewer_Form")
        Image_Viewer_Form.resize(385, 502)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Image_Viewer_Form.sizePolicy().hasHeightForWidth())
        Image_Viewer_Form.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(Image_Viewer_Form)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Image_Viewer_Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.btn_1x = QPushButton(self.widget)
        self.btn_1x.setObjectName(u"btn_1x")
        self.btn_1x.setMinimumSize(QSize(25, 25))
        self.btn_1x.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setFamilies([u"OCR-A BT"])
        font.setPointSize(10)
        self.btn_1x.setFont(font)
        self.btn_1x.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_1x)

        self.btn_2x = QPushButton(self.widget)
        self.btn_2x.setObjectName(u"btn_2x")
        self.btn_2x.setMinimumSize(QSize(25, 25))
        self.btn_2x.setMaximumSize(QSize(25, 25))
        self.btn_2x.setFont(font)
        self.btn_2x.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_2x)

        self.btn_3x = QPushButton(self.widget)
        self.btn_3x.setObjectName(u"btn_3x")
        self.btn_3x.setMinimumSize(QSize(25, 25))
        self.btn_3x.setMaximumSize(QSize(25, 25))
        self.btn_3x.setFont(font)
        self.btn_3x.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_3x)

        self.btn_rotate_left = QPushButton(self.widget)
        self.btn_rotate_left.setObjectName(u"btn_rotate_left")
        self.btn_rotate_left.setMinimumSize(QSize(25, 25))
        self.btn_rotate_left.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon/resources/icon/icons8_rotate_left.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_rotate_left.setIcon(icon)
        self.btn_rotate_left.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_rotate_left)

        self.btn_rotate_right = QPushButton(self.widget)
        self.btn_rotate_right.setObjectName(u"btn_rotate_right")
        self.btn_rotate_right.setMinimumSize(QSize(25, 25))
        self.btn_rotate_right.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon/resources/icon/icons8_rotate_right.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_rotate_right.setIcon(icon1)
        self.btn_rotate_right.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_rotate_right)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_open = QPushButton(self.widget)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(35, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon/resources/icon/icons8_opened_folder.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_open.setIcon(icon2)
        self.btn_open.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btn_open)

        self.btn_explorer = QPushButton(self.widget)
        self.btn_explorer.setObjectName(u"btn_explorer")
        self.btn_explorer.setMinimumSize(QSize(35, 25))
        icon3 = QIcon()
        icon3.addFile(u":/icon/resources/icon/icons8_file_explorer.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_explorer.setIcon(icon3)
        self.btn_explorer.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.btn_explorer)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Image_Viewer_Form)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.image_viwer_label = QLabel(self.widget_2)
        self.image_viwer_label.setObjectName(u"image_viwer_label")
        sizePolicy1.setHeightForWidth(self.image_viwer_label.sizePolicy().hasHeightForWidth())
        self.image_viwer_label.setSizePolicy(sizePolicy1)
        self.image_viwer_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.image_viwer_label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)


        self.retranslateUi(Image_Viewer_Form)

        QMetaObject.connectSlotsByName(Image_Viewer_Form)
    # setupUi

    def retranslateUi(self, Image_Viewer_Form):
        Image_Viewer_Form.setWindowTitle(QCoreApplication.translate("Image_Viewer_Form", u"Form", None))
        self.btn_1x.setText(QCoreApplication.translate("Image_Viewer_Form", u"1x", None))
        self.btn_2x.setText(QCoreApplication.translate("Image_Viewer_Form", u"2x", None))
        self.btn_3x.setText(QCoreApplication.translate("Image_Viewer_Form", u"3x", None))
        self.btn_rotate_left.setText("")
        self.btn_rotate_right.setText("")
#if QT_CONFIG(statustip)
        self.btn_open.setStatusTip(QCoreApplication.translate("Image_Viewer_Form", u"Open File", None))
#endif // QT_CONFIG(statustip)
        self.btn_open.setText("")
#if QT_CONFIG(statustip)
        self.btn_explorer.setStatusTip(QCoreApplication.translate("Image_Viewer_Form", u"Open In Explorer", None))
#endif // QT_CONFIG(statustip)
        self.btn_explorer.setText("")
        self.image_viwer_label.setText("")
    # retranslateUi

