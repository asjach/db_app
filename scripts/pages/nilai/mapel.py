from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_mapel_kegiatan import Ui_Form
from models.nilai.mapel import Mapel

class PageMapel(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.id_kelas = None
        self.kelas = None
        self.data_id_mapel = None
        self.id_kegiatan = None
        self.cur_kegiatan_idx = None
        self.SQL = Mapel()
        self.cbo_kegiatan.currentIndexChanged.connect(self.cbo_kegiatan_selected)
        self.tbl_mapel.itemSelectionChanged.connect(self.tbl_mapel_selected)
        self.tbl_mapel.itemChanged.connect(self.update_mapel)
        self.tbl_list_mapel.itemSelectionChanged.connect(self.tbl_list_mapel_selected)
        self.cbo_guru.textActivated.connect(self.cbo_guru_selected)
        self.btn_tambah.clicked.connect(self.tambah_mapel)
        self.btn_hapus.clicked.connect(self.delete_mapel)
        self.btn_salin.clicked.connect(self.salin_dari_pas)
        self.btn_clear_mapel.clicked.connect(self.clear_mapel_by_kegiatan)

    def show_page(self):
        self.txt_jenjang = self.parent.cbo_jenjang.currentText()
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.txt_tingkat = self.parent.cbo_tingkat.currentText()
        self.txt_kelas = self.parent.cbo_kelas.currentText()
        self.fill_cbo_guru()
        self.fill_cbo_kegiatan()
        self.fill_tbl_mapel()
        self.fill_tbl_list_mapel()
        
        
    # CBO KEGIATAN
    def fill_cbo_kegiatan(self): 
        data = self.SQL.get_kegiatan(
            self.txt_jenjang, 
            self.txt_tapel
        )
        self.cbo_kegiatan.blockSignals(True)
        populate_combobox(self.cbo_kegiatan, data, 'kegiatan', 'id')
        if self.cur_kegiatan_idx:
            self.cbo_kegiatan.setCurrentIndex(self.cur_kegiatan_idx)
        else:
            self.cbo_kegiatan.setCurrentIndex(0)
        self.cbo_kegiatan.blockSignals(False)

    def cbo_kegiatan_selected(self):
        if self.cbo_kegiatan.currentText() in ['UAP', 'NA', 'US', 'RTR']:
            self.txt_tingkat = '6'
        self.fill_tbl_mapel()
        self.fill_tbl_list_mapel()
        self.cur_kegiatan_idx = self.cbo_kegiatan.currentIndex()

    # CBO_GURU
    def fill_cbo_guru(self):
        data = self.SQL.get_guru_aktif(self.txt_jenjang, self.txt_tapel)
        self.cbo_guru.blockSignals(True)
        populate_combobox(self.cbo_guru, data, 'nama_lengkap', 'id_guru')
        self.cbo_guru.blockSignals(False)

    def cbo_guru_selected(self):
        sukses = False
        data = self.data_id_mapel
        id_guru = self.cbo_guru.currentData()
        if data:
            try:
                for item in data:
                    sukses |= update_from_controls('mapel_riwayat', 'id', item['id'], **{'id_guru': id_guru})
                if sukses:
                    self.tbl_mapel.clearSelection()
                    self.fill_tbl_mapel()
            except Exception as e:
                print(f'Terjadi error saat update guru {e}')

    # TABEL MAPEL
    def fill_tbl_mapel(self):
        data, fields = self.SQL.get_mapel(
            self.txt_jenjang, 
            self.txt_tapel, 
            self.txt_tingkat, 
            self.txt_kelas,
            self.cbo_kegiatan.currentText()
            )
        fill_table_with_input(
            data=data, 
            table=self.tbl_mapel, 
            column_names=fields,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_mapel,
            )

    def tbl_mapel_selected(self):
        self.data_id_mapel = table_selected(self.tbl_mapel, self, self.parent)

    def tambah_mapel(self):
        id_kelas = self.parent.cbo_kelas.currentData()
        id_kegiatan = self.cbo_kegiatan.currentData()
        list_mapel = [input.strip() for input in self.list_input_pelajaran.text().split(",") if input.strip()]
        if not id_kelas or not id_kegiatan or not list_mapel: 
            return
        for mapel in list_mapel:
            self.SQL.insert_by_list_mapel(id_kelas, id_kegiatan, mapel)
        self.fill_tbl_mapel()
        self.fill_tbl_list_mapel()
        self.list_input_pelajaran.clear()

    def update_mapel(self):
        if self.data_id_mapel:
            sukses = handle_item_changed(
                tabel_ui=self.tbl_mapel,
                tabel_sql='mapel_riwayat',
                primary_key='id',
                must_insert=['id_kelas', 'id_kegiatan', 'mapel'],
                not_updatable_column=['id'],
            )
            if sukses:
                self.fill_tbl_mapel()
                self.fill_tbl_list_mapel()

    def delete_mapel(self):
        if self.data_id_mapel:
            for data in self.data_id_mapel:
                if data['id'] != None:
                    delete_by_id('mapel_riwayat', 'id', data['id'])
        self.fill_tbl_mapel()
        self.fill_tbl_list_mapel()
        
    def fill_tbl_list_mapel(self):
        data = self.SQL.get_mapel_list(
            self.txt_jenjang,
            self.txt_tapel,
            self.cbo_kegiatan.currentText())
        generate_table(data = data,table=self.tbl_list_mapel)

    def tbl_list_mapel_selected(self):
        table_selected(self.tbl_list_mapel, self, self.parent)

    def salin_dari_pas(self):
        if self.cbo_kegiatan.currentText() == 'PAT':
            sukses = self.SQL.insert_by_kegiatan_mapel(
                self.txt_jenjang,
                self.txt_tapel,
                self.cbo_kegiatan.currentData()
            )
            if sukses:
                self.fill_tbl_mapel()
                self.fill_tbl_list_mapel()

    def clear_mapel_by_kegiatan(self):
        if self.cbo_kegiatan.currentData():
            sukses = self.SQL.clear_mapel(self.id_kegiatan)
            if sukses:
                self.fill_tbl_mapel()
                self.fill_tbl_list_mapel()




        