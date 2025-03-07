from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox
from ui.ui_page_riwayat_mengajar import Ui_Form
from models.guru.riwayat_mengajar import RiwayatMengajar
from utils.fungsi.general_functions import *
from utils.key_value.kolom_sql import GURU

class PageRiwayatMengajar(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.cbo_jenjang = self.parent.cbo_jenjang
        self.cbo_tapel = self.parent.cbo_tapel
        self.SQL = RiwayatMengajar()
        self.btn_insert.clicked.connect(self.btn_insert_clicked)
        self.tbl_riwayat_mengajar.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_riwayat_mengajar, self, self.parent)
        )
        self.tbl_riwayat_mengajar.itemChanged.connect(self.update_kelas_guru)

    def show_page(self):
        self.fill_cbo_kelas()
        self.fill_cbo_guru()
        self.fill_tbl_riwayat()

    def fill_tbl_riwayat(self):
        data = self.SQL.get_riwayat_mengajar(
            self.cbo_jenjang.currentText(), 
            self.cbo_tapel.currentText()
        )
        generate_table(
            data=data,
            table=self.tbl_riwayat_mengajar,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_kelas_guru,

        )

    def delete_kelas_guru(self):
        sukses = delete_by_id('guru_kelas_mengajar', 'id', self.id)
        if sukses: self.fill_tbl_riwayat()
    
    def update_kelas_guru(self):
        sukses = update_from_table(
            tabel_sql='guru_kelas_mengajar',
            tabel_ui=self.tbl_riwayat_mengajar,
            not_updatable_column=['id'],
            key='id',
            key_value=self.id
        )
        if sukses:
            self.fill_tbl_riwayat()

    def fill_cbo_guru(self):
        self.cbo_guru.clear()
        data_guru = self.SQL.get_guru_aktif(
            jenjang=self.cbo_jenjang.currentText(),
            tapel=self.cbo_tapel.currentText()
        )
        if data_guru:
            for guru in data_guru:
                self.cbo_guru.addItem(guru['nama_lengkap'], userData=guru['id_guru'])

    def fill_cbo_kelas(self):
        self.cbo_kelas.clear()
        data_kelas = self.SQL.get_kelas_aktif(
            jenjang=self.cbo_jenjang.currentText(),
            tapel=self.cbo_tapel.currentText()
        )
        if data_kelas:
            for kelas in data_kelas:
                self.cbo_kelas.addItem(kelas['kelas'], userData=kelas['id_kelas'])

    def btn_insert_clicked(self):
        sukses = False
        try:
            id_kelas = self.cbo_kelas.currentData()
            id_guru = self.cbo_guru.currentData()
            sukses = self.SQL.insert_kelas_guru(id_kelas, id_guru)
        except Exception as e:
            print(e)
        if sukses:
            self.fill_tbl_riwayat()