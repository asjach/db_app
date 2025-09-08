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
from PIL import Image


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
        self.page_control.setVisible(False)
        
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
        self.btn_4x.clicked.connect(lambda: self.zoom_x(4))
        self.btn_5x.clicked.connect(lambda: self.zoom_x(5))
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
        
        # Close any existing file (PDF or image) to reset state
        self.close_file()
        
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
        # Ensure PDF state is cleared
        self.pdf_document = None
        self.page_control.setVisible(False)
        
        # Load the image
        self.qimage = QImage(imagePath)
        self.qpixmap = QPixmap(self.qlabel_image.size())
        if not self.qimage.isNull():
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

    def loadPDF(self, pdf_source, page=None):
        self.page_control.setVisible(True)
        if isinstance(pdf_source, bytes):
            self.pdf_document = fitz.open("pdf", pdf_source)  # Load dari bytes
        else:
            self.pdf_document = fitz.open(pdf_source)  # Load dari file path
        if page:
            self.current_page = page
        else:
            self.current_page = 0
            self.spin_page.setValue(self.current_page+1)
        self.render_pdf_page(self.current_page)

    def zoom_x(self, value):
        old_zoom = self.zoomX
        self.zoomX = value
        
        # Hitung pusat pandangan saat ini
        current_center_x = self.position[0] + self.qlabel_image.width() / 2
        current_center_y = self.position[1] + self.qlabel_image.height() / 2
        
        if self.pdf_document and not self.qimage.isNull():
            # Render ulang halaman PDF dengan DPI baru
            self.render_pdf_page(self.current_page)
        elif not self.qimage.isNull():
            # Skalakan gambar untuk non-PDF
            self.qimage_scaled = self.qimage.scaled(
                int(self.qlabel_image.width() * self.zoomX),
                int(self.qlabel_image.height() * self.zoomX),
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            )
        else:
            # No valid image or PDF loaded, exit early
            return
        
        # Sesuaikan posisi agar pusat pandangan tetap
        new_center_x = current_center_x * (self.zoomX / old_zoom)
        new_center_y = current_center_y * (self.zoomX / old_zoom)
        self.position = (
            new_center_x - self.qlabel_image.width() / 2,
            new_center_y - self.qlabel_image.height() / 2
        )
        
        # Pastikan posisi tetap dalam batas gambar
        self.position = (
            max(0, min(self.position[0], self.qimage_scaled.width() - self.qlabel_image.width())),
            max(0, min(self.position[1], self.qimage_scaled.height() - self.qlabel_image.height()))
        )
        self.update()

    def spin_page_changed(self):
        if self.spin_page.value() > len(self.pdf_document):
            self.spin_page.setValue(len(self.pdf_document))
        self.current_page = self.spin_page.value() - 1
        self.render_pdf_page(self.current_page)

    def close_file(self):
        """Menutup file yang sedang dibuka (image atau PDF)."""
        # Close PDF document if it exists
        if self.pdf_document:
            self.pdf_document.close()
            self.pdf_document = None
            self.current_page = 0
            self.page_control.setVisible(False)
        
        # Reset image-related variables
        self.qimage = QImage()
        self.qpixmap = QPixmap()
        self.qimage_scaled = QImage()
        self.image_path = ""
        self.zoomX = 1
        self.position = [0, 0]
        
        # Clear the display
        self.image_viwer_label.clear()
        self.update()


    def render_pdf_page(self, page_number):
        if not self.pdf_document:
            return
    
        page = self.pdf_document[page_number]

        dpi = int(100 * self.zoomX)
        dpi = max(100, min(300, dpi))  # Batas bawah 100, batas atas 300
        pix = page.get_pixmap(dpi=dpi)
        qimage = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        self.qimage = qimage
        self.qpixmap = QPixmap(self.qlabel_image.size())
        
        # Skalakan gambar dengan zoom saat ini
        self.qimage_scaled = self.qimage.scaled(
            int(self.qlabel_image.width() * self.zoomX),
            int(self.qlabel_image.height() * self.zoomX),
            QtCore.Qt.KeepAspectRatio,
        )
        
        # Pertahankan posisi relatif (misalnya, bagian bawah)
        if self.position == [0, 0]:  # Hanya untuk halaman pertama
            self.position = [0, self.qimage_scaled.height() - self.qlabel_image.height()]
        
        # Pastikan posisi tetap dalam batas
        self.position = (
            max(0, min(self.position[0], self.qimage_scaled.width() - self.qlabel_image.width())),
            max(0, min(self.position[1], self.qimage_scaled.height() - self.qlabel_image.height()))
        )
        self.update()

    def next_page(self):
        if self.pdf_document and self.current_page < len(self.pdf_document) - 1:
            self.current_page += 1
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
        old_zoom = self.zoomX
        self.zoomX = value
        
        # Hitung pusat pandangan saat ini (misalnya, bagian bawah)
        current_center_x = self.position[0] + self.qlabel_image.width() / 2
        current_center_y = self.position[1] + self.qlabel_image.height() / 2
        
        if self.pdf_document:
            # Render ulang halaman PDF dengan DPI baru
            self.render_pdf_page(self.current_page)
        else:
            # Skalakan gambar untuk non-PDF
            self.qimage_scaled = self.qimage.scaled(
                int(self.qlabel_image.width() * self.zoomX),
                int(self.qlabel_image.height() * self.zoomX),
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            )
        
        # Sesuaikan posisi agar pusat pandangan tetap
        new_center_x = current_center_x * (self.zoomX / old_zoom)
        new_center_y = current_center_y * (self.zoomX / old_zoom)
        self.position = (
            new_center_x - self.qlabel_image.width() / 2,
            new_center_y - self.qlabel_image.height() / 2
        )
        
        # Pastikan posisi tetap dalam batas gambar
        self.position = (
            max(0, min(self.position[0], self.qimage_scaled.width() - self.qlabel_image.width())),
            max(0, min(self.position[1], self.qimage_scaled.height() - self.qlabel_image.height()))
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
        if self.pdf_document:
            self.render_pdf_page(self.current_page)
        else:
            self.qimage_scaled = self.qimage.scaled(
                int(self.qlabel_image.width() * self.zoomX),
                int(self.qlabel_image.height() * self.zoomX),
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            )
        self.update()

    def zoom_out(self):
        if self.zoomX > 0.5:
            self.zoomX -= 0.25
            if self.pdf_document:
                self.render_pdf_page(self.current_page)
            else:
                self.qimage_scaled = self.qimage.scaled(
                    int(self.qlabel_image.width() * self.zoomX),
                    int(self.qlabel_image.height() * self.zoomX),
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation
                )
            self.update()

    def gotoPage(self, page_number):
        if self.pdf_document:
            max_page = len(self.pdf_document) - 1
            if 0 <= page_number <= max_page:
                self.current_page = page_number
                self.spin_page.setValue(self.current_page + 1)  # Sinkronisasi dengan spinbox
                self.render_pdf_page(self.current_page)
