from PySide6.QtWidgets import QWidget
from models.pembayaran.riwayat_biaya import RiwayatBiaya
from ui.ui_page_riwayat_biaya import Ui_Form
from utils.fungsi.general_functions import *


class PageRiwayatBiaya(QWidget, Ui_Form):
    def __init__(self, parent:None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        
        self.SQL = RiwayatBiaya()
        self.tbl_riwayat_biaya.itemSelectionChanged.connect(self.tbl_biaya_selected)
        self.tbl_riwayat_biaya.itemChanged.connect(self.update_riwayat_biaya)
        self.tbl_biaya_siswa.itemSelectionChanged.connect(self.tbl_biaya_siswa_selected)
        self.tbl_biaya_siswa.itemChanged.connect(self.update_tagihan_siswa)
        self.btn_tambah.clicked.connect(self.insert_riwayat_biaya)
        self.btn_generate_biaya.clicked.connect(self.generate_biaya_siswa)
        self.btn_clear_tagihan.clicked.connect(self.clear_tagihan_by_riwayat_biaya)

    def show_page(self):
        self.txt_tapel.setText(self.parent.cbo_tapel.currentText())
        self.fill_cbo_biaya()
        self.fill_tbl_biaya()

    def fill_cbo_biaya(self):
        data = self.SQL.get_biaya()
        populate_combobox(self.cbo_biaya, data, 'nama_biaya', 'id')
        self.cbo_biaya.setCurrentIndex(-1)

    def insert_riwayat_biaya(self):
        id_biaya = self.cbo_biaya.currentData()
        if self.line_nominal.text() != '' and id_biaya:
            sukses = self.SQL.insert_riwayat_biaya(
                id_biaya=id_biaya,
                tapel = self.txt_tapel.text(),
                periode=self.line_periode.text(),
                nominal=self.line_nominal.text()
            )
            if sukses:
                self.cbo_biaya.setCurrentIndex(-1)
                self.line_periode.clear()
                self.line_nominal.clear()
                self.fill_tbl_biaya()

    def fill_tbl_biaya(self):
        data, fields = self.SQL.get_riwayat_biaya(self.parent.cbo_tapel.currentText())
        generate_table(
            data=data,
            column_names=fields,
            table=self.tbl_riwayat_biaya,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_riwayat_biaya,
            mode_input=True
        )

    def tbl_biaya_selected(self):
        table_selected(self.tbl_riwayat_biaya, self, self.parent)
        self.id_riwayat_biaya = self.id
        if self.id not in ['', None]:
            self.txt_tapel.setText(self.tapel)
        self.fill_tbl_biaya_siswa()

    def update_riwayat_biaya(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_riwayat_biaya,
            tabel_sql='riwayat_biaya',
            primary_key='id',
            must_insert=['id_biaya', 'tapel', 'nominal'],
            updatable_column=['id_biaya', 'tapel', 'periode', 'nominal', 'tgl_mulai', 'tgl_selesai', 'catatan']
        )
        if sukses:
            self.fill_tbl_biaya()

    def delete_riwayat_biaya(self):
        id=self.id_riwayat_biaya
        if id:
            self.clear_tagihan_by_riwayat_biaya()
            delete_by_id('riwayat_biaya', 'id', id)
            self.fill_tbl_biaya()


    def clear_tagihan_by_riwayat_biaya(self):
        if self.id_riwayat_biaya:
            sukses = self.SQL.delete_tagihan_by_biaya(self.id_riwayat_biaya)
            if sukses:
                self.fill_tbl_biaya()
                self.fill_tbl_biaya_siswa()
                return sukses


    def fill_tbl_biaya_siswa(self):
        data_tagihan = self.SQL.get_tagihan_siswa_by_biaya(self.id_riwayat_biaya)
        generate_table(
            data=data_tagihan, 
            table=self.tbl_biaya_siswa,
        )

    def tbl_biaya_siswa_selected(self):
        table_selected(self.tbl_biaya_siswa, self, self.parent)
        self.id_tagihan = self.id

    def update_tagihan_siswa(self):
        sukses  = handle_item_changed(
            self.tbl_biaya_siswa,
            'tagihan',
            primary_key='id',
            must_insert=['id', 'nominal_tagihan'],
            updatable_column=['nominal_tagihan']
        )
        if sukses:
            self.fill_tbl_biaya_siswa()
    def generate_biaya_siswa(self):
        sukses = self.SQL.generate_biaya_siswa(
            id_biaya=self.id_biaya,
            id_riwayat_biaya=self.id,
            tapel=self.tapel)
        if sukses:
            self.show_page()
 