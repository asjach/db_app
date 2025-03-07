from PySide6.QtWidgets import QWidget

from ui.ui_page_rekap_siswa import Ui_Form


class PageBukuInduk(QWidget, Ui_Form):
    def __init__(self, parent:None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        