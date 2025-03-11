from utils.database import ConnectDB
from PySide6.QtWidgets import QMessageBox, QLineEdit, QComboBox, QPlainTextEdit, QLabel, QDoubleSpinBox
from utils.fungsi.functions import text_to_date

def value_from_db(key):
    con = ConnectDB()
    sql = "SELECT nilai FROM key_value WHERE kunci = %s"
    params = (key,)
    data = con.get_one_data(sql, params)
    if data:
        data_string = data["nilai"]
    else:
        data_string = None
    return data_string


def save_value_to_db(key, nilai):
    con = ConnectDB()
    sql_select = """SELECT kunci FROM key_value WHERE kunci=%s"""
    params_select = (key,)
    kunci = con.get_data(sql_select, params_select)
    if len(kunci)> 0 :
        sql = "UPDATE key_value SET nilai = %s WHERE kunci = %s"
    else:
        sql = "INSERT INTO key_value (nilai, kunci) VALUES(%s, %s)"
    params = (nilai, key)
    return con.update_data(sql, params)


def delete_by_id(table_sql, id_name, id_value):
    con = ConnectDB()
    msg = QMessageBox()
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setWindowTitle("Konfirmasi Penghapusan Data")
    msg.setText(f"Pilih \"Ya\" untuk menghapus data terpiilh\nID\t: {id_name} value: {id_value}")
    aksi = msg.exec()
    if aksi == QMessageBox.Ok:
        if id_name == 'id':
            sql = "DELETE FROM {} WHERE {} = {}".format(table_sql, id_name, id_value)
        elif id_name in ['id_guru', 'nis_lokal']:
            sql = "DELETE FROM {} WHERE {} = '{}'".format(table_sql, id_name, id_value)
        return con.update_data(sql)
    else:
        return False
    

def update_from_controls(tabel_sql, key_column, key_value, **data):
    if not data:
        raise ValueError("Tidak ada data untuk diperbarui.")
    con = ConnectDB()
    placeholders = ", ".join([f"{column} = %s" for column in data.keys()])
    sql = f"UPDATE {tabel_sql} SET {placeholders} WHERE {key_column} = %s"
    params = tuple(data.values()) + (key_value,)
    return con.update_data(sql, params)


def list_from_db(key, tipedata="str")->list:
    conn = ConnectDB()
    sql = """SELECT nilai FROM key_value WHERE kunci = %s;"""
    params = (key,)
    data = conn.get_one_data(sql, params)
    if data:
        data_string = data["nilai"]
        data_string = data_string.replace(", ", ",")
        data_string = data_string.replace("--", "")
        data_list = data_string.split(",")
        if tipedata == "str":
            data_list = list(map(str, data_list))
        elif tipedata == "int":
            data_list = list(map(int, data_list))
    else:
        data_list = []
    return data_list


def get_field_list(table_name):
    con = ConnectDB()
    sql = "DESCRIBE {}".format(table_name)
    data = con.get_data(sql)
    fields = [field['Field'] for field in data]
    return fields


def save_to_db(controls, db_data, update_function):
    new_data = extract_data_from_controls(controls)
    is_changed = False
    changed_data = {}  # Menyimpan data yang berubah
    for key, value in new_data.items():
        db_value = db_data.get(key)
        if (db_value is None and value == "") or (db_value == "" and value is None):
            continue
        if db_value != value:
            changed_data[key] = (db_value, value)  # Simpan data lama dan baru
            is_changed = True
    if is_changed:
        success = update_function(**new_data)
        if success:
            return True
        else:
            return False
    else:
        return False
    

def extract_data_from_controls(controls):
    extracted_data = {}
    for control, key in controls:
        if isinstance(control, (QLineEdit, QLabel)):
            value = control.text().strip()  # Ambil teks dan hilangkan spasi
            extracted_data[key] = None if value == "" else value
        elif isinstance(control, QComboBox):
            value = control.currentText().strip()
            extracted_data[key] = None if value == "" else value
        elif isinstance(control, QPlainTextEdit):
            value = control.toPlainText().strip()
            extracted_data[key] = None if value == "" else value
        elif isinstance(control, QDoubleSpinBox):
            value = control.value()
            extracted_data[key] = None if value == "" else value
        

        # Konversi field tanggal jika perlu
        if any(substr in key for substr in ['tgl', 'tanggal', 'tmt']) and extracted_data[key]:
            extracted_data[key] = text_to_date(extracted_data[key])  # Konversi ke date
        
    return extracted_data


def opsi_order(opsi_order):
    order_mapping = {
        "Nama": 'nama_lengkap',
        "JK": 'jk, nama_lengkap',
        "Urutan": 'r.no_urut',
        "No Urut": 'no_urut',
        "Ayah": 'ayah_nama',
        "Ibu": 'ibu_nama',
        "Alamat": 'kampung, nama_lengkap',
        "Pilihan Jenjang": 'pilihan_jenjang, nama_lengkap',
        "Aktif":'is_active, nama_lengkap',
        "Tingkat":'tingkat, nama_lengkap',
        "Tanggal Keluar": 'tgl_keluar',
        "Tanggal Keluar DESC": 'tgl_keluar DESC',
        }
    return order_mapping.get(opsi_order, '')


def opsi_search(opsi_search):
    mapping = {
        "Nama": "nama_lengkap",
        "Ayah": "ayah_nama",
        "Ibu": "ibu_nama",
        "Alamat": "kampung",
        "NIS": 'nis_lokal',
        "JK": 'jk',
        "Status Awal": 'status_awal',
        "Status Akhir": 'status_akhir',
        "Keaktifan": 'is_active'
        }
    return mapping.get(opsi_search, '')