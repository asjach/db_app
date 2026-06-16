from pathlib import Path
from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_copy_dokumen import Ui_Form
from models.model_dokumen import Model_Dokumen
from utils.fungsi.general_functions import *
# from utils.static_values import KETERANGAN, JENIS_DOKUMEN
from utils.app_config import DIREKTORI_DOKUMEN


class PageCopyDokumen(QWidget, Ui_Form):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.MODEL = Model_Dokumen()
        self.setup_connections()

    def setup_connections(self): 
        self.cbo_target.currentIndexChanged.connect(self.show_page)
        self.cbo_filter_jenis_dokumen.currentIndexChanged.connect(self.cbo_jenis_dokumen_selected)
        self.cbo_filter_keterangan.currentIndexChanged.connect(self.cbo_filter_keterangan_selected)
        self.tbl_daftar_nama.itemSelectionChanged.connect(self.tbl_daftar_nama_selected)
        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        self.btn_copy.clicked.connect(self.copy_dokumen)

    def show_page(self):
        self.fill_cbo_daftar_dokumen()
        self.fill_tbl_daftar_nama()

    def fill_cbo_daftar_dokumen(self):
        data_jenis_dokumen = list(static_values['JENIS_DOKUMEN'])
        populate_combobox(self.cbo_filter_jenis_dokumen, data_jenis_dokumen)

    def cbo_jenis_dokumen_selected(self):
        self.line_jenis_dokumen.setText(self.cbo_filter_jenis_dokumen.currentText())
        self.line_keterangan.clear()
        self.fill_cbo_keterangan(self.line_jenis_dokumen.text())
        self.fill_tbl_daftar_nama()

    def fill_cbo_keterangan(self, jenis_dokumen):
        data_keterangan = list(static_values['KETERANGAN'].get(jenis_dokumen, ''))
        populate_combobox(self.cbo_filter_keterangan, data_keterangan)

    def cbo_filter_keterangan_selected(self):
        self.line_keterangan.setText(self.cbo_filter_keterangan.currentText())

    def fill_tbl_daftar_nama(self): 
        target = self.cbo_target.currentText().lower()
        if target == 'siswa':
            data = self.MODEL.get_daftar_siswa_copy(
                jenjang=self.parent.str_jenjang,
                tapel=self.parent.cbo_tapel.currentText(),
                tingkat=self.parent.quoted_daftar_tingkat,
                kelas = self.parent.quoted_daftar_kelas, 
                search_text=self.parent.line_search.text(),
                opsi=self.radio_active_only.isChecked(),
                jenis_dok=self.line_jenis_dokumen.text(),
                keterangan=self.line_keterangan.text()
            )
        elif target == 'guru':
            data = self.MODEL.get_daftar_guru_copy(
                search_text=self.parent.line_search.text()
            ) 
        generate_table(
            data=data,
            table=self.tbl_daftar_nama,
        )

    def tbl_daftar_nama_selected(self):
        self.selected_data = table_selected(self.tbl_daftar_nama, self, self.parent)

    def btn_browse_clicked(self):
        get_directory(self.line_tujuan, self.parent, 'Pilih Folder', "C:/")

    def copy_dokumen(self):
        try:
            # Validasi input
            folder_tujuan = self.line_tujuan.text().strip()
            folder_asal = str((DIREKTORI_DOKUMEN / self.cbo_target.currentText().lower()).resolve())
            
            if not folder_tujuan or not folder_asal:
                raise ValueError("Folder asal atau tujuan tidak boleh kosong")
            
            # Normalisasi folder asal menggunakan Path
            folder_asal = str(Path(folder_asal).resolve())
            if not os.path.exists(folder_asal):
                raise FileNotFoundError(f"Folder asal {folder_asal} tidak ditemukan")
            
            # Buat folder tujuan jika belum ada
            os.makedirs(folder_tujuan, exist_ok=True)
            
            # Simpan daftar file yang bermasalah
            file_not_found = []
            
            for file in self.selected_data:
                try:
                    # Ambil nama file dan bersihkan
                    namafile_asal = file.get('namafile', '').strip()
                    if not namafile_asal:
                        print(f"Warning: Nama file kosong untuk data {file}")
                        continue
                    
                    # Pastikan hanya nama file, bukan path
                    namafile_asal = os.path.basename(namafile_asal)
                    path_asal = os.path.join(folder_asal, namafile_asal)
                    
                    # Debug: Cetak path untuk pemeriksaan
                    print(f"Debug: Mencoba akses {path_asal}")
                    
                    # Validasi file asal
                    if not os.path.exists(path_asal):
                        print(f"Warning: File {path_asal} tidak ditemukan")
                        file_not_found.append(path_asal)
                        continue
                    
                    # Tentukan nama file baru
                    if self.cbo_opsi_namafile.currentText().lower() == 'nisn':
                        ekstensi = os.path.splitext(namafile_asal)[1].lower()
                        nisn = file.get('nisn', '')
                        if not nisn:
                            print(f"Warning: NISN kosong untuk file {namafile_asal}")
                            continue
                        namafile_baru = f'{nisn}{ekstensi}'
                    else:
                        namafile_baru = namafile_asal
                    
                    path_baru = os.path.join(folder_tujuan, namafile_baru)
                    
                    # Copy file
                    shutil.copy2(path_asal, path_baru)
                    # print(f"Berhasil copy: {path_asal} -> {path_baru}")
                    
                except Exception as e:
                    print(f"Error saat memproses file {namafile_asal}: {str(e)}")
                    continue
                    
            # Laporkan file yang tidak ditemukan
            if file_not_found:
                print(f"\nRingkasan: {len(file_not_found)} file tidak ditemukan:")
                for f in file_not_found:
                    print(f"- {f}")
                    
        except Exception as e:
            print(f"Error utama: {str(e)}")

