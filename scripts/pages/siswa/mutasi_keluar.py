from ui.ui_page_mutasi_keluar import Ui_Form
from utils.fungsi.general_functions import *
from models.siswa.mutasi_keluar import MutasiKeluar
from PySide6.QtWidgets import QMainWindow, QWidget

class PageMutasiKeluar(Ui_Form, QWidget):
    def __init__(self, parent: QMainWindow = None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = MutasiKeluar()
        self.signals_slots()


    def _dynamic_attributs(self):
        self.txt_jenjang = self.parent.cbo_jenjang.currentText()
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.txt_tingkat = self.parent.cbo_tingkat.currentText()
        self.txt_kelas = self.parent.cbo_kelas.currentText()
        self.txt_search_by = self.parent.cbo_search_by.currentText()
        self.txt_search = self.parent.line_search.text()
        self.txt_order_by = self.parent.cbo_order_by.currentText()
        self.parameter_siswa_aktif = {
            'jenjang':self.txt_jenjang,
            'tapel':self.txt_tapel,
            'tingkat':self.txt_tingkat,
            'kelas':self.txt_kelas,
            'search_by':self.txt_search_by,
            'search_text':self.txt_search,
            'order_by':self.txt_search_by,
        }
        self.params_tabel = {
            'stretch_column':2,
            'hidden_column':[0, 1, 3, 5, 6, 7],
            'icon_akhir':":/icon/resources/icon/more_than.svg",
            'fungsi_akhir':self.keluarkan_siswa
        }

    def signals_slots(self):
        self.tbl_list_siswa.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_list_siswa, self, self.parent))
        self.tbl_siswa_keluar.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_siswa_keluar, self, self.parent))
        self.tbl_siswa_keluar.itemChanged.connect(self.update_from_tabel)

    def show_page(self):
        self._dynamic_attributs()
        self.fill_tabel_daftar_siswa()
        self.fill_tabel_siswa_keluar()
    
    def fill_tabel_daftar_siswa(self):
        fill_table(
            self.tbl_list_siswa, 
            self.SQL.list_siswa_aktif, 
            self.parameter_siswa_aktif,
            self.params_tabel
            )

    def fill_tabel_siswa_keluar(self):
        params = {
            'jenjang'   :self.txt_jenjang,
            'tapel'     :self.txt_tapel,
            'order_by'  :self.txt_order_by,
            'search_by' :self.txt_search_by,
            'search'    :self.txt_search,
        }
        tabel_params = {
            'fungsi_awal':self.batal_keluar_siswa,
            'icon_awal':":/icon/resources/icon/multiply.svg",
        }

        fill_table(
            self.tbl_siswa_keluar,
            self.SQL.daftar_siswa_keluar,
            params,
            tabel_params
        )

    def keluarkan_siswa(self):
        self.SQL.mutasikan_siswa(
            id=self.id,
            tgl_keluar=text_to_date(self.line_tgl_mutasi.text()),
        )
        self.show_page()

    def batal_keluar_siswa(self):
        self.SQL.batal_keluar(
            self.txt_jenjang,
            self.txt_tapel,
            self.nis_lokal,
            self.id,
        )
        self.show_page()
    
    def update_from_tabel(self):
        params = {
            "tabel_ui": self.tbl_siswa_keluar,
            "tabel_sql": "",
            "not_updatable_column":["id", "nis_lokal"],
            "key": "id",
            "key_value": self.id
        }
        sukses = update_from_table(**params)
        if sukses:
            print("Berhasil Update")
            return True
