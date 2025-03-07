from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_buku_induk_guru import Ui_Form
from models.guru.guru import ModelGuru
from utils.fungsi.functions import *
from utils.fungsi.table_functions import table_selected, fill_table


class PageBukuIndukGuru(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = ModelGuru()
        self.tbl_daftar_guru.currentItemChanged.connect(
            lambda: table_selected(self.tbl_daftar_guru, self, self.parent)
        )

    def _dynamic_attrtibutes(self):
        self.txt_order=self.parent.cbo_order_by.currentText()
        self.txt_search_by= self.parent.cbo_search_by.currentText()
        self.txt_search = self.parent.line_search.text()

    def show_page(self):
        self._dynamic_attrtibutes()
        self.fill_table()

    def fill_table(self):
        get_params = {
            'order_by' : self.txt_order,
            'search_by' : self.txt_search_by,
            'search' : self.txt_search,
        }
        fill_table(
            table_name=self.tbl_daftar_guru,
            get_function=self.SQL.get_buku_induk_guru,
            get_params=get_params,
        )