from utils.database import ConnectDB

class ModelDokumen:
    def __init__(self):
        self.sql = ConnectDB()

    def get_data_siswa_aktif(self, jenjang, tapel, tingkat, kelas, search_text):
        sql = """SELECT r.nis_lokal, nama_lengkap, nisn
                FROM 
                    siswa_riwayat r
                INNER JOIN siswa s ON s.nis_lokal = r.nis_lokal
                WHERE 
                    jenjang = %s
                    AND tapel LIKE %s
                    AND tingkat LIKE %s
                    AND kelas LIKE %s
                    AND nama_lengkap LIKE %s
                ORDER BY jenjang, tapel, tingkat, kelas, nama_lengkap, jk
                """
        params = (jenjang, f"%{tapel}%", f"%{tingkat}%", f"%{kelas}%", f"%{search_text}%")
        return self.sql.get_data(sql, params)
    
    def get_data_siswa(self, search_text):
        sql = """SELECT nis_lokal, nama_lengkap, jk
                FROM siswa
                WHERE nama_lengkap LIKE %s
                ORDER BY nama_lengkap
                LIMIT 20
                """
        params = (f"%{search_text}%",)
        return self.sql.get_data(sql, params)    
    def get_data_guru(self, search_text):
        sql = """
                SELECT id_guru, nama_lengkap
                FROM guru
                WHERE nama_lengkap like %s
                ORDER BY is_active DESC, nama_lengkap
            """
        params = (f"%{search_text}%",)
        return self.sql.get_data(sql, params)
    
    def get_dokumen_by_nomor_induk(self, nomor_induk, filter=''):
        sql = """SELECT id, nomor_induk, jenis_dokumen, keterangan, namafile
                FROM dokumen
                WHERE nomor_induk=%s
                AND jenis_dokumen LIKE %s"""
        params = (nomor_induk,f"%{filter}%")
        return self.sql.get_data(sql, params)
    
    def get_detail_dokumen(self, id):
        sql = """
            SELECT id, jenis_dokumen, keterangan, 
            """

    def input_dokumen(self, **data):
        con = ConnectDB()
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        sql = f"""
            INSERT INTO dokumen ({columns})
            VALUES ({placeholders})
            """
        params = tuple(data.values())
        return con.update_data(sql, params)
