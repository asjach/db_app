from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_with_table_widget import Ui_Form
from models.preferensi.sekolah import Sekolah

class PageSekolah(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Sekolah()
        self.tbl_widget.itemSelectionChanged.connect(self.tbl_selected)
        self.tbl_widget.itemChanged.connect(self.update_from_table)

    def show_page(self):
        self.fill_tbl_sekolah()

    def fill_tbl_sekolah(self):
        data, fields = self.SQL.get_daftar_sekolah(self.parent.line_search.text())
        generate_table(
            data = data,
            table=self.tbl_widget,
            column_names=fields,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_sekolah,
            mode_input=True
        )

    def tbl_selected(self):
        table_selected(self.tbl_widget, self, self.parent)

    def update_from_table(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_widget,
            tabel_sql='daftar_sekolah',
            primary_key='id',
            must_insert=['nama_sekolah'],
            not_updatable_column=['id']
        )
        if sukses:
            self.fill_tbl_sekolah()

    def delete_sekolah(self):
        sukses = delete_by_id('daftar_sekolah', 'id', self.id)
        if sukses:
            self.fill_tbl_sekolah()

    