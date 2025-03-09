from utils.database import ConnectDB
# from utils.fungsi.general_functions import *

class BiodataSiswa(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def cari_siswa(self, search_by, search_text):
        sql = f"""
            SELECT      nis_lokal, nama_lengkap, ayah_nama, ibu_nama 
            FROM        siswa 
            WHERE       {search_by} LIKE %s 
            LIMIT       20
            """
        params = (f"%{search_text}%",)
        return self.get_data(sql, params)

    def get_detail_siswa(self, nis_lokal):
        sql = "SELECT * FROM siswa WHERE nis_lokal=%s"
        params = (nis_lokal,)
        return self.get_one_data(sql, params)
    
    def get_detail_by_nis(self, nis_lokal):
        sql = "SELECT * FROM siswa WHERE nis_lokal = %s"
        params = (nis_lokal,)
        return self.get_data(sql, params)

    def list_alamat(self):
        sql = """SELECT * FROM daftar_alamat"""
        return self.get_data(sql)

    def list_sekolah(self):
        sql = "SELECT * FROM daftar_sekolah"
        return self.get_data(sql)

    def get_dokumen_path(self, nis_lokal):
        sql = """
            SELECT      namafile, jenis_dokumen 
            FROM        dokumen
            WHERE       nomor_induk = %s;
            """
        params = (nis_lokal,)
        result = self.get_data(sql, params)
        return result

    def update_identitas_siswa(self, **data):
        placeholders = ", ".join(["{} = %s".format(column) for column in data.keys()])
        sql = "UPDATE siswa SET {} WHERE nis_lokal= %s".format(placeholders)
        params = tuple(data.values()) + (data["nis_lokal"],)
        return self.update_data(sql, params)