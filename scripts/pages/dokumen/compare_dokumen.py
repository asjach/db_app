from PySide6.QtWidgets import QWidget, QMainWindow
from PySide6.QtCore import QTimer, QEvent
from ui.ui_page_compare_dokumen import Ui_Form
from models.model_dokumen import Model_Dokumen
from scripts.widgets.dokumen_viewer import DokumenViewer
from utils.fungsi.general_functions import *
from send2trash import send2trash
# from utils.static_values import KETERANGAN, JENIS_DOKUMEN
from utils.app_config import DIREKTORI_DOKUMEN

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
        self.MODEL = Model_Dokumen()
        self.search_timer = QTimer(self)
        self.viewer1_layout.addWidget(self.dokumen_viewer1)
        self.viewer2_layout.addWidget(self.dokumen_viewer2)
        
        self.search_timer.setSingleShot(True)  # Timer hanya berjalan sekali
        self.search_timer.timeout.connect(self.fill_daftar_nama)
        folder_scan = value_from_db('SCAN DIRECTORY')
        self.line_source.setText(folder_scan)
        self.setup_connections()

    def setup_connections(self):
        self.fill_cbo_target()
        self.fill_cbo_jenis_dokumen()
        self.cbo_target.currentIndexChanged.connect(self.cbo_target_selected)
        self.radio_is_active.toggled.connect(self.fill_daftar_nama)
        self.line_search.textChanged.connect(self.on_search_text_edited)
        self.cbo_daftar_nama.currentIndexChanged.connect(self.cbo_daftar_nama_selected)
        self.btn_prev_nama.clicked.connect(lambda: prev_item(self.cbo_daftar_nama))
        self.btn_next_nama.clicked.connect(lambda: next_item(self.cbo_daftar_nama))
        self.cbo_daftar_dokumen.currentIndexChanged.connect(self.cbo_daftar_dokumen_selected)
        self.btn_prev_dok.clicked.connect(self.btn_prev_dok_clicked)
        self.btn_next_dok.clicked.connect(self.btn_next_dok_clicked)

        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        self.cbo_list_files.currentIndexChanged.connect(self.cbo_list_files_selected)
        self.btn_prev_file.clicked.connect(self.btn_prev_file_clicked)
        self.btn_next_file.clicked.connect(self.btn_next_file_clicked)
        self.btn_hapus.clicked.connect(self.btn_hapus_clicked)

        self.cbo_jenis_dokumen.currentIndexChanged.connect(self.cbo_jenis_dokumen_selected)
        self.btn_tambah.clicked.connect(self.btn_tambah_clicked)
        self.fill_cbo_list_files()

        for combo in self.combo_boxes:
            combo.installEventFilter(self)
        

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
        if target.lower() == 'siswa': 
            opsi = self.radio_is_active.isChecked()
            if opsi:
                data = self.MODEL.get_daftar_siswa(
                    jenjang = self.parent.str_jenjang,
                    tapel = self.parent.cbo_tapel.currentText(),
                    tingkat=self.parent.quoted_daftar_tingkat,
                    kelas = self.parent.quoted_daftar_kelas,
                    search_text=self.line_search.text(),
                    order_by=self.parent.cbo_order_by.currentText(), 
                    opsi=True
                    )
            else:
                data = self.MODEL.get_daftar_siswa(
                    jenjang = self.parent.str_jenjang,
                    tapel = self.parent.cbo_tapel.currentText(),
                    tingkat=self.parent.quoted_daftar_tingkat,
                    kelas = self.parent.quoted_daftar_kelas,
                    search_text=self.line_search.text(),
                    order_by=self.parent.cbo_order_by.currentText(), 
                    opsi=False
                    )
        elif target.lower() == 'guru':
            data = self.MODEL.get_daftar_guru(search_text=self.line_search.text())
        if data:
            populate_combobox(
                    self.cbo_daftar_nama, data, 
                    text_data=['nama_lengkap', 'jml_dok'], 
                    user_data=['nomor_induk', 'nama_lengkap'],
                    separator=''
            )

    def cbo_daftar_nama_selected(self): 
        self.fill_cbo_daftar_dokumen()

    def on_search_text_edited(self, text):
        """Menangani perubahan teks di line_search dengan delay 300 ms."""
        if not text:
            self.search_timer.stop()
            self.fill_daftar_nama()
        else:
            self.search_timer.start(300)

    def fill_cbo_daftar_dokumen(self):
        data_nama = self.cbo_daftar_nama.currentData()
        if data_nama:
            nomor_induk = data_nama['nomor_induk']
            data = self.MODEL.get_daftar_dokumen(nomor_induk)
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
            dokumen_path = DIREKTORI_DOKUMEN
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
        folder = get_directory(self.line_source, self.parent, "Pilih Folder", start_dir=default_folder)
        if folder:
            save_value_to_db("SCAN DIRECTORY", folder) 
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
        file = f"{os.path.normpath(os.path.join(self.line_source.text(),self.cbo_list_files.currentText()))}"
        if file and os.path.isfile(file):
            self.dokumen_viewer2.loadFile(file)
        else:
            self.dokumen_viewer2.close_file()  # Kosongkan viewer jika file tidak valid

    def btn_hapus_clicked(self):
        file = self.cbo_list_files.currentText()
        path = f"{os.path.normpath(os.path.join(self.line_source.text(),file))}"
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
        data_jenis_dokumen = list(static_values['JENIS_DOKUMEN'])
        populate_combobox(self.cbo_jenis_dokumen, data_jenis_dokumen)

    def cbo_jenis_dokumen_selected(self):
        self.fill_cbo_opsi_keterangan(self.cbo_jenis_dokumen.currentText())

    def fill_cbo_opsi_keterangan(self, jenis_dokumen): 
        data_keterangan = list(static_values['KETERANGAN'].get(jenis_dokumen, ''))
        populate_combobox(self.cbo_opsi_keterangan, data_keterangan)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel and isinstance(obj, QComboBox):
            return True
        return super().eventFilter(obj, event)
    
    def btn_tambah_clicked(self):
        data = self.cbo_daftar_nama.currentData()
        source_path = f"{os.path.normpath(os.path.join(self.line_source.text(),self.cbo_list_files.currentText()))}"
        nama_lengkap = data.get('nama_lengkap', '')
        nomor_induk = data.get('nomor_induk', '')
        jenis_dokumen = self.cbo_jenis_dokumen.currentText()
        keterangan = self.cbo_opsi_keterangan.currentText()
        namafile = create_namafile2(nama_lengkap, nomor_induk, jenis_dokumen, keterangan, source_path)
        dest_folder = f"{DIREKTORI_DOKUMEN}/{self.cbo_target.currentText().lower()}"
        dest_path = os.path.normpath(os.path.join(dest_folder, namafile))
        
        sukses = False
        if jenis_dokumen not in ['', None]:
            sukses = self.MODEL.tambah_dokumen(
                no_induk=nomor_induk,
                jenis_dokumen=jenis_dokumen,
                keterangan=keterangan,
                sub_folder=self.cbo_target.currentText(),
                namafile=namafile
            )
        if not sukses:
            QMessageBox.warning(self, "Error", "Gagal menambahkan file ke database.")
            return
        try:
            dest_dir = os.path.dirname(dest_path) or "."
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(source_path, dest_path)
            QMessageBox.information(self, "Berhasil", "Berhasil menambahkan dokumen ke Database.")
        except (OSError, shutil.Error) as e:
            QMessageBox.critical(self, "Error", f"File operation failed: {str(e)}")
            return
        finally:
            self.fill_cbo_list_files()
            self.fill_daftar_nama()
            self.fill_cbo_daftar_dokumen()




