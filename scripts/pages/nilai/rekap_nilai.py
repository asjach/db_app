from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox
from ui.ui_page_rekap_nilai import Ui_Form
from utils.fungsi.general_functions import *
from models.nilai.rekap_nilai import RekapNilai
from PySide6.QtCore import QBuffer, QIODevice, QByteArray
from reportlab.lib.pagesizes import A4, GOV_LEGAL
from template.rekap_nilai import TemplateRekapNilai
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView

class PageRekapNilai(Ui_Form, QWidget):
    def __init__(self, parent: QMainWindow = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.cbo_jenjang = self.parent.cbo_jenjang
        self.cbo_tapel = self.parent.cbo_tapel
        self.cbo_tingkat = self.parent.cbo_tingkat
        self.cbo_kelas = self.parent.cbo_kelas 

        self.SQL = RekapNilai()
        self.doc = QPdfDocument()
        self.signal_slot()

    def signal_slot(self):
        self.kegiatan_tbl.itemSelectionChanged.connect(self.kegiatan_tbl_selected)
        self.kelas_tbl.itemSelectionChanged.connect(self.kelas_tbl_selected)
        radio = [self.f4_radio, self.a4_radio, self.portait_radio, self.landscape_radio]
        spin = [self.margin_left_spin, self.margin_top_spin, self.margin_right_spin, self.margin_bottom_spin,
                self.tinggi_baris_spin, self.kolom_pelajaran_spin, self.kolom_nama_spin, self.nilai_merah_spin]
        self.gabungan = radio + spin
        for ctl in radio:
            ctl.toggled.connect(self.show_pdf)
        for ctl in spin:
            ctl.valueChanged.connect(self.show_pdf)

    def show_page(self):
        self.fill_kegiatan_tbl()


    def fill_kegiatan_tbl(self):
        data = self.SQL.get_kegiatan_riwayat(self.cbo_tapel.currentText())
        generate_table(
            data= data,
            table=self.kegiatan_tbl,
            hidden_column=[0, 5, 6, 7, 8, 9]
        )
        

    def kegiatan_tbl_selected(self):
        table_selected(self.kegiatan_tbl, self, self.parent)
        self.id_kegiatan = self.id
        self.fill_kelas_tbl()

    def fill_kelas_tbl(self):
        data = self.SQL.get_kelas_riwayat_with_peserta(self.jenjang, self.tapel, self.id_kegiatan)
        generate_table(
            data=data,
            table=self.kelas_tbl,
            hidden_column=[0, 1, 2, 3, 5]
        )

    def kelas_tbl_selected(self):
        self.save_setting()
        table_selected(self.kelas_tbl, self, self.parent)
        self.id_kelas = self.id
        self.load_setting_rekap_nilai()
        self.show_pdf()
    
    def show_pdf(self):
        buffer = QBuffer()
        kertas = GOV_LEGAL if self.f4_radio.isChecked() else A4
        orientasi = "portait" if self.portait_radio.isChecked() else "landscape"
        opsi_nama = "lengkap" if self.lengkap_radio.isChecked() else "singkat"
        data_nilai = self.get_rekap_nilai()
        self.wali_kelas = self.nama_lengkap
        data = self.convert_mysql_to_reportlab(data_nilai)
        nilai_pelajaran = [[self.safe_float(x) for x in row[3:-1]] for row in data[1:]]
        rata_rata_pelajaran = [int(round(sum(x) / len(x), 0)) for x in zip(*nilai_pelajaran)]
        baris_rata_rata_pelajaran = ["RATA-RATA KELAS"] + [""] + [""] + [str(nilai) for nilai in rata_rata_pelajaran]
        data.append(baris_rata_rata_pelajaran)
        if self.perkelas_radio.isChecked():
            if not self.id_kegiatan: return
            rekap_nilai = TemplateRekapNilai(self)
            self.pdf_buffer = rekap_nilai.build_pdf(
                top = self.margin_top_spin.value(),
                left = self.margin_left_spin.value(),
                bottom = self.margin_bottom_spin.value(),
                right=self.margin_right_spin.value(),
                orientasi=orientasi,
                kertas = kertas,
                data_detail=data
                )
        if self.tiga_besar_radio.isChecked():
            if not self.id_kegiatan: return

        buffer.setData(QByteArray(self.pdf_buffer))
        buffer.open(QIODevice.ReadOnly)
        self.pdf_viewer.setDocument(self.doc)
        self.pdf_viewer.setPageMode(QPdfView.PageMode.MultiPage)
        self.pdf_viewer.setZoomMode(QPdfView.ZoomMode.FitInView)
        self.doc.load(buffer)
    
    def get_rekap_nilai(self):
        jenjang = self.jenjang
        tapel = self.tapel
        tingkat = self.tingkat
        kelas = self.kelas
        kegiatan = self.kegiatan
        data_mapel = self.SQL.get_list_mapel(jenjang, tapel, kegiatan, tingkat, kelas, )
        mapel_list = [mapel['mapel'] for mapel in data_mapel]
        kolom_mapel = ", ".join([f"MAX(CASE WHEN mapel = '{mapel}' THEN nilai END) AS `{mapel}`" for mapel in mapel_list])
        data = self.SQL.get_nilai_by_kegiatan(kolom_mapel, jenjang, tapel, tingkat, kelas, kegiatan)
        return data
    
    def load_setting_rekap_nilai(self):
        setting = self.SQL.get_setting_rekap_nilai(self.id)
        if setting: 
            for ctl in self.gabungan:
                ctl.blockSignals(True)
            self.f4_radio.setChecked(True) if setting['kertas'] == "F4" else self.a4_radio.setChecked(True)
            self.portait_radio.setChecked(True) if setting['orientasi'] == "Portait" else self.landscape_radio.setChecked(True)
            self.margin_left_spin.setValue(setting['margin_left'])
            self.margin_top_spin.setValue(setting['margin_top'])
            self.margin_right_spin.setValue(setting['margin_right'])
            self.margin_bottom_spin.setValue(setting['margin_bottom'])
            self.tinggi_baris_spin.setValue(setting['tinggi_baris'])
            self.kolom_nama_spin.setValue(setting['kolom_nama'])
            self.kolom_pelajaran_spin.setValue(setting['kolom_pelajaran'])
            self.nilai_merah_spin.setValue(setting['kkm'])
            for ctl in self.gabungan:
                ctl.blockSignals(False)
    
    def save_setting(self):
        sukses = False
        try:
            kertas = "F4" if self.f4_radio.isChecked() else "A4"
            orientasi = "Portait" if self.portait_radio.isChecked() else "Landscape"
            sukses = self.SQL.update_setting_rekap_nilai(
                id = self.id,  
                kertas=kertas,
                orientasi=orientasi,
                left=self.margin_left_spin.value(),
                top=self.margin_top_spin.value(),
                right = self.margin_right_spin.value(),
                bottom=self.margin_bottom_spin.value(),
                tinggi_baris=self.tinggi_baris_spin.value(),
                kolom_nama= self.kolom_nama_spin.value(),
                kolom_pelajaran=self.kolom_pelajaran_spin.value(),
                kkm=self.nilai_merah_spin.value()
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan: {e}")
        if sukses:
            print("Berhasil mengupdate Setting Rekap Nilai")

    def convert_mysql_to_reportlab(self, data):
        if not data:
            return []
        header = list(data[0].keys())

        header_tbl = header_for_table(header)
        table_data = [header_tbl]
        for row in data:
            table_data.append([format_cell_data(row[key], zero="") for key in header])
        return table_data

    def safe_float(self, val):
        try:
            return float(val)
        except ValueError:
            return 0.0