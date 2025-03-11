import decimal
from datetime import datetime, date
from utils.database import ConnectDB
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QApplication
from PySide6.QtGui import QFontMetrics, QFont, QIcon
from utils.fungsi.functions import show_message, date_to_text, text_to_date
from utils.static_values import KOLOM_ANGKA, KOLOM_TANGGAL, KOLOM_FLOAT, LEFT_COLUMN
from PySide6.QtCore import Qt
import pandas as pd

from PySide6.QtWidgets import (
    QTableWidget, QTableWidgetItem, QHeaderView, QProgressBar
)
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtCore import Qt

def generate_table(
    data,
    table: QTableWidget,
    
    left_column=None,
    hidden_column=None,
    stretch_column=None,
    margin=20,
    max_column_size=1000,
    row_height=24,
    font_family="Segoe UI",
    font_size=9,
    icon_awal=None,
    icon_akhir=None,
    fungsi_awal=None,
    fungsi_akhir=None,
    zero=None
):

    if isinstance(data, pd.DataFrame):
        data = data.fillna("")
        data = data.to_dict(orient="records")
        
    if not data:
        table.clear()
        table.setRowCount(0)
        table.setColumnCount(0)
        return

    if not isinstance(data, (list, tuple)) or not all(isinstance(row, dict) for row in data):
        raise ValueError("Parameter 'data' harus berupa list atau tuple berisi dictionary.")

    if left_column is None:
        left_column = LEFT_COLUMN

    table.clearContents()
    table.setRowCount(len(data))
    table.setColumnCount(len(data[0]) + (1 if icon_awal else 0) + (1 if icon_akhir else 0))

    headers = []
    if icon_awal:
        headers.append("")
    headers.extend(header_for_table(data[0].keys()))
    if icon_akhir:
        headers.append("")

    table.setHorizontalHeaderLabels(headers)
    table.setFont(QFont(font_family, font_size))
    metrics = QFontMetrics(table.font())
    column_widths = [0] * len(headers)
    table.setUpdatesEnabled(False)
    table.blockSignals(True)
    for row_num, row_data in enumerate(data):
        if icon_awal:
            add_icon_button(table, row_num, 0, icon_awal, fungsi_awal)
        start_col = 1 if icon_awal else 0
        for col_num, (key, item_data) in enumerate(row_data.items(), start_col):
            item_data = format_cell_data(item_data, zero=zero)
            item = QTableWidgetItem(item_data)
            key = header_for_db(key)
            if isinstance(key, str) and key.lower() in left_column:
                align = Qt.AlignLeft | Qt.AlignVCenter
            else:
                align = Qt.AlignHCenter | Qt.AlignVCenter
            item.setTextAlignment(align)
            table.setItem(row_num, col_num, item)
            update_column_width(metrics, column_widths, col_num, item_data, max_column_size)
        if icon_akhir:
            add_icon_button(table, row_num, len(headers) - 1, icon_akhir, fungsi_akhir)
    if hidden_column:
        for col_index in hidden_column:
            table.setColumnHidden(col_index, True)

    if stretch_column is not None:
        if isinstance(stretch_column, int):
            table.horizontalHeader().setSectionResizeMode(stretch_column, QHeaderView.Stretch)
        elif isinstance(stretch_column, (list, tuple)):
            for col_index in stretch_column:
                table.horizontalHeader().setSectionResizeMode(col_index, QHeaderView.Stretch)

    adjust_column_widths(table, column_widths, headers, metrics, margin)
    table.resizeRowsToContents()
    table.verticalHeader().setMinimumSectionSize(row_height)
    table.setUpdatesEnabled(True)
    table.blockSignals(False)


def fill_table(table_name, get_function, get_params={}, table_params={}, ):
    if table_name is None:
        show_message("ui table belum ada")
        return
    if isinstance(get_params, dict):
        data = get_function(**get_params)
    elif isinstance(get_params, (tuple, list)):
        data = get_function(*get_params)
    table_name.blockSignals(True)
    if isinstance(table_params, dict):
        generate_table(
            data=data,
            table=table_name,
            **table_params)
    elif isinstance(table_params, (tuple, list)):
        generate_table(
            data=data,
            table=table_name,
            *table_params)
    else:
        raise TypeError("table_params must be a dict, tuple, or list")
    table_name.blockSignals(False)


def table_selected(table_name, objek, parent=None, atribut=[]):
    set_attributes_values(objek, table_name, parent, *atribut)
    return get_selected_table_data(table_name)


def add_icon_button(table:QTableWidget, row_num, col_num, icon, fungsi):
    button = QPushButton()
    button.setFlat(True)
    button.setIcon(QIcon(icon))
    button.clicked.connect(fungsi)
    table.setCellWidget(row_num, col_num, button)


def set_attributes_values(objek, tabel, parent=None, *atribut_texts):
    atribut_values = {}
    all_columns = not atribut_texts
    for column in range(tabel.columnCount()):
        item = tabel.item(tabel.currentRow(), column)
        if not item: continue
        nama_kolom = header_for_db(tabel.horizontalHeaderItem(column).text())
        if all_columns or nama_kolom in atribut_texts:
            atribut_values[nama_kolom] = item.text()
            if nama_kolom == "nis_lokal":
                atribut_values["nis_index"] = column
    for atribut, nilai in atribut_values.items():
        setattr(objek, atribut, nilai)
    if parent:
        if "nis_lokal" in atribut_values:
            setattr(parent, "nis_lokal", atribut_values["nis_lokal"])
            setattr(parent, "nis_index", atribut_values["nis_index"])
        elif "id_guru" in atribut_values:
            setattr(parent, "id_guru", atribut_values["id_guru"])
    return atribut_values


def update_column_width(metrics, column_widths, col_num, item_data, max_column_size=None):
    cell_width = metrics.horizontalAdvance(item_data)
    if max_column_size and cell_width > max_column_size:
        cell_width = max_column_size
    if cell_width > column_widths[col_num]:
        column_widths[col_num] = cell_width


def adjust_column_widths(table, column_widths, headers, metrics, margin):
    for col_num, column_width in enumerate(column_widths):
        header_width = metrics.horizontalAdvance(headers[col_num])
        table.setColumnWidth(col_num, max(column_width, header_width) + margin)


def header_for_table(headers):
    keys = headers
    new_keys = []
    for key in keys:
        if key:
            new_key = key.replace("_", " ").upper()
        else:
            new_key = "x"
        new_keys.append(new_key)
    return new_keys


def header_for_db(headers):
    if isinstance(headers, list):
        keys = headers
        new_keys = []
        for key in keys:
            if key:
                new_key = key.replace(" ", "_").lower()
                new_keys.append(new_key)
            else:
                new_keys.append("")
        return new_keys
    elif isinstance(headers, str):
        key = headers
        new_key = ""
        new_key = key.replace(" ", "_").lower()
        return new_key
    return None

def format_cell_data(item_data, zero=None):
    if item_data is None: return ""
    elif isinstance(item_data, (datetime, date)): return date_to_text(item_data, 'YMD')
    elif isinstance(item_data, int):
        if item_data == 0: return str(zero) if zero is not None else ""
        else: return str(item_data)
    elif isinstance(item_data, (decimal.Decimal, float)):
        if item_data == 0:
            return str(zero) if zero is not None else ""
        if isinstance(item_data, decimal.Decimal) and item_data == item_data.to_integral_value():
            return f"{item_data:.0f}"
        if isinstance(item_data, float):
            if item_data.is_integer(): return f"{item_data:.0f}"
            else: return f"{item_data:.2f}"
        else: return str(item_data)
    elif isinstance(item_data, dict):
        return {key: format_cell_data(value) for key, value in item_data.items()}
    elif isinstance(item_data, list):
        return [format_cell_data(item) for item in item_data]
    return str(item_data)


def fill_table_with_input(
    data,
    table: QTableWidget,
    column_names=None,  # Nama kolom opsional untuk kasus data kosong
    left_column=None,
    hidden_column=None,
    stretch_column=None,
    icon_awal=None,
    icon_akhir=None,
    fungsi_awal=None,
    fungsi_akhir=None,
    zero=None,
    margin=20,
    max_column_size=1000,
    row_height=24,
    font_family="Segoe UI",
    font_size=9,
):
    """
    Mengisi tabel dengan data, menambahkan baris kosong untuk input baru.
    - Jika data kosong dan column_names=None, tabel kosong tanpa baris.
    - Jika data kosong dan column_names diisi, tambah satu baris kosong.
    """
    # Default untuk left_column
    if left_column is None:
        left_column = LEFT_COLUMN
    
    # Validasi input data
    if not isinstance(data, (list, tuple)) or not all(isinstance(row, dict) for row in data):
        raise ValueError("Parameter 'data' harus berupa list atau tuple berisi dictionary.")

    # Bersihkan tabel dan nonaktifkan update
    table.clearContents()
    table.setUpdatesEnabled(False)
    table.blockSignals(True)

    # Kasus data kosong
    if not data:
        if column_names is None:
            # Tidak ada data dan tidak ada column_names: tabel kosong tanpa baris
            table.setRowCount(0)
            num_columns = (1 if icon_awal else 0) + (1 if icon_akhir else 0) or 1
            table.setColumnCount(num_columns)
            headers = [""] * num_columns
            table.setHorizontalHeaderLabels(headers)
            table.setFont(QFont(font_family, font_size))
            # Tidak ada baris kosong ditambahkan
        else:
            # Data kosong tapi column_names ada: tambah satu baris kosong
            table.setRowCount(1)
            num_columns = len(column_names) + (1 if icon_awal else 0) + (1 if icon_akhir else 0)
            table.setColumnCount(num_columns)
            headers = []
            if icon_awal:
                headers.append("")
            headers.extend(column_names)
            if icon_akhir:
                headers.append("")
            table.setHorizontalHeaderLabels(headers)
            table.setFont(QFont(font_family, font_size))
            add_empty_row(table, 0, headers, icon_awal, icon_akhir, fungsi_awal, fungsi_akhir)
    
    # Kasus ada data
    else:
        table.setRowCount(len(data) + 1)  # Tambah 1 untuk baris kosong di akhir
        num_columns = len(data[0]) + (1 if icon_awal else 0) + (1 if icon_akhir else 0)
        table.setColumnCount(num_columns)
        
        # Buat header dari kunci data
        headers = []
        if icon_awal:
            headers.append("")
        headers.extend(header_for_table(data[0].keys()))  # Fungsi pendukung diasumsikan ada
        if icon_akhir:
            headers.append("")
        
        table.setHorizontalHeaderLabels(headers)
        table.setFont(QFont(font_family, font_size))
        metrics = QFontMetrics(table.font())
        column_widths = [0] * len(headers)

        # Isi data
        for row_num, row_data in enumerate(data):
            if icon_awal:
                add_icon_button(table, row_num, 0, icon_awal, fungsi_awal)
            start_col = 1 if icon_awal else 0
            for col_num, (key, item_data) in enumerate(row_data.items(), start_col):
                item_data = format_cell_data(item_data, zero=zero)  # Fungsi pendukung diasumsikan ada
                item = QTableWidgetItem(item_data)
                key = header_for_db(key)  # Fungsi pendukung diasumsikan ada
                if isinstance(key, str) and key.lower() in left_column:
                    align = Qt.AlignLeft | Qt.AlignVCenter
                else:
                    align = Qt.AlignHCenter | Qt.AlignVCenter
                item.setTextAlignment(align)
                table.setItem(row_num, col_num, item)
                update_column_width(metrics, column_widths, col_num, item_data, max_column_size)  # Fungsi pendukung

            if icon_akhir:
                add_icon_button(table, row_num, len(headers) - 1, icon_akhir, fungsi_akhir)

        # Tambah baris kosong di akhir
        add_empty_row(table, len(data), headers, icon_awal, icon_akhir, fungsi_awal, fungsi_akhir)

        # Pengaturan tambahan
        if hidden_column:
            for col_index in hidden_column:
                table.setColumnHidden(col_index, True)
        if stretch_column is not None:
            if isinstance(stretch_column, int):
                table.horizontalHeader().setSectionResizeMode(stretch_column, QHeaderView.Stretch)
            elif isinstance(stretch_column, (list, tuple)):
                for col_index in stretch_column:
                    table.horizontalHeader().setSectionResizeMode(col_index, QHeaderView.Stretch)
        adjust_column_widths(table, column_widths, headers, metrics, margin)  # Fungsi pendukung

    # Finalisasi tampilan
    table.resizeRowsToContents()
    table.verticalHeader().setMinimumSectionSize(row_height)
    table.setUpdatesEnabled(True)
    table.blockSignals(False)


def add_empty_row(table, row_index, headers, icon_awal, icon_akhir, fungsi_awal, fungsi_akhir):
    """Menambahkan baris kosong di indeks tertentu untuk input data baru."""
    if icon_awal:
        add_icon_button(table, row_index, 0, icon_awal, fungsi_awal)
    if icon_akhir:
        add_icon_button(table, row_index, len(headers) - 1, icon_akhir, fungsi_akhir)


def handle_item_changed(
        tabel_ui:QTableWidget, 
        tabel_sql, 
        primary_key, 
        must_insert, 
        updatable_column=None, 
        not_updatable_column=None):
    """Menangani perubahan item dalam QTableWidget untuk menentukan apakah update atau insert."""
    sukses = True
    row = tabel_ui.currentRow()
    is_last_row = row == tabel_ui.rowCount() - 1
    row_data = get_row_data(tabel_ui, numeric_fields=[], date_fields=[], row=row)
    if not row_data:
        return False
    primary_key_value = row_data.get(primary_key)
    if is_last_row:
        for col in must_insert:
            if row_data.get(col) in [None, '']: 
                print(f"Menunggu input lengkap sebelum insert: {col} kosong.")
                return False
        sukses = insert_from_table(tabel_sql, row_data)
    elif primary_key_value:
        sukses = update_from_table(
            tabel_ui=tabel_ui,
            tabel_sql=tabel_sql,
            updatable_column=updatable_column,
            not_updatable_column=not_updatable_column,
            key=primary_key,
            key_value=primary_key_value
        )
    else:
        print("Primary key tidak ditemukan, update dibatalkan.")
    if sukses:
        return True
    return False

def insert_from_table(tabel_sql, row_data: dict):
    if not tabel_sql or not row_data:
        return False
    con = ConnectDB()
    columns = ", ".join([key for key in row_data if row_data[key] not in [None, '']])
    placeholders = ", ".join(["%s"] * len([key for key in row_data if row_data[key] not in [None, '']]))
    sql = f"INSERT INTO {tabel_sql} ({columns}) VALUES ({placeholders})"
    params = tuple(row_data[key] for key in row_data if row_data[key] not in [None, ''])
    return con.update_data(sql, params)


def get_row_data(tabel_ui: QTableWidget, numeric_fields, date_fields, row):
    if tabel_ui is None: 
        return {}
    column_count = tabel_ui.columnCount()
    headers = [header_for_db(tabel_ui.horizontalHeaderItem(col).text()) for col in range(column_count)]
    row_data = {}
    if numeric_fields is None:
        numeric_fields = []
    if date_fields is None:
        date_fields = []
    for col in range(column_count):
        item = tabel_ui.item(row, col)
        cell_value = item.text() if item else None  # None lebih aman daripada ""
        if col in numeric_fields:
            try:
                cell_value = float(cell_value) if cell_value else None
            except ValueError:
                cell_value = None  # Jika gagal parsing, set ke None
        if col in date_fields:
            try:
                cell_value = text_to_date(cell_value)
            except ValueError:
                cell_value = None  # Jika gagal parsing, set ke None
        row_data[headers[col]] = cell_value

    return row_data

def get_selected_table_data(table: QTableWidget, target_columns=None):
    tabel = table
    selected_ranges = tabel.selectedRanges()
    if not selected_ranges:
        return None
    if target_columns is None:
        target_columns = []
        for col in range(tabel.columnCount()):
            header_item = tabel.horizontalHeaderItem(col)
            if header_item:
                target_columns.append(header_for_db(header_item.text()))
    if not isinstance(target_columns, list):
        raise ValueError("target_columns harus berupa list atau None.")
    index_kolom = {}
    for col in range(tabel.columnCount()):
        header_item = tabel.horizontalHeaderItem(col)
        if header_item and header_for_db(header_item.text()) in target_columns:
            index_kolom[header_for_db(header_item.text())] = col
    if not index_kolom:
        raise ValueError(f"Tidak ada kolom yang sesuai dengan target_columns: {target_columns}")
    result = []
    for selected_range in selected_ranges:
        top_row = selected_range.topRow()
        bottom_row = selected_range.bottomRow()
        for row in range(top_row, bottom_row + 1):
            row_data = {}
            for col_name, col_index in index_kolom.items():
                item = tabel.item(row, col_index)
                row_data[col_name] = item.text() if item else None
            result.append(row_data)
    return result

def update_from_table(
        tabel_ui: QTableWidget, 
        tabel_sql, 
        updatable_column=None, 
        not_updatable_column=None, 
        key=None, 
        key_value=None,
        # update_function = None
    ):
    # Validasi parameter
    if tabel_ui is None: return False
    if key is None: 
        print("Error: Primary key tidak ditemukan.")
        return False

    # Cek apakah ada kolom yang sama di kedua parameter
    if updatable_column and not_updatable_column:
        common_columns = set(updatable_column).intersection(set(not_updatable_column))
        if common_columns:
            print(f"Error: Kolom berikut ada di kedua parameter: {', '.join(common_columns)}")
            return False

    sukses = False
    nama_kolom = header_for_db(tabel_ui.horizontalHeaderItem(tabel_ui.currentColumn()).text())
    nilai = tabel_ui.item(tabel_ui.currentRow(), tabel_ui.currentColumn()).text().strip()
    # print(nilai)
    # Proses konversi tanggal jika diperlukan
    if 'tgl' in nama_kolom.lower() or 'tanggal' in nama_kolom.lower():
        try: 
            nilai = text_to_date(nilai)
        except ValueError as e:
            print(f"Error konversi nilai ke tanggal: {e}")
            return False
        
    con = ConnectDB()
    if updatable_column:
        if nama_kolom in updatable_column:
            sql = f"""UPDATE {tabel_sql} SET {nama_kolom} = %s WHERE {key} = %s;"""
            params = (nilai, key_value)
            sukses = con.update_data(sql, params)
    # Eksekusi update berdasarkan kolom yang tidak dapat diperbarui
    elif not_updatable_column:
        if nama_kolom not in not_updatable_column:
            sql = f"""UPDATE {tabel_sql} SET {nama_kolom} = %s WHERE {key} = %s;"""
            params = (nilai, key_value)
            sukses = con.update_data(sql, params)
    if sukses: 
        print(f'Update berhasil: {nama_kolom} dengan nilai {nilai}')
        
    else:
        print("Update gagal.")
    return sukses

def convert_item_value(value, header_name):
    """ Konversi nilai dari QTableWidgetItem berdasarkan tipe data """
    if value is None or value.strip() == "":
        return "NULL", None  # Kosong → NULL di SQL
    
    # value = value.strip().replace("'", "''")  # Escape SQL

    if header_name in KOLOM_ANGKA:
        try:
            int_value = int(value)
            return str(int_value), int_value
        except ValueError:
            return "NULL", None  # Jika gagal, anggap NULL
    
    if header_name in KOLOM_FLOAT:
        try:
            float_value = float(value)
            return str(float_value), float_value
        except ValueError:
            return "NULL", None

    if header_name in KOLOM_TANGGAL:
        date_value = text_to_date(value)  # Konversi ke format tanggal
        return (f"'{date_value}'", date_value) if date_value else ("NULL", None)

    return f"'{value}'", value  # Default: String dengan petik satu


def cek_eksistensi(conn, tabel_db, kolom_key, key_value):
    """Cek apakah key_value sudah ada di database"""
    sql = f"SELECT 1 FROM {tabel_db} WHERE {kolom_key} = %s LIMIT 1"
    result = conn.get_one_data(sql, (key_value,))
    return bool(result)

import pandas as pd

def generate_insert_queries(tabel_db, excel_file_path):
    """Membuat query INSERT berdasarkan data dari sheet Excel, mempertahankan 'NA' sebagai string"""
    queries = []
    df = pd.read_excel(excel_file_path, sheet_name=tabel_db, keep_default_na=False)
    for index, row in df.iterrows():
        fields = []
        values = []
        new_data = {}
        for header_name, value in row.items():
            item_text = str(value).strip()
            sql_value, py_value = convert_item_value(item_text, header_name)
            fields.append(header_name)
            values.append(sql_value)
            new_data[header_name] = py_value
        if not fields:
            continue
        sql_insert = f"INSERT INTO {tabel_db} ({', '.join(fields)}) VALUES ({', '.join(['%s'] * len(values))})"
        queries.append((sql_insert, tuple(new_data.values())))
    
    return queries

# def generate_update_queries(conn, tabel_db, excel_file_path, kolom_key):
#     """Membuat query UPDATE berdasarkan perbandingan data lama dan baru dari file Excel"""
#     queries = []
    
#     # Baca file Excel menggunakan pandas
#     df = pd.read_excel(excel_file_path)
    
#     # Iterasi melalui setiap baris dalam DataFrame
#     for index, row in df.iterrows():
#         fields = []
#         new_data = {}
#         key_value = None

#         # Iterasi melalui setiap kolom dalam baris
#         for header_name, value in row.items():
#             header_db = header_for_db(str(header_name))
            
#             item_text = str(value).strip() if pd.notna(value) else None
#             sql_value, py_value = convert_item_value(item_text, header_db)

#             if header_db == kolom_key:
#                 key_value = py_value
            
#             fields.append(header_db)
#             new_data[header_db] = py_value

#         if not fields or key_value is None:
#             continue

#         # Hanya proses UPDATE jika data sudah ada
#         if cek_eksistensi(conn, tabel_db, kolom_key, key_value):
#             old_data = get_old_data(conn, tabel_db, kolom_key, key_value)
#             changes = []
#             update_values = []

#             for key, new_value in new_data.items():
#                 old_value = old_data.get(key, None)
#                 old_value_str = str(old_value).strip() if old_value is not None else ""
#                 new_value_str = str(new_value).strip() if new_value is not None else ""

#                 if old_value_str != new_value_str:
#                     changes.append(f"{key} = %s")
#                     update_values.append(new_value)

#             if changes:
#                 key_condition = f"{kolom_key} = %s"
#                 sql_update = f"UPDATE {tabel_db} SET {', '.join(changes)} WHERE {key_condition}"
#                 queries.append((sql_update, tuple(update_values) + (key_value,)))

#     return queries

def get_old_data(conn, tabel_db, kolom_key, key_value):
    """Mengambil data lama dari database berdasarkan primary key"""
    query = f"SELECT * FROM {tabel_db} WHERE {kolom_key} = %s"
    params = (key_value,)
    result = conn.get_one_data(query, params)
    return result if result else {}  # Jika tidak ada data, kembalikan dictionary kosong


def generate_table_raw(data, table: QTableWidget):
    """Mengisi QTableWidget dengan data secara optimal."""
    
    if not isinstance(data, (list, tuple)) or not all(isinstance(row, dict) for row in data):
        raise ValueError("Parameter 'data' harus berupa list atau tuple berisi dictionary.")

    if not data:
        table.clear()
        table.setRowCount(0)
        table.setColumnCount(0)
        return

    table.setUpdatesEnabled(False)  # Matikan update GUI sementara
    table.blockSignals(True)        # Matikan sinyal sementara
    table.setSortingEnabled(False)  # Matikan sorting sementara
    
    table.clearContents()
    table.setRowCount(len(data))
    table.setColumnCount(len(data[0]))

    headers = list(data[0].keys())
    table.setHorizontalHeaderLabels(headers)

    # Buat semua item terlebih dahulu untuk menghindari alokasi berulang
    for row_num, row_data in enumerate(data):
        for col_num, (key, value) in enumerate(row_data.items()):
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, value)  # Lebih cepat daripada setItem()
            table.setItem(row_num, col_num, item)

    table.setSortingEnabled(True)   # Aktifkan kembali sorting
    table.blockSignals(False)       # Aktifkan kembali sinyal
    table.setUpdatesEnabled(True)


def sum_column(tabel, column):
    total = 0
    for row in range(tabel.rowCount()):
        item = tabel.item(row, column)
        if item is not None:
            total += int(item.text() or 0)
    return total


def copyCells(tabel):
    try:
        copied_cells = sorted(tabel.selectedIndexes())
        copy_text = ""
        max_column = copied_cells[-1].column()
        merged_cells = {}
        
        # Mendata sel yang digabungkan (rowSpan)
        for c in copied_cells:
            row = c.row()
            column = c.column()
            merge_range = tabel.rowSpan(row, column)
            if merge_range > 1:
                merged_cells[(row, column)] = merge_range
        
        # Menambahkan header tabel ke teks
        headers = [f'"{tabel.horizontalHeaderItem(column).text()}"' for column in range(max_column + 1)]
        copy_text = "\t".join(headers) + "\n"
        
        current_row = 0
        current_column = 0
        for c in copied_cells:
            row = c.row()
            column = c.column()
            merge_range = merged_cells.get((row, column), 1)
            
            # Jika baris berubah, pindah ke baris berikutnya
            if row != current_row:
                current_row = row
                current_column = 0  # Reset posisi kolom
                
            cell = tabel.item(row, column)
            cell_text = cell.text() if cell is not None else ""
            
            # Tambahkan tanda kutip ganda di sekitar teks
            cell_text = f'"{cell_text}"'
            
            # Menambahkan tab sesuai perbedaan posisi kolom
            copy_text += "\t" * (column - current_column)
            copy_text += cell_text
            
            # Tambahkan tab untuk sel yang digabungkan
            copy_text += "\t" * (merge_range - 1)
            
            # Perbarui kolom saat ini
            current_column = column + merge_range
            
            # Tambahkan baris baru jika di akhir kolom, atau tab jika tidak
            if column == max_column:
                copy_text += "\n"
            else:
                copy_text += "\t"
        
        # Salin teks ke clipboard
        QApplication.clipboard().setText(copy_text)
    except ValueError:
        return None


def count_column(tabel: QTableWidget, column: int, filter: str):
    count = 0
    for row in range(tabel.rowCount()):
        item = tabel.item(row, column)
        if item is not None:
            if item.text() == filter:
                count += 1
            else:
                pass
    return count

def next_table_item(tabel: QTableWidget, cur_row=None):
    current_row = cur_row if cur_row else tabel.currentRow()
    next_row = current_row + 1
    if next_row < tabel.rowCount():
        tabel.selectRow(next_row)
    else:
        tabel.selectRow(0)


def prev_table_item(tabel: QTableWidget):
    current_row = tabel.currentRow()
    prev_row = current_row - 1
    if prev_row < 0:
        prev_row = tabel.rowCount() - 1
    tabel.selectRow(prev_row)