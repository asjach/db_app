from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_with_table_widget import Ui_Form
from models.model_siswa import Model_Siswa
from utils.fungsi.general_functions import *
from utils.key_value.kolom_sql import *

class PageDaftarKelas(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.nis_lokal = None
        self.SQL = Model_Siswa()
        self._signals_slots()
        
    def _signals_slots(self):
        self.tbl_widget.itemSelectionChanged.connect(self._tbl_selected)
        self.tbl_widget.itemChanged.connect(self._update_table)
    
    def show_page(self):
        self._fill_table_widget()

    # @measure_time
    def _fill_table_widget(self):
        data = self.SQL.get_daftar_kelas(
            jenjang= self.parent.str_jenjang,
            tapel = self.parent.cbo_tapel.currentText(),
            tingkat = self.parent.quoted_daftar_tingkat,
            kelas = self.parent.quoted_daftar_kelas,
            search_by=self.parent.cbo_search_by.currentText(),
            search = self.parent.line_search.text(),
            opsi_kolom=self.opsi_kolom,
            order_by = self.parent.cbo_order_by.currentText(),
        )
        generate_table(
            data=data,
            table=self.tbl_widget,
        )

    def _tbl_selected(self):
        table_selected(self.tbl_widget, self, self.parent)
        
    def _update_table(self):
        tabel = self.tbl_widget
        current_column = tabel.currentColumn()
        header_item = tabel.horizontalHeaderItem(current_column)
        if header_item is not None:
            nama_kolom = header_for_db(header_item.text())
            nilai = tabel.item(tabel.currentRow(), tabel.currentColumn()).text()
            value = convert_item_value(nilai, nama_kolom)[1]
        else:
            nama_kolom = None
        if nama_kolom in ["is_active", "status_awal", "status_akhir", "no_urut", "no"]:
            sukses = self.SQL.update_riwayat_siswa(self.id, nama_kolom, value)
        else: 
            sukses = self.SQL.update_biodata_siswa(nama_kolom, value, self.nis_lokal)
        if sukses: 
            self._fill_table_widget()

    @property
    def opsi_kolom(self):
        kolom = DAFTAR_KELAS.get(self.parent.cbo_kolom.currentText().lower(), DAFTAR_KELAS['default'])
        return kolom