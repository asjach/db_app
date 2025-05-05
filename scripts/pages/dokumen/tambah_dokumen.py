from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox
from ui.ui_page_tambah_dokumen import Ui_Form
from models.dokumen.tambah_dokumen import ModelTambahDokumen
from scripts.widgets.dokumen_viewer import DokumenViewer
from utils.fungsi.general_functions import *
from utils.static_values import KETERANGAN, JENIS_DOKUMEN



class PageTambahDokumen(QWidget, Ui_Form):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.dokumen_viewer = DokumenViewer()
        self.viewer_layout.addWidget(self.dokumen_viewer)
        self.MODEL = ModelTambahDokumen()
        self.btn_tambah.setEnabled(False)
        self.activator = [self.plain_source, self.line_nama, self.line_no_induk, self.line_jenis_dokumen, self.line_keterangan]
        self.fill_list_daftar_dokumen()
        self.setup_connections()

    def setup_connections(self):
        self.cbo_target.currentIndexChanged.connect(self.cbo_target_changed)
        self.tbl_daftar_nama.itemSelectionChanged.connect(self.tbl_daftar_nama_selected)
        self.btn_clear_source.clicked.connect(self.btn_clear_clicked)
        self.plain_source.textChanged.connect(self.source_changed)
        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        self.list_jenis_dokumen.itemSelectionChanged.connect(self.list_jenis_dokumen_selected)
        self.list_keterangan.itemSelectionChanged.connect(self.list_keterangan_selected)
        self.btn_tambah.clicked.connect(self.btn_tambah_clicked)
        for ctl in self.activator:
            ctl.textChanged.connect(self.activate_btn_tambah)
            ctl.textChanged.connect(self.create_dest_path)


    def show_page(self):
        self.fill_tbl_daftar_nama()

    def cbo_target_changed(self):
        self.fill_tbl_daftar_nama()
        self.line_nama.clear()
        self.line_no_induk.clear()

    def fill_tbl_daftar_nama(self):
        if self.cbo_target.currentIndex() == 0:
            data = self.MODEL.get_daftar_siswa(
                jenjang=self.parent.cbo_jenjang.currentText(),
                tapel=self.parent.cbo_tapel.currentText(),
                tingkat=self.parent.cbo_tingkat.currentText(),
                kelas = self.parent.cbo_kelas.currentText(),
                search_text=self.parent.line_search.text(), 
                order_by=self.parent.cbo_order_by.currentText())
        elif self.cbo_target.currentIndex() == 1:
            data = self.MODEL.get_daftar_guru(
                search_text=self.parent.line_search.text(),
                order_by=self.parent.cbo_order_by.currentText())
        try:
            generate_table(data, self.tbl_daftar_nama,stretch_column=1)
        except Exception as e:
            print(e)

    def tbl_daftar_nama_selected(self):
        table_selected(self.tbl_daftar_nama, self, self.parent)
        self.line_nama.setText(self.nama_lengkap)
        self.line_no_induk.setText(self.no_induk)


    def btn_clear_clicked(self):
        self.plain_source.clear()
        self.dokumen_viewer.close_file()

    def source_changed(self):
        source = self.plain_source.toPlainText()
        if  source != '':
            self.dokumen_viewer.loadFile(source)
        # self.create_dest_path()

    def btn_browse_clicked(self):
        open_dialog(self.parent, self.plain_source)

    def fill_list_daftar_dokumen(self):
        data_jenis_dokumen = list(JENIS_DOKUMEN)
        populate_combobox(self.list_jenis_dokumen, data_jenis_dokumen)

    def list_jenis_dokumen_selected(self):
        self.line_jenis_dokumen.setText(self.list_jenis_dokumen.currentItem().text())
        self.line_keterangan.clear()
        self.fill_list_keterangan(self.line_jenis_dokumen.text())
        # self.create_dest_path()

    def fill_list_keterangan(self, jenis_dokumen):
        data_keterangan = list(KETERANGAN.get(jenis_dokumen, ''))
        populate_combobox(self.list_keterangan, data_keterangan)

    def list_keterangan_selected(self):
        self.line_keterangan.setText(self.list_keterangan.currentItem().text())
        # self.create_dest_path()
    
    def create_dest_path(self):
        source_path = self.plain_source.toPlainText()
        nama_lengkap = self.line_nama.text()
        nomor_induk = self.line_no_induk.text()
        jenis_dokumen = self.line_jenis_dokumen.text()
        keterangan = self.line_keterangan.text()
        dest_folder = f"{value_from_db('DOKUMEN_PATH')}/{self.cbo_target.currentText().lower()}"
        self.namafile = create_namafile2(nama_lengkap, nomor_induk, jenis_dokumen, keterangan, source_path)
        if self.namafile:
            self.fullpath = os.path.join(dest_folder, self.namafile)
            self.plain_destination.setPlainText(self.fullpath)

    def activate_btn_tambah(self):
        source = self.plain_source.toPlainText()
        nama_lengkap = self.line_nama.text()
        no_induk = self.line_no_induk.text()
        jenis_dokumen = self.line_jenis_dokumen.text()
        if source == '' or nama_lengkap == '' or no_induk == '' or jenis_dokumen == '':
            self.btn_tambah.setEnabled(False)
        else:
            self.btn_tambah.setEnabled(True)

    def btn_tambah_clicked(self):
        source_path = self.plain_source.toPlainText().strip()
        dest_path = self.plain_destination.toPlainText().strip()
        
        # Validasi input
        if not source_path or not dest_path:
            QMessageBox.warning(self, "Error", "Source or destination path cannot be empty.")
            return
        
        if not os.path.isfile(source_path):
            QMessageBox.warning(self, "Error", "Source file does not exist.")
            return

        # Bentuk sudah_path berdasarkan direktori sumber
        source_dir = os.path.dirname(source_path) or "."
        sudah_path = os.path.join(source_dir, "sudah", self.namafile)
        
        # Tambah dokumen ke model
        sukses = self.MODEL.tambah_dokumen(
            no_induk=self.line_no_induk.text(),
            jenis_dokumen=self.line_jenis_dokumen.text(),
            keterangan=self.line_keterangan.text(),
            sub_folder=self.cbo_target.currentText(),
            namafile=self.namafile
        )
        
        if not sukses:
            QMessageBox.warning(self, "Error", "Failed to add document to database.")
            return

        try:
            # MODE: COPY
            if self.radio_mode_copy.isChecked():
                # Buat folder tujuan jika belum ada
                dest_dir = os.path.dirname(dest_path) or "."
                os.makedirs(dest_dir, exist_ok=True)
                shutil.copy(source_path, dest_path)
                
                # Pindahkan file sumber ke folder sudah jika dicentang
                if self.radio_move_sudah.isChecked():
                    os.makedirs(os.path.join(source_dir, "sudah"), exist_ok=True)
                    shutil.move(source_path, sudah_path)
                
                # Siklus ke file berikutnya jika dipilih
                if self.radio_cycle.isChecked():
                    self.line_nama.clear()
                    self.line_no_induk.clear()
                    self.btn_browse.click()  # Panggil fungsi browse
                    return
            
            # MODE: MOVE
            else:
                dest_dir = os.path.dirname(dest_path) or "."
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(source_path, dest_path)
                if self.radio_cycle.isChecked():
                    self.line_nama.clear()
                    self.line_no_induk.clear()
                    self.btn_browse.click()
                    return
            self.clear_after_tambah()
            
        except (OSError, shutil.Error) as e:
            QMessageBox.critical(self, "Error", f"File operation failed: {str(e)}")
            return

    def clear_after_tambah(self):
        self.tbl_daftar_nama.clearSelection()
        self.line_nama.clear()
        self.line_no_induk.clear()
        self.plain_source.clear()
        self.plain_destination.clear()
        self.dokumen_viewer.close_file()


        
        
