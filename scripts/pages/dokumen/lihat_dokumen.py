from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_lihat_dokumen import Ui_Form
from models.model_dokumen import Model_Dokumen
from scripts.widgets.dokumen_viewer import DokumenViewer
from utils.fungsi.general_functions import *
from utils.app_config import DIREKTORI_DOKUMEN

class PageLihatDokumen(QWidget, Ui_Form):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.dokumen_viewer = DokumenViewer()
        self.viewer_layout.addWidget(self.dokumen_viewer)
        self.MODEL = Model_Dokumen()
        self.setup_connections()

    def setup_connections(self):
        self.fill_cbo_target()
        self.cbo_target.currentTextChanged.connect(self.cbo_target_selected)
        self.tbl_daftar_nama.itemSelectionChanged.connect(self.tbl_daftar_nama_selected)
        self.tbl_daftar_dokumen.itemSelectionChanged.connect(self.tbl_daftar_dokumen_selected)

    def show_page(self):
        self.fill_tbl_daftar_nama()

    def fill_cbo_target(self):
        target = ['Siswa', 'Guru']
        populate_combobox(self.cbo_target, target)

    def cbo_target_selected(self): 
        self.fill_tbl_daftar_nama()
    
    def fill_tbl_daftar_nama(self):
        target = self.cbo_target.currentText()
        if target.lower() == 'siswa':
            data = self.MODEL.get_daftar_siswa_jml_dok(
                jenjang=self.parent.str_jenjang,
                tapel=self.parent.cbo_tapel.currentText(),
                tingkat=self.parent.quoted_daftar_tingkat,
                kelas = self.parent.quoted_daftar_kelas,
                search_text=self.parent.line_search.text(),
                order_by=self.parent.cbo_order_by.currentText(),
            )
        elif target.lower() == 'guru':
            data = self.MODEL.get_daftar_guru(
                search_text=self.parent.line_search.text(),
                order_by=self.parent.cbo_order_by.currentText(),
            )
        generate_table(
            data=data,
            table=self.tbl_daftar_nama,
            hidden_column=[0]
        )

    def tbl_daftar_nama_selected(self):
        table_selected(self.tbl_daftar_nama, self, self.parent)
        self.fill_tbl_daftar_dokumen()
        if self.tbl_daftar_dokumen.rowCount() > 0:
            self.tbl_daftar_dokumen.selectRow(0)
        else:
            self.dokumen_viewer.close_file()

    def fill_tbl_daftar_dokumen(self): 
        data = self.MODEL.get_daftar_dokumen(
            nomor_induk=self.nomor_induk
        )
        generate_table(
            data = data, 
            table = self.tbl_daftar_dokumen,
            hidden_column=[4,5],
            stretch_column=2
        )

    def tbl_daftar_dokumen_selected(self):
        table_selected(self.tbl_daftar_dokumen, self, self.parent)
        target = self.cbo_target.currentText().lower()
        path = str((DIREKTORI_DOKUMEN / target / self.namafile).resolve())
        self.show_dokumen(path)

    def show_dokumen(self, path):
        self.dokumen_viewer.loadFile(path)
