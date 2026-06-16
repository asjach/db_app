from PySide6.QtWidgets import QWidget

from models.model_siswa import Model_Siswa
from ui.ui_page_buku_induk import Ui_Form
from utils.fungsi.general_functions import *
from utils.key_value.kolom_sql import BUKU_INDUK


class PageBukuInduk(QWidget, Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.MODEL = Model_Siswa()
        self.connect_signals()

    def connect_signals(self):
        self.cbo_opsi_data.currentIndexChanged.connect(self.show_page)

    def show_page(self):
        self.fill_tbl_daftar_siswa()

    def fill_tbl_daftar_siswa(self):
        generate_table(data=self.data_buku_induk(), table=self.tbl_daftar_siswa)

    def data_buku_induk(self):
        search_by = self.parent.cbo_search_by.currentText()
        search_text = self.parent.line_search.text()
        order_by = self.parent.cbo_order_by.currentText()
        opsi_data = self.cbo_opsi_data.currentText().lower()
        if opsi_data == "seluruh siswa":
            data = self.MODEL.get_all_siswa(
                search_by, search_text, order_by, self.opsi_kolom
            )
        else:
            data = self.MODEL.get_all_siswa_aktif(
                search_by, search_text, order_by, self.opsi_kolom, opsi_data
            )
        return data

    @property
    def opsi_kolom(self):
        kolom = BUKU_INDUK.get(
            self.parent.cbo_kolom.currentText().lower(), BUKU_INDUK["default"]
        )
        return kolom
