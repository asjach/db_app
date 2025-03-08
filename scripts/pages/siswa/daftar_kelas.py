from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_with_table_widget import Ui_Form
from models.siswa.daftar_kelas import DaftarKelas
from utils.fungsi.general_functions import *
from utils.key_value.kolom_sql import *

class PageDaftarKelas(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = DaftarKelas()
        self._dynamic_attributs()
        self._signals_slots()
        
    def _dynamic_attributs(self):
        self.txt_jenjang = self.parent.cbo_jenjang.currentText()
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.txt_tingkat = self.parent.cbo_tingkat.currentText()
        self.txt_kelas = self.parent.cbo_kelas.currentText()
        self.txt_search_by = self.parent.cbo_search_by.currentText()
        self.txt_search = self.parent.line_search.text()
        self.txt_order = self.parent.cbo_order_by.currentText()
        self.txt_kolom = self.parent.cbo_kolom.currentText()

    def _signals_slots(self):
        self.tbl_widget.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_widget, self, self.parent))
        self.tbl_widget.itemChanged.connect(self.update_table)
    
    def show_page(self):
        self._dynamic_attributs()
        self.fill_table_widget()

    # @measure_time
    def fill_table_widget(self):
        data = self.SQL.get_daftar_kelas(
            jenjang= self.txt_jenjang,
            tapel = self.txt_tapel,
            tingkat = self.txt_tingkat,
            kelas = self.txt_kelas,
            opsi_kolom=self.opsi_kolom,
            search_by=self.txt_search_by,
            search = self.txt_search,
            order_by = self.txt_order,
        )
        generate_table(
            data=data,
            table=self.tbl_widget,

        )


    def update_table(self):
        tabel = self.tbl_widget
        current_column = tabel.currentColumn()
        header_item = tabel.horizontalHeaderItem(current_column)
        if header_item is not None:
            nama_kolom = header_for_db(header_item.text())
            nilai = tabel.item(tabel.currentRow(), tabel.currentColumn()).text().strip()
            value = convert_item_value(nilai, nama_kolom)[1]
        else:
            nama_kolom = None
        if nama_kolom in ["is_active", "status_awal", "status_akhir", "no_urut"]:
            sukses = self.SQL.update_riwayat_siswa(
                id=self.id,
                nama_kolom=nama_kolom,
                nilai=value
            )
        else:
            sukses = self.SQL.update_biodata_siswa(
                nama_kolom=nama_kolom,
                nilai=value,
                nis_lokal=self.nis_lokal
            )
        if sukses:
            self.fill_table_widget()

    @property
    def opsi_kolom(self):
        kolom = DAFTAR_KELAS.get(self.txt_kolom.lower(), DAFTAR_KELAS['default'])
        return kolom