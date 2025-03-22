from PySide6.QtWidgets import QWidget
from models.pembayaran.transaksi import Transaksi
from ui.ui_page_transaksi_pembayaran import Ui_Form
from utils.fungsi.general_functions import *
from PySide6.QtCore import QDate, QLocale


class PageTransaksi(QWidget, Ui_Form):
    def __init__(self, parent:None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Transaksi()
        self.date_bayar.setDate(QDate.currentDate())
        self.date_awal.setDate(QDate.currentDate())
        self.date_akhir.setDate(QDate.currentDate())
        self.date_bayar.setLocale(QLocale.Indonesian)
        self.date_awal.setLocale(QLocale.Indonesian)
        self.date_akhir.setLocale(QLocale.Indonesian)
        self.tbl_siswa.itemSelectionChanged.connect(self.tbl_siswa_selected)
        self.tbl_tagihan.itemSelectionChanged.connect(self.tbl_tagihan_selected)
        self.line_nominal_bayar.textChanged.connect(self.line_nominal_bayar_edited)
        self.btn_bayar.clicked.connect(self.bayar_tagihan)
        self.date_awal.dateChanged.connect(self.fill_tbl_transaksi)
        self.date_akhir.dateChanged.connect(self.fill_tbl_transaksi)

        self.fill_cbo_petugas()
        self.fill_cbo_biaya()

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
        generate_table(
            data, 
            self.tbl_siswa, 
            hidden_column=[0], 
            stretch_column=1
            )

    def tbl_siswa_selected(self):
        table_selected(self.tbl_siswa, self, self.parent)
        self.fill_tbl_tagihan()

    def fill_tbl_tagihan(self):
        data = self.SQL.tagihan_siswa(self.nis_lokal)
        generate_table(
            data=data,
            table=self.tbl_tagihan,
            hidden_column=[0, 1],
            stretch_column=2
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
                self.label_nominal_tagihan.setText(format_cell_data(data['nominal_tagihan'], separator_ribuan=SEPARATOR_RIBUAN))
                self.label_status.setText(data['status_tagihan'])
                self.line_nominal_bayar.setText(format_cell_data(data['nominal_tagihan'], separator_ribuan=SEPARATOR_RIBUAN))
        
    def line_nominal_bayar_edited(self):
        text = self.line_nominal_bayar.text().replace(".", "")  # Hapus separator ribuan
        if not text.isdigit():
            return
        text_int = int(text)
        text_formatted = f"{text_int:,}".replace(",", ".")
        cursor_pos = self.line_nominal_bayar.cursorPosition()
        self.line_nominal_bayar.blockSignals(True)  # Hindari pemicu ulang textEdited
        self.line_nominal_bayar.setText(text_formatted)
        self.line_nominal_bayar.blockSignals(False)
        new_cursor_pos = cursor_pos + (text_formatted.count(".") - text.count("."))
        self.line_nominal_bayar.setCursorPosition(new_cursor_pos)
        txt_terbilang = terbilang(text)
        self.label_terbilang.setText(txt_terbilang.title())

    def fill_cbo_petugas(self):
        data_petugas = self.SQL.get_petugas_tu()
        populate_combobox(self.cbo_petugas, data_petugas, 'nama_lengkap', 'id_petugas')
        populate_combobox(self.cbo_filter_petugas, data_petugas, 'nama_lengkap', 'id_petugas')
        self.cbo_filter_petugas.setCurrentIndex(-1)

    
    def fill_cbo_biaya(self):
        data_biaya = self.SQL.get_jenis_biaya()
        populate_combobox(self.cbo_filter_biaya, data_biaya, 'nama_biaya', 'id')

    def fill_tbl_transaksi(self):
        tgl_awal = self.date_awal.date().toString('yyyy-MM-dd')
        tgl_akhir = self.date_akhir.date().toString('yyyy-MM-dd')
        if self.radio_rentang.isChecked():
            data_transaksi = self.SQL.get_pembayaran_by_tanggal(tgl_awal, tgl_akhir)
        elif self.radio_filter.isChecked():
            data_transaksi = self.SQL.get_pembayaran_by_filter(

            )
        elif self.radio_rentang_filter.isChecked():
            data_transaksi = ''
        generate_table(
            data=data_transaksi,
            table=self.tbl_transaksi,
        )

    def bayar_tagihan(self):
        nominal_bayar = self.line_nominal_bayar.text()
        if  nominal_bayar == '':
            QMessageBox.warning(self, "Peringatan", "Nominal tidak boleh kosong")
            return
        else:
            tgl_bayar = self.date_bayar.date().toString()
            nominal_bayar = self.line_nominal_bayar.text()
            pesan = f"Pembayaran:\nNama Siswa:\t\t{self.label_nama.text()}\ntgl_bayar:\t\t{tgl_bayar}\nNominal: \t\t{nominal_bayar}"
            msg = QMessageBox()
            msg.setWindowTitle("Konfirmasi Pembayaran")
            msg.setText(pesan)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            aksi = msg.exec()
            if aksi ==  QMessageBox.Ok:
                id_tagihan = self.label_id_tagihan.text()
                tgl_bayar = self.date_bayar.date().toPython()
                metode_pembayaran = self.cbo_metode.currentText().lower()
                id_petugas = self.cbo_petugas.currentData()
                nominal_bayar = nominal_bayar.replace(".","").replace(",",".")
                sukses = self.SQL.bayar_tagihan(
                    id_tagihan=id_tagihan,
                    tgl_bayar=tgl_bayar,
                    nominal_bayar=nominal_bayar,
                    metode_pembayaran=metode_pembayaran,
                    id_petugas=id_petugas,
                )
                if sukses:
                    QMessageBox.information(self, "Berhasil", "Berhasil melakukan input pembayaran")
                    self.show_page()