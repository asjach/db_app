from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_ceklis_emis import Ui_Form
from models.model_siswa import Model_Siswa
from utils.fungsi.general_functions import *
from utils.key_value.kolom_sql import *

class PageCeklisEMIS(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.nis_lokal = None
        self.MODEL = Model_Siswa()
        self.connect_signals()

    def connect_signals(self):
        self.tbl_tidak.itemSelectionChanged.connect(lambda: table_selected(self.tbl_tidak, self, self.parent))
        self.tbl_ya.itemSelectionChanged.connect(lambda: table_selected(self.tbl_ya, self, self.parent))

    def show_page(self):
        self.fill_tbl_ya_tidak() 
        self.fill_tbl_tidak()
        self.fill_tbl_ya() 
    
    def fill_tbl_ya_tidak(self):
        data = self.MODEL.get_siswa_all(self.parent.last_search_text)
        generate_table(
            data=data,
            table=self.tbl_ya_tidak
        )

    def fill_tbl_tidak(self):
        data = self.MODEL.get_siswa_tidak(
            self.parent.str_tingkat, 
            self.parent.last_search_text
        )
        generate_table(
            data=data,
            table=self.tbl_tidak,
            hidden_column=[0], 
            fungsi_akhir=self.set_ya,
            icon_akhir=":/icon/resources/icon/more_than.svg"
        )

    def fill_tbl_ya(self):
        data = self.MODEL.get_siswa_ya(
            self.parent.str_tingkat, 
            self.parent.last_search_text
        )
        generate_table(
            data=data,
            table=self.tbl_ya,
            hidden_column=[0],
            fungsi_akhir=self.set_tidak,
            icon_akhir=":/icon/resources/icon/multiply.svg"
        )

    def btn_set_tidak_all(self):...

    def set_ya(self):
        sukses = self.MODEL.set_ya(self.nis_lokal)
        if sukses:
            self.show_page()

    def set_tidak(self):
        sukses = self.MODEL.set_tidak(self.nis_lokal)
        if sukses:
            self.show_page()