from ui.ui_main_2 import Ui_MainWindow
from PySide6.QtCore import Qt, QPoint, Slot, QEvent
from PySide6.QtWidgets import QMainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Window frameless
        self.setWindowFlags(
            Qt.Window
            | Qt.FramelessWindowHint
            | Qt.WindowSystemMenuHint
            | Qt.WindowCloseButtonHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        )

        # state awal
        self._mousePressed = False
        self._mousePos = None
        self._windowPos = None

        # maximize by default
        self.showMaximized()

        # setup tombol sesuai state
        self.btn_restore.setVisible(True)
        self.btn_maximize.setVisible(False)

        # pasang sinyal
        self.connect_signals()

        # kursor drag di area window_dragger
        self.window_dragger.setCursor(Qt.SizeAllCursor)

    def connect_signals(self):
        self.btn_close.clicked.connect(self.on_btn_close_clicked)
        self.btn_minimize.clicked.connect(self.on_btn_minimize_clicked)
        self.btn_maximize.clicked.connect(self.on_btn_maximize_clicked)
        self.btn_restore.clicked.connect(self.on_btn_restore_clicked)

        # pasang event filter hanya ke area drag
        self.window_dragger.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.window_dragger:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self._mousePressed = True
                self._mousePos = event.globalPos()
                self._windowPos = self.pos()
                return True

            elif event.type() == QEvent.MouseMove and self._mousePressed:
                if self.windowState() == Qt.WindowMaximized:
                    # restore dulu
                    self.on_btn_restore_clicked()
                    # letakkan window di bawah mouse
                    self.move(self._mousePos - QPoint(
                        self.window_dragger.width() // 2,
                        self.window_dragger.height() // 2,
                    ))
                    self._windowPos = self.pos()
                self.move(self._windowPos + (event.globalPos() - self._mousePos))
                return True

            elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
                self._mousePressed = False
                return True

            elif event.type() == QEvent.MouseButtonDblClick and event.button() == Qt.LeftButton:
                if not bool(self.windowState() & Qt.WindowMaximized):
                    self.on_btn_maximize_clicked()
                else:
                    self.on_btn_restore_clicked()
                return True

        return super().eventFilter(obj, event)

    # -----------------------------
    # Tombol kontrol
    # -----------------------------
    @Slot()
    def on_btn_close_clicked(self):
        self.close()

    @Slot()
    def on_btn_minimize_clicked(self):
        self.setWindowState(Qt.WindowMinimized)

    @Slot()
    def on_btn_maximize_clicked(self):
        self.setWindowState(Qt.WindowMaximized)
        self.btn_restore.setVisible(True)
        self.btn_maximize.setVisible(False)

    @Slot()
    def on_btn_restore_clicked(self):
        self.setWindowState(Qt.WindowNoState)
        self.btn_restore.setVisible(False)
        self.btn_maximize.setVisible(True)
