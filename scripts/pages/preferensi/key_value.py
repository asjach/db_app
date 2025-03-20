from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_with_table_widget import Ui_Form
from models.preferensi.key_value import KeyValue

class PageKeyValue(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = KeyValue()
        self.tbl_widget.itemSelectionChanged.connect(self.tbl_key_value_selected)
        self.tbl_widget.itemChanged.connect(self.update_key_value)

    def show_page(self):
        self.fill_table()

    def fill_table(self):
        data, fields = self.SQL.get_key_value(self.parent.line_search.text())
        generate_table(
            data=data,
            column_names=fields,
            table=self.tbl_widget,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_key_value,
            mode_input=True

        )

    def tbl_key_value_selected(self):
        table_selected(self.tbl_widget, self, self.parent)
    
    def update_key_value(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_widget,
            tabel_sql='key_value',
            primary_key='id',
            must_insert=['kunci'],
            not_updatable_column=['id']
        )
        if sukses:
            self.fill_table()

    def delete_key_value(self):
        sukses = delete_by_id(
            table_sql='key_value',
            id_name='id',
            id_value=self.id
        )
        if sukses:
            self.fill_table()