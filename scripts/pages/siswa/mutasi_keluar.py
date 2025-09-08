from ui.ui_page_mutasi_keluar import Ui_Form
from utils.fungsi.general_functions import *
from models.model_siswa import Model_Siswa
from PySide6.QtWidgets import QMainWindow, QWidget

class PageMutasiKeluar(Ui_Form, QWidget):
    def __init__(self, parent: QMainWindow = None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Model_Siswa()
        self.date_tgl_mutasi.setDate(datetime.now())
        self.signals_slots()


    def _dynamic_attributs(self):
        self.txt_jenjang = self.parent.str_jenjang
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.txt_tingkat = self.parent.quoted_daftar_tingkat
        self.txt_kelas = self.parent.quoted_daftar_kelas
        self.txt_search_by = self.parent.cbo_search_by.currentText()
        self.txt_search = self.parent.line_search.text()
        self.txt_order_by = self.parent.cbo_order_by.currentText()


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
        data = self.SQL.list_siswa_aktif(
            jenjang=self.txt_jenjang,
            tapel=self.txt_tapel,
            tingkat=self.txt_tingkat,
            kelas=self.txt_kelas,
            status_akhir='Aktif',
            search_by=self.txt_search_by,
            search_text=self.txt_search
        )
        generate_table(
            data=data,
            table=self.tbl_list_siswa,
            icon_akhir=":/icon/resources/icon/more_than.svg",
            fungsi_akhir=self.keluarkan_siswa,
            stretch_column=2,
            hidden_column=[0]
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
        tgl_keluar = self.date_tgl_mutasi.date().toString("yyyy-MM-dd")
        self.SQL.mutasikan_siswa(
            id=self.id,
            tgl_keluar=tgl_keluar,
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
            "tabel_sql": "siswa_mutasi_keluar",
            "not_updatable_column":["id", "nis_lokal"],
            "key": "id",
            "key_value": int(self.id)
        }
        sukses = update_from_table(**params)
        if sukses:
            self.show_page()
            return True
