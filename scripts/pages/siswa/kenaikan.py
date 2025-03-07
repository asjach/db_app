from ui.ui_page_kenaikan import Ui_Form
from utils.fungsi.general_functions import *
from models.siswa.kenaikan import Kenaikan
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QAction

class PageKenaikan(Ui_Form, QWidget):
    def __init__(self, parent: QMainWindow = None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Kenaikan()
        self.btn_naikkan.clicked.connect(self.naikkan_siswa)
        self.tidak_naik_action = QAction("Tidak Naikkan Siswa Terpilih")
        self.batal_naik_action = QAction("Batal Naik Siswa Terpilih")
        self.batal_naik_all_action = QAction("Batalkan Kenaikan Seluruh Siswa")
        self.batal_tidak_naik_action = QAction("Batal Tidak Naik Siswa")

    def _signals_slots(self):
        self.tbl_list_siswa.itemSelectionChanged.connect(
            lambda:table_selected(self.tbl_list_siswa, self, self.parent, ['id', 'nis_lokal']))
        self.tbl_siswa_naik.itemSelectionChanged.connect(
            lambda:table_selected(self.tbl_siswa_naik, self, self.parent, ['id', 'nis_lokal']))
        self.tbl_siswa_tidak_naik.itemSelectionChanged.connect(
            lambda:table_selected(self.tbl_siswa_tidak_naik, self, self.parent, ['id', 'nis_lokal']))
    
    def _dynamic_attributs(self):
        self.txt_jenjang = self.parent.cbo_jenjang.currentText()
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.txt_tingkat = self.parent.cbo_tingkat.currentText()
        self.txt_kelas = self.parent.cbo_kelas.currentText()
        self.txt_search_by = self.parent.cbo_search_by.currentText()
        self.txt_search = self.parent.line_search.text()
        self.txt_order = self.parent.cbo_order_by.currentText()
        self.txt_kolom = self.parent.cbo_kolom.currentText()
        self.next_tapel = tapel_berikutnya(self.txt_tapel)
        self.next_tingkat = f"{int(self.txt_tingkat)+1}" if self.txt_tingkat else ""
        self.next_kelas = (
            f"{int(self.txt_kelas[0])+1}{self.txt_kelas[-1]}" if self.txt_kelas else ""
        )

    def show_page(self):
        self._dynamic_attributs()
        self.fill_tbl_list_siswa()
        self.fill_tbl_siswa_naik()
        self.fill_tbl_siswa_tidak_naik()

    def fill_tbl_list_siswa(self):
        params = {
            'jenjang':self.txt_jenjang,
            'tapel':self.txt_tapel,
            'tingkat':self.txt_tingkat,
            'kelas':self.txt_kelas,
            'search_by':self.txt_search_by,
            'search_text':self.txt_search,
            'status_akhir':'Aktif',
            'order_by':self.txt_order,
        }
        params_table = {
            'stretch_column':2,
            'hidden_column':[0],
        }
        fill_table(self.tbl_list_siswa, self.SQL.list_siswa_aktif, params, params_table)

    def fill_tbl_siswa_naik(self):   
        params = {
            'jenjang':self.txt_jenjang,
            'tapel':self.next_tapel,
            'tingkat':self.next_tingkat,
            'kelas':self.next_kelas,
            'search_text':self.txt_search,
            'status_awal':"Kenaikan",
        }
        fill_table(
            self.tbl_siswa_naik,
            self.SQL.list_siswa_aktif,
            params
        )


    def fill_tbl_siswa_tidak_naik(self):
        params = {
            'jenjang':self.txt_jenjang,
            'tapel':self.next_tapel,
            'tingkat':self.txt_tingkat,
            'kelas':self.txt_kelas,
            'search_text':self.txt_search,
            'status_awal':"Mengulang",
        }
        fill_table(
            self.tbl_siswa_tidak_naik,
            self.SQL.list_siswa_aktif,
            params
        )

    def naikkan_siswa(self):
        tgl_masuk = text_to_date(self.line_tgl_naik.text())
        self.SQL.naikkan_siswa(
            self.txt_jenjang, 
            self.txt_tapel, 
            tgl_masuk)
        self.tbl_list_siswa._last_data_hash = None
        self.tbl_siswa_naik._last_data_hash = None
        self.tbl_siswa_tidak_naik._last_data_hash = None
        self.show_page()

    def tidak_naikkan_siswa(self):
        tgl_masuk = text_to_date(self.line_tgl_naik.text())
        self.SQL.tidak_naikkan_siswa(tgl_masuk, self.id)
        self.tbl_list_siswa._last_data_hash = None
        self.tbl_siswa_naik._last_data_hash = None
        self.tbl_siswa_tidak_naik._last_data_hash = None
        self.show_page()

    def batal_naik(self):
        self.SQL.batal_naik_siswa(
            self.id,
            self.txt_jenjang,
            self.txt_tapel,
            self.nis_lokal,
        )
        self.tbl_list_siswa._last_data_hash = None
        self.tbl_siswa_naik._last_data_hash = None
        self.tbl_siswa_tidak_naik._last_data_hash = None
        self.show_page()
    
    def batal_naik_all(self):
        self.SQL.batal_naik_all(
            self.txt_jenjang, 
            self.txt_tapel
            )
        self.tbl_list_siswa._last_data_hash = None
        self.tbl_siswa_naik._last_data_hash = None
        self.tbl_siswa_tidak_naik._last_data_hash = None
        self.show_page()

    def batal_tidak_naik(self):
        self.SQL.batal_tidak_naik_siswa(
            self.txt_jenjang, 
            self.txt_tapel,
            self.id,
            self.nis_lokal
            )
        self.tbl_list_siswa._last_data_hash = None
        self.tbl_siswa_naik._last_data_hash = None
        self.tbl_siswa_tidak_naik._last_data_hash = None
        self.show_page()
        
