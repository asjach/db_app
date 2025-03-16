from PySide6.QtWidgets import QWidget, QMainWindow, QComboBox, QRadioButton, QDoubleSpinBox
from PySide6.QtCore import QTimer
from ui.ui_page_cetak_rapor import Ui_Form
from models.nilai.cetak_rapor import CetakRapor
from utils.fungsi.general_functions import *
from template.rapor_mi import TemplateRapor
from scripts.widgets.dokumen_viewer import DokumenViewer
import json

class PageCetakRapor(QWidget, Ui_Form):
    def __init__(self, parent: QMainWindow):
        """Initialize the PageCetakRapor widget.

        Args:
            parent (QMainWindow): The parent widget.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.nis_lokal = None
        self.SQL = CetakRapor()
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
            self.cbo_kertas, self.cbo_orientasi,
            self.opsi_cover, self.opsi_id_madrasah, self.opsi_id_siswa, self.opsi_petunjuk,
            self.opsi_nilai, self.opsi_catatan, self.opsi_mutasi,
            self.spin_left, self.spin_top, self.spin_right, self.spin_bottom,
            self.radio_walas,
            self.spin_x_walas, self.spin_y_walas, self.spin_size_walas,
            self.spin_x_mudir, self.spin_y_mudir, self.spin_size_mudir,
            self.spin_tinggi_baris, self.spin_ukuran_catatan, self.spin_jarak_catatan,
            self.cbo_halaman,
            self.radio_peringkat_10,
        ]
        
        for opsi in opsi_opsi:
            if isinstance(opsi, QDoubleSpinBox):
                opsi.valueChanged.connect(self.opsi_selected)
            elif isinstance(opsi, QComboBox):
                opsi.currentIndexChanged.connect(self.opsi_selected)
            elif isinstance(opsi, QRadioButton):
                opsi.toggled.connect(self.opsi_selected)

    def show_page(self):
        """Show the page and initialize its contents."""
        self.fill_cbo_kelas()
        self.set_setting()
        self.fill_cbo_kegiatan()
        self.fill_tbl_siswa()
        
    def fill_cbo_kelas(self):
        """Fill the class combo box with data."""
        data = self.SQL.get_kelas(self.parent.cbo_jenjang.currentText(), self.parent.cbo_tapel.currentText())
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
            self.parent.cbo_jenjang.currentText(), 
            self.parent.cbo_tapel.currentText()
        )
        populate_combobox(self.cbo_kegiatan, data, 'kegiatan', 'id')
        self.cbo_kegiatan.setCurrentIndex(index)


    def cbo_kegiatan_selected(self):
        self.fill_tbl_siswa()
        self.show_pdf()

    def fill_tbl_siswa(self):
        data = self.SQL.get_siswa_aktif(
            self.parent.cbo_jenjang.currentText(),
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
            'show_ttd_walas': self.radio_walas.isChecked(),
            'x_walas': self.spin_x_walas.value(),
            'y_walas': self.spin_y_walas.value(),
            'size_walas': self.spin_size_walas.value(),
            'x_mudir': self.spin_x_mudir.value(),
            'y_mudir': self.spin_y_mudir.value(),
            'size_mudir': self.spin_size_mudir.value(),
            'tinggi_baris': self.spin_tinggi_baris.value(),
            'jarak_catatan': self.spin_jarak_catatan.value(),
            'ukuran_catatan': self.spin_ukuran_catatan.value(),
            'show_ttd_walas': self.radio_walas.isChecked(),
            '10_besar': self.radio_peringkat_10.isChecked()
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
            self.spin_left.setValue(float(setting_db.get('margin_left', 1.5)))
            self.spin_top.setValue(float(setting_db.get('margin_top', 1.5)))
            self.spin_right.setValue(float(setting_db.get('margin_right', 1.5)))
            self.spin_bottom.setValue(float(setting_db.get('margin_bottom', 1.5)))
            self.radio_walas.setChecked(bool(setting_db.get('show_ttd_walas', True)))
            self.spin_x_walas.setValue(float(setting_db.get('x_walas', 0)))
            self.spin_y_walas.setValue(float(setting_db.get('y_walas', 0)))
            self.spin_size_walas.setValue(float(setting_db.get('size_walas', 2)))
            self.spin_x_mudir.setValue(float(setting_db.get('x_mudir', 0)))
            self.spin_y_mudir.setValue(float(setting_db.get('y_mudir', 0)))
            self.spin_size_mudir.setValue(float(setting_db.get('size_mudir', 1.4)))
            self.spin_tinggi_baris.setValue(float(setting_db.get('tinggi_baris', 0.6)))
            self.spin_jarak_catatan.setValue(float(setting_db.get('jarak_catatan', 15)))
            self.spin_ukuran_catatan.setValue(setting_db.get('ukuran_catatan', 11))
            self.radio_walas.setChecked(setting_db.get('show_ttd_walas', True))
            self.radio_peringkat_10.setChecked(setting_db.get('10_besar', True))

    def update_setting_rapor(self):
        current_settings = json.dumps(self.nilai_setting())
        self.SQL.update_setting_rapor(self.cbo_kelas.currentData(), current_settings)

    def cek_setting(self):
        current_settings = self.nilai_setting()
        db_settings = self.SQL.get_setting_rapor(self.cbo_kelas.currentData())['setting_rapor']
        db_settings = json.loads(db_settings)
        return current_settings == db_settings
    
    def show_pdf(self, limit=True):
        id_kelas = self.cbo_kelas.currentData()
        id_kegiatan = self.cbo_kegiatan.currentData()
        nis_lokal = self.nis_lokal if self.nis_lokal else ''
        try:
            data_setting = self.nilai_setting()
            data_rapor = self.SQL.data_rapor(id_kelas, id_kegiatan, nis_lokal, limit=limit)
            # print(data_rapor)
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
        namafile = f"rapor kelas {kelas}"
        save_pdf(self, self.pdf_data, namafile)

    def print_pdf(self):
        print_with_foxit(self.pdf_data, )