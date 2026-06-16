from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_prestasi import Ui_Form
from models.model_nilai import Model_Nilai

class PagePrestasi(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.id_kegiatan = None
        self.id_peserta = None
        self.cur_kegiatan_idx = None
        self.SQL = Model_Nilai()
        self.tbl_prestasi.itemSelectionChanged.connect(self.tbl_prestasi_selected)
        self.tbl_prestasi.itemChanged.connect(self.update_prestasi)
        self.tbl_peserta.itemSelectionChanged.connect(self.tbl_peserta_selected)
        self.line_search.textChanged.connect(self.fill_tbl_peserta)


    def show_page(self):
        self.txt_jenjang = self.parent.str_jenjang
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.fill_cbo_kegiatan()
        self.fill_tbl_peserta()
        self.fill_tbl_prestasi()
    
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

    def refresh(self):
        self.fill_tbl_prestasi()

    def fill_tbl_peserta(self):
        data= self.SQL.get_peserta_all(
            id_kegiatan=self.cbo_kegiatan.currentData(),
                kelas=self.parent.quoted_daftar_kelas,
                search_text=self.line_search.text()
        )
        generate_table(
            data=data, 
            table=self.tbl_peserta,
            hidden_column=[0, 1],
            fungsi_akhir=self.tambah_prestasi_peserta,
            icon_akhir=":/icon/resources/icon/more_than.svg",
            )
        
    def tbl_peserta_selected(self):
        table_selected(self.tbl_peserta, self, self.parent)
        self.id_peserta = self.id
        
    def fill_tbl_prestasi(self):
        data= self.SQL.get_prestasi_kegiatan(id_kegiatan=self.cbo_kegiatan.currentData(),
        )
        generate_table(
            data=data,
            table=self.tbl_prestasi,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_prestasi,
        )

    def tbl_prestasi_selected(self):
        table_selected(self.tbl_prestasi, self, self.parent)
        self.id_prestasi = self.id


    def update_prestasi(self, item:QTableWidgetItem):
        update_from_table_v2(
            tabel_ui=self.tbl_prestasi,
            tabel_sql='nilai_prestasi',
            item=item,
            updatable_column=['jenis_prestasi', 'keterangan'],
            key='id',
            key_value=self.id
        )

    def delete_prestasi(self):
        sukses = delete_by_id('nilai_prestasi','id', self.id_prestasi)
        if sukses: self.refresh()

    def tambah_prestasi_peserta(self):
        if self.id_peserta:
            sukses = self.SQL.tambah_prestasi_siswa(self.id_peserta)
        if sukses:
            self.fill_tbl_prestasi()