from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_pref_alamat import Ui_Form
from models.preferensi.sekolah import Sekolah

class PageSekolah(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Sekolah()

    def show_page(self):
        self.fill_tbl_sekolah()

    def fill_tbl_sekolah(self):
        data, fields = self.SQL.get_daftar_sekolah(self.parent.line_search.text())
        fill_table_with_input(
            data = data,
            table=self.tbl_alamat,
            column_names=fields,
        )