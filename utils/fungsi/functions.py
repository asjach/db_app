
from PySide6.QtWidgets import (QLineEdit, QLabel, QPlainTextEdit, QComboBox,  QApplication,QMessageBox,)
from datetime import datetime
import time
import pandas as pd
from utils.static_values import KOLOM_TANGGAL


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} dieksekusi dalam {end_time - start_time:.6f} detik")
        return result
    return wrapper


# TEXT FUNCTIONS
def date_to_text(tanggal, format='YMD'):
    if not tanggal:
        return ""
    if isinstance(tanggal, datetime):
        tanggal = tanggal.date()
    nama_bulan = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni", 
        7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember",
    }
    nama_bulan_singkat = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "Mei", 6: "Jun", 
        7: "Jul", 8: "Ags", 9: "Sep", 10: "Okt", 11: "Nov", 12: "Des",
        }
    hari = tanggal.day
    tahun = tanggal.year
    if format == None:
        bulan = nama_bulan[tanggal.month]
        tanggal_formatted = f"{hari:02d} {bulan} {tahun}"
    elif format == "singkat":
        bulan = nama_bulan_singkat[tanggal.month]
        tanggal_formatted = f"{hari:02d} {bulan} {tahun}"
    elif format == 'YMD':
        tanggal_formatted = tanggal.strftime('%Y-%m-%d')
    return tanggal_formatted


def text_to_date(tanggal):
    if not tanggal or tanggal.strip() == "":
        return None

    # Jika input sudah berupa datetime, langsung konversi ke date
    if isinstance(tanggal, datetime):
        return tanggal.date()

    # Pisahkan bagian tanggal dan waktu jika ada
    bagian_waktu = None
    if " " in tanggal:
        parts = tanggal.split(" ", 1)  # Split hanya pada spasi pertama
        tanggal_part = parts[0]
        if len(parts) > 1 and ":" in parts[1]:  # Jika ada waktu (mengandung ":")
            bagian_waktu = parts[1]
        else:
            tanggal_part = tanggal  # Jika tidak ada format waktu, gunakan seluruh string

    else:
        tanggal_part = tanggal

    # Dictionary untuk mapping nama bulan ke angka
    nama_bulan = {
        nama: i + 1
        for i, group in enumerate([
            ["jan", "january", "januari"],
            ["feb", "february", "februari", "peb", "pebruari"],
            ["mar", "march", "maret"],
            ["apr", "april"],
            ["mei", "may"],
            ["jun", "june", "juni"],
            ["jul", "july", "juli"],
            ["aug", "august", "agustus", "agu"],
            ["sep", "september"],
            ["okt", "october", "oktober", "oct"],
            ["nov", "november", "nop", "nopember"],
            ["des", "december", "desember", "dec"]
        ])
        for nama in group
    }

    # Daftar pola tanggal yang akan dicoba untuk parsing
    patterns = [
        "%Y-%m-%d", "%Y/%m/%d", "%Y %m %d",
        "%d-%m-%Y", "%d/%m/%Y", "%d %m %Y",
        "%d-%b-%y", "%d/%b/%y", "%d %b %y",
        "%d-%B-%y", "%d/%B/%y", "%d %B %y",
        "%d-%B-%Y", "%d/%B/%Y", "%d %B %Y"
    ]

    # Tambahan pola dengan waktu jika ada bagian_waktu
    if bagian_waktu:
        time_patterns = [f"{p} %H:%M:%S" for p in patterns]
        patterns.extend(time_patterns)

    # Mencoba parsing dengan berbagai format
    for pattern in patterns:
        try:
            date_obj = datetime.strptime(tanggal if not bagian_waktu else f"{tanggal_part} {bagian_waktu}", pattern)
            # Jika hanya ingin tanggal, gunakan .date()
            date_obj = date_obj.date()

            # Jika tahun dalam format dua digit, ubah ke format empat digit
            if date_obj.year < 100:
                current_year = datetime.now().year
                current_century = current_year // 100 * 100
                if date_obj.year > (current_year % 100):
                    date_obj = date_obj.replace(year=current_century - 100 + date_obj.year)
                else:
                    date_obj = date_obj.replace(year=current_century + date_obj.year)

            return date_obj
        except ValueError:
            pass  # Jika parsing gagal, coba format lain

    # Jika format pola gagal, coba parsing manual
    parts = tanggal_part.split()
    if len(parts) < 3:
        raise ValueError(f"Format tanggal tidak valid: {tanggal}")

    try:
        hari = int(parts[0])
        bulan_text = parts[1].lower()
        tahun = int(parts[2])

        # Konversi tahun dua digit ke empat digit
        if tahun < 100:
            current_year = datetime.now().year
            current_century = current_year // 100 * 100
            if tahun > (current_year % 100):
                tahun = current_century - 100 + tahun
            else:
                tahun = current_century + tahun

        # Konversi nama bulan menjadi angka
        if bulan_text not in nama_bulan:
            raise ValueError(f"Nama bulan tidak valid: {bulan_text}")
        bulan = nama_bulan[bulan_text]

        # Membentuk objek tanggal
        return datetime(tahun, bulan, hari).date()

    except ValueError:
        raise ValueError(f"Format tanggal tidak valid: {tanggal}")


# def show_frame(frame):
#     if frame.isVisible():
#         frame.setVisible(False)
#     else:
#         frame.setVisible(True)


def tapel_berikutnya(tapel):
    years = tapel.split("-")
    if len(years) != 2:
        return "input string tidak valid"
    try:
        next_year = [str(int(year) + 1) for year in years]
    except ValueError:
        return "Input string tidak valid"
    return "-".join(next_year)


def tapel_sebelumnya(tapel: str):
    years = tapel.split("-")
    if len(years) != 2:
        return "input string tidak valid"
    try:
        prev_year = [str(int(year) - 1) for year in years]
    except ValueError:
        return "Input string tidak valid"
    return "-".join(prev_year)


def copy_value(widget):
    if isinstance(widget, (QLineEdit, QLabel)):
        value = widget.text()
    elif isinstance(widget, (QComboBox)):
        value = widget.currentText()
    elif isinstance(widget, QPlainTextEdit):
        value = widget.toPlainText()
    elif isinstance(widget, str):
        value = widget
    else:
        value = "ADA YANG SALAH"
    if value!="":
        QApplication.clipboard().setText(value)
    else:
        QApplication.clipboard().setText("KOSONG")


def format_telp_62(no_telp: str) -> str:
    if no_telp not in ["", None]:
        no_telp = f"62{no_telp[1:]}"
    else:
        no_telp = ""
    return no_telp


def count_len(label, line):
    length = str(len(line.text()))
    label.setText(length)


def fill_nis_kemenag(nis_lokal):
    thn = nis_lokal[0:2]
    urut = nis_lokal[9:]
    nis_kemenag = f"111232040082{thn}{urut}"
    return nis_kemenag


def singkat_nama(nama, x = 21, list_prioritas= None):
    if list_prioritas == None:
        list_prioritas = ["MUHAMMAD", "MUHAMAD", "MOHAMMAD", "MOCHAMAD","MOHAMAD", "MOCHAMMAD", "ABDUL"]
    def singkat_sub_nama(sub):
        return sub[0] + '.' if len(sub) > 1 else sub

    nama = nama.upper()
    list_prioritas = [p.upper() for p in list_prioritas]
    nama_split = nama.split()
    hasil = []

    # Jika panjang nama kurang dari atau sama dengan x, kembalikan nama asli
    if len(nama) <= x:
        return nama

    # Prioritaskan penyingkatan nama yang ada dalam list_prioritas atau nama pertama
    for i, sub in enumerate(nama_split):
        if sub in list_prioritas:
            hasil.append(singkat_sub_nama(sub))
        else:
            hasil.append(sub)

    # Fungsi untuk menghitung panjang nama tanpa menghitung singkatan
    def panjang_tanpa_singkatan(hasil):
        panjang = 0
        for sub in hasil:
            if len(sub) > 2 or (len(sub) == 2 and '.' not in sub):
                panjang += len(sub) + 1  # +1 untuk spasi
        return panjang - 1  # kurangi 1 spasi tambahan

    # Jika masih melebihi x, singkat dari belakang kecuali nama pertama
    while panjang_tanpa_singkatan(hasil) > x and len(hasil) > 1:
        for i in range(len(hasil) - 1, 0, -1):  # Jangan singkat nama pertama kecuali ada di list_prioritas
            if len(hasil[i]) > 1 and '.' not in hasil[i]:
                hasil[i] = singkat_sub_nama(hasil[i])
                break

    hasil_akhir = ' '.join(hasil)
    return hasil_akhir


def clear_inputs(controls):
    for control in controls:
        if isinstance(control, (QLineEdit, QPlainTextEdit)):
            control.clear()
        elif isinstance(control, QComboBox):
            control.setCurrentIndex(-1)
        elif isinstance(control, QLabel):
            control.clear()


def insert_data_to_controls(data, controls):
    """
    Memasukkan data dari dictionary ke kontrol GUI.

    Parameters:
        data (dict): Data yang akan dimasukkan ke kontrol.
        controls (list): Daftar pasangan (kontrol, key) untuk menghubungkan kontrol ke data.
    """
    for control, key in controls:
        value = data.get(key, None)  # Ambil nilai, default None
        
        # Pemrosesan khusus untuk key tanggal
        if any(substr in key for substr in ['tgl', 'tanggal', 'tmt']) and value:
            value = date_to_text(value)  # Konversi ke format teks tanggal
        
        # Set nilai ke kontrol berdasarkan jenis kontrol
        if isinstance(control, (QLineEdit, QLabel)):
            control.setText("" if value is None else str(value))  # None jadi "" hanya untuk tampilan
        elif isinstance(control, QPlainTextEdit):
            control.setPlainText("" if value is None else str(value))
        elif isinstance(control, QComboBox):
            control.setCurrentText("" if value is None else str(value))


def pesan_konfirmasi(judul='Konfirmasi', pesan='Pesan Konfirmasi'):
    konfirimasi = QMessageBox(QMessageBox.Question, judul, pesan, QMessageBox.Ok | QMessageBox.Cancel)
    aksi = konfirimasi.exec()
    if aksi == QMessageBox.Ok:
        return True
    return False

def pesan_sukses(judul='Sukses', pesan='Pesan Sukses'):
    konfirimasi = QMessageBox(QMessageBox.Information, judul, pesan, QMessageBox.Ok)
    aksi = konfirimasi.exec()


def show_message(text='Pesan', title='', icon=QMessageBox.Information):
    """Menampilkan message box dengan judul dan teks tertentu."""
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec()


def log_message(parent, text: str):
    """Menampilkan pesan di QStatusBar."""
    parent.statusBar.showMessage(text)

def read_excel(path, sheet_name=None):
    try:
        if sheet_name:
            df = pd.read_excel(path, sheet_name=sheet_name, dtype=str, keep_default_na=False)
        else:
            df = pd.read_excel(path, dtype=str, keep_default_na=False)
        for col in df.columns:
                if any(keyword in col.lower() for keyword in KOLOM_TANGGAL):
                    df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
        data = df.fillna("").to_dict(orient='records')
        return data
    except Exception as e:
        print(f"Error membaca File: {e}")
        return []
    
