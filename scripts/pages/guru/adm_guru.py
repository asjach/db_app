from PySide6.QtWidgets import QWidget, QMainWindow, QSpinBox
from ui.ui_page_adm_guru import Ui_Form
from models.model_guru import Model_Guru
from utils.fungsi.general_functions import *
from template.adm_guru import TemplateAdmGuru
# from utils.key_value.kolom_sql import GURU
from scripts.widgets.dokumen_viewer import DokumenViewer
from PySide6.QtCore import QTimer
from functools import partial

TIMER_DELAY = 300

class PageAdmGuru(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.MODEL = Model_Guru()
        self.viewer = DokumenViewer()
        self.viewer_layout.addWidget(self.viewer)
        self.spin = [
            self.spin_sisi_jilid,
            self.spin_sisi_lain,
            self.spin_ayah, 
            self.spin_ibu, 
            self.spin_alamat,
            self.spin_agenda,
            self.spin_tinggi_baris_agenda,
            self.spin_presensi, 
            self.spin_nilai,
            self.spin_jumlah_baris,
            self.spin_tinggi_baris,
            self.spin_kolom_nama_lengkap,
            self.spin_kolom_nama_singkat,
            self.spin_kolom_tanggal,
            ]
        
        self.combobox = [
            self.cbo_kelas, 
            self.cbo_semester, 
            self.cbo_guru, 
            self.cbo_kertas,
            self.cbo_baris_agenda,
            ]
        
        self.radio = [
            self.radio_agenda, 
            self.radio_cover, 
            self.radio_presensi, 
            self.radio_nilai, 
            self.radio_pengembalian, 
            self.radio_penyerahan,
            self.radio_identitas,
            ]
        self.update_timer = QTimer()
        self.update_timer.setSingleShot(True)
        self.connect_signals()

    def connect_signals(self):
        self.update_timer.timeout.connect(self.show_in_viewer)
        for spin in self.spin:
            spin.valueChanged.connect(self.start_timer)
        for cbo in self.combobox:
            cbo.currentIndexChanged.connect(self.start_timer)
        for radio in self.radio:
            radio.toggled.connect(self.start_timer)
        self.btn_print.clicked.connect(self.print_pdf)
        self.btn_save_pdf.clicked.connect(self.save_pdf)

    def start_timer(self):
        self.update_timer.start(TIMER_DELAY)

    def show_page(self):
        self.fill_cbo_kelas()
        self.fill_cbo_guru()
        self.show_in_viewer()

    def fill_cbo_kelas(self):
        data_kelas = self.MODEL.get_list_kelas(
            jenjang = self.parent.str_jenjang,
            tapel=self.parent.cbo_tapel.currentText()
        )
        populate_combobox(
            cbo_widget=self.cbo_kelas, 
            data=data_kelas,
            text_data='kelas',
            user_data='id'
            )

    def fill_cbo_guru(self):
        data_guru = self.MODEL.get_list_guru(
            self.parent.str_jenjang,
            self.parent.cbo_tapel.currentText()
        )
        populate_combobox(cbo_widget=self.cbo_guru,data=data_guru)
        
    @measure_time
    def generated_pdf(self):
        data_siswa = self.MODEL.get_daftar_nama_siswa(
            jenjang=self.parent.str_jenjang,
            tapel = self.parent.cbo_tapel.currentText(),
            kelas = self.cbo_kelas.currentText()
        )
        setting = {
            'kertas': self.cbo_kertas.currentText(),
            # RADIO
            'sisi_jilid': self.spin_sisi_jilid.value(),
            'sisi_lain': self.spin_sisi_lain.value(),

            # cover
            'cover': self.radio_cover.isChecked(),

            # agenda
            'agenda': self.radio_agenda.isChecked(),
            'jml_agenda': self.spin_agenda.value(),
            'baris_agenda': self.cbo_baris_agenda.currentText(),
            'tinggi_baris_agenda': self.spin_tinggi_baris_agenda.value(),

            # presensi
            'presensi':self.radio_presensi.isChecked(),
            'jml_presensi':self.spin_presensi.value(),
            'lebar_tanggal': self.spin_kolom_tanggal.value(),

            # daftar nilai
            'daftar_nilai':self.radio_nilai.isChecked(),
            'jml_daftar_nilai':self.spin_nilai.value(),

            # pengembalian
            'pengembalian': self.radio_pengembalian.isChecked(),

            # penyerahan
            'penyerahan': self.radio_penyerahan.isChecked(),

            # identitas
            'identitas': self.radio_identitas.isChecked(),
            'lebar_nama_lengkap': self.spin_kolom_nama_lengkap.value(),
            'lebar_nama_ayah': self.spin_ayah.value(),
            'lebar_nama_ibu': self.spin_ibu.value(),
            'lebar_alamat': self.spin_alamat.value(),

            # umum
            'jumlah_baris': self.spin_jumlah_baris.value(),
            'tinggi_baris': self.spin_tinggi_baris.value(),
            'lebar_nama_singkat': self.spin_kolom_nama_singkat.value(),
        }
        data = {
            'nama_guru': self.cbo_guru.currentText(),
            'jenjang': self.parent.str_jenjang,
            'tapel': self.parent.cbo_tapel.currentText(),
            'semester': self.cbo_semester.currentText(),
            'kelas': self.cbo_kelas.currentText(),
            'data_siswa': data_siswa
        }
        
        template_pdf = TemplateAdmGuru(
            setting=setting,
            data=data)
        
        return template_pdf.create_pdf()
    
    def show_in_viewer(self):
        self.pdf_data = self.generated_pdf()
        current_page = self.viewer.spin_page.value()-1
        if self.pdf_data:
            self.viewer.loadPDF(self.pdf_data, current_page)

    def save_pdf(self):
        """Save generated PDF to file"""
        try:
            if not self.pdf_data:
                print("Error", "Tidak ada PDF yang tersedia untuk disimpan")
                return
            namafile = f'Admin Guru {self.cbo_guru.currentText()}'
            open_after_save = self.radio_open_pdf.isChecked()
            
            save_pdf(self, self.pdf_data, namafile, open_after_save)
        except Exception as e:
            print(f"Failed to save PDF: {str(e)}")

    def print_pdf(self):
        """Print generated PDF"""
        try:
            if not self.pdf_data:
                print("Error", "Tidak ada PDF yang tersedia untuk dicetak")
                return
                
            print_with_foxit(self.pdf_data)
        except Exception as e:
            print(f"Failed to print PDF: {str(e)}")
