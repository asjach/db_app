from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_cetak_rapor import Ui_Form
from models.nilai.cetak_rapor import CetakRapor
from utils.fungsi.general_functions import  *
from template.rapor_mi import TemplateRapor
from scripts.widgets.dokumen_viewer import DokumenViewer


class PageCetakRapor(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = CetakRapor()
        self.viewer = DokumenViewer()
        self.viewer_layout.addWidget(self.viewer)
        self.cbo_kelas.currentIndexChanged.connect(self.cbo_kelas_selected)
        self.cbo_kegiatan.currentIndexChanged.connect(self.cbo_kegiatan_selected)

    def show_page(self):
        self.txt_jenjang = self.parent.cbo_jenjang.currentText()
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.fill_cbo_kelas()
        self.fill_cbo_kegiatan()
        self.fill_tbl_siswa()

    def fill_cbo_kelas(self):
        data = self.SQL.get_kelas(self.txt_jenjang, self.txt_tapel)
        populate_combobox(self.cbo_kelas,  data, 'kelas', 'id')

    def cbo_kelas_selected(self):
        self.fill_tbl_siswa()
        self.show_pdf()

    def fill_cbo_kegiatan(self):
        data = self.SQL.get_kegiatan(self.txt_jenjang, self.txt_tapel)
        populate_combobox(self.cbo_kegiatan,  data, 'kegiatan', 'id')

    def cbo_kegiatan_selected(self):
        self.fill_tbl_siswa()
        self.show_pdf()

    def fill_tbl_siswa(self):
        data = self.SQL.get_siswa_aktif(
            self.txt_jenjang, 
            self.txt_tapel, 
            self.cbo_kelas.currentText(),
            self.cbo_kegiatan.currentText()
            )
        generate_table(
            data=data,
            table=self.tbl_siswa,
            hidden_column=[0, 1, 2, 3]
        )

    def tbl_siswa_selected(self):
        table_selected(self.tbl_siswa, self, self.parent, ['id'])

    def show_pdf(self):
        data = self.SQL.data_rapor(
            self.txt_jenjang, 
            self.txt_tapel, 
            self.cbo_kelas.currentText(), 
            self.cbo_kegiatan.currentText()
        )
        template = TemplateRapor(parent=self, data=data)
        pdf_data = template.create_rapor()
        self.viewer.loadPDF(pdf_data)
        

