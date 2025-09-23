from ui.ui_page_kenaikan import Ui_Form
from utils.fungsi.general_functions import *
from models.model_siswa import Model_Siswa
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QAction

class PageKenaikan(Ui_Form, QWidget):
    def __init__(self, parent: QMainWindow = None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Model_Siswa()
        self.date_tgl_naik.setDate(datetime.now())
        self.btn_naikkan.clicked.connect(self.naikkan_siswa)
        self.tidak_naik_action = QAction("Tidak Naikkan Siswa Terpilih")
        self.batal_naik_action = QAction("Batal Naik Siswa Terpilih")
        self.batal_naik_all_action = QAction("Batalkan Kenaikan Seluruh Siswa")
        self.batal_tidak_naik_action = QAction("Batal Tidak Naik Siswa")
        self._signals_slots()

    def _signals_slots(self):
        self.tbl_list_siswa_kenaikan.itemSelectionChanged.connect(
            lambda:table_selected(self.tbl_list_siswa_kenaikan, self, self.parent, ['id', 'nis_lokal']))
        self.tbl_siswa_naik.itemSelectionChanged.connect(
            lambda:table_selected(self.tbl_siswa_naik, self, self.parent, ['id', 'nis_lokal']))
        self.tbl_siswa_tidak_naik.itemSelectionChanged.connect(
            lambda:table_selected(self.tbl_siswa_tidak_naik, self, self.parent, ['id', 'nis_lokal']))
    
    def _dynamic_attributs(self):
        self.txt_jenjang = self.parent.str_jenjang
        self.txt_tapel = self.parent.str_tapel
        self.txt_tingkat = self.parent.quoted_daftar_tingkat
        self.txt_kelas = self.parent.quoted_daftar_kelas
        self.txt_search_by = self.parent.str_search_by
        self.txt_search = self.parent.last_search_text
        self.txt_order = self.parent.str_order_by
        self.txt_kolom = self.parent.cbo_kolom.currentText()
        self.next_tapel = self.parent.str_next_tapel
        self.next_tingkat = f"'{int(self.parent.str_daftar_tingkat)+1}'" if self.txt_tingkat else ""
        self.next_kelas = (
            f"'{int(self.parent.str_kelas[0])+1}{self.parent.str_kelas[-1]}'" if self.parent.str_kelas else ""
        )

    def show_page(self):
        self._dynamic_attributs()
        self.fill_tbl_list_siswa()
        self.fill_tbl_siswa_naik()
        self.fill_tbl_siswa_tidak_naik()
        self.aktivasi_btn_naikkan()

    def fill_tbl_list_siswa(self):
        data = self.SQL.list_siswa_aktif(
            jenjang=self.txt_jenjang,
            tapel=self.txt_tapel,
            tingkat=self.txt_tingkat,
            status_akhir='Aktif',
            search_by=self.txt_search_by,
            search_text=self.txt_search
        )
        generate_table(
            data=data,
            table=self.tbl_list_siswa_kenaikan,
            hidden_column=[0],
            stretch_column=2
        )

    def fill_tbl_siswa_naik(self):   
        data = self.SQL.list_siswa_aktif(
            jenjang=self.txt_jenjang,
            tapel=self.next_tapel,
            tingkat=self.next_tingkat,
            status_awal='Kenaikan',
            search_text=self.txt_search
        )
        generate_table(
            data=data,
            table=self.tbl_siswa_naik
        )

    def fill_tbl_siswa_tidak_naik(self):
        params = {
            'jenjang':self.txt_jenjang,
            'tapel':self.next_tapel,
            'tingkat':self.txt_tingkat,
            'search_text':self.txt_search,
            'status_awal':"Mengulang",
        }
        fill_table(
            self.tbl_siswa_tidak_naik,
            self.SQL.list_siswa_aktif,
            params
        )

    def naikkan_siswa(self):
        tgl_masuk = self.date_tgl_naik.date().toString('yyyy-MM-dd')
        self.SQL.naikkan_siswa(
            self.txt_jenjang, 
            self.txt_tapel, 
            tgl_masuk)
        self.show_page()

    def tidak_naikkan_siswa(self):
        tgl_masuk = self.date_tgl_naik.date().toString('yyyy-MM-dd')
        self.SQL.tidak_naikkan_siswa(tgl_masuk, self.id)
        self.show_page()

    def batal_naik(self):
        self.SQL.batal_naik_siswa(
            self.id,
            self.txt_jenjang,
            self.txt_tapel,
            self.nis_lokal,
        )
        self.show_page()
    
    def batal_naik_all(self):
        self.SQL.batal_naik_all(
            self.txt_jenjang, 
            self.txt_tapel
            )
        self.show_page()

    def batal_tidak_naik(self):
        self.SQL.batal_tidak_naik_siswa(
            self.txt_jenjang, 
            self.txt_tapel,
            self.id,
            self.nis_lokal
            )
        self.show_page()

    def aktivasi_btn_naikkan(self):
        ada_data = self.tbl_list_siswa_kenaikan.rowCount() > 0
        self.btn_naikkan.setEnabled(ada_data)
        
