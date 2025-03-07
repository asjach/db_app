from ui.ui_page_kelulusan import Ui_Form
from utils.fungsi.functions import *
from models.siswa.kelulusan import Kelulusan
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QWidget
from utils.fungsi.table_functions import table_selected, fill_table, update_from_table

class PageKelulusan(Ui_Form, QWidget):
    def __init__(self, parent: QMainWindow = None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Kelulusan()
        self.tidak_lulus_action = QAction("Tidak Luluskan Siswa Terpilih")
        self.batal_lulus_action = QAction("Batal Lulus Siswa Terpilih")
        self.batal_lulus_all_action = QAction("Batalkan Kelulusan Seluruh Siswa")
        self.batal_tidak_lulus_action = QAction("Batal Tidak Lulus Siswa")
        self._signals_slots()
        
    def _dynamic_attributs(self):
        self.txt_jenjang = self.parent.cbo_jenjang.currentText()
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.txt_tingkat = self.parent.cbo_tingkat.currentText()
        self.txt_kelas = self.parent.cbo_kelas.currentText()
        self.txt_search_by = self.parent.cbo_search_by.currentText()
        self.txt_search = self.parent.line_search.text()
        self.txt_order = self.parent.cbo_order_by.currentText()
        self.next_tapel = tapel_berikutnya(self.txt_tapel)
        self.next_tingkat = f"{int(self.txt_tingkat)+1}" if self.txt_tingkat else ""
        self.next_kelas = (
            f"{int(self.txt_kelas[0])+1}{self.txt_kelas[-1]}" if self.txt_kelas else ""
        )

    def _signals_slots(self):
        self.btn_luluskan.clicked.connect(self.luluskan_siswa)
        self.tbl_list_siswa.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_list_siswa,self, self.parent)
        )
        self.tbl_siswa_lulus.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_siswa_lulus,self, self.parent)
            )
        self.tbl_siswa_tidak_lulus.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_siswa_tidak_lulus,self, self.parent)
            )
        self.tbl_siswa_lulus.itemChanged.connect(self.update_detail_lulusan)

    def show_page(self):
        self._dynamic_attributs()
        self.fill_tbl_list_siswa()
        self.fill_tbl_siswa_lulus()
        self.fill_tbl_siswa_tidak_lulus()

    def fill_tbl_list_siswa(self):
        params = {
           'jenjang':self.txt_jenjang,
            'tapel':self.txt_tapel,
            'tingkat':"6",
            'kelas': '',
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

    def fill_tbl_siswa_lulus(self):    
        params = {
            'jenjang':self.txt_jenjang,
            'tapel':self.txt_tapel,
            'search_by': self.txt_search_by,
            'search_text':self.txt_search,
            'order_by': self.txt_order
        } 
        fill_table(self.tbl_siswa_lulus, self.SQL.siswa_lulus, params)   


    def fill_tbl_siswa_tidak_lulus(self):
        params = {
            'jenjang':self.txt_jenjang,
            'tapel':self.next_tapel,
            'tingkat':'6',
            'kelas':'',
            'status_awal':"Mengulang",
            'status_akhir':"Aktif",
            'search_text':self.txt_search,
            'search_by':self.txt_search_by,
            'order_by':self.txt_order,
        }
        fill_table(
            self.tbl_siswa_tidak_lulus,
            self.SQL.list_siswa_aktif,
            params
        )

    def update_detail_lulusan(self):
        params = {
            'tabel_ui': self.tbl_siswa_lulus,
            'tabel_sql': 'siswa_lulusan',
            'not_updatable_column': ['id', 'nis_lokal'],
            'key': 'id',
            'key_value':self.id
        }
        update_from_table(**params)

    def luluskan_siswa(self):
        tgl_lulus = text_to_date(self.line_tgl_lulus.text())
        self.SQL.luluskan_siswa(
            self.txt_jenjang, 
            self.txt_tapel, 
            tgl_lulus)
        self.tbl_list_siswa._last_data_hash = None
        self.tbl_siswa_lulus._last_data_hash = None
        self.tbl_siswa_tidak_lulus._last_data_hash = None
        self.show_page()

    def tidak_luluskan_siswa(self):
        tgl_tidak_lulus = text_to_date(self.line_tgl_lulus.text())
        self.SQL.tidak_luluskan_siswa(
            self.txt_tapel,
            tgl_tidak_lulus, 
            self.id
            )
        self.tbl_list_siswa._last_data_hash = None
        self.tbl_siswa_lulus._last_data_hash = None
        self.tbl_siswa_tidak_lulus._last_data_hash = None
        self.show_page()

    def batal_lulus(self):
        self.SQL.batal_lulus_siswa(
            self.txt_jenjang,
            self.txt_tapel,
            self.nis_lokal,
            self.id
        )
        self.tbl_list_siswa._last_data_hash = None
        self.tbl_siswa_lulus._last_data_hash = None
        self.tbl_siswa_tidak_lulus._last_data_hash = None
        self.show_page()
    
    def batal_lulus_all(self):
        self.SQL.batal_lulus_semua(
            self.txt_jenjang, 
            self.txt_tapel
            )
        self.tbl_list_siswa._last_data_hash = None
        self.tbl_siswa_lulus._last_data_hash = None
        self.tbl_siswa_tidak_lulus._last_data_hash = None
        self.show_page()

    def batal_tidak_lulus(self):
        self.SQL.batal_tidak_naik_siswa(
            self.txt_jenjang, 
            self.txt_tapel,
            self.id,
            self.nis_lokal
            )
        self.tbl_list_siswa._last_data_hash = None
        self.tbl_siswa_lulus._last_data_hash = None
        self.tbl_siswa_tidak_lulus._last_data_hash = None
        self.show_page()

    # def eventFilter(self, source, event):
    #     if event.type() == QEvent.ContextMenu:
    #         self.handle_context_menu(source)
    #         action = self.parent.cmenu.exec(source.mapToGlobal(event.pos()))
    #         if action == self.tidak_lulus_action:
    #             self.tidak_luluskan_siswa()
    #         elif action == self.batal_lulus_action:
    #             self.batal_lulus()
    #         elif action == self.batal_lulus_all_action:
    #             self.batal_lulus_all()
    #         elif action == self.batal_tidak_lulus_action:
    #             self.batal_tidak_lulus()
    #         elif action == self.parent.hideshow_frame_action:
    #             show_frame(self.frame_kiri)
    #             show_frame(self.tbl_siswa_tidak_lulus)
    #     return super().eventFilter(source, event)

    # def handle_context_menu(self, source):
    #     self.parent.cmenu.clear()
    #     if source in [self.tbl_list_siswa]:
    #         self.parent.cmenu.addActions(
    #             [
    #                 self.tidak_lulus_action,
    #                 self.parent.hideshow_frame_action,
    #             ]
    #     )
    #     elif source == self.tbl_siswa_lulus:
    #         self.parent.cmenu.addActions(
    #             [
    #                 self.batal_lulus_action,
    #                 self.batal_lulus_all_action,
    #                 self.parent.hideshow_frame_action,
    #             ]
    #         )
    #     elif source == self.tbl_siswa_tidak_lulus:
    #         self.parent.cmenu.addActions(
    #             [
    #                 self.batal_tidak_lulus_action,
    #                 self.parent.hideshow_frame_action,
    #             ]
    #         )