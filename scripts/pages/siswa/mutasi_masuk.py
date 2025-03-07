# from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_mutasi_masuk import Ui_Form
from models.siswa.mutasi_masuk import MutasiMasuk
from utils.fungsi.general_functions import *
from PySide6.QtWidgets import QMainWindow, QWidget

class PageMutasiMasuk(Ui_Form, QWidget):
    def __init__(self, parent: QMainWindow = None):
        super().__init__(parent)
        self.setupUi(self)
        self.cbo_jk.setCurrentIndex(-1)
        self.cbo_kelas.setCurrentIndex(-1)
        self.parent = parent
        self.SQL = MutasiMasuk()
        self.signals_slots()
    
    def _dynamic_attributs(self):
        self.txt_jenjang = self.parent.cbo_jenjang.currentText()
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.txt_search_by = self.parent.cbo_search_by.currentText()
        self.txt_search = self.parent.line_search.text()
        self.txt_order = self.parent.cbo_order_by.currentText()
        self.input_psb = [
            self.line_no_urut,
            self.line_nama_lengkap,
            self.cbo_jk,
            self.cbo_kelas,
        ]

    def signals_slots(self):
        self.btn_tambah.clicked.connect(self.tambah_calon_siswa)
        self.tbl_daftar_calon_siswa.itemChanged.connect(self.update_calon_siswa)
        self.tbl_daftar_calon_siswa.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_daftar_calon_siswa, self, self.parent, 
            ['id', 'kandidat_nis', 'nama_lengkap'])
        )
        self.tbl_diterima.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_diterima, self, self.parent, ['id'])
        )
        self.btn_terima.clicked.connect(self._terima_calon_siswa_operations)
        self.btn_batal.clicked.connect(self._batal_terima_siswa_operations)
        self.line_nama_lengkap.textChanged.connect(self._cek_input)
        self.cbo_jk.currentIndexChanged.connect(self._cek_input)
        self.cbo_kelas.currentIndexChanged.connect(self._cek_input)
        

    def show_page(self):
        self._cek_input()
        self._dynamic_attributs()
        self.fill_daftar_calon_siswa()
        self.fill_calon_belum()
        self.fill_calon_sudah()
        self._fill_no_urut()

    def fill_daftar_calon_siswa(self):
        opsi_kolom = "*"
        fill_table(
            table_name=self.tbl_daftar_calon_siswa,
            get_function=self.SQL.daftar_calon_siswa,
            table_params={
                'icon_akhir':":/icon/resources/icon/multiply.svg",
                'fungsi_akhir':self.delete_pendaftar_operations
            },
            get_params={
                'jenjang': self.txt_jenjang,
                'tapel':self.txt_tapel,
                'opsi_kolom':opsi_kolom,
                'search_by':self.txt_search_by,
                'search':self.txt_search,
                'order_by':self.txt_order,
            }
        )

    def fill_calon_belum(self):
        fill_table(
            table_name=self.tbl_calon_belum,
            get_function=self.SQL.calon_belum_diterima,
            get_params={
                'jenjang': self.txt_jenjang,
                'tapel':self.txt_tapel,
                'search_by':self.txt_search_by,
                'search':self.txt_search,
                'order_by':self.txt_order
            },
        )

    def fill_calon_sudah(self):
        fill_table(
            table_name=self.tbl_diterima,
            get_function=self.SQL.calon_diterima,
            get_params={
                'jenjang': self.txt_jenjang,
                'tapel':self.txt_tapel,
                'search_by':self.txt_search_by,
                'search':self.txt_search,
                'order_by':self.txt_order
            }
        )

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
            self.tbl_daftar_calon_siswa._last_data_hash = None
            self._tambah_pendaftar_success_messages()
        

    def _tambah_operations(self):
        parameter = {
            "jenjang":  self.txt_jenjang,
            "tapel": self.txt_tapel,
            "no_urut": self.line_no_urut.text(),
            "nama_lengkap": self.line_nama_lengkap.text().upper(),
            "jk": self.cbo_jk.currentText(),
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
        tgl_masuk = text_to_date(self.line_tgl_masuk.text())
        sukses = self.SQL.terima_pendaftar(
            jenjang= self.txt_jenjang,
            tapel=self.txt_tapel,
            tgl_masuk=tgl_masuk
        )
        if sukses:
            self.tbl_daftar_calon_siswa._last_data_hash = None
            self.show_page()

    def delete_pendaftar_operations(self):
        scroll_position = self.tbl_daftar_calon_siswa.verticalScrollBar().value()
        if self.id:
            sukses = delete_by_id("siswa_psb", "id", self.id)
            if sukses:
                self.tbl_daftar_calon_siswa._last_data_hash = None
                self.show_page()
                self.tbl_daftar_calon_siswa.verticalScrollBar().setValue(scroll_position)

    def _batal_terima_siswa_operations(self):
        sukses = self.SQL.batal_terima_pendaftar(self.id, self.kandidat_nis)
        if sukses:
            self.tbl_daftar_calon_siswa._last_data_hash = None
            self.show_page()

    def _cek_input(self):
        if self.line_nama_lengkap.text() == ''\
            or self.cbo_jk.currentText() == ''\
            or self.cbo_kelas.currentText() =='':
            self.btn_tambah.setVisible(False)
        else: self.btn_tambah.setVisible(True)

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

