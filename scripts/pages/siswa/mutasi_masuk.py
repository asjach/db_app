# from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_mutasi_masuk import Ui_Form
from models.model_siswa import Model_Siswa
from utils.fungsi.general_functions import *
from PySide6.QtWidgets import QMainWindow, QWidget


class PageMutasiMasuk(Ui_Form, QWidget):
    def __init__(self, parent: QMainWindow = None):
        super().__init__(parent)
        self.setupUi(self)
        self.input_psb = [
            self.line_no_urut,
            self.line_nama_lengkap,
            self.cbo_jk,
            self.cbo_kelas,
            self.line_ibu,
            self.line_ayah
        ]
        self.cbo_jk.setCurrentIndex(-1)
        self.cbo_kelas.setCurrentIndex(-1)
        self.parent = parent
        self.SQL = Model_Siswa()
        self.date_tgl_masuk.setDate(datetime.now())
        self.btn_tambah.setEnabled(False)
        self.btn_terima.setEnabled(False)
        self.signals_slots()
        

    def signals_slots(self):
        self.btn_tambah.clicked.connect(self.tambah_calon_siswa)
        self.tbl_daftar_calon_siswa.itemChanged.connect(self.update_calon_siswa)
        self.tbl_daftar_calon_siswa.itemSelectionChanged.connect(self.tbl_daftar_calon_siswa_selected)
        self.tbl_diterima.itemSelectionChanged.connect(self.tbl_diterima_selected)
        self.btn_terima.clicked.connect(self._terima_calon_siswa_operations)
        self.line_nama_lengkap.textChanged.connect(self.aktivasi_btn_tambah)
        self.cbo_jk.currentIndexChanged.connect(self.aktivasi_btn_tambah)
        self.cbo_kelas.currentIndexChanged.connect(self.aktivasi_btn_tambah)


    def show_page(self):
        self.fill_daftar_calon_siswa()
        self.fill_calon_belum()
        self.fill_calon_sudah()
        self._fill_no_urut()
        self.aktivasi_btn_terima()
        self.aktivasi_btn_tambah()


    def fill_daftar_calon_siswa(self):
        opsi_kolom = "*"
        data = self.SQL.daftar_calon_siswa(
            jenjang= self.parent.str_jenjang,
                tapel=self.parent.str_tapel,
                opsi_kolom=opsi_kolom,
                search_by=self.parent.str_search_by,
                search=self.parent.last_search_text,
                order_by=self.parent.str_order_by,
        )
        generate_table(
            data=data,
            table=self.tbl_daftar_calon_siswa,
            icon_akhir= ":/icon/resources/icon/multiply.svg",
            fungsi_akhir= self.delete_pendaftar_operations
        )

    def tbl_daftar_calon_siswa_selected(self):
        table_selected(self.tbl_daftar_calon_siswa, self, self.parent, ['id'])

    def fill_calon_belum(self):
        data = self.SQL.calon_belum_diterima(
            jenjang= self.parent.str_jenjang,
                tapel=self.parent.str_tapel,
                search_by=self.parent.str_search_by,
                search=self.parent.last_search_text,
                order_by=self.parent.str_order_by
        )
        generate_table(
            data=data,
            table=self.tbl_calon_belum,
        )

    def fill_calon_sudah(self):
        data = self.SQL.calon_diterima(
            jenjang= self.parent.str_jenjang,
            tapel=self.parent.str_tapel,
            search_by=self.parent.str_search_by,
            search=self.parent.last_search_text,
            order_by=self.parent.str_order_by
        )
        generate_table(
            data=data,
            table=self.tbl_diterima,
            fungsi_akhir=self._batal_terima_siswa_operations,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            hidden_column=[1,3],
            stretch_column=2
        )
    
    def tbl_diterima_selected(self):
        table_selected(self.tbl_diterima, self, self, self.parent, ['id'])

    def update_calon_siswa(self):
        if self.id:
            try:
                params = {
                    'tabel_ui': self.tbl_daftar_calon_siswa,
                    'tabel_sql': 'siswa_psb',
                    'not_updatable_column': ['id',],
                    'key': 'id',
                    'key_value' : self.id
                }
                update_from_table(**params)
            except Exception as e:
                print(e)
                return False

    def tambah_calon_siswa(self):
        sukses = self._tambah_operations()
        if sukses:
            self._tambah_pendaftar_success_messages()

    def _tambah_operations(self):
        parameter = {
            "jenjang":  self.parent.str_jenjang,
            "tapel": self.parent.str_tapel,
            "no_urut": self.line_no_urut.text(),
            "nama_lengkap": self.line_nama_lengkap.text().upper(),
            "jk": self.cbo_jk.currentText(),
            "ayah_nama": self.line_ayah.text(),
            "ibu_nama": self.line_ibu.text(),
            "kls_masuk": self.cbo_kelas.currentText(),
            "is_accepted": "",
            "is_active": "Ya",
        }
        return self.SQL.tambah_pendaftar(**parameter)

    def _tambah_pendaftar_success_messages(self):
        self.id = None
        self.tbl_daftar_calon_siswa.clearSelection()
        clear_inputs(self.input_psb)
        self._fill_no_urut()
        self.show_page()
        self.tbl_daftar_calon_siswa.updateGeometry()
        self.tbl_daftar_calon_siswa.repaint()
        self.tbl_daftar_calon_siswa.verticalScrollBar().setValue(
            self.tbl_daftar_calon_siswa.verticalScrollBar().maximum()
        )

    def _terima_calon_siswa_operations(self):
        tgl_masuk = self.date_tgl_masuk.date().toString('yyyy-MM-dd')
        sukses = self.SQL.terima_pendaftar(
            jenjang= self.parent.str_jenjang,
            tapel=self.parent.str_tapel,
            tgl_masuk=tgl_masuk
        )
        if sukses:
            self.show_page()

    def delete_pendaftar_operations(self):
        scroll_position = self.tbl_daftar_calon_siswa.verticalScrollBar().value()
        if self.id:
            sukses = delete_by_id("siswa_psb", "id", self.id)
            if sukses:
                self.show_page()
                self.tbl_daftar_calon_siswa.verticalScrollBar().setValue(scroll_position)

    def _batal_terima_siswa_operations(self):
        sukses = self.SQL.batal_terima_pendaftar(self.id, self.kandidat_nis)
        if sukses:
            self.show_page()

    def aktivasi_btn_tambah(self):
        """Aktifkan tombol Tambah jika semua input wajib terisi"""
        nama_ok = self.line_nama_lengkap.text().strip() != ''
        jk_ok = self.cbo_jk.currentText().strip() != ''
        kelas_ok = self.cbo_kelas.currentText().strip() != ''
        self.btn_tambah.setEnabled(nama_ok and jk_ok and kelas_ok)


    def aktivasi_btn_terima(self):
        """Aktifkan tombol Terima jika ada baris di tabel calon_belum"""
        ada_data = self.tbl_calon_belum.rowCount() > 0
        self.btn_terima.setEnabled(ada_data)


    def _fill_no_urut(self):
        if self.tbl_daftar_calon_siswa.rowCount() > 0:
            max_value = self.get_max_no_urut()
            no_urut = f"{max_value + 1:04}"
            self.line_no_urut.setText(no_urut)
        else:
            self.line_no_urut.setText("0001")

    def get_max_no_urut(self):
        tabel = self.tbl_daftar_calon_siswa
        max_value = 0
        for row in range(tabel.rowCount()):
            item = tabel.item(row, 3)
            if item is not None:
                text_value = item.text().strip()
                if text_value.isdigit():
                    value = int(text_value)
                else:
                    value = 0
                if value > max_value:
                    max_value = value
        return max_value
