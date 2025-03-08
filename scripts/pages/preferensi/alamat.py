from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_with_table_widget import Ui_Form
from models.preferensi.alamat import Alamat

class PageAlamat(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Alamat()
        self.tbl_widget.itemSelectionChanged.connect(self.tbl_alamat_selected)
        self.tbl_widget.itemChanged.connect(self.update_alamat)
        
    def show_page(self):
        self.fill_table_alamat()

    def fill_table_alamat(self):
        data, fields = self.SQL.get_alamat(self.parent.line_search.text())
        fill_table_with_input(
            data=data,
            table=self.tbl_widget,
            column_names=fields,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_alamat,
        )
    
    def tbl_alamat_selected(self):
        table_selected(self.tbl_widget, self, self.parent)

    def update_alamat(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_widget,
            tabel_sql='daftar_alamat',
            primary_key='id',
            must_insert=['kampung'],
            not_updatable_column=['id']
        )
        if sukses:
            self.fill_table_alamat()
        
    def delete_alamat(self):
        sukses = delete_by_id('daftar_alamat', 'id', self.id)
        if sukses:
            self.fill_table_alamat()
