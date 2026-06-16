from pathlib import Path
from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_rename_dokumen import Ui_Form
from models.model_dokumen import Model_Dokumen
from utils.fungsi.general_functions import *
# from utils.static_values import KETERANGAN, JENIS_DOKUMEN
from utils.app_config import DIREKTORI_DOKUMEN


class PageRenameDokumen(QWidget, Ui_Form):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.nis_lokal = None
        self.id_guru = None
        self.control_rename = [
            self.cbo_nama_new, 
            self.cbo_jenis_dokumen_new, 
            self.cbo_keterangan_new,
            self.cbo_nama_new,
            ]
        self.MODEL = Model_Dokumen()
        self.setup_connections()

    def setup_connections(self): 
        self.cbo_target.currentIndexChanged.connect(self.fill_table_daftar_nama)
        self.tbl_daftar_nama.itemSelectionChanged.connect(self.tbl_daftar_nama_selected)
        self.tbl_daftar_dokumen.itemSelectionChanged.connect(self.tbl_daftar_dokumen_selected)
        self.cbo_jenis_dokumen_new.currentIndexChanged.connect(self.cbo_jenis_dokumen_selected)
        for cbo in self.control_rename:
            cbo.currentIndexChanged.connect(self.update_nama_file)
        self.line_search.textChanged.connect(self.fill_cbo_nama_new)
        self.cbo_nama_new.textActivated.connect(self.fill_nis_new)
    
    def show_page(self):
        self.fill_table_daftar_nama()
        self.fill_cbo_jenis_dokumen()
        self.fill_cbo_nama_new()

    def fill_table_daftar_nama(self):
        target = self.cbo_target.currentText().lower()
        if target == 'siswa':
            data = self.MODEL.get_data_siswa(self.parent.line_search.text())
        elif target == 'guru':
            data = self.MODEL.get_data_guru(self.parent.line_search.text())
        generate_table(
            table=self.tbl_daftar_nama,
            data=data,
            stretch_column=1
        )

    def tbl_daftar_nama_selected(self):
        target = self.cbo_target.currentText().lower()
        table_selected(self.tbl_daftar_nama, self, self.parent)
        if target == 'siswa':
            nomor_induk = self.nis_lokal
        else:
            nomor_induk = self.id_guru
        self.line_no_induk.setText(nomor_induk)
        self.line_nama.setText(self.nama_lengkap)
        self.fill_table_daftar_dokumen(nomor_induk)

    def fill_table_daftar_dokumen(self, nomor_induk):
        data = self.MODEL.get_dokumen_by_nomor_induk(nomor_induk)
        generate_table(
            table=self.tbl_daftar_dokumen,
            data=data,
            hidden_column=[4]
        )

    def tbl_daftar_dokumen_selected(self):
        table_selected(self.tbl_daftar_dokumen, self, self.parent)
        self.line_id_dokumen.setText(self.id)
        self.line_jenis_dokumen_old.setText(self.jenis_dokumen)
        self.line_keterangan_old.setText(self.keterangan)
        self.line_namafile_old.setText(self.namafile)
        path = str((DIREKTORI_DOKUMEN / self.line_namafile_old.text()).resolve())
        self.plain_path_old.setPlainText(path)

    def fill_cbo_jenis_dokumen(self): 
        data_jenis_dokumen = list(static_values['JENIS_DOKUMEN'])
        populate_combobox(self.cbo_jenis_dokumen_new, data_jenis_dokumen)

    def cbo_jenis_dokumen_selected(self):
        self.fill_cbo_keterangan(self.cbo_jenis_dokumen_new.currentText())

    def fill_cbo_keterangan(self, jenis_dokumen):
        data_keterangan = list(static_values['TEMPLATE_KETERANGAN'].get(jenis_dokumen, ''))
        populate_combobox(self.cbo_keterangan_new, data_keterangan)

    def update_nama_file(self):
        namafile = create_namafile2(
            nama_lengkap=self.cbo_nama_new.currentText(),
            nomor_induk=self.line_no_induk_new.text(),
            jenis_dokumen=self.cbo_jenis_dokumen_new.currentText(),
            keterangan=self.cbo_keterangan_new.currentText(),
            source_path=self.plain_path_old.toPlainText())
        self.label_namafile_new.setText(namafile)
        new_path = str((DIREKTORI_DOKUMEN / self.cbo_target.currentText().lower() / self.line_namafile_old.text()).resolve())
        self.plain_path_new.setPlainText(new_path)
    
    def fill_cbo_nama_new(self):
        target = self.cbo_target.currentText().lower()
        data = self.MODEL.get_list_nama(target, self.line_search.text())
        if data:
            populate_combobox(self.cbo_nama_new, data, text_data='nama_lengkap', user_data='no_induk')
        print(self.cbo_nama_new.currentData())
    
    def fill_nis_new(self):
        self.line_no_induk_new.setText(self.cbo_nama_new.currentData())