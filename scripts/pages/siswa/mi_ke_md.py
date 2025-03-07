
from ui.ui_page_mi_ke_md import Ui_Form
from utils.fungsi.general_functions import *
from models.siswa.mi2md import MI2MD
from PySide6.QtWidgets import QMessageBox, QWidget, QMainWindow

class PageMI2MD(Ui_Form, QWidget):
    def __init__(self, parent: QMainWindow = None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = MI2MD()

        self.mi_tbl.itemSelectionChanged.connect(
            lambda:table_selected(self.mi_tbl, self, self.parent, ['id', 'nis_lokal'])
        )
        self.md_tbl.itemSelectionChanged.connect(
            lambda:table_selected(self.md_tbl, self, self.parent, ['id', 'nis_lokal'])
        )
        self.btn_update_ke_mi.clicked.connect(self.sesuaikan_ke_mi)
        self.btn_update_ke_md.clicked.connect(self.sesuaikan_ke_md)

    def _dynamic_attributs(self):
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.txt_tingkat = self.parent.cbo_tingkat.currentText()
        self.txt_kelas = self.parent.cbo_kelas.currentText()
        self.txt_search_by = self.parent.cbo_search_by.currentText()
        self.txt_search = self.parent.line_search.text()

    def show_page(self):
        self._dynamic_attributs()
        self.fill_tabel_mi()
        self.fill_tabel_md()
        self.fill_tbl_beda()

    def fill_tabel_mi(self):
        params = {
            'tapel':self.txt_tapel,
            'tingkat':self.txt_tingkat,
            'kelas':self.txt_kelas,
            'search_by':self.txt_search_by,
            'search_text':self.txt_search,
        }
        table_params = {
            'fungsi_akhir':self.insert_to_md_clicked,
            'icon_akhir':":/icon/resources/icon/more_than.svg",
        }
        fill_table(self.mi_tbl, self.SQL.get_mi_only, params, table_params)
        
    def fill_tabel_md(self):
        params = {
            'jenjang':'MD',
            'tapel':self.txt_tapel,
            'tingkat':self.txt_tingkat,
            'kelas':self.txt_kelas,
            'search_by':self.txt_search_by,
            'search_text':self.txt_search,
        }
        table_params = {
            'icon_akhir':":/icon/resources/icon/multiply.svg",
            'fungsi_akhir':self.batal_insert_clicked,
            'hidden_column': [5,6,7],
            'stretch_column': 2
        }
        fill_table(self.md_tbl, self.SQL.list_siswa_aktif,params, table_params)
        
    def fill_tbl_beda(self):
        params = {'tapel':self.txt_tapel,}
        fill_table(self.tbl_beda, self.SQL.get_siswa_beda_kelas, params)
        
    def sesuaikan_ke_mi(self):
        sukses = False
        tapel = self.txt_tapel
        if tapel == "":
            return
        sukses = self.SQL.update_ke_mi(tapel)
        self.md_tbl._last_data_hash = None
        self.mi_tbl._last_data_hash = None
        self.tbl_beda._last_data_hash = None

        if sukses:
            QMessageBox.information(self, "Berhasil", "Rombel siswa telah berhasil disesuaikan ke MI")
            self.fill_tbl_beda()
    
    def sesuaikan_ke_md(self):
        sukses = False
        tapel = self.txt_tapel
        if tapel == "":
            return
        sukses = self.SQL.update_ke_md(tapel)
        self.md_tbl._last_data_hash = None
        self.mi_tbl._last_data_hash = None
        self.tbl_beda._last_data_hash = None
        if sukses:
            QMessageBox.information(self, "Berhasil", "Rombel siswa telah berhasil disesuaikan ke MD")
            self.fill_tbl_beda()

    def insert_to_md_clicked(self):
        self.SQL.insert_to_md(self.id)
        self.md_tbl._last_data_hash = None
        self.mi_tbl._last_data_hash = None
        self.tbl_beda._last_data_hash = None
        self.show_page()

    def batal_insert_clicked(self):
        self.SQL.batal_insert_to_md(self.id)
        self.md_tbl._last_data_hash = None
        self.mi_tbl._last_data_hash = None
        self.tbl_beda._last_data_hash = None
        self.show_page()
        
