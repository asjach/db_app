from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox
from utils.fungsi.general_functions import *
from ui.ui_page_pref_riwayat_kelas import Ui_Form
from models.preferensi.riwayat_kelas import RiwayatKelas

class PageRiwayatKelas(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.jenjang= None
        self.tapel = None
        self.cbo_jenjang = self.parent.cbo_jenjang
        self.cbo_tapel = self.parent.cbo_tapel
        self.SQL = RiwayatKelas()
        self.tbl_jenjang.itemSelectionChanged.connect(self.tabel_jenjang_selected)
        self.tbl_jenjang.itemChanged.connect(self.update_jenjang)
        self.tbl_tapel.itemSelectionChanged.connect(self.tabel_tapel_selected)
        self.tbl_tapel.itemChanged.connect(self.update_tapel)
        self.tbl_kelas.itemSelectionChanged.connect(self.tabel_kelas_selected)
        self.tbl_kelas.itemChanged.connect(self.update_kelas)
        self.btn_tambah_kelas.clicked.connect(self.tambah_kelas_from_list)
        self.cbo_wali_kelas.currentIndexChanged.connect(self.update_wali_kelas)

    def show_page(self):
        self.jenjang = self.cbo_jenjang.currentText()
        self.tapel = self.cbo_tapel.currentText()
        self.fill_tabel_jenjang()
        self.fill_tabel_tapel()
        self.fill_tabel_kelas()
        self.fill_cbo_wali_kelas()

    def fill_tabel_jenjang(self):
        data = self.SQL.get_jenjang()
        fill_table_with_input(
            data=data,
            table=self.tbl_jenjang,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_jenjang,
        )
    
    def tabel_jenjang_selected(self):
        table_selected(self.tbl_jenjang, self, self.parent)
        self.fill_tabel_kelas()
        self.fill_cbo_wali_kelas()

    def update_jenjang(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_jenjang,
            tabel_sql='jenjang',
            primary_key='id',
            must_insert=['jenjang'],
            not_updatable_column=['id'],
            )
        if sukses:
            self.fill_tabel_jenjang()

    def delete_jenjang(self):
        sukses = delete_by_id('jenjang', 'id', self.id)
        if sukses: self.fill_tabel_jenjang()


    def fill_tabel_tapel(self):
        data = self.SQL.get_tapel()
        fill_table_with_input(
            data=data,
            table=self.tbl_tapel,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_tapel,
        )

    def tabel_tapel_selected(self):
        table_selected(self.tbl_tapel, self, self.parent)
        self.fill_tabel_kelas()
        self.fill_cbo_wali_kelas()

    def update_tapel(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_tapel,
            tabel_sql='tapel',
            primary_key='id',
            must_insert=['tapel'],
            not_updatable_column=['id'],
            )
        if sukses:
            self.fill_tabel_tapel()

    def delete_tapel(self):
        sukses = delete_by_id('tapel', 'id', self.id)
        if sukses: self.fill_tabel_tapel()

    def fill_tabel_kelas(self):
        data, kolom = self.SQL.get_kelas(self.jenjang, self.tapel)
        fill_table_with_input(
            data=data,
            table=self.tbl_kelas,
            column_names=kolom,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_kelas,
        )

    def tabel_kelas_selected(self):
        table_selected(self.tbl_kelas, self, self.parent, ['id'])
        self.id_kelas = self.id

    def update_kelas(self):
        sukses = handle_item_changed(
            tabel_ui=self.tbl_kelas,
            tabel_sql='kelas_riwayat',
            primary_key='id',
            must_insert=['jenjang', 'tapel', 'tingkat', 'kelas'],
            not_updatable_column=['id'],
            )
        if sukses:
            self.fill_tabel_kelas()

    def delete_kelas(self):
        sukses = delete_by_id('kelas_riwayat', 'id', self.id)
        if sukses: self.fill_tabel_kelas()

    def tambah_kelas_from_list(self):
        teks = self.line_tambah_kelas.text()
        list_kelas = [kelas.strip() for kelas in teks.split(", ")]
        if teks != "":
            for kelas in list_kelas:
                tingkat = kelas[:-1]
                self.SQL.tambah_kelas(
                    jenjang = self.jenjang,
                    tapel=self.tapel,
                    tingkat=tingkat,
                    kelas=kelas
                )
            self.fill_tabel_kelas()
            self.line_tambah_kelas.clear()
        else:
            QMessageBox.warning(self, "Informasi", "Isi list kelas terlebih dahulu")

    def fill_cbo_wali_kelas(self):
        self.cbo_wali_kelas.clear()
        data_guru = self.SQL.daftar_guru(self.jenjang, self.tapel)
        for guru in data_guru:
            self.cbo_wali_kelas.addItem(guru['nama_lengkap'], userData=guru['id_guru'])
        
    def update_wali_kelas(self):
        sukses = False
        if self.id_kelas:
            sukses = self.SQL.update_wali_kelas(self.id_kelas, self.cbo_wali_kelas.currentData())
        if sukses:
            self.fill_tabel_kelas()