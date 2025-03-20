from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_biaya import Ui_Form
from models.preferensi.biaya import Biaya

class PageBiaya(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Biaya()
        self.tbl_widget.itemSelectionChanged.connect(self.tbl_biaya_selected)
        self.tbl_widget.itemChanged.connect(self.update_biaya)
        # self.btn_update.clicked.connect(self.update_sql_insert)

    def show_page(self):
        self.fill_tbl_biaya()

    def fill_tbl_biaya(self):
        data, fields = self.SQL.get_jenis_biaya(search_text=self.parent.line_search.text())
        generate_table(
            data=data,
            column_names=fields,
            table=self.tbl_widget,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_biaya,
            mode_input=True
        )

    def tbl_biaya_selected(self):
        table_selected(self.tbl_widget, self, self.parent)
        # self.plain_sql_insert.setPlainText(self.sql_insert)

    def update_biaya(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_widget,
            tabel_sql='biaya',
            primary_key='id',
            must_insert=['nama_biaya'],
            not_updatable_column=['id']
        )
        if sukses:
            self.fill_tbl_biaya()

    def delete_biaya(self):
        delete_by_id(
            table_sql='biaya',
            id_name='id',
            id_value=self.id
        )
        self.fill_tbl_biaya()

    # def update_sql_insert(self):
    #     sukses = self.SQL.update_sql_insert(self.id, self.plain_sql_insert.toPlainText())
    #     if sukses:
    #         self.fill_tbl_biaya()
    #         self.plain_sql_insert.clear()
                