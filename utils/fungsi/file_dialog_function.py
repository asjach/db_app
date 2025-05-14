import os, shutil, platform, subprocess
from PySide6.QtWidgets import QFileDialog, QLineEdit, QLabel, QPlainTextEdit
from utils.fungsi.db_functions import save_value_to_db, value_from_db
from datetime import datetime


def save_as_file(parent, source, last_folder):
    last_opened_folder = last_folder
    file_path, _ = QFileDialog.getSaveFileName(
        parent = parent,
        Caption = "Save Image As",
        dir = last_opened_folder,
        filter="PNG Image (*.png);;JPEG Image (*.jpg);;Bitmap Image (*.bmp)",
    )
    if file_path:
        shutil.copy(source, file_path)
    open_in_explorer(file_path)


def create_filename(nama, jenis_dok, keterangan, source_path, dest_folder):
    """
    nama: nama santri atau guru
    jenis_dok: jelas
    keterangan: jelas
    source_path = diambil extensinya
    dest_folder = folder tujuan untuk cek apakah file dengan nama yang sama sudah ada belum
    """
    ekstensi = get_extension(source_path)
    
    if keterangan == '':
        keterangan_str = ''
    else:
        keterangan_str = f'_{keterangan}'

    base_name = f"{nama}_{jenis_dok}{keterangan_str}"
    file_name = f"{base_name}.{ekstensi}"
    full_path = os.path.join(dest_folder, file_name)
    
    # Jika file sudah ada, tambahkan nomor urut
    counter = 1
    while os.path.exists(full_path):
        file_name = f"{base_name}{counter}.{ekstensi}"
        full_path = os.path.join(dest_folder, file_name)
        counter += 1
    return file_name

def create_namafile2(nama_lengkap, nomor_induk, jenis_dokumen, keterangan, source_path):
    if source_path:
        keterangan = f' {keterangan}' if keterangan not in ['', None] else ''
        timestamp = datetime.now().strftime("%H%M%S")
        ekstensi = get_extension(source_path)
        return f'{nomor_induk}-{nama_lengkap}_{jenis_dokumen}{keterangan}_{timestamp}.{ekstensi}'


def get_extension(file_path: str):
    if file_path:
        return os.path.splitext(file_path)[-1].lstrip('.')
    else:
        return None


def create_folder(path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))


def open_with_default_app(filepath):
    file_path = filepath
    if not os.path.exists(file_path):
        print("File tidak ditemukan")
        return
    try:
        if platform.system() == "Darwin":
            subprocess.call(("open", file_path))
        elif platform.system() == "Windows":
            os.startfile(file_path)
        else:
            subprocess.call(("xdg-open", file_path))
    except subprocess.CalledProcessError:
        print("Gagal membuka file")
        return

def open_in_explorer(filepath):
    if not filepath:
        print("Path tidak valid")
        return
    file_path = os.path.normpath(filepath)
    if not os.path.exists(file_path):
        print("File tidak ditemukan")
        return
    try:
        if os.path.isfile(file_path):
            subprocess.Popen(f'explorer /select,"{file_path}"', shell=True)
        else:
            subprocess.Popen(f'explorer "{file_path}"', shell=True)
    except Exception as e:
        print(f"Gagal membuka file: {e}")


# def open_dialog(parent: None, text_widget):
#     # last_opened_folder = value_from_db("LAST_SELECTED_FOLDER")
#     last_opened_folder = ''
#     # print(last_opened_folder)
#     if not os.path.exists(last_opened_folder):
#         last_opened_folder = None
#     filename, _ = QFileDialog.getOpenFileName(parent=parent, caption="Pilih File", dir=last_opened_folder)
#     if filename:
#         folder_terakhir = os.path.dirname(filename)
#         save_value_to_db("LAST_SELECTED_FOLDER", folder_terakhir)
#         if isinstance(text_widget, (QLineEdit, QLabel)):
#             text_widget.setText(filename)
#         elif isinstance(text_widget, QPlainTextEdit):
#             text_widget.setPlainText(filename)
#         return True
#     else:
#         text_widget.clear()
#     return False

def open_dialog(parent=None, text_widget=None):
    # Ambil folder terakhir dari database
    last_opened_folder = value_from_db("LAST_SELECTED_FOLDER") or ''
    
    # Jika folder tidak ada atau tidak valid, set ke None
    if not last_opened_folder or not os.path.exists(last_opened_folder):
        last_opened_folder = None
    
    # Buka dialog pemilihan file dengan folder terakhir (jika ada)
    filename, _ = QFileDialog.getOpenFileName(
        parent=parent,
        caption="Pilih File",
        dir=last_opened_folder
    )
    
    if filename:
        # Simpan folder terakhir ke database
        folder_terakhir = os.path.dirname(filename)
        save_value_to_db("LAST_SELECTED_FOLDER", folder_terakhir)
        
        # Update widget sesuai tipe
        if isinstance(text_widget, (QLineEdit, QLabel)):
            text_widget.setText(filename)
        elif isinstance(text_widget, QPlainTextEdit):
            text_widget.setPlainText(filename)
        return True
    else:
        text_widget.clear()
        return False

def save_as_path(parent, namafile):
    last_opened_folder = os.path.join(value_from_db("LAST_SELECTED_FOLDER"), namafile)
    filepath, _ = QFileDialog.getSaveFileName(
        parent = parent,
        caption = "Save Image As",
        dir = last_opened_folder,
        filter="Excel Files (*.xlsx)",
    )
    if filepath:
        return filepath
    return False


def get_directory(text_widget: QLineEdit | QPlainTextEdit, 
                  parent=None, 
                  caption="Pilih Folder", 
                  start_dir=""):
    """
    Membuka dialog untuk memilih folder dan mengatur path folder ke teks widget.
    
    :parameter
        text_widget : Widget teks (QLineEdit atau QPlainTextEdit) untuk menampilkan path folder
        parent      : Widget induk untuk dialog (opsional, default None)
        caption     : Judul dialog pemilihan folder (default "Pilih Folder")
        start_dir   : Direktori awal untuk dialog (default direktori saat ini)
    
    :return
        str: Path folder yang dipilih, atau None jika dialog dibatalkan
    """
    # Buka dialog pemilihan folder
    folder_path = QFileDialog.getExistingDirectory(
        parent=parent,
        caption=caption,
        dir=start_dir,
        options=QFileDialog.ShowDirsOnly
    )
    
    # Jika folder dipilih (folder_path tidak kosong)
    if folder_path:
        # Set teks ke widget sesuai tipe
        if isinstance(text_widget, QLineEdit):
            text_widget.setText(folder_path)
        elif isinstance(text_widget, QPlainTextEdit):
            text_widget.setPlainText(folder_path)
        else:
            raise TypeError("text_widget harus QLineEdit atau QPlainTextEdit")
        
        return folder_path
    
    # Jika dialog dibatalkan, kembalikan None
    return None


def get_files_in_directory(path_source: str | QLineEdit | QPlainTextEdit, file_types: list = None) -> list:
    """
    Mengambil daftar file dari folder dengan tipe file tertentu.
    
    :parameter
        path_source : Path folder (string) atau widget teks (QLineEdit/QPlainTextEdit) yang berisi path
        file_types  : Daftar ekstensi file yang diizinkan (misalnya, ['.pdf', '.png', '.jpg']),
                      default: ['.pdf', '.png', '.jpg', '.jpeg', '.gif']
    
    :return
        list: Daftar nama file (dengan path lengkap) yang sesuai dengan tipe file
    """
    # Tentukan tipe file default jika tidak diberikan
    if file_types is None:
        file_types = ['.pdf', '.png', '.jpg', '.jpeg', '.gif']
    
    # Normalisasi ekstensi (pastikan dalam huruf kecil dan dengan titik)
    file_types = [ext.lower() if ext.startswith('.') else f'.{ext.lower()}' for ext in file_types]
    
    # Ambil path dari path_source
    if isinstance(path_source, (QLineEdit, QPlainTextEdit)):
        path = path_source.text() if isinstance(path_source, QLineEdit) else path_source.toPlainText()
    else:
        path = path_source
    
    # Validasi path
    if not path or not os.path.isdir(path):
        print(f"Path tidak valid atau bukan direktori: {path}")
        return []
    
    # Ambil daftar file
    file_list = []
    try:
        for entry in os.scandir(path):
            if entry.is_file() and os.path.splitext(entry.name)[1].lower() in file_types:
                file_list.append(entry.path)
    except Exception as e:
        print(f"Gagal memindai direktori: {e}")
        return []
    
    return file_list