from PySide6.QtWidgets import QWidget
from ui.ui_widget_image_viewer import Ui_Image_Viewer_Form
from PySide6.QtGui import QImage, QPixmap, QPainter
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QTransform
from utils.fungsi.file_dialog_function import open_with_default_app, open_in_explorer


class Widget_Image_Viewer(Ui_Image_Viewer_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qimage = QImage()
        self.qlabel_image = self.image_viwer_label
        self.label_width = self.image_viwer_label.width()
        self.label_height = self.image_viwer_label.height()

        self.qimage_scaled = QImage()
        self.qpixmap = QPixmap()
        self.zoomX = 1
        self.position = [0, 0]
        self.panFlag = True
        self.image_path = ""

        self.qlabel_image.setSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored
        )
        self.setup_connections()
        self.__connectEvents()

    def __connectEvents(self):
        self.qlabel_image.mousePressEvent = self.mousePressAction
        self.qlabel_image.mouseMoveEvent = self.mouseMoveAction
        self.qlabel_image.mouseReleaseEvent = self.mouseReleaseAction
        self.qlabel_image.resizeEvent = self.onResize
        self.qlabel_image.wheelEvent = self.wheelEvent

    def setup_connections(self):
        self.btn_1x.clicked.connect(lambda: self.zoom_x(1))
        self.btn_2x.clicked.connect(lambda: self.zoom_x(2))
        self.btn_3x.clicked.connect(lambda: self.zoom_x(3))
        self.btn_rotate_left.clicked.connect(lambda: self.transform(-90))
        self.btn_rotate_right.clicked.connect(lambda: self.transform(90))
        self.btn_open.clicked.connect(lambda: open_with_default_app(self.image_path))
        self.btn_explorer.clicked.connect(lambda: open_in_explorer(self.image_path))

    def onResize(self, event):
        self.label_width = self.image_viwer_label.width()
        self.label_height = self.image_viwer_label.height()
        if not self.qimage.isNull():
            self.qpixmap = QPixmap(self.qlabel_image.size())
            self.qpixmap.fill(QtCore.Qt.transparent)
            self.qimage_scaled = self.qimage.scaled(
                int(self.qlabel_image.width() * self.zoomX),
                int(self.qlabel_image.height() * self.zoomX),
                QtCore.Qt.KeepAspectRatio,
            )
            self.update()
        else:
            return

    def wheelEvent(self, event):
        if QApplication.keyboardModifiers() == Qt.ControlModifier:
            delta = event.angleDelta().y()
            if delta > 0:
                self.zoom_in()
            elif delta < 0:
                self.zoom_out()
        elif QApplication.keyboardModifiers() == Qt.AltModifier:
            delta = event.angleDelta().x()
            if delta > 0:
                self.position = self.position[0] - 100, self.position[1]
            elif delta < 0:
                self.position = self.position[0] + 100, self.position[1]
            self.update()
        else:
            delta = event.angleDelta().y()
            if delta > 0:
                self.position = self.position[0], self.position[1] - 100
            elif delta < 0:
                self.position = self.position[0], self.position[1] + 100
            self.update()

    def loadImage(self, imagePath):
        if imagePath:
            self.image_path = imagePath
            self.qimage = QImage(imagePath)
            lebar_gambar = self.qimage.width()
            tinggi_gambar = self.qimage.height()
            self.qpixmap = QPixmap(self.qlabel_image.size())
            if not self.qimage.isNull():
                if lebar_gambar > tinggi_gambar:
                    self.zoomX = 1.5
                else:
                    self.zoomX = 1.75
                self.position = [0, 0]
                self.qimage_scaled = self.qimage.scaled(
                    int(self.qlabel_image.width() * self.zoomX),
                    int(self.qlabel_image.height() * self.zoomX),
                    QtCore.Qt.KeepAspectRatio,
                )
                self.update()
            else:
                return
        elif imagePath == "" or imagePath == None:
            self.image_viwer_label.clear()

    def loadImage_1x(self, imagePath):
        if imagePath:
            self.zoomX = 1
            self.image_path = imagePath
            self.qimage = QImage(self.image_path)
            self.qpixmap = QPixmap(self.qlabel_image.size())
            if not self.qimage.isNull():
                self.position = [0, 0]
                self.qimage_scaled = self.qimage.scaled(
                    int(self.qlabel_image.width() * self.zoomX),
                    int(self.qlabel_image.height() * self.zoomX),
                    QtCore.Qt.KeepAspectRatio,
                )
                self.update()
            else:
                return
        elif imagePath == "" or imagePath == None:
            self.image_viwer_label.clear()

    def update(self):
        if not self.qimage_scaled.isNull():
            px, py = self.position
            px = (
                px
                if (px <= self.qimage_scaled.width() - self.qlabel_image.width())
                else (self.qimage_scaled.width() - self.qlabel_image.width())
            )
            py = (
                py
                if (py <= self.qimage_scaled.height() - self.qlabel_image.height())
                else (self.qimage_scaled.height() - self.qlabel_image.height())
            )
            px = px if (px >= 0) else 0
            py = py if (py >= 0) else 0
            self.position = (px, py)
            self.qpixmap.fill(QtCore.Qt.transparent)
            painter = QPainter()
            painter.begin(self.qpixmap)
            painter.drawImage(
                QtCore.QPoint(0, 0),
                self.qimage_scaled,
                QtCore.QRect(
                    int(self.position[0]),
                    int(self.position[1]),
                    int(self.qlabel_image.width()),
                    int(self.qlabel_image.height()),
                ),
            )
            painter.end()
            self.qlabel_image.setPixmap(self.qpixmap)
        else:
            pass

    def mousePressAction(self, QMouseEvent):
        x, y = QMouseEvent.pos().x(), QMouseEvent.pos().y()
        if self.panFlag:
            self.pressed = QMouseEvent.pos()
            self.anchor = self.position

    def mouseMoveAction(self, QMouseEvent):
        x, y = QMouseEvent.pos().x(), QMouseEvent.pos().y()
        if self.pressed:
            dx, dy = x - self.pressed.x(), y - self.pressed.y()
            self.position = self.anchor[0] - dx, self.anchor[1] - dy
            self.update()

    def mouseReleaseAction(self, QMouseEvent):
        self.pressed = None

    def zoom_x(self, value):
        self.zoomX = value
        px, py = self.position
        self.position = (px, py)
        self.qimage_scaled = self.qimage.scaled(
            int(self.qlabel_image.height() * self.zoomX),
            int(self.qlabel_image.height() * self.zoomX),
            QtCore.Qt.KeepAspectRatio,
        )
        self.update()

    def zoom_in(self):
        self.zoomX += 0.3
        px, py = self.position
        self.position = (px, py)
        self.qimage_scaled = self.qimage.scaled(
            int(self.qlabel_image.width() * self.zoomX),
            int(self.qlabel_image.height() * self.zoomX),
            QtCore.Qt.KeepAspectRatio,
        )
        self.update()

    def zoom_out(self):
        if self.zoomX > 1:
            self.zoomX -= 0.3
            px, py = self.position
            self.position = (px, py)
            self.qimage_scaled = self.qimage.scaled(
                int(self.qlabel_image.width() * self.zoomX),
                int(self.qlabel_image.height() * self.zoomX),
                QtCore.Qt.KeepAspectRatio,
            )
            self.update()

    def transform(self, angle_degrees):
        transform = QTransform()
        transform.rotate(angle_degrees)
        self.qimage = self.qimage.transformed(transform)
        self.qimage_scaled = self.qimage.scaled(
            int(self.qlabel_image.width() * self.zoomX),
            int(self.qlabel_image.height() * self.zoomX),
            Qt.KeepAspectRatio,
        )
        self.update()
