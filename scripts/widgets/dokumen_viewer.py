from PySide6.QtWidgets import QWidget
from ui.ui_widget_dokumen_viewer import Ui_Dokumen_Viewer
import os
from PySide6.QtGui import QImage, QPixmap, QPainter
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QTransform
from utils.fungsi.file_dialog_function import open_with_default_app, open_in_explorer
from PySide6.QtGui import QFont


import fitz  # PyMuPDF

class DokumenViewer(Ui_Dokumen_Viewer, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pdf_document = None  # Objek PDF
        self.image_labels = []
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
        self.pdf_document = None
        self.current_page = 0
        
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
        self.btn_next_page.clicked.connect(self.next_page)
        self.btn_prev_page.clicked.connect(self.previous_page)
        self.spin_page.valueChanged.connect(self.spin_page_changed)

    def loadFile(self, filePath, zoom_factor=1):
        if not filePath:
            return

        self.image_path = filePath
        ext = os.path.splitext(filePath)[-1].lower()

        if ext in [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".heic"]:
            self.loadImage(filePath, zoom_factor)
        elif ext == ".pdf":
            self.loadPDF(filePath)
        else:
            self.image_viwer_label.setText('Unsupported file format!')
            font = QFont()
            font.setPointSize(24)
            self.image_viwer_label.setAlignment(Qt.AlignCenter)
            self.image_viwer_label.setFont(font)
            self.close_file()

    def loadImage(self, imagePath, zoom_factor=1):
        self.qimage = QImage(imagePath)
        self.qpixmap = QPixmap(self.qlabel_image.size())
        if not self.qimage.isNull():
            # self.zoomX = 1.5 if self.qimage.width() > self.qimage.height() else 1.75
            self.zoomX = zoom_factor
            self.position = [0, 0]
            self.qimage_scaled = self.qimage.scaled(
                int(self.qlabel_image.width() * self.zoomX),
                int(self.qlabel_image.height() * self.zoomX),
                QtCore.Qt.KeepAspectRatio,
            )
            self.update()
        else:
            print("Failed to load image!")

    def loadPDF(self, pdf_source):
        if isinstance(pdf_source, bytes):
            self.pdf_document = fitz.open("pdf", pdf_source)  # Load dari bytes
        else:
            self.pdf_document = fitz.open(pdf_source)  # Load dari file path
        self.current_page = 0
        self.spin_page.setValue(self.current_page+1)
        self.render_pdf_page(self.current_page)

    def spin_page_changed(self):
        if self.spin_page.value() > len(self.pdf_document):
            self.spin_page.setValue(len(self.pdf_document))
        self.current_page = self.spin_page.value() - 1
        self.render_pdf_page(self.current_page)

    def close_file(self):
        """Menutup file yang sedang dibuka (image atau PDF)."""
        if self.pdf_document:
            # Jika PDF sedang dibuka, tutup dokumen
            self.pdf_document.close()
            self.pdf_document = None
            self.current_page = 0
        
        if not self.qimage.isNull():
            # Jika image sedang ditampilkan, reset variabel terkait
            self.qimage = QImage()
            self.qpixmap = QPixmap()
            self.qimage_scaled = QImage()
            # print("Image closed successfully.")
        
        # Reset tampilan
        self.update()
        self.image_path = ""  # Reset path file
        self.image_viwer_label.clear()
        # print("File viewer has been reset.")


    def render_pdf_page(self, page_number):
        if not self.pdf_document:
            return

        page = self.pdf_document[page_number]
        pix = page.get_pixmap(dpi=300)  # Render page at 150 DPI
        qimage = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        self.qimage = qimage
        self.qpixmap = QPixmap(self.qlabel_image.size())
        self.zoomX = 1
        self.position = [0, 0]
        self.qimage_scaled = self.qimage.scaled(
            int(self.qlabel_image.width() * self.zoomX),
            int(self.qlabel_image.height() * self.zoomX),
            QtCore.Qt.KeepAspectRatio,
        )
        self.update()

    def next_page(self):
        if self.pdf_document and self.current_page < len(self.pdf_document) - 1:
            self.current_page += 1
            # self.render_pdf_page(self.current_page)
            self.spin_page.setValue(self.current_page+1)

    def previous_page(self):
        if self.pdf_document and self.current_page > 0:
            self.current_page -= 1
            # self.render_pdf_page(self.current_page)
            self.spin_page.setValue(self.current_page+1)

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
            # painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
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

    def zoom_x(self, value):
        self.zoomX = value
        px, py = self.position
        self.position = (px, py)
        self.qimage_scaled = self.qimage.scaled(
            int(self.qlabel_image.width() * self.zoomX),
            int(self.qlabel_image.height() * self.zoomX),
            QtCore.Qt.KeepAspectRatio,
        )
        self.update()

    def wheelEvent(self, event):
        delta_x, delta_y = event.angleDelta().x(), event.angleDelta().y()
        modifiers = QApplication.keyboardModifiers()

        if modifiers == Qt.ControlModifier:  # Zoom dengan Ctrl + Scroll
            self.zoom_in() if delta_y > 0 else self.zoom_out()

        elif modifiers == Qt.AltModifier:  # Panning horizontal dengan Alt + Scroll
            self.position = (self.position[0] + (100 if delta_x < 0 else -100), self.position[1])
            self.update()

        elif self.pdf_document:  # Scroll untuk PDF
            current_y = self.position[1]
            max_y = max(0, self.qimage_scaled.height() - self.qlabel_image.height())
            wheel_tolerance = 3

            # Inisialisasi akumulator jika belum ada
            self.wheel_count_up = getattr(self, 'wheel_count_up', 0)
            self.wheel_count_down = getattr(self, 'wheel_count_down', 0)

            if delta_y > 0:  # Scroll ke atas
                if current_y > 0:
                    self.position = (self.position[0], max(0, current_y - 100))
                elif self.current_page > 0:
                    self.wheel_count_up += 1
                    if self.wheel_count_up >= wheel_tolerance:
                        self.previous_page()
                        self.wheel_count_up = 0
                self.wheel_count_down = 0  # Reset akumulator lawan arah

            elif delta_y < 0:  # Scroll ke bawah
                if current_y < max_y:
                    self.position = (self.position[0], min(max_y, current_y + 100))
                elif self.current_page < len(self.pdf_document) - 1:
                    self.wheel_count_down += 1
                    if self.wheel_count_down >= wheel_tolerance:
                        self.next_page()
                        self.wheel_count_down = 0
                self.wheel_count_up = 0  # Reset akumulator lawan arah

            self.update()

        else:  # Panning vertikal untuk gambar (non-PDF)
            self.position = (self.position[0], self.position[1] + (-100 if delta_y > 0 else 100))
            self.update()


    def zoom_in(self):
        self.zoomX += 0.25
        px, py = self.position
        self.position = (px, py)
        self.qimage_scaled = self.qimage.scaled(
            int(self.qlabel_image.width() * self.zoomX),
            int(self.qlabel_image.height() * self.zoomX),
            QtCore.Qt.KeepAspectRatio,
        )
        self.update()

    def zoom_out(self):
        if self.zoomX > 0.5:
            self.zoomX -= 0.25
            px, py = self.position
            self.position = (px, py)
            self.qimage_scaled = self.qimage.scaled(
                int(self.qlabel_image.width() * self.zoomX),
                int(self.qlabel_image.height() * self.zoomX),
                QtCore.Qt.KeepAspectRatio,
            )
            self.update()

    def gotoPage(self, page_number):
        if self.pdf_document:
            max_page = len(self.pdf_document) - 1
            if 0 <= page_number <= max_page:
                self.current_page = page_number
                self.spin_page.setValue(self.current_page + 1)  # Sinkronisasi dengan spinbox
                self.render_pdf_page(self.current_page)
