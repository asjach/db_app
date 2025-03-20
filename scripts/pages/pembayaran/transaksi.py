from PySide6.QtWidgets import QWidget
from models.pembayaran.transaksi import Transaksi
from ui.ui_page_transaksi_pembayaran import Ui_Form
from utils.fungsi.general_functions import *


class PageTransaksi(QWidget, Ui_Form):
    def __init__(self, parent:None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Transaksi()
        self.tbl_siswa.itemSelectionChanged.connect(self.tbl_siswa_selected)
        self.tbl_tagihan.itemSelectionChanged.connect(self.tbl_tagihan_selected)

    def show_page(self):
        self.fill_tbl_siswa()
        self.fill_tbl_transaksi()

    def fill_tbl_siswa(self):
        data = self.SQL.siswa_aktif(
            tapel = self.parent.cbo_tapel.currentText(),
            tingkat=self.parent.cbo_tingkat.currentText(),
            kelas = self.parent.cbo_kelas.currentText(),
            search_text=self.parent.line_search.text()
        )
        generate_table(data, self.tbl_siswa)

    def tbl_siswa_selected(self):
        table_selected(self.tbl_siswa, self, self.parent)
        self.fill_tbl_tagihan()

    def fill_tbl_tagihan(self):
        data = self.SQL.tagihan_siswa(self.nis_lokal)
        generate_table(
            data=data,
            table=self.tbl_tagihan,
        )

    def tbl_tagihan_selected(self):
        table_selected(self.tbl_tagihan, self, self.parent)
        self.id_tagihan = self.id
        self.show_detail_tagihan()

    def show_detail_tagihan(self):
        if self.id_tagihan:
            data = self.SQL.detail_tagihan(self.id_tagihan)
            if data:
                self.label_nis_lokal.setText(data['nis_lokal'])
                self.label_nama.setText(data['nama_lengkap'])
                self.label_ortu.setText(data['orangtua'])
                self.label_id_tagihan.setText(str(data['id']))
                self.label_nama_biaya.setText(data['nama_biaya'])
                self.label_periode.setText(data['periode'])
                self.label_nominal_tagihan.setText(format_cell_data(data['nominal_tagihan']))
                self.label_status.setText(data['status_tagihan'])


    def fill_tbl_transaksi(self):...