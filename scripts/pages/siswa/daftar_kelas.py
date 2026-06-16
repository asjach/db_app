from PySide6.QtWidgets import QMainWindow, QWidget

from models.model_siswa import Model_Siswa
from ui.ui_page_daftar_kelas import Ui_Form
from utils.fungsi.general_functions import *
from utils.key_value.kolom_sql import *


class PageDaftarKelas(QWidget, Ui_Form):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.nis_lokal = None
        self.SQL = Model_Siswa()
        self.plain_custom.setPlainText("r.nis_lokal")
        self.plain_custom.setAcceptDrops(True)
        self.list_kolom.setStyleSheet("QListWisdget::item{padding: 3px 5px;}")
        self.splitter.setStretchFactor(0, 1)
        self._signals_slots()

    def _signals_slots(self):
        self.tbl_widget.itemSelectionChanged.connect(self._tbl_selected)
        self.tbl_widget.itemChanged.connect(self._update_table)
        self.btn_preview.clicked.connect(self.show_page)

    def show_page(self):
        self._fill_list_kolom()
        self._fill_table_widget()

    def _fill_list_kolom(self):
        data = self.SQL.get_kolom_siswa()
        populate_list_widget(self.list_kolom, data)

    def _fill_table_widget(self):
        data = self.SQL.get_daftar_kelas(
            jenjang=self.parent.str_jenjang,
            tapel=self.parent.str_tapel,
            tingkat=self.parent.quoted_daftar_tingkat,
            kelas=self.parent.quoted_daftar_kelas,
            search_by=self.parent.str_search_by,
            search=self.parent.last_search_text,
            opsi_kolom=self._opsi_kolom,
            order_by=self.parent.str_order_by,
        )
        generate_table(data, self.tbl_widget)

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
    def _opsi_kolom(self):
        self.widget_custom.setVisible(False)
        kolom = DAFTAR_KELAS.get(
            self.parent.cbo_kolom.currentText().lower(), DAFTAR_KELAS["default"]
        )
        if self.parent.cbo_kolom.currentText().lower() == "custom":
            kolom = self.plain_custom.toPlainText()
            self.widget_custom.setVisible(True)
        return kolom

    def fill_no_urut(self):
        if self.parent.str_kelas:
            tabel = self.tbl_widget
            for row in range(tabel.rowCount()):
                id_riwayat = tabel.item(row, 0).text()
                nilai = row + 1
                self.SQL.update_no_urut(id_riwayat, nilai)
            self._fill_table_widget()
        else:
            print(self.parent.str_kelas)

    # def fill_nis_kemenag(self):
    #     sukses = False
    #     jml_sukses = 0
    #     jml_gagal = 0
    #     tabel = self.tbl_daftar_kelas
    #     jml_baris = tabel.rowCount()
    #     if jml_baris > 0:
    #         for row in range(jml_baris):
    #             nis_lokal = tabel.item(row, 1).text()
    #             thn_masuk = nis_lokal[0:2]
    #             no_urut = nis_lokal[9:]
    #             nilai = f"111232040082{thn_masuk}{no_urut}"
    #             sukses = self.SQL.update_nis_kemenag(nis_lokal, nilai)
    #             if sukses:
    #                 jml_sukses += 1
    #             else:
    #                 jml_gagal += 1
    #     QMessageBox.information(self, "Catatan", f"Detail Update\nSukses: {jml_sukses}\nGagal: {jml_gagal}")
    #     self.show_page()
