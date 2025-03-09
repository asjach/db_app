from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_with_table_widget import Ui_Form
from models.nilai.riwayat_kegiatan import RiwayatKegiatan

class PageRiwayatKegiatan(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = RiwayatKegiatan()
        self.tbl_widget.itemSelectionChanged.connect(self.table_selected)
        self.tbl_widget.itemChanged.connect(self.update_riwayat_kegiatan)

    def show_page(self):
        self.fill_table()

    def fill_table(self):
        data, fields = self.SQL.get_kegiatan_riwayat(self.parent.cbo_tapel.currentText())
        fill_table_with_input(
            data=data,
            column_names=fields,
            table=self.tbl_widget,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_riwayat_kegiatan,
        )

    def table_selected(self):
        table_selected(self.tbl_widget, self, self.parent)

    def update_riwayat_kegiatan(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_widget,
            tabel_sql='kegiatan_riwayat',
            primary_key='id',
            must_insert=['jenjang', 'tapel', 'semester', 'kegiatan'],
            not_updatable_column=['id']
        )
        if sukses:self.fill_table()

    def delete_riwayat_kegiatan(self):
        sukses = delete_by_id(
            table_sql='kegiatan_riwayat',
            id_name='id',
            id_value=self.id
        )
        if sukses:self.fill_table()