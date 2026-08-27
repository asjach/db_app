import decimal, os
from datetime import datetime, date
from utils.database import ConnectDB
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QApplication
from PySide6.QtGui import QFontMetrics, QFont, QIcon
from utils.fungsi.functions import show_message, date_to_text, text_to_date, get_json_data, validate_sql_identifier
from PySide6.QtCore import Qt
import pandas as pd
from utils.app_config import SEPARATOR_DESIMAL, SEPARATOR_RIBUAN, BASE_DIR

static_values = get_json_data(os.path.join(BASE_DIR, "utils/static_values.json"))

def generate_table(
    data,
    table: QTableWidget,
    column_names=None,
    left_column=None,
    hidden_column=None,
    stretch_column=None,
    margin=24,
    row_height=24,
    max_column_size=1000,
    font_family="Segoe UI",
    font_size=10,
    icon_awal=None,
    icon_akhir=None,
    fungsi_awal=None,
    fungsi_akhir=None,
    zero=None,
    separator_ribuan=None,
    separator_desimal=None,
    kolom_currency=None,
    mode_input=False,
):
    """
    Mengisi tabel dengan data. Jika mode_input=True, tambahkan baris kosong untuk input baru.
    - Jika mode_input=True dan data kosong serta column_names=None, tabel kosong tanpa baris.
    - Jika mode_input=True dan data kosong serta column_names diisi, tambah satu baris kosong.
    - Jika mode_input=False dan data kosong, tabel dihapus.
    """
    if left_column is None:
        left_column = static_values['LEFT_COLUMN']
    if separator_desimal is None:
        separator_desimal = SEPARATOR_DESIMAL
    if separator_ribuan is None:
        separator_ribuan = SEPARATOR_RIBUAN
    if kolom_currency is None:
        kolom_currency = static_values['KOLOM_CURRENCY']
    if isinstance(data, pd.DataFrame):
        data = data.fillna("")
        data = data.to_dict(orient="records")
    if not isinstance(data, (list, tuple)) or not all(isinstance(row, dict) for row in data):
        raise ValueError("Parameter 'data' harus berupa list atau tuple berisi dictionary.")

    # Selalu bersihkan tabel sepenuhnya sebelum memulai
    prepare_table(table)
    table.clear()  # Hapus isi dan header

    if not data:
        if mode_input:
            if column_names is None:
                # Tabel kosong tanpa baris atau header lama
                table.setRowCount(1)
                num_columns = (1 if icon_awal else 0) + (1 if icon_akhir else 0) or 1
                table.setColumnCount(num_columns)
                headers = [""] * num_columns
                table.setHorizontalHeaderLabels(headers)
                table.setFont(QFont(font_family, font_size))
            else:
                # Tambah satu baris kosong
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
        else:
            # Mode biasa: hapus tabel sepenuhnya
            table.setRowCount(0)
            table.setColumnCount(0)
            # finalize_table(table)
            return
    else:
        # Logika untuk data tidak kosong (tidak diubah karena tidak relevan dengan bug)
        table.setRowCount(len(data) + (1 if mode_input else 0))
        num_columns = len(data[0]) + (1 if icon_awal else 0) + (1 if icon_akhir else 0)
        table.setColumnCount(num_columns)

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

        for row_num, row_data in enumerate(data):
            if icon_awal:
                add_icon_button(table, row_num, 0, icon_awal, fungsi_awal)
            start_col = 1 if icon_awal else 0
            for col_num, (key, item_data) in enumerate(row_data.items(), start_col):
                apply_format = kolom_currency and key in kolom_currency
                item_data = format_cell_data(
                    item_data,
                    zero=zero,
                    separator_ribuan=separator_ribuan if apply_format else None,
                    separator_desimal=separator_desimal if apply_format else None
                )
                item = QTableWidgetItem(item_data)
                key = header_for_db(key)
                if isinstance(key, str) and key.lower() in left_column:
                    align = Qt.AlignLeft | Qt.AlignVCenter
                elif isinstance(key, str) and key.lower() in kolom_currency:
                    align = Qt.AlignRight | Qt.AlignVCenter
                else:
                    align = Qt.AlignHCenter | Qt.AlignVCenter
                item.setTextAlignment(align)
                table.setItem(row_num, col_num, item)
                update_column_width(metrics, column_widths, col_num, item_data, max_column_size)
            if icon_akhir:
                add_icon_button(table, row_num, len(headers) - 1, icon_akhir, fungsi_akhir)

        if mode_input:
            add_empty_row(table, len(data), headers, icon_awal, icon_akhir, fungsi_awal, fungsi_akhir)

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

    finalize_table(table, font_size=font_size)

def prepare_table(table: QTableWidget, clear=True):
    table.blockSignals(True)
    if clear:
        table.clearContents()
    table.setUpdatesEnabled(False)
    

def finalize_table(table: QTableWidget, font_size=10):
    row_height = max(24, font_size * 2 )
    table.verticalHeader().setDefaultSectionSize(row_height)
    table.verticalHeader().setDefaultAlignment(Qt.AlignRight)
    table.setUpdatesEnabled(True)
    table.blockSignals(False)

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


def add_icon_button(table:QTableWidget, row_num, col_num, icon, fungsi):
    button = QPushButton()
    button.setFlat(True)
    button.setIcon(QIcon(icon))
    button.clicked.connect(fungsi)
    table.setCellWidget(row_num, col_num, button)
    

def update_column_width(metrics, column_widths, col_num, item_data, max_column_size=None):
    cell_width = metrics.horizontalAdvance(item_data)
    if max_column_size and cell_width > max_column_size:
        cell_width = max_column_size
    if cell_width > column_widths[col_num]:
        column_widths[col_num] = cell_width


def format_cell_data(item_data, zero=None, separator_ribuan=None, separator_desimal=None):
    
    if item_data is None:
        return ""
    if isinstance(item_data, (datetime, date)):
        return date_to_text(item_data, 'YMD')
    elif isinstance(item_data, int):
        if item_data == 0:
            return str(zero) if zero is not None else ""
        else:
            if separator_ribuan:
                return f"{item_data:,}".replace(",", separator_ribuan)
            return str(item_data)
    elif isinstance(item_data, (decimal.Decimal, float)):
        if item_data == 0:
            return str(zero) if zero is not None else ""
        if isinstance(item_data, decimal.Decimal) and item_data == item_data.to_integral_value():
            # Bilangan bulat dari Decimal
            if separator_ribuan:
                return f"{int(item_data):,}".replace(",", separator_ribuan)
            return f"{item_data:.0f}"
        if isinstance(item_data, float) and item_data.is_integer():
            # Bilangan bulat dari float
            if separator_ribuan:
                return f"{int(item_data):,}".replace(",", separator_ribuan)
            return f"{item_data:.0f}"
        else:
            # Bilangan desimal
            formatted = f"{item_data:.2f}"
            if separator_ribuan or separator_desimal:
                # Pisahkan bagian integer dan desimal
                integer_part, decimal_part = formatted.split(".")
                if separator_ribuan:
                    integer_part = f"{int(integer_part):,}".replace(",", separator_ribuan)
                if separator_desimal:
                    return f"{integer_part}{separator_desimal}{decimal_part}"
                return f"{integer_part}.{decimal_part}"
            return formatted
    elif isinstance(item_data, dict):
        return {key: format_cell_data(value, zero, separator_ribuan, separator_desimal) 
                for key, value in item_data.items()}
    elif isinstance(item_data, list):
        return [format_cell_data(item, zero, separator_ribuan, separator_desimal) 
                for item in item_data]
    return str(item_data)


def add_empty_row(table, row_index, headers, icon_awal, icon_akhir, fungsi_awal, fungsi_akhir):
    """Menambahkan baris kosong di indeks tertentu untuk input data baru."""
    if icon_awal:
        add_icon_button(table, row_index, 0, icon_awal, fungsi_awal)
    if icon_akhir:
        add_icon_button(table, row_index, len(headers) - 1, icon_akhir, fungsi_akhir)


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
    row_data = get_row_data(tabel_ui, numeric_fields=None, date_fields=None, row=row)
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

def handle_item_changed_v2(
    tabel_ui: QTableWidget,
    tabel_sql: str,
    item: QTableWidgetItem,  # Tambahkan parameter item
    primary_key: str,
    must_insert: list = None,
    updatable_column: list = None,
    not_updatable_column: list = None
):
    """Menangani perubahan item dalam QTableWidget untuk update atau insert, termasuk saat paste."""
    if tabel_ui is None or item is None:
        return False

    # Dapatkan baris dan kolom dari item yang diubah
    row = item.row()
    col = item.column()
    is_last_row = row == tabel_ui.rowCount() - 1

    # Dapatkan data baris
    row_data = get_row_data(tabel_ui, row=row)
    if not row_data:
        return False
    primary_key_value = row_data.get(primary_key)

    # Dapatkan nama kolom dan nilai yang diubah
    header_item = tabel_ui.horizontalHeaderItem(col)
    if header_item is None:
        print(f"Kolom pada indeks {col} tidak memiliki header.")
        return False
    nama_kolom = header_for_db(header_item.text())
    nilai = item.text()
    nilai = convert_item_value(nilai, nama_kolom)[1]

    sukses = True
    con = ConnectDB()
    if is_last_row and must_insert:
        # Baris terakhir: coba insert jika semua kolom wajib terisi
        for col in must_insert:
            if row_data.get(col) in [None, '']:
                print(f"Menunggu input lengkap sebelum insert: {col} kosong.")
                return False
        sukses = insert_from_table(tabel_sql, row_data)
        if sukses:
            print(f"Insert berhasil untuk baris {row}.")
        else:
            print(f"Insert gagal untuk baris {row}.")
    elif primary_key_value:
        # Baris dengan primary key: coba update kolom yang diubah
        if updatable_column and nama_kolom not in updatable_column:
            print(f"Kolom {nama_kolom} tidak dapat diupdate (bukan updatable_column).")
            return False
        if not_updatable_column and nama_kolom in not_updatable_column:
            print(f"Kolom {nama_kolom} tidak dapat diupdate (not_updatable_column).")
            return False
        sql = f"""UPDATE {tabel_sql} SET {nama_kolom} = %s WHERE {primary_key} = %s;"""
        params = (nilai, primary_key_value)
        sukses = con.update_data(sql, params)
        if sukses:
            print(f"Update berhasil: {nama_kolom} dengan nilai {nilai} pada baris {row}.")
        else:
            print(f"Update gagal: {nama_kolom} pada baris {row}.")
    else:
        print(f"Baris {row}: Primary key tidak ditemukan, update dibatalkan.")

    return sukses


def get_row_data(tabel_ui: QTableWidget, numeric_fields=None, date_fields=None, row=None):
    if tabel_ui is None: 
        return {}
    if numeric_fields is None:
        numeric_fields = static_values['KOLOM_ANGKA']
    if date_fields is None:
        date_fields = static_values['KOLOM_TANGGAL']
    column_count = tabel_ui.columnCount()
    headers = [header_for_db(tabel_ui.horizontalHeaderItem(col).text()) for col in range(column_count)]
    row_data = {}
    # if numeric_fields is None:
    #     numeric_fields = []
    # if date_fields is None:
    #     date_fields = []
    for col in range(column_count):
        item = tabel_ui.item(row, col)
        cell_value = item.text() if item else None
        if col in numeric_fields:
            try:
                cell_value = float(cell_value) if cell_value else None
            except ValueError:
                cell_value = None
        if col in date_fields:
            try:
                cell_value = text_to_date(cell_value)
            except ValueError:
                cell_value = None
        row_data[headers[col]] = cell_value
    return row_data

def findColumnByName(tabel: QTableWidget, nama_kolom_ui: str) -> int:
    for col in range(tabel.columnCount()):
        header_item = tabel.horizontalHeaderItem(col)
        if header_item and header_item.text().strip().lower() == nama_kolom_ui.strip().lower():
            return col
    return -1  # Jika tidak ditemukan

def update_from_table(
        tabel_ui: QTableWidget, 
        tabel_sql, 
        updatable_column=None, 
        not_updatable_column=None, 
        key=None, 
        key_value=None,
    ):
    if tabel_ui is None: return False
    if key is None: 
        print("Error: Primary key tidak ditemukan.")
        return False
    tabel_sql = validate_sql_identifier(tabel_sql)
    if updatable_column and not_updatable_column:
        common_columns = set(updatable_column).intersection(set(not_updatable_column))
        if common_columns:
            print(f"Error: Kolom berikut ada di kedua parameter: {', '.join(common_columns)}")
            return False
    sukses = False
    nilai = tabel_ui.item(tabel_ui.currentRow(), tabel_ui.currentColumn()).text()
    nilai = convert_item_value(nilai, header_for_db(tabel_ui.horizontalHeaderItem(tabel_ui.currentColumn()).text()))[1]
    
    con = ConnectDB()
    nama_kolom = validate_sql_identifier(header_for_db(tabel_ui.horizontalHeaderItem(tabel_ui.currentColumn()).text()))
    if updatable_column:
        if nama_kolom in updatable_column:
            sql = """UPDATE {} SET {} = %s WHERE {} = %s;""".format(tabel_sql, nama_kolom, key)
            params = (nilai, key_value)
            sukses = con.update_data(sql, params)
    elif not_updatable_column:
        if nama_kolom not in not_updatable_column:
            sql = """UPDATE {} SET {} = %s WHERE {} = %s;""".format(tabel_sql, nama_kolom, key)
            params = (nilai, key_value)
            sukses = con.update_data(sql, params)
    if sukses: 
        print(f'Update berhasil: {nama_kolom} dengan nilai {nilai}')
    else:
        print("Update gagal.")
    return sukses


def insert_from_table(tabel_sql, row_data: dict):
    if not tabel_sql or not row_data:
        return False
    con = ConnectDB()
    tabel_sql = validate_sql_identifier(tabel_sql)
    valid_columns = [validate_sql_identifier(key) for key in row_data if row_data[key] not in [None, '']]
    columns = ", ".join(valid_columns)
    placeholders = ", ".join(["%s"] * len(valid_columns))
    sql = f"INSERT INTO {tabel_sql} ({columns}) VALUES ({placeholders})"
    params = tuple(row_data[key] for key in row_data if row_data[key] not in [None, ''])
    return con.update_data(sql, params)


def convert_item_value(value, header_name, separator_ribuan=None, separator_desimal=None):
    """ Konversi nilai dari QTableWidgetItem berdasarkan tipe data """
    if value is None or value.strip() == "":
        return "NULL", None  # Kosong → NULL di SQL
    if separator_ribuan is None:
        separator_ribuan = SEPARATOR_RIBUAN
    if separator_desimal is None:
        separator_desimal = SEPARATOR_DESIMAL
    
    cleaned_value = value.strip()
    
    # Terapkan pembersihan separator hanya untuk KOLOM_CURRENCY
    if header_name in static_values['KOLOM_CURRENCY']:
        if separator_ribuan and separator_ribuan in cleaned_value:
            cleaned_value = cleaned_value.replace(separator_ribuan, "")
        if separator_desimal and separator_desimal in cleaned_value:
            cleaned_value = cleaned_value.replace(separator_desimal, ".")
    
    if header_name in static_values['KOLOM_ANGKA']:
        try:
            int_value = int(cleaned_value)
            return str(int_value), int_value
        except ValueError:
            return "NULL", None  # Jika gagal, anggap NULL
    elif header_name in static_values['KOLOM_CURRENCY']:
        try:
            float_value = float(cleaned_value)
            return str(float_value), float_value
        except ValueError:
            return "NULL", None
    elif header_name in static_values['KOLOM_FLOAT']:
        try:
            float_value = float(cleaned_value)
            return str(float_value), float_value
        except ValueError:
            return "NULL", None
    elif header_name in static_values['KOLOM_TANGGAL']:
        date_value = text_to_date(cleaned_value)  # Konversi ke format tanggal
        return (f"'{date_value}'", date_value) if date_value else ("NULL", None)
    else:
        # Default: String dengan petik satu, tanpa pembersihan separator
        return f"'{cleaned_value}'", cleaned_value
    

# def convert_item_value(value, header_name, separator_ribuan=None, separator_desimal=None):
#     """ Konversi nilai dari QTableWidgetItem berdasarkan tipe data """
#     if value is None or value.strip() == "":
#         return "NULL", None  # Kosong → NULL di SQL
#     if separator_ribuan is None:
#         separator_ribuan=SEPARATOR_RIBUAN
#     if separator_desimal is None:
#         separator_desimal = SEPARATOR_DESIMAL
#     cleaned_value = value.strip()
#     if separator_ribuan and separator_ribuan in cleaned_value:
#         cleaned_value = cleaned_value.replace(separator_ribuan, "")
#     if separator_desimal and separator_desimal in cleaned_value:
#         cleaned_value = cleaned_value.replace(separator_desimal, ".")
#     if header_name in KOLOM_ANGKA:
#         try:
#             int_value = int(cleaned_value)
#             return str(int_value), int_value
#         except ValueError:
#             return "NULL", None  # Jika gagal, anggap NULL
#     if header_name in KOLOM_FLOAT:
#         try:
#             float_value = float(cleaned_value)
#             return str(float_value), float_value
#         except ValueError:
#             return "NULL", None
#     if header_name in KOLOM_TANGGAL:
#         date_value = text_to_date(cleaned_value)  # Konversi ke format tanggal
#         return (f"'{date_value}'", date_value) if date_value else ("NULL", None)
#     return f"'{cleaned_value}'", cleaned_value  # Default: String dengan petik satu


def cek_eksistensi(conn, tabel_db, kolom_key, key_value):
    """Cek apakah key_value sudah ada di database"""
    tabel_db = validate_sql_identifier(tabel_db)
    kolom_key = validate_sql_identifier(kolom_key)
    sql = f"SELECT 1 FROM {tabel_db} WHERE {kolom_key} = %s LIMIT 1"
    result = conn.get_one_data(sql, (key_value,))
    return bool(result)


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


def get_old_data(conn, tabel_db, kolom_key, key_value):
    """Mengambil data lama dari database berdasarkan primary key"""
    tabel_db = validate_sql_identifier(tabel_db)
    kolom_key = validate_sql_identifier(kolom_key)
    query = f"SELECT * FROM {tabel_db} WHERE {kolom_key} = %s"
    params = (key_value,)
    result = conn.get_one_data(query, params)
    return result if result else {}  # Jika tidak ada data, kembalikan dictionary kosong


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
        if not copied_cells:
            return None

        copy_text = ""
        # Kumpulkan kolom unik yang dipilih
        selected_columns = sorted(set(c.column() for c in copied_cells))
        
        # Buat header hanya untuk kolom yang dipilih
        headers = [f'"{tabel.horizontalHeaderItem(col).text()}"' for col in selected_columns if tabel.horizontalHeaderItem(col) is not None]
        if headers:
            copy_text = "\t".join(headers) + "\n"
        
        # Tangani merged cells
        merged_cells = {}
        for c in copied_cells:
            row = c.row()
            column = c.column()
            merge_range = tabel.rowSpan(row, column)
            if merge_range > 1:
                merged_cells[(row, column)] = merge_range
        
        current_row = copied_cells[0].row()
        row_text = []
        current_column = 0
        
        for c in copied_cells:
            row = c.row()
            column = c.column()
            
            # Jika pindah ke baris baru
            if row != current_row:
                if row_text:  # Tambahkan baris hanya jika ada data
                    copy_text += "\t".join(row_text) + "\n"
                row_text = []
                current_row = row
                current_column = selected_columns[0]  # Reset ke kolom pertama yang dipilih
            
            # Tambahkan tab untuk kolom yang dilewati
            while current_column < column and current_column in selected_columns:
                row_text.append('""')  # Sel kosong untuk kolom yang dipilih
                current_column = selected_columns[selected_columns.index(current_column) + 1] if current_column in selected_columns[:-1] else current_column + 1
            
            # Ambil teks sel
            cell = tabel.item(row, column)
            cell_text = cell.text() if cell is not None else ""
            cell_text = f'"{cell_text}"'
            
            # Tambahkan teks sel
            row_text.append(cell_text)
            
            # Tangani merged cells
            merge_range = merged_cells.get((row, column), 1)
            current_column = column + merge_range
            
            # Jika ini adalah kolom terakhir yang dipilih di baris ini
            if column == selected_columns[-1]:
                if row_text:  # Tambahkan baris hanya jika ada data
                    copy_text += "\t".join(row_text) + "\n"
                row_text = []
                current_column = selected_columns[0]  # Reset ke kolom pertama yang dipilih
        
        # Jangan tambahkan baris terakhir jika row_text kosong
        if row_text and any(t.strip('""') for t in row_text):  # Pastikan ada data non-kosong
            copy_text += "\t".join(row_text) + "\n"
        
        # Salin teks ke clipboard
        QApplication.clipboard().setText(copy_text.strip())  # Hapus newline terakhir jika ada
        return copy_text
    except Exception as e:
        print(f"Error saat menyalin sel: {e}")
        return None
    

def pasteCells(tabel):
    clipboard = QApplication.clipboard()
    paste_text = clipboard.text()

    if not paste_text:
        return

    selected = tabel.selectedIndexes()
    if not selected:
        return
    # tabel.blockSignals(True)
    # Ambil baris unik yang dipilih (untuk mengetahui berapa baris target)
    selected_rows = sorted(set(index.row() for index in selected))
    selected_columns = sorted(set(index.column() for index in selected))

    if not selected_rows or not selected_columns:
        return

    start_row = selected_rows[0]
    start_col = selected_columns[0]
    total_selected_rows = len(selected_rows)

    # Parsing data dari clipboard
    copied_rows = paste_text.strip().split("\n")
    parsed_data = []
    for row_data in copied_rows:
        columns = [cell.strip('"') for cell in row_data.strip().split("\t")]
        parsed_data.append(columns)

    num_copied_rows = len(parsed_data)

    # Looping atau pemangkasan data sesuai jumlah baris yang dipilih
    for i in range(total_selected_rows):
        data_row = parsed_data[i % num_copied_rows]  # ulang jika i > jumlah data

        target_row = selected_rows[i]
        if target_row >= tabel.rowCount():
            tabel.setRowCount(target_row + 1)

        for j, cell_text in enumerate(data_row):
            target_col = start_col + j
            if target_col >= tabel.columnCount():
                tabel.setColumnCount(target_col + 1)

            item = QTableWidgetItem(cell_text)
            tabel.setItem(target_row, target_col, item)
    # tabel.blockSignals(False)


def update_from_table_v2(
        tabel_ui: QTableWidget, 
        tabel_sql, 
        item: QTableWidgetItem,  # Tambahkan parameter item
        updatable_column=None, 
        not_updatable_column=None, 
        key=None, 
        key_value=None,
    ):
    if tabel_ui is None or item is None:
        return False
    if key is None: 
        print("Error: Primary key tidak ditemukan.")
        return False
    if updatable_column and not_updatable_column:
        common_columns = set(updatable_column).intersection(set(not_updatable_column))
        if common_columns:
            print(f"Error: Kolom berikut ada di kedua parameter: {', '.join(common_columns)}")
            return False

    # Dapatkan baris dan kolom dari item
    row = item.row()
    col = item.column()

    # Dapatkan nama kolom dari header
    header_item = tabel_ui.horizontalHeaderItem(col)
    if header_item is None:
        print(f"Kolom pada indeks {col} tidak memiliki header.")
        return False
    nama_kolom = header_for_db(header_item.text())

    # Dapatkan nilai item
    nilai = item.text()
    nilai = convert_item_value(nilai, nama_kolom)[1]
    
    con = ConnectDB()
    sukses = False
    if updatable_column:
        if nama_kolom in updatable_column:
            sql = f"""UPDATE {tabel_sql} SET {nama_kolom} = %s WHERE {key} = %s;"""
            params = (nilai, key_value)
            sukses = con.update_data(sql, params)
    elif not_updatable_column:
        if nama_kolom not in not_updatable_column:
            sql = f"""UPDATE {tabel_sql} SET {nama_kolom} = %s WHERE {key} = %s;"""
            params = (nilai, key_value)
            sukses = con.update_data(sql, params)

    if sukses: 
        print(f'Update berhasil: {nama_kolom} dengan nilai {nilai}')
    else:
        print(f"Update gagal untuk {nama_kolom}")
    return sukses


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


def export_to_excel(table_widget: QTableWidget, file_path: str):
    """
    Export data dari QTableWidget ke file Excel
    
    Parameters:
    table_widget (QTableWidget): Tabel widget yang akan diekspor
    file_path (str): Path untuk menyimpan file Excel
    """
    try:
        # Mendapatkan jumlah baris dan kolom
        row_count = table_widget.rowCount()
        col_count = table_widget.columnCount()
        
        # Mendapatkan header
        headers = []
        for col in range(col_count):
            header_item = table_widget.horizontalHeaderItem(col)
            headers.append(header_item.text() if header_item else f"Column {col+1}")
        
        # Mengumpulkan data
        data = []
        for row in range(row_count):
            row_data = []
            for col in range(col_count):
                item = table_widget.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)
        df = pd.DataFrame(data, columns=headers)
        df.to_excel(file_path, index=False)
        return True, f"Data berhasil diekspor ke {file_path}"
    except Exception as e:
        return False, f"Error saat mengekspor: {str(e)}"
    

# def update_table_font(table:QTableWidget):
#     # Perbarui font dan ukuran tabel
#     table.setFont(QFont(table.font_family, table.base_font_size))
#     table.resizeRowsToContents()
#     table.resizeColumnsToContents()