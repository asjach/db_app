from PySide6.QtWidgets import QWidget, QDateEdit
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
        self.tbl_transaksi.itemSelectionChanged.connect(self.tbl_transaksi_selected)
        self.line_nominal_bayar.textChanged.connect(self.line_nominal_bayar_edited)
        self.btn_bayar.clicked.connect(self.bayar_tagihan)
        self.date_awal.dateChanged.connect(self.fill_tbl_transaksi)
        self.date_akhir.dateChanged.connect(self.fill_tbl_transaksi)
        self.cbo_filter_biaya.currentIndexChanged.connect(self.fill_tbl_transaksi)
        self.radio_hari.toggled.connect(self.radio_tgl_toggled)
        self.radio_bulan.toggled.connect(self.radio_tgl_toggled)
        self.radio_tahun.toggled.connect(self.radio_tgl_toggled)
        self.btn_tgl_awal_prev.clicked.connect(lambda: self.ubah_tanggal(self.date_awal, -1))
        self.btn_tgl_awal_next.clicked.connect(lambda: self.ubah_tanggal(self.date_awal, 1))
        self.btn_tgl_akhir_prev.clicked.connect(lambda: self.ubah_tanggal(self.date_akhir, -1))
        self.btn_tgl_akhir_next.clicked.connect(lambda: self.ubah_tanggal(self.date_akhir, 1))
        self.fill_cbo_petugas()
        self.fill_cbo_biaya()
        self.cbo_filter_biaya.setCurrentIndex(-1)

    def show_page(self):
        
        self.fill_tbl_siswa()
        self.fill_tbl_transaksi()
        

    def fill_tbl_siswa(self):
        data = self.SQL.siswa_aktif(
            tapel = self.parent.cbo_tapel.currentText(),
            tingkat=self.parent.cbo_tingkat.currentText(),
            kelas = self.parent.cbo_kelas.currentText(),
            search_text=self.parent.line_search.text())
        generate_table(
            data, 
            self.tbl_siswa, 
            hidden_column=[0, 3],
            stretch_column=1)

    def tbl_siswa_selected(self):
        table_selected(self.tbl_siswa, self, self.parent)
        self.fill_tbl_tagihan()
        self.label_nama.setText(self.nama_lengkap)
        self.label_kelas.setText(self.kelas)
        self.label_ortu.setText(self.orangtua)
        self.label_nis_lokal.setText(self.nis_lokal)
        self.clear_details()

    def clear_details(self):
        self.label_id_tagihan.clear()
        self.label_nama_biaya.clear()
        self.label_periode.clear()
        self.label_nominal_tagihan.clear()
        self.label_status.clear()
        self.label_terbilang.clear()
        self.line_nominal_bayar.clear()

    def fill_tbl_tagihan(self):
        if self.nis_lokal:
            data = self.SQL.tagihan_siswa(self.nis_lokal)
            generate_table(
                data=data,
                table=self.tbl_tagihan,
                hidden_column=[1],
                stretch_column=2,
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
                self.label_status.setText(data['status_tagihan'])
                self.label_nominal_tagihan.setText(format_cell_data(data['nominal_tagihan'], separator_ribuan=SEPARATOR_RIBUAN))
                self.label_sudah_bayar.setText(format_cell_data(data['sudah'], separator_ribuan=SEPARATOR_RIBUAN))
                self.line_nominal_bayar.setText(format_cell_data(data['nominal_tagihan']-data['sudah'], separator_ribuan=SEPARATOR_RIBUAN))
        
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
    
    def fill_cbo_biaya(self):
        data_biaya = self.SQL.get_jenis_biaya()
        populate_combobox(self.cbo_filter_biaya, data_biaya, 'nama_biaya', 'id')

    def fill_tbl_transaksi(self):
        tgl_awal = self.date_awal.date().toString('yyyy-MM-dd')
        tgl_akhir = self.date_akhir.date().toString('yyyy-MM-dd')
        data_transaksi = self.SQL.get_pembayaran_by_tanggal(
            tgl_awal = tgl_awal, 
            tgl_akhir=tgl_akhir,
            search_by=self.parent.cbo_search_by.currentText(),
            search_text=self.parent.line_search.text(),
            nama_biaya=self.cbo_filter_biaya.currentText()
            )
        if data_transaksi:
            generate_table(
                data=data_transaksi,
                table=self.tbl_transaksi,
                icon_akhir=":/icon/resources/icon/multiply.svg",
                fungsi_akhir=self.delete_transaksi
            )

    def tbl_transaksi_selected(self):
        table_selected(self.tbl_transaksi, self, self.parent)

    def delete_transaksi(self):
        sukses = delete_by_id('pembayaran', 'id', self.id)
        if sukses:
            self.fill_tbl_transaksi()
            self.fill_tbl_tagihan()

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
                    self.fill_tbl_tagihan()
                    self.fill_tbl_transaksi()

    def radio_tgl_toggled(self):
        if self.radio_hari.isChecked():
            # Hari ini untuk tanggal awal dan akhir
            today = QDate.currentDate()
            self.date_awal.setDate(today)
            self.date_akhir.setDate(today)
        
        elif self.radio_bulan.isChecked():
            # Tanggal 1 bulan ini sampai tanggal terakhir bulan ini
            today = QDate.currentDate()
            first_day = QDate(today.year(), today.month(), 1)
            last_day = first_day.addDays(first_day.daysInMonth() - 1)
            self.date_awal.setDate(first_day)
            self.date_akhir.setDate(last_day)
        
        elif self.radio_tahun.isChecked():
            # Ambil tahun ajaran dari QComboBox
            tapel = self.parent.cbo_tapel.currentText()  # Misalnya "2024-2025"
            try:
                # Pisahkan tahun awal dan tahun akhir dari string tapel
                start_year, end_year = map(int, tapel.split('-'))
                # Tanggal awal: 1 Juli tahun awal
                start_date = QDate(start_year, 7, 1)
                # Tanggal akhir: 30 Juni tahun akhir
                end_date = QDate(end_year, 6, 30)
                self.date_awal.setDate(start_date)
                self.date_akhir.setDate(end_date)
            except ValueError:
                # Tangani jika format tapel tidak valid (misalnya bukan "YYYY-YYYY")
                today = QDate.currentDate()
                current_year = today.year()
                if today.month() >= 7:
                    start_year = current_year
                else:
                    start_year = current_year - 1
                start_date = QDate(start_year, 7, 1)
                end_date = QDate(start_year + 1, 6, 30)
                self.date_awal.setDate(start_date)
                self.date_akhir.setDate(end_date)

    def ubah_tanggal(self, date_edit: QDateEdit, days_to_add: int):
        """
        Mengubah tanggal pada QDateEdit sebanyak 1 hari, memastikan date_awal tidak melebihi date_akhir,
        dan jika mencapai batas, geser tanggal lainnya juga.
        - date_edit: Objek QDateEdit yang akan diubah (self.date_awal atau self.date_akhir)
        - days_to_add: 1 untuk tambah 1 hari, -1 untuk kurang 1 hari
        """
        current_date = date_edit.date()
        new_date = current_date.addDays(days_to_add)
        
        if date_edit == self.date_awal:
            if new_date > self.date_akhir.date():
                # Jika date_awal akan melebihi date_akhir, geser date_akhir juga 1 hari
                self.date_akhir.setDate(self.date_akhir.date().addDays(1))
            self.date_awal.setDate(new_date)
        
        elif date_edit == self.date_akhir:
            if new_date < self.date_awal.date():
                # Jika date_akhir akan kurang dari date_awal, geser date_awal juga -1 hari
                self.date_awal.setDate(self.date_awal.date().addDays(-1))
            self.date_akhir.setDate(new_date)