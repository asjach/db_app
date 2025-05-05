from PySide6.QtWidgets import QWidget, QMainWindow
from PySide6.QtCore import QTimer, QEvent
from ui.ui_page_compare_dokumen import Ui_Form
from models.dokumen.compare_dokumen import ModelCompareDokumen
from scripts.widgets.dokumen_viewer import DokumenViewer
from utils.fungsi.general_functions import *
from send2trash import send2trash
from utils.static_values import KETERANGAN, JENIS_DOKUMEN

class PageCompareDokumen(QWidget, Ui_Form):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.combo_boxes = [
            self.cbo_daftar_nama, 
            self.cbo_daftar_dokumen, 
            self.cbo_jenis_dokumen, 
            self.cbo_list_files,
            ]
        self.dokumen_viewer1 = DokumenViewer()
        self.dokumen_viewer2 = DokumenViewer()
        self.MODEL = ModelCompareDokumen()
        self.search_timer = QTimer(self)
        self.viewer1_layout.addWidget(self.dokumen_viewer1)
        self.viewer2_layout.addWidget(self.dokumen_viewer2)
        
        self.search_timer.setSingleShot(True)  # Timer hanya berjalan sekali
        self.search_timer.timeout.connect(self.fill_daftar_nama)
        self.setup_connections()

    def setup_connections(self):
        self.fill_cbo_target()
        self.fill_cbo_jenis_dokumen()
        self.cbo_target.currentIndexChanged.connect(self.cbo_target_selected)
        self.cbo_daftar_nama.currentIndexChanged.connect(self.cbo_daftar_nama_selected)
        self.cbo_daftar_dokumen.currentIndexChanged.connect(self.cbo_daftar_dokumen_selected)
        self.btn_prev_nama.clicked.connect(lambda: prev_item(self.cbo_daftar_nama))
        self.btn_next_nama.clicked.connect(lambda: next_item(self.cbo_daftar_nama))
        self.btn_prev_dok.clicked.connect(self.btn_prev_dok_clicked)
        self.btn_next_dok.clicked.connect(self.btn_next_dok_clicked)
        self.btn_prev_file.clicked.connect(self.btn_prev_file_clicked)
        self.btn_next_file.clicked.connect(self.btn_next_file_clicked)
        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        self.cbo_list_files.currentIndexChanged.connect(self.cbo_list_files_selected)
        self.line_search.textEdited.connect(self.on_search_text_edited)
        self.btn_hapus.clicked.connect(self.btn_hapus_clicked)
        self.cbo_jenis_dokumen.currentIndexChanged.connect(self.cbo_jenis_dokumen_selected)
        for combo in self.combo_boxes:
            combo.installEventFilter(self)
        self.radio_is_active.toggled.connect(self.fill_daftar_nama)

    def show_page(self): 
        self.fill_daftar_nama()
    
    def fill_cbo_target(self):
        target = ['Siswa', 'Guru']
        populate_combobox(self.cbo_target, target)

    def cbo_target_selected(self): 
        if self.cbo_target.currentText():
            self.fill_daftar_nama()
        else:
            self.cbo_daftar_nama.clear()
            self.cbo_daftar_dokumen.clear()
            self.dokumen_viewer1.close_file()

    def fill_daftar_nama(self): 
        target = self.cbo_target.currentText()
        # self.cbo_daftar_nama.clear()  # Kosongkan combobox sebelum mengisi
        if target.lower() == 'siswa': 
            opsi = self.radio_is_active.isChecked()
            data = self.MODEL.get_daftar_siswa(
                jenjang = self.parent.cbo_jenjang.currentText(),
                tapel = self.parent.cbo_tapel.currentText(),
                tingkat=self.parent.cbo_tingkat.currentText(),
                kelas = self.parent.cbo_kelas.currentText(),
                search_text=self.line_search.text(),
                opsi=opsi)
        elif target.lower() == 'guru':
            data = self.MODEL.get_daftar_guru(search_text=self.line_search.text())
        else:
            data = []
        if data:
            populate_combobox(
                self.cbo_daftar_nama, data, 
                text_data=['nama_lengkap', 'ayah_nama', 'ibu_nama', 'jml_dok'], 
                user_data='nomor_induk',
                separator=''
            )
        else:
            self.cbo_daftar_nama.addItem("Tidak ada data ditemukan")

    def cbo_daftar_nama_selected(self): 
        self.fill_cbo_daftar_dokumen()

    def on_search_text_edited(self, text):
        """Menangani perubahan teks di line_search dengan delay 300 ms."""
        if not text:  # Jika teks kosong, langsung perbarui tanpa delay
            self.search_timer.stop()  # Hentikan timer jika sedang berjalan
            self.fill_daftar_nama()
        else:
            # Mulai timer untuk menunda pembaruan (300 ms)
            self.search_timer.start(300)

    def fill_cbo_daftar_dokumen(self):
        data = self.MODEL.get_daftar_dokumen(self.cbo_daftar_nama.currentData())
        populate_combobox(
            cbo_widget=self.cbo_daftar_dokumen,
            data=data,
            text_data=['jenis_dokumen', 'keterangan'],
            user_data=['id', 'sub_folder', 'namafile']
        )

    def cbo_daftar_dokumen_selected(self): 
        self.show_dokumen()
        
    def show_dokumen(self): 
        target = self.cbo_target.currentText().lower()
        data_dokumen = self.cbo_daftar_dokumen.currentData()
        if data_dokumen and isinstance(data_dokumen, dict):
            namafile = data_dokumen.get('namafile', '')
            dokumen_path = value_from_db('DOKUMEN_PATH')
            if namafile and dokumen_path:
                path = f"{dokumen_path}/{target}/{namafile}"
                self.dokumen_viewer1.loadFile(path)
            else:
                self.dokumen_viewer1.close_file()
        else:
            self.dokumen_viewer1.close_file()

    def btn_prev_dok_clicked(self):
        prev_item(self.cbo_daftar_dokumen)
    
    def btn_next_dok_clicked(self):
        next_item(self.cbo_daftar_dokumen)

    def btn_prev_file_clicked(self):
        prev_item(self.cbo_list_files)

    def btn_next_file_clicked(self):
        next_item(self.cbo_list_files)

    def btn_browse_clicked(self): 
        default_folder = f"{value_from_db('SCAN DIRECTORY')}"
        get_directory(
            self.line_source,
            self.parent,
            "Pilih Folder",
            start_dir=default_folder)
        self.fill_cbo_list_files()
        
    def fill_cbo_list_files(self): 
        folder_path = os.path.normpath(self.line_source.text())
        if folder_path and os.path.isdir(folder_path):
            files = get_files_in_directory(folder_path)
            populate_combobox(self.cbo_list_files, files)
        else:
            self.cbo_list_files.clear()  # Kosongkan combobox jika folder tidak valid

    def cbo_list_files_selected(self):
        self.show_dokumen2()

    def show_dokumen2(self): 
        file = os.path.normpath(self.cbo_list_files.currentText())
        if file and os.path.isfile(file):
            self.dokumen_viewer2.loadFile(file)
        else:
            self.dokumen_viewer2.close_file()  # Kosongkan viewer jika file tidak valid

    def btn_hapus_clicked(self):
        path = self.cbo_list_files.currentText()
        if path and os.path.exists(path):
            confirm = QMessageBox.question(
                self, "Hapus File", 
                f"Apakah Anda benar ingin menghapus file:\n{path}",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if confirm == QMessageBox.Yes:
                try:
                    send2trash(path)
                    # os.remove(path) # hapus permanen
                    self.fill_cbo_list_files()  # Perbarui daftar file
                except OSError as e:
                    QMessageBox.critical(self, "Error", f"Gagal menghapus file: {e}")
        else:
            QMessageBox.warning(self, "Peringatan", "Tidak ada file yang dipilih atau file tidak ditemukan.")

    def fill_cbo_jenis_dokumen(self): 
        data_jenis_dokumen = list(JENIS_DOKUMEN)
        populate_combobox(self.cbo_jenis_dokumen, data_jenis_dokumen)

    def cbo_jenis_dokumen_selected(self):
        self.fill_cbo_opsi_keterangan(self.cbo_jenis_dokumen.currentText())

    def fill_cbo_opsi_keterangan(self, jenis_dokumen): 
        data_keterangan = list(KETERANGAN.get(jenis_dokumen, ''))
        populate_combobox(self.cbo_opsi_keterangan, data_keterangan)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel and isinstance(obj, QComboBox):
            return True
        return super().eventFilter(obj, event)
    

        



