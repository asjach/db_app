from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_peserta import Ui_Form
from models.model_nilai import Model_Nilai
# from utils.static_values import ULANGAN, UJIAN

class Page_Peserta(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.current_index = 0
        self.SQL = Model_Nilai()
        self.cbo_kegiatan.currentIndexChanged.connect(self.cbo_kegiatan_selected)
        self.tbl_widget.itemSelectionChanged.connect(self.table_selected)
        self.tbl_widget.itemChanged.connect(self.update_peserta)
        self.btn_generate.clicked.connect(self.generate_peserta)
        self.btn_clear.clicked.connect(self.clear_peserta)

    def show_page(self):
        self.fill_cbo_kegiatan(self.current_index)

    def fill_cbo_kegiatan(self, index):
        data_kegiatan = self.SQL.get_kegiatan(
            self.parent.str_jenjang, 
            self.parent.cbo_tapel.currentText())
        self.cbo_kegiatan.clear()
        for kegiatan in data_kegiatan:
            self.cbo_kegiatan.addItem(kegiatan['kegiatan'], userData=kegiatan['id'])
        self.cbo_kegiatan.setCurrentIndex(index)

    def refresh(self):
        self.fill_table()
        self.fill_tbl_peserta_belum_masuk()
        self.fill_tbl_peserta_tidak_aktif()

    def cbo_kegiatan_selected(self):
        self.current_index = self.cbo_kegiatan.currentIndex()
        self.refresh()
        

    def fill_table(self):
        if self.parent.data_kelas:
            data, fields = self.SQL.get_peserta_kegiatan(
                id_kegiatan=self.cbo_kegiatan.currentData(),
                id_kelas=self.parent.data_kelas
            )
            generate_table(
                data=data,
                column_names=fields, 
                table=self.tbl_widget,
                icon_akhir=":/icon/resources/icon/multiply.svg",
                fungsi_akhir=self.delete_peserta,
                mode_input=True
            )
        
    def table_selected(self):
        self.selected_data = table_selected(self.tbl_widget, self, self.parent)
        print(self.selected_data)


    def update_peserta(self, item: QTableWidgetItem):
        handle_item_changed_v2(
            tabel_ui=self.tbl_widget,
            tabel_sql='kegiatan_peserta',
            item=item,
            primary_key='id',
            must_insert=['id', 'id_kelas', 'id_kegiatan', 'nis_lokal'],
            not_updatable_column=['id']
        )

    def delete_peserta(self):
        sukses = delete_by_id('kegiatan_peserta','id', self.id)
        if sukses: self.refresh()

    def fill_tbl_peserta_belum_masuk(self):
        data = self.SQL.peserta_belum_masuk(
            jenjang=self.parent.str_jenjang,
            tapel=self.parent.cbo_tapel.currentText(),
            id_kegiatan=self.cbo_kegiatan.currentData()
        )
        generate_table(
            data=data,
            table=self.tbl_siswa_aktif_belum_masuk
        )

    def fill_tbl_peserta_tidak_aktif(self):
        data = self.SQL.peserta_tidak_aktif(
            jenjang=self.parent.str_jenjang,
            tapel=self.parent.cbo_tapel.currentText(),
            id_kegiatan=self.cbo_kegiatan.currentData()
        )
        generate_table(
            data=data,
            table=self.tbl_peserta_tidak_aktif
        )

    def generate_peserta(self):
        sukses = False
        list_kelas = self.SQL.get_kelas_riwayat(
            self.parent.str_jenjang, 
            self.parent.cbo_tapel.currentText()
        )
        for kelas in list_kelas:
            jenjang = kelas['jenjang']
            tapel = kelas['tapel']
            tingkat = kelas['tingkat']
            id_kelas = kelas['id']
            kls = kelas['kelas']
            id_kegiatan = self.cbo_kegiatan.currentData()
            kegiatan = self.cbo_kegiatan.currentText()
            if kegiatan in static_values['ULANGAN']:
                sukses = self.SQL.generate_peserta(jenjang, tapel, id_kelas, kls, id_kegiatan)
                self.SQL.generate_no_peserta(tapel, kegiatan)
            elif kegiatan in static_values['UJIAN']:
                if tingkat in ['6', '9', '12']:
                    sukses = self.SQL.generate_peserta(jenjang, tapel, id_kelas, kls, id_kegiatan)
            else: return
        if sukses: self.refresh()

    def clear_peserta(self):
        konfirimasi = pesan_konfirmasi("Hapus Seluruh Peserta", "Anda akan menghapus seluruh Peserta kegiatan")
        if konfirimasi:
            sukses  = self.SQL.clear_peserta(self.cbo_kegiatan.currentData())
            if sukses: self.refresh()