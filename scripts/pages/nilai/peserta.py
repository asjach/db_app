from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_peserta import Ui_Form
from models.nilai.peserta import Peserta

class PagePeserta(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.current_index = 0
        self.SQL = Peserta()
        self.cbo_kegiatan.currentIndexChanged.connect(self.cbo_kegiatan_selected)
        self.tbl_widget.itemSelectionChanged.connect(self.table_selected)
        self.tbl_widget.itemChanged.connect(self.update_peserta)
        self.btn_generate.clicked.connect(self.generate_peserta)
        self.btn_clear.clicked.connect(self.clear_peserta)

    def show_page(self):
        self.fill_cbo_kegiatan(self.current_index)

    def fill_cbo_kegiatan(self, index):
        data_kegiatan = self.SQL.get_kegiatan(
            self.parent.cbo_jenjang.currentText(), 
            self.parent.cbo_tapel.currentText())
        self.cbo_kegiatan.clear()
        for kegiatan in data_kegiatan:
            self.cbo_kegiatan.addItem(kegiatan['kegiatan'], userData=kegiatan['id'])
        self.cbo_kegiatan.setCurrentIndex(index)

    def cbo_kegiatan_selected(self):
        self.current_index = self.cbo_kegiatan.currentIndex()
        self.fill_table()
        
    def fill_table(self):
        data, fields = self.SQL.get_peserta_kegiatan(
            id_kegiatan=self.cbo_kegiatan.currentData(),
            id_kelas=self.parent.cbo_kelas.currentData()
        )
        fill_table_with_input(
            data=data,
            column_names=fields, 
            table=self.tbl_widget,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_peserta,
        )
    
    def table_selected(self):
        table_selected(self.tbl_widget, self, self.parent)


    def update_peserta(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_widget,
            tabel_sql='kegiatan_peserta',
            primary_key='id',
            must_insert=['id_kelas', 'id_kegiatan', 'nis_lokal'],
            not_updatable_column=['id']
        )
        if sukses: self.fill_table()

    def delete_peserta(self):
        sukses = delete_by_id('kegiatan_peserta','id', self.id)
        if sukses: self.fill_table()

    def generate_peserta(self):
        sukses = False
        list_kelas = self.SQL.get_kelas_riwayat(
            self.parent.cbo_jenjang.currentText(), 
            self.parent.cbo_tapel.currentText()
        )
        for kelas in list_kelas:
            jenjang = kelas['jenjang']
            tapel = kelas['tapel']
            tingkat = kelas['tingkat']
            id_kelas = kelas['id']
            kls = kelas['kelas']
            id_kegiatan = self.cbo_kegiatan.currentData()
            kegiatan = self.cbo_kegiatan.currentText()
            if kegiatan in ['PAS', 'AS Ganjil']:
                sukses = self.SQL.generate_peserta(jenjang, tapel, id_kelas, kls, id_kegiatan)
            elif kegiatan in ['PAT', 'AS Genap']:
                if tingkat not in ['6', '9', '12']:
                    sukses = self.SQL.generate_peserta(jenjang, tapel, id_kelas, kls, id_kegiatan)
            elif kegiatan in ['UAP', 'RTR', 'NA', 'US', 'AM']:
                if tingkat in ['6', '9', '12']:
                    sukses = self.SQL.generate_peserta(jenjang, tapel, id_kelas, kls, id_kegiatan)
            else: return
        if sukses: self.fill_table()

    def clear_peserta(self):
        konfirimasi = pesan_konfirmasi("Hapus Seluruh Peserta", "Anda akan menghapus seluruh Peserta kegiatan")
        if konfirimasi:
            sukses  = self.SQL.clear_peserta(self.cbo_kegiatan.currentData())
            if sukses: self.fill_table()