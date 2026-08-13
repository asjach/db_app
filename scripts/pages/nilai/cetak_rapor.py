from PySide6.QtWidgets import QWidget, QMainWindow, QComboBox, QRadioButton, QDoubleSpinBox
from PySide6.QtCore import QTimer
from ui.ui_page_cetak_rapor import Ui_Form
from models.model_nilai import Model_Nilai
from utils.fungsi.general_functions import *
from template.rapor_mi import TemplateRapor
from scripts.widgets.dokumen_viewer import DokumenViewer
import json

class PageCetakRapor(QWidget, Ui_Form):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.nis_lokal = None
        self.group_bio.setVisible(False)
        self.SQL = Model_Nilai()
        self.viewer = DokumenViewer()
        self.viewer_layout.addWidget(self.viewer)
        self.pdf_update = QTimer(self)
        self.pdf_update.setSingleShot(True)  # Pastikan hanya dieksekusi sekali
        self.pdf_update.timeout.connect(self.update_setting_pdf)

        # Connect signals to slots
        self.cbo_kelas.textActivated.connect(self.cbo_kelas_selected)
        self.cbo_kegiatan.currentIndexChanged.connect(self.cbo_kegiatan_selected)
        self.tbl_siswa.itemSelectionChanged.connect(self.tbl_siswa_selected)
        self.cbo_halaman.currentIndexChanged.connect(self.cbo_halaman_selected)
        self.btn_save_pdf.clicked.connect(self.save_pdf)
        self.btn_print.clicked.connect(self.print_pdf)
        self.btn_generate_pdf.clicked.connect(self.generate_pdf)

        # List of widgets to connect to opsi_selected
        opsi_opsi = [
            self.cbo_kertas, 
            self.cbo_orientasi,
            self.opsi_cover, 
            self.opsi_id_madrasah, 
            self.opsi_id_siswa, 
            self.opsi_petunjuk,
            self.opsi_nilai, 
            self.opsi_catatan, 
            self.opsi_mutasi,
            self.spin_left, 
            self.spin_top, 
            self.spin_right, 
            self.spin_bottom,

            self.radio_show_mudir,
            self.radio_show_walas, 
            self.spin_size_mudir, 
            self.spin_size_walas,

            self.spin_bio_tinggi, 
            self.spin_bio_x_mudir, 
            self.spin_bio_y_mudir, 
            self.spin_nilai_tinggi,
            self.spin_nilai_x_mudir, 
            self.spin_nilai_y_mudir, 
            self.spin_nilai_x_walas, 
            self.spin_nilai_y_walas, 

            self.spin_catatan_tinggi,
            self.spin_catatan_jarak,
            self.spin_catatan_size,
            self.spin_catatan_x_mudir, 
            self.spin_catatan_y_mudir, 
            self.spin_catatan_x_walas, 
            self.spin_catatan_y_walas, 
            self.cbo_halaman,
            self.cbo_peringkat,
        ]
        
        for opsi in opsi_opsi:
            if isinstance(opsi, QDoubleSpinBox):
                opsi.valueChanged.connect(self.opsi_selected)
            elif isinstance(opsi, QComboBox):
                opsi.currentIndexChanged.connect(self.opsi_selected)
            elif isinstance(opsi, QRadioButton):
                opsi.toggled.connect(self.opsi_selected)

    def show_page(self):
        self.fill_cbo_kelas()
        self.set_setting()
        self.fill_cbo_kegiatan()
        self.fill_tbl_siswa()
        
    def fill_cbo_kelas(self):
        data = self.SQL.get_kelas(self.parent.str_jenjang, self.parent.cbo_tapel.currentText())
        populate_combobox(self.cbo_kelas, data, 'kelas', 'id')

    def cbo_kelas_selected(self):
        index_kegiatan = self.cbo_kegiatan.currentIndex()
        self.set_setting()
        self.fill_cbo_kegiatan(index_kegiatan)
        self.fill_tbl_siswa()
        self.tbl_siswa.selectRow(0)
        self.show_pdf()
        
    def fill_cbo_kegiatan(self, index=0):
        data = self.SQL.get_kegiatan(
            self.parent.str_jenjang, 
            self.parent.cbo_tapel.currentText()
        )
        populate_combobox(self.cbo_kegiatan, data, 'kegiatan', 'id')
        self.cbo_kegiatan.setCurrentIndex(index)


    def cbo_kegiatan_selected(self):
        self.fill_tbl_siswa()
        self.show_pdf()


    def fill_tbl_siswa(self):
        data = self.SQL.get_siswa_aktif(
            self.parent.str_jenjang,
            self.parent.cbo_tapel.currentText(),
            self.cbo_kelas.currentText(),
            self.cbo_kegiatan.currentText()
        )
        generate_table(
            data=data,
            table=self.tbl_siswa,
            hidden_column=[0, 1, 2, 3]
        )

    def tbl_siswa_selected(self):
        table_selected(self.tbl_siswa, self, self.parent, ['id', 'nis_lokal'])
        self.show_pdf()

    def cbo_halaman_selected(self):
        for opsi in [self.opsi_nilai, self.opsi_catatan, self.opsi_cover, 
                    self.opsi_id_madrasah, self.opsi_id_siswa, 
                    self.opsi_petunjuk, self.opsi_mutasi]:
            opsi.setChecked(False)
        halaman = self.cbo_halaman.currentText().lower()
        if halaman == 'nilai':
            self.opsi_nilai.setChecked(True)
            self.opsi_catatan.setChecked(True)
        elif halaman == 'identitas':
            self.opsi_cover.setChecked(True)
            self.opsi_id_madrasah.setChecked(True)
            self.opsi_id_siswa.setChecked(True)
        elif halaman == 'nilai dan identitas':
            self.opsi_nilai.setChecked(True)
            self.opsi_catatan.setChecked(True)
            self.opsi_cover.setChecked(True)
            self.opsi_id_madrasah.setChecked(True)
            self.opsi_id_siswa.setChecked(True)
        elif halaman == 'custom':
            self.opsi_nilai.setChecked(True)

    def opsi_selected(self):
        self.pdf_update.start(500)
    
    def update_setting_pdf(self):
        self.show_pdf()
        self.update_setting_rapor()

    def nilai_setting(self):

        return {
            'kertas': self.cbo_kertas.currentText(),
            'orientasi': self.cbo_orientasi.currentText(),
            'margin_left': self.spin_left.value(),
            'margin_top': self.spin_top.value(),
            'margin_right': self.spin_right.value(),
            'margin_bottom': self.spin_bottom.value(),

            'show_ttd_mudir': self.radio_show_mudir.isChecked(),
            'show_ttd_walas': self.radio_show_walas.isChecked(),
            'size_mudir': self.spin_size_mudir.value(),
            'size_walas': self.spin_size_walas.value(),

            'bio_tinggi': self.spin_bio_tinggi.value(),
            'bio_x_mudir': self.spin_bio_x_mudir.value(),
            'bio_y_mudir': self.spin_bio_y_mudir.value(),

            'show_peringkat': self.cbo_peringkat.currentText(),
            'nilai_tinggi': self.spin_nilai_tinggi.value(),
            'nilai_x_mudir': self.spin_nilai_x_mudir.value(),
            'nilai_y_mudir': self.spin_nilai_y_mudir.value(),

            'nilai_x_walas': self.spin_nilai_x_walas.value(),
            'nilai_y_walas': self.spin_nilai_y_walas.value(),

            'jarak_catatan': self.spin_catatan_jarak.value(),
            'ukuran_catatan': self.spin_catatan_size.value(),
            'catatan_x_mudir': self.spin_catatan_x_mudir.value(),
            'catatan_y_mudir': self.spin_catatan_y_mudir.value(),
            'catatan_x_walas': self.spin_catatan_x_walas.value(),
            'catatan_y_walas': self.spin_catatan_y_walas.value(),
        }

    def set_setting(self):
        setting_db = self.SQL.get_setting_rapor(self.cbo_kelas.currentData())['setting_rapor']
        if setting_db:
            if isinstance(setting_db, str):
                try:
                    setting_db = json.loads(setting_db)
                except json.JSONDecodeError:
                    print("ERROR: Format JSON setting tidak valid.")
                    setting_db = {}
        if setting_db:
            self.cbo_kertas.setCurrentText(setting_db.get('kertas', 'A4'))
            self.cbo_orientasi.setCurrentText(setting_db.get('orientasi', 'Portrait'))
            self.spin_left.setValue(setting_db.get('margin_left', 1.5))
            self.spin_top.setValue(setting_db.get('margin_top', 1.5))
            self.spin_right.setValue(setting_db.get('margin_right', 1.5))
            self.spin_bottom.setValue(setting_db.get('margin_bottom', 1.5))
            self.cbo_peringkat.setCurrentText(setting_db.get('show_peringkat', '10 Besar'))
            # umum/general
            self.radio_show_mudir.setChecked(setting_db.get('show_ttd_mudir'))
            self.radio_show_walas.setChecked(setting_db.get('show_ttd_walas'))
            self.spin_size_mudir.setValue(setting_db.get('size_mudir', 1.4))
            self.spin_size_walas.setValue(setting_db.get('size_walas', 2))
            # halaman biodata
            self.spin_bio_tinggi.setValue(setting_db.get('bio_tinggi'))
            self.spin_bio_x_mudir.setValue(setting_db.get('bio_x_mudir'))
            self.spin_bio_y_mudir.setValue(setting_db.get('bio_y_mudir'))
            # halaman nilai
            self.spin_nilai_tinggi.setValue(setting_db.get('nilai_tinggi', 0))
            self.spin_nilai_x_mudir.setValue(setting_db.get('nilai_x_mudir', 0))
            self.spin_nilai_y_mudir.setValue(setting_db.get('nilai_y_mudir', 0))
            self.spin_nilai_x_walas.setValue(setting_db.get('nilai_x_walas', 0))
            self.spin_nilai_y_walas.setValue(setting_db.get('nilai_y_walas', 0))
            # hamalan catatan
            self.spin_catatan_jarak.setValue(setting_db.get('jarak_catatan', 0))
            self.spin_catatan_size.setValue(setting_db.get('ukuran_catatan', 0))
            self.spin_catatan_x_mudir.setValue(setting_db.get('catatan_x_mudir', 0))
            self.spin_catatan_y_mudir.setValue(setting_db.get('catatan_y_mudir', 0))
            self.spin_catatan_x_walas.setValue(setting_db.get('catatan_x_walas', 0))
            self.spin_catatan_y_walas.setValue(setting_db.get('catatan_y_walas', 0))

    def update_setting_rapor(self):
        current_settings = json.dumps(self.nilai_setting())
        self.SQL.update_setting_rapor(self.cbo_kelas.currentData(), current_settings)
    
    def show_pdf(self, limit=1):
        id_kelas = self.cbo_kelas.currentData()
        id_kegiatan = self.cbo_kegiatan.currentData()
        nis_lokal = self.nis_lokal if self.nis_lokal else ''
        try:
            data_setting = self.nilai_setting()
            data_rapor = self.SQL.data_rapor(id_kelas, id_kegiatan, nis_lokal, limit=limit)
            if data_rapor:
                template = TemplateRapor(parent=self, data={'data_rapor': data_rapor, 'setting': data_setting})
                self.pdf_data = template.create_rapor()
                self.viewer.loadPDF(self.pdf_data)
            else:
                self.pdf_data = None
                self.viewer.close_file()
        except Exception as e:
            print(f"Error generating PDF: {e}")

    def generate_pdf(self):
        self.nis_lokal = ''
        self.show_pdf(False)

    def save_pdf(self):
        kelas = self.cbo_kelas.currentText()
        
        namafile = f"Rapor Kelas {kelas} {self.parent.str_jenjang} Tapel {self.parent.cbo_tapel.currentText()}"
        save_pdf(self, self.pdf_data, namafile)

    def print_pdf(self):
        print_with_foxit(self.pdf_data, )
        

    def kirim_wa(self):
        ...