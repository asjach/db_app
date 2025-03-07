import os, shutil, platform, subprocess
from PySide6.QtWidgets import QFileDialog, QLineEdit, QLabel, QPlainTextEdit
from utils.fungsi.db_functions import save_value_to_db, value_from_db


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
    if not filepath:  # Cek apakah filepath kosong atau None
        print("Path tidak valid")
        return

    file_path = os.path.normpath(filepath)  # Sesuaikan path dengan OS
    if not os.path.exists(file_path):
        print("File tidak ditemukan")
        return

    try:
        # Gunakan File Explorer yang sudah terbuka jika ada
        subprocess.Popen(f'explorer /select,"{file_path}"', shell=True)
    except Exception as e:
        print(f"Gagal membuka file: {e}")


def open_dialog(parent: None, text_widget):
    # last_opened_folder = value_from_db("LAST_SELECTED_FOLDER")
    last_opened_folder = ''
    # print(last_opened_folder)
    if not os.path.exists(last_opened_folder):
        last_opened_folder = None
    filename, _ = QFileDialog.getOpenFileName(parent=parent, caption="Pilih File", dir=last_opened_folder)
    if filename:
        folder_terakhir = os.path.dirname(filename)
        save_value_to_db("LAST_SELECTED_FOLDER", folder_terakhir)
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
