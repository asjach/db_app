from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_ekskul_kegiatan import Ui_Form
from models.model_nilai import Model_Nilai
# from utils.static_values import ULANGAN, UJIAN

class PageEkskul(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.data_id_ekskul = None
        self.id_kegiatan = None
        self.cur_kegiatan_idx = None
        self.SQL = Model_Nilai()
        self.cbo_kegiatan.currentIndexChanged.connect(self.cbo_kegiatan_selected)
        self.tbl_riwayat_ekskul.itemSelectionChanged.connect(self.tbl_riwayat_ekskul_selected)
        self.tbl_riwayat_ekskul.itemChanged.connect(self.update_ekskul)
        self.cbo_pembimbing.textActivated.connect(self.cbo_pembimbing_selected)
        self.btn_tambah.clicked.connect(self.tambah_riwayat_ekskul)
        self.btn_hapus.clicked.connect(self.delete_ekskul)
        self.cbo_pembimbing.setCurrentIndex(-1)

    def show_page(self):
        self.txt_jenjang = self.parent.str_jenjang
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.fill_cbo_pembimbing()
        self.fill_cbo_kegiatan()
        self.fill_tbl_riwayat_ekskul()
        self.fill_tbl_ekskul()
        
    # # CBO KEGIATAN
    def fill_cbo_kegiatan(self): 
        data = self.SQL.get_kegiatan(
            self.txt_jenjang, 
            self.txt_tapel
        )
        self.cbo_kegiatan.blockSignals(True)
        populate_combobox(self.cbo_kegiatan, data, 'kegiatan', 'id')
        if self.cur_kegiatan_idx:
            self.cbo_kegiatan.setCurrentIndex(self.cur_kegiatan_idx)
        else:
            self.cbo_kegiatan.setCurrentIndex(0)
        self.cbo_kegiatan.blockSignals(False)

    def cbo_kegiatan_selected(self):
        self.fill_tbl_riwayat_ekskul()
        self.fill_tbl_ekskul()
        self.cur_kegiatan_idx = self.cbo_kegiatan.currentIndex()

    # CBO_GURU
    def fill_cbo_pembimbing(self):
        data = self.SQL.get_pembimbing()
        self.cbo_pembimbing.blockSignals(True)
        populate_combobox(self.cbo_pembimbing, data, 'nama_lengkap', 'id_pembimbing')
        self.cbo_pembimbing.blockSignals(False)

    def cbo_pembimbing_selected(self):
        sukses = False
        data = self.data_id_ekskul
        id_pembimbing = self.cbo_pembimbing.currentData()
        if data:
            try:
                for item in data:
                    sukses |= update_from_controls('ekskul_riwayat', 'id', item['id'], **{'id_pembimbing': id_pembimbing})
                if sukses:
                    self.tbl_riwayat_ekskul.clearSelection()
                    self.fill_tbl_riwayat_ekskul()
            except Exception as e:
                print(f'Terjadi error saat update pembimbing {e}')

    # # TABEL RIWAYAT EKSKUL
    def fill_tbl_riwayat_ekskul(self):
        kegiatan = self.cbo_kegiatan.currentText()
        if kegiatan in static_values['ULANGAN']:
            data, fields = self.SQL.get_riwayat_ekskul(
                jenjang = self.txt_jenjang, 
                tapel = self.txt_tapel, 
                kegiatan = self.cbo_kegiatan.currentText()
                )
        generate_table(
            data=data, 
            table=self.tbl_riwayat_ekskul, 
            column_names=fields,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_ekskul,
            mode_input=True
            )

    def tbl_riwayat_ekskul_selected(self):
        self.data_id_ekskul = table_selected(self.tbl_riwayat_ekskul, self, self.parent)

    def tambah_riwayat_ekskul(self):

        id_kegiatan = self.cbo_kegiatan.currentData()
        list_ekskul = [input.strip() for input in self.list_input_ekskul.text().split(",") if input.strip()]
        if not id_kegiatan or not list_ekskul: 
            return
        for ekskul in list_ekskul:
            self.SQL.insert_by_list_ekskul(id_kegiatan, ekskul)
        self.fill_tbl_riwayat_ekskul()
        self.list_input_ekskul.clear()

    def update_ekskul(self):
        if self.data_id_ekskul:
            sukses = handle_item_changed(
                tabel_ui=self.tbl_riwayat_ekskul,
                tabel_sql='ekskul_riwayat',
                primary_key='id',
                must_insert=['id_kegiatan', 'ekskul'],
                not_updatable_column=['id'],
            )
            if sukses:
                self.fill_tbl_riwayat_ekskul()

    def delete_ekskul(self):
        if self.data_id_ekskul:
            for data in self.data_id_ekskul:
                if data['id'] != None:
                    delete_by_id('ekskul_riwayat', 'id', data['id'])
        self.fill_tbl_riwayat_ekskul()
        
    def fill_tbl_ekskul(self):
        data = self.SQL.get_ekskul()
        generate_table(data = data,table=self.tbl_ekskul)





        