from PySide6.QtWidgets import QDialog
from ui.ui_dialog_input_preferensi import Ui_Form
from models.main import ModelMain
from utils.fungsi.table_functions import *
from utils.fungsi.functions import *

class DialogInputPreferensi(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.setSizeGripEnabled(True)
        self.main_model = ModelMain()
        self.id = None
        self.nilai_combo = {
            'tapel': {
                'primary_key': 'id',
                'must_insert': ['tapel', 'no_urut'],
                'not_updatable_column': ['id']
            },
            'riwayat_kelas': {
                'primary_key': 'id',
                'must_insert': ['jenjang', 'tapel', 'tingkat', 'kelas'],
                'not_updatable_column': ['id']
            },
            'jenjang': {
                'primary_key': 'id',
                'must_insert': ['jenjang'],
                'not_updatable_column': ['id']
            },
        }
        
        # Isi comboBox dengan daftar tabel yang tersedia
        for item in self.nilai_combo:
            self.comboBox.addItem(item)
        
    def show_dialog(self):
        self.fill_table()
        
        # Koneksi sinyal
        self.tabel.itemSelectionChanged.connect(lambda: table_selected(self.tabel, self))
        self.tabel.itemChanged.connect(self.on_item_changed)
        self.comboBox.currentIndexChanged.connect(self.fill_table)

    def fill_table(self):
        """Mengisi tabel dengan data terbaru dari database."""
        self.tabel.blockSignals(True)  # Matikan sementara sinyal untuk mencegah loop
        self.tabel.clearContents()  # Hapus isi tabel sebelum mengisi ulang
        self.tabel.setRowCount(0)  # Pastikan tabel kosong sebelum memuat data

        # Ambil data terbaru dari database
        data = self.main_model.get_tabel(self.comboBox.currentText(), 'id')

        # Isi tabel dengan data terbaru
        fill_table_with_input(
            data=data,
            table=self.tabel,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_data,
        )

        self.tabel.blockSignals(False)  # Nyalakan kembali sinyal setelah selesai

    def on_item_changed(self, item):
        """Menangani perubahan item pada tabel."""
        row = item.row()
        
        # Dapatkan daftar kolom yang wajib diisi
        must_insert = self.nilai_combo[self.comboBox.currentText()]['must_insert']
        
        # Cek apakah semua kolom di must_insert sudah terisi
        all_filled = all(
            self.tabel.item(row, col) and self.tabel.item(row, col).text().strip()
            for col in range(self.tabel.columnCount())
            if self.tabel.horizontalHeaderItem(col) and self.tabel.horizontalHeaderItem(col).text() in must_insert
        )

        if not all_filled:
            print("Menunggu input lengkap sebelum memproses perubahan.")
            return  # Jangan lanjutkan jika ada kolom yang masih kosong

        # Ambil informasi lain yang diperlukan
        id = self.nilai_combo[self.comboBox.currentText()]['primary_key']
        not_updatable_column = self.nilai_combo[self.comboBox.currentText()]['not_updatable_column']

        # Matikan sinyal sementara agar tidak terjadi loop pemanggilan
        self.tabel.blockSignals(True)
        sukses = handle_item_changed(
            tabel_ui=self.tabel,
            tabel_sql=self.comboBox.currentText(),
            primary_key=id,
            must_insert=must_insert,
            not_updatable_column=not_updatable_column,
        )
        self.tabel.blockSignals(False)

        if sukses:
            print("Data berhasil diperbarui, mengisi tabel kembali...")
            self.fill_table()

    def delete_data(self):
        """Menghapus data berdasarkan ID yang dipilih."""
        primary_key = self.nilai_combo[self.comboBox.currentText()]['primary_key']
        sukses = delete_by_id(self.comboBox.currentText(), primary_key, self.id)
        if sukses:
            print("Data berhasil dihapus, mengisi tabel kembali...")
            self.fill_table()
