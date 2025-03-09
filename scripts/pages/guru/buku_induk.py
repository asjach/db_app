from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_with_table_widget import Ui_Form
from models.guru.buku_induk import BukuInduk
from utils.fungsi.general_functions import *

class PageBukuIndukGuru(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = BukuInduk()
        self.tbl_widget.currentItemChanged.connect(self.table_selected)
        self.tbl_widget.itemChanged.connect(self.update_data_guru)

    def _dynamic_attrtibutes(self):
        self.txt_order=self.parent.cbo_order_by.currentText()
        self.txt_search_by= self.parent.cbo_search_by.currentText()
        self.txt_search = self.parent.line_search.text()

    def show_page(self):
        self._dynamic_attrtibutes()
        self.fill_table()

    def fill_table(self):
        data = self.SQL.get_buku_induk_guru(
            order_by= self.txt_order,
            search_by=self.txt_search_by,
            search=self.txt_search
        )
        fill_table_with_input(
            data=data,
            table=self.tbl_widget,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_guru,
        )

    def table_selected(self):
        table_selected(self.tbl_widget, self, self.parent)

    def update_data_guru(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_widget,
            tabel_sql='guru',
            primary_key='id_guru',
            must_insert=['id_guru', 'nama_lengkap'],
            not_updatable_column=['id_guru'],
        )
        if sukses:
            self.fill_table()

    def delete_guru(self):
        sukses = delete_by_id('guru', 'id_guru', self.id_guru)
        if sukses: self.fill_table()
