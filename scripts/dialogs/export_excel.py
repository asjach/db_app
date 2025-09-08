from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
from ui.ui_dialog_export_excel import Ui_Form
from PySide6.QtCore import Qt, QEvent
from PySide6 import QtGui
from models.model_preferensi import Model_Preferensi
from utils.fungsi.general_functions import populate_combobox, generate_table, export_to_excel, copyCells

class DialogExportExcel(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.setWindowState(Qt.WindowMaximized)
        self.setSizeGripEnabled(True)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Model_Preferensi()
        self.fill_data()
        self.connect_signals()

    def connect_signals(self):
        self.cbo_opsi_data.currentIndexChanged.connect(self.cbo_opsi_data_selected)
        self.cbo_nama_data_kolom.currentIndexChanged.connect(self.cbo_nama_data_kolom_selected)
        self.cbo_kolom.currentIndexChanged.connect(self.cbo_kolom_selected)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_preview.clicked.connect(self.show_data_in_table)
        self.btn_export.clicked.connect(self.export_data_to_excel)
        self.tableWidget.installEventFilter(self)

    def fill_data(self):
        self.fill_cbo_jenjang()
        self.fill_cbo_kelas()
        self.fill_cbo_status()
        self.fill_cbo_order()
        self.fill_cbo_nama_data_kolom()
        self.fill_plain_kolom_kolom()
        self.fill_plain_filter()
        self.fill_cbo_kolom()


    def fill_cbo_jenjang(self):
        opsi_data = self.cbo_opsi_data.currentText()
        self.cbo_jenjang.clear()
        if opsi_data == 'Siswa': 
            data = ["--Semua--", "MI", "MD", "MI-MD", "MI Saja", "MD Saja", "MI Saja/MD Saja"]
        else:
            data = ["--Semua--", "MI", "MD"]
        populate_combobox(
                self.cbo_jenjang,
                data=data
        )

#   FILL
    def fill_cbo_kelas(self):
        data_kelas = [{'kelas': '--Semua--'}]
        tingkat = None if self.cbo_tingkat.currentText() == '--Semua--' else self.cbo_tingkat.currentText()
        data = self.SQL.get_daftar_kelas(
            tapel=self.parent.cbo_tapel.currentText(),
            tingkat=tingkat
        )
        data_kelas.extend(data)
        populate_combobox(
            cbo_widget=self.cbo_kelas,
            data=data_kelas,
            text_data='kelas'
        )
    
    def fill_cbo_order(self):
        opsi_data = self.cbo_opsi_data.currentText()
        if opsi_data == 'Siswa':
            data = ["Nama Lengkap", "JK", "Ayah", "Ibu", "Alamat"]
        else:
            data = ["Nama Lengkap", "JK"]
        populate_combobox(self.cbo_order, data)

    def fill_cbo_status(self):
        opsi_data = self.cbo_opsi_data.currentText()
        if opsi_data == 'Siswa':
            data = ["Ya", "Tidak", "--Semua--"]
        else:
            data = ["Guru dan Tendik", "Guru", "Tenaga Kependidikan"]
        populate_combobox(self.cbo_status, data)


    def fill_cbo_nama_data_kolom(self):
        data = self.SQL.get_kolom_export(self.cbo_opsi_data.currentText().lower())
        populate_combobox(
            cbo_widget=self.cbo_nama_data_kolom,
            data=data,
            text_data='nama_data',
            user_data=['id', 'tabel', 'kolom_kolom', 'filter_tambahan']
        )

    def fill_plain_kolom_kolom(self):
        data = self.cbo_nama_data_kolom.currentData()
        if data:
            data_kolom_kolom = self.cbo_nama_data_kolom.currentData()['kolom_kolom']
            self.plain_kolom_kolom.setPlainText(data_kolom_kolom)

    def fill_plain_filter(self):
        data = self.cbo_nama_data_kolom.currentData()
        if data:
            data_filter = self.cbo_nama_data_kolom.currentData()['filter_tambahan']
            self.plain_filter_tambahan.setPlainText(data_filter)

    def fill_cbo_kolom(self):
        try:
            daftar_kolom_filtered = []
            if self.cbo_opsi_data.currentText() == 'Siswa':
                daftar_kolom = self.SQL.get_column_names('siswa')
            else:
                daftar_kolom = self.SQL.get_column_names('guru')
            
            kolom_exists = self.plain_kolom_kolom.toPlainText()
            list_kolom_exist = []
            if kolom_exists.strip():
                list_kolom_exist = [item.strip() for item in kolom_exists.split(",") if item.strip()]
            
            daftar_kolom_filtered = [item for item in daftar_kolom if item not in list_kolom_exist]
            
            self.cbo_kolom.blockSignals(True)  # Blokir sinyal saat mengisi ulang
            self.cbo_kolom.clear()  # Kosongkan combobox sebelum mengisi ulang
            populate_combobox(
                cbo_widget=self.cbo_kolom,
                data=daftar_kolom_filtered
            )
            self.cbo_kolom.blockSignals(False)  # Aktifkan kembali sinyal
        except Exception as e:
            print(f"Error in fill_cbo_kolom: {e}")
            self.cbo_kolom.clear()
            populate_combobox(cbo_widget=self.cbo_kolom, data=[])

#   SELECTED
    def cbo_opsi_data_selected(self):
        self.fill_cbo_jenjang()
        self.fill_cbo_order()
        self.fill_cbo_status()
        self.fill_cbo_kolom()
        self.fill_cbo_nama_data_kolom()
        self.fill_plain_kolom_kolom()
        self.fill_plain_filter()
        self.cbo_kolom.setCurrentIndex(-1)
        if self.cbo_opsi_data.currentText() == 'Siswa':
            self.frame_tingkat.setVisible(True)
            self.frame_kelas.setVisible(True)
        else:
            self.frame_tingkat.setVisible(False)
            self.frame_kelas.setVisible(False)

    def cbo_kolom_selected(self):
        selected_kolom = self.cbo_kolom.currentText()
        if selected_kolom:  # Pastikan ada nilai yang dipilih
            cursor = self.plain_kolom_kolom.textCursor()  # Dapatkan posisi kursor saat ini
            cursor.insertText(f", {selected_kolom}")  # Sisipkan teks di posisi kursor
            self.plain_kolom_kolom.setTextCursor(cursor)  # Perbarui kursor
            cursor.movePosition(QtGui.QTextCursor.End)  # Pindah ke akhir dokumen
            self.plain_kolom_kolom.setTextCursor(cursor)
            
            # Putuskan sinyal sementara untuk mencegah loop
            self.cbo_kolom.blockSignals(True)
            self.fill_cbo_kolom()  # Perbarui cbo_kolom untuk menghapus nilai yang baru ditambahkan
            self.cbo_kolom.setCurrentIndex(-1)  # Atur ulang pilihan
            self.cbo_kolom.blockSignals(False)  # Sambungkan kembali sinyal

    def cbo_nama_data_kolom_selected(self):
            self.fill_plain_kolom_kolom()
            self.fill_plain_filter()
            self.cbo_kolom.blockSignals(True)
            self.fill_cbo_kolom()  # Perbarui cbo_kolom untuk menghapus nilai yang baru ditambahkan
            self.cbo_kolom.setCurrentIndex(-1)

# CLICKED
    def btn_save_clicked(self):
        cur_index = self.cbo_nama_data_kolom.currentIndex()
        tabel = self.cbo_opsi_data.currentText()
        nama_data = self.cbo_nama_data_kolom.currentText()
        kolom_kolom = self.plain_kolom_kolom.toPlainText()
        sukses = self.SQL.save_kolom_export(
            tabel=tabel,
            nama_data=nama_data,
            kolom_kolom=kolom_kolom,
            filter_tambahan=self.plain_filter_tambahan.toPlainText()
        )
        if sukses:
            QMessageBox.information(self, "Berhasil", "Berhasil Menyimpan Data Kolom")
            self.fill_cbo_nama_data_kolom()
            self.cbo_nama_data_kolom.setCurrentIndex(-1)
            self.plain_kolom_kolom.clear()
            self.plain_filter_tambahan.clear()
            self.cbo_nama_data_kolom.setCurrentIndex(cur_index)

    def show_data_in_table(self):
        jenjang = self.cbo_jenjang.currentIndex()
        tingkat = None if self.cbo_tingkat.currentText() == '--Semua--' else self.cbo_tingkat.currentText()
        kelas = None if self.cbo_kelas.currentText() == '--Semua--' else self.cbo_kelas.currentText()
        kolom = self.plain_kolom_kolom.toPlainText()
        if self.cbo_opsi_data.currentText() == 'Siswa':
            data = self.SQL.get_data_siswa(
                kolom=kolom,
                jenjang=jenjang,
                tapel=self.parent.cbo_tapel.currentText(),
                tingkat=tingkat,
                kelas=kelas,
                status = self.cbo_status.currentText(),
                order=self.cbo_order.currentText(),
                filter_tambahan=self.plain_filter_tambahan.toPlainText()
            )
        else:
            data = self.SQL.get_data_guru(
                jenjang=jenjang,
                tapel=self.parent.cbo_tapel.currentText(),
                fungsi_jabatan=self.cbo_status.currentText(),
                kolom=kolom,
                filter_tambahan=self.plain_filter_tambahan.toPlainText()
            )
        generate_table(
            data=data,
            table=self.tableWidget
            )
        
    def export_data_to_excel(self):
        success = False
        table = self.tableWidget
        file_path, _ = QFileDialog.getSaveFileName(None, "Save Excel File", "", "Excel Files (*.xlsx)")
        if file_path:
            success, message = export_to_excel(table, file_path)
            print(message)
        if success:
            QMessageBox.information(self,"Sukses Export", message)
        else:
            QMessageBox.warning(self, "Gagal Export", message)

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
                copyCells(source)
                return True
        return super().eventFilter(source, event)