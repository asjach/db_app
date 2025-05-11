from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import populate_combobox, generate_table, open_dialog, table_selected, save_pdf, print_with_foxit
from ui.ui_page_kartu_peserta import Ui_Form
from models.nilai.kartu_peserta import KartuPeserta
from template.kartu_peserta import TemplateKartuPeserta
from scripts.widgets.dokumen_viewer import DokumenViewer
import json
from reportlab.pdfbase import pdfmetrics

class PageKartuPeserta(QWidget, Ui_Form):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = KartuPeserta()
        self.viewer = DokumenViewer()
        self.viewer_layout.addWidget(self.viewer)
        self.fill_fonts()

        # Referensi kontrol
        self.cbo_tapel = self.parent.cbo_tapel
        self.DEFAULT_SETTING = {
            'page_size': 'A4', 'orientation': 'portrait', 
            'left_margin': 1, 'top_margin': 1, 
            'lebar_kartu': 9, 'tinggi_kartu': 5, 
            'horizontal_gap': 0.05, 'vertical_gap': 0.05,
            'font': 'Times New Roman',
            'background': '',
            'nama': True, 'x_nama': 1, 'y_nama': 1, 'size_nama': 12,
            'ttl': False, 'x_ttl': 1, 'y_ttl': 1, 'size_ttl': 12,
            'nopes': False, 'x_nopes': 1, 'y_nopes': 1, 'size_nopes': 12,
            'kelas': True, 'x_kelas': 1, 'y_kelas': 1, 'size_kelas': 12,
            'no_induk': False,'x_no_induk': 1,'y_no_induk': 1,'size_no_induk': 12,
            'nisn': False,'x_nisn': 1,'y_nisn': 1,'size_nisn': 12,
            'foto': False,'x_foto': 1,'y_foto': 1,'w_foto': 3,'h_foto': 4,
        }

        self.all_controls = (
            [self.cbo_jenis, self.cbo_kertas, self.cbo_orientasi, self.cbo_fonts] +
            [
                self.spin_margin_left, 
                self.spin_margin_top, 
                self.spin_horizontal, 
                self.spin_vertikal,

                self.spin_lebar, 
                self.spin_tinggi, 
                self.x_nama, 
                self.y_nama, 
                self.size_nama,

                self.x_ttl, 
                self.y_ttl, 
                self.size_ttl, 
                self.x_nopes, 
                self.y_nopes, 
                self.size_nopes,

                self.x_kelas, 
                self.y_kelas, 
                self.size_kelas, 
                self.x_no_induk, 
                self.y_no_induk, 
                self.size_no_induk,

                self.x_nisn, 
                self.y_nisn, 
                self.size_nisn, 
                self.x_foto, 
                self.y_foto, 
                self.w_foto, 
                self.h_foto
            ] +
            [
                self.radio_nama, 
                self.radio_ttl, 
                self.radio_nopes, 
                self.radio_no_induk,
                self.radio_kelas, 
                self.radio_nisn, 
                self.radio_foto
            ] +
            [self.plain_background]
        )

        # Signal-slot
        self._connect_signals()

    def _connect_signals(self):
        self.cbo_kegiatan.currentIndexChanged.connect(self.on_kegiatan_changed)
        self.cbo_jenis.currentIndexChanged.connect(self.jenis_setting_changed)
        self.btn_browse.clicked.connect(lambda: open_dialog(self, self.plain_background))
        self.btn_save_setting.clicked.connect(self.save_setting_kartu)
        self.btn_generate_all.clicked.connect(self.generate_all)
        self.btn_generate_selected.clicked.connect(self.generate_selected)
        self.btn_save_pdf.clicked.connect(self.save_pdf)
        self.btn_print.clicked.connect(self.print_kartu)
        self.btn_reset.clicked.connect(self.reset_setting)
        self.btn_clear.clicked.connect(self.clear_setting)
        self.spin_presisi.valueChanged.connect(self.presisi_changed)
        
        

        # Listener perubahan kontrol untuk refresh preview
        self.blok_sinyal(True)
        for ctl in self.all_controls:
            if hasattr(ctl, 'currentIndexChanged'):
                ctl.currentIndexChanged.connect(self.refresh_preview)
            elif hasattr(ctl, 'valueChanged'):
                ctl.valueChanged.connect(self.refresh_preview)
            elif hasattr(ctl, 'toggled'):
                ctl.toggled.connect(self.refresh_preview)
            elif hasattr(ctl, 'textChanged'):
                ctl.textChanged.connect(self.refresh_preview)
        self.blok_sinyal(False)
    
    def reset_setting(self):
        self.apply_setting(None)
        self.show_pdf(selected_only=False, limit_preview=True)

    def blok_sinyal(self, blocked: bool):
        for control in self.all_controls:
            control.blockSignals(blocked)

    def show_page(self):
        self.fill_cbo_kegiatan()
        self.fill_tbl_peserta()

    def fill_cbo_kegiatan(self):
        data = self.SQL.get_kegiatan(
            jenjang=self.parent.cbo_jenjang.currentText(),
            tapel=self.parent.cbo_tapel.currentText()
        )
        populate_combobox(self.cbo_kegiatan, data, 'kegiatan', 'id')
    
    def fill_fonts(self):
        all_fonts = pdfmetrics.getRegisteredFontNames()
        populate_combobox(self.cbo_fonts, all_fonts)

    def on_kegiatan_changed(self):
        self.set_setting_kartu()
        self.fill_tbl_peserta()
        self.refresh_preview()

    def fill_tbl_peserta(self):
        data = self.data_peserta(limit=False)
        generate_table(data, self.tbl_daftar_peserta, hidden_column=[0, 1, 2, 5, 6])

    def data_peserta(self, limit=True):
        kegiatan = self.cbo_kegiatan.currentText()
        is_distinct = kegiatan in {'UAS', 'PAS', 'PAT', 'AS'}
        return self.SQL.get_data_peserta(
            tapel=self.cbo_tapel.currentText(),
            kegiatan=kegiatan,
            distintc=is_distinct,
            limit=limit
        )

    def selected_data(self):
        return table_selected(self.tbl_daftar_peserta, self, self.parent)

    def apply_setting(self, setting):
        s = {**self.DEFAULT_SETTING, **(setting or {})}

        self.cbo_kertas.setCurrentText(s['page_size'])
        self.cbo_orientasi.setCurrentText(s['orientation'])
        self.spin_margin_left.setValue(s['left_margin'])
        self.spin_margin_top.setValue(s['top_margin'])
        self.spin_horizontal.setValue(s['horizontal_gap'])
        self.spin_vertikal.setValue(s['vertical_gap'])
        self.spin_lebar.setValue(s['lebar_kartu'])
        self.spin_tinggi.setValue(s['tinggi_kartu'])

        self.cbo_fonts.setCurrentText(s['font'])
        self.plain_background.setPlainText(s['background'])

        self.radio_nama.setChecked(s['nama'])
        self.x_nama.setValue(s['x_nama'])
        self.y_nama.setValue(s['y_nama'])
        self.size_nama.setValue(s['size_nama'])

        self.radio_ttl.setChecked(s['ttl'])
        self.x_ttl.setValue(s['x_ttl'])
        self.y_ttl.setValue(s['y_ttl'])
        self.size_ttl.setValue(s['size_ttl'])

        self.radio_nopes.setChecked(s['nopes'])
        self.x_nopes.setValue(s['x_nopes'])
        self.y_nopes.setValue(s['y_nopes'])
        self.size_nopes.setValue(s['size_nopes'])

        self.radio_kelas.setChecked(s['kelas'])
        self.x_kelas.setValue(s['x_kelas'])
        self.y_kelas.setValue(s['y_kelas'])
        self.size_kelas.setValue(s['size_kelas'])

        self.radio_no_induk.setChecked(s['no_induk'])
        self.x_no_induk.setValue(s['x_no_induk'])
        self.y_no_induk.setValue(s['y_no_induk'])
        self.size_no_induk.setValue(s['size_no_induk'])

        self.radio_nisn.setChecked(s['nisn'])
        self.x_nisn.setValue(s['x_nisn'])
        self.y_nisn.setValue(s['y_nisn'])
        self.size_nisn.setValue(s['size_nisn'])

        self.radio_foto.setChecked(s['foto'])
        self.x_foto.setValue(s['x_foto'])
        self.y_foto.setValue(s['y_foto'])
        self.w_foto.setValue(s['w_foto'])
        self.h_foto.setValue(s['h_foto'])

    def get_setting_kartu(self):
        return {
            'page_size': self.cbo_kertas.currentText(),
            'orientation': self.cbo_orientasi.currentText(),
            'left_margin': self.spin_margin_left.value(),
            'top_margin': self.spin_margin_top.value(),
            'lebar_kartu': self.spin_lebar.value(),
            'tinggi_kartu': self.spin_tinggi.value(),
            'horizontal_gap': self.spin_horizontal.value(),
            'vertical_gap': self.spin_vertikal.value(),
            'background': self.plain_background.toPlainText(),
            'font': self.cbo_fonts.currentText(),

            'nama': self.radio_nama.isChecked(), 
            'x_nama': self.x_nama.value(), 
            'y_nama': self.y_nama.value(), 
            'size_nama': self.size_nama.value(),

            'ttl': self.radio_ttl.isChecked(), 
            'x_ttl': self.x_ttl.value(), 
            'y_ttl': self.y_ttl.value(), 
            'size_ttl': self.size_ttl.value(),

            'nopes': self.radio_nopes.isChecked(), 
            'x_nopes': self.x_nopes.value(), 
            'y_nopes': self.y_nopes.value(), 
            'size_nopes': self.size_nopes.value(),

            'kelas': self.radio_kelas.isChecked(), 
            'x_kelas': self.x_kelas.value(), 
            'y_kelas': self.y_kelas.value(), 
            'size_kelas': self.size_kelas.value(),

            'no_induk': self.radio_no_induk.isChecked(), 
            'x_no_induk': self.x_no_induk.value(), 
            'y_no_induk': self.y_no_induk.value(), 
            'size_no_induk': self.size_no_induk.value(),

            'nisn': self.radio_nisn.isChecked(), 
            'x_nisn': self.x_nisn.value(), 
            'y_nisn': self.y_nisn.value(), 
            'size_nisn': self.size_nisn.value(),

            'foto': self.radio_foto.isChecked(), 
            'x_foto': self.x_foto.value(), 
            'y_foto': self.y_foto.value(), 
            'w_foto': self.w_foto.value(), 
            'h_foto': self.h_foto.value(),
        }
    
    def set_setting_kartu(self):
        self.blok_sinyal(True)
        jenis_setting = self.jenis_setting()
        record = self.SQL.get_setting(self.cbo_kegiatan.currentData(), jenis_setting)
        setting_kartu_db = record.get(jenis_setting) if record else None
        
        if setting_kartu_db:
            if isinstance(setting_kartu_db, str):
                try:
                    setting_kartu_db = json.loads(setting_kartu_db)
                except json.JSONDecodeError:
                    print("ERROR: Format JSON setting tidak valid")
                    setting_kartu_db = {}
        self.apply_setting(setting_kartu_db)
        self.blok_sinyal(False)

    def jenis_setting_changed(self):
        self.set_setting_kartu()
        self.refresh_preview()

    def jenis_setting(self):
        if self.cbo_jenis.currentText() == 'Kartu Peserta':
            return 'setting_kartu'
        elif self.cbo_jenis.currentText() == 'Tempelan Bangku':
            return 'setting_tempelan'

    def save_setting_kartu(self):
        id_kegiatan = self.cbo_kegiatan.currentData()
        value = json.dumps(self.get_setting_kartu())
        self.SQL.update_setting(id_kegiatan, value, self.jenis_setting())

    def clear_setting(self):
        self.SQL.update_setting(
            id_kegiatan = self.cbo_kegiatan.currentData(),
            value=None,
            jenis_setting=self.jenis_setting()
        )
        self.apply_setting(None)
        

    def refresh_preview(self):
        self.show_pdf(selected_only=False, limit_preview=True)

    def create_kartu_peserta(self, selected_only=False, limit=True):
        data_peserta = self.selected_data() if selected_only else self.data_peserta(limit)
        setting_kartu = self.get_setting_kartu()

        if not data_peserta or not setting_kartu:
            self.viewer.image_viwer_label.clear()
            return None

        generator = TemplateKartuPeserta(self, data={
            'setting_kartu': setting_kartu,
            'data_peserta': data_peserta
        })
        return generator.build_pdf().getvalue()

    def show_pdf(self, selected_only=False, limit_preview=False):
        pdf_data = self.create_kartu_peserta(selected_only=selected_only, limit=limit_preview)
        self.pdf_data = pdf_data
        if pdf_data:
            self.viewer.loadPDF(pdf_data)

    def generate_all(self):
        self.tbl_daftar_peserta.clearSelection()
        self.show_pdf(selected_only=False, limit_preview=False)

    def generate_selected(self):
        self.show_pdf(selected_only=True, limit_preview=False)

    def save_pdf(self):
        namafile = f'kartu_peserta_{self.cbo_kegiatan.currentText()} {self.parent.cbo_tapel.currentText()}'
        save_pdf(self, self.pdf_data, namafile)

    def print_kartu(self):
        print_with_foxit(self.pdf_data)

    def presisi_changed(self):
        for control in [
                self.spin_margin_left, 
                self.spin_margin_top, 
                self.spin_horizontal, 
                self.spin_vertikal,
                self.spin_lebar, 
                self.spin_tinggi, 
                self.x_nama, 
                self.y_nama,
                self.x_ttl, 
                self.y_ttl, 
                self.x_nopes, 
                self.y_nopes, 
                self.x_kelas, 
                self.y_kelas, 
                self.x_no_induk, 
                self.y_no_induk, 
                self.x_nisn, 
                self.y_nisn, 
                self.x_foto, 
                self.y_foto, 
                self.w_foto, 
                self.h_foto
            ]:
            control.setSingleStep(self.spin_presisi.value())


