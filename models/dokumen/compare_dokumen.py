from utils.database import ConnectDB

class ModelCompareDokumen:
    def __init__(self):
        self.sql = ConnectDB()

    def get_daftar_siswa(self, jenjang = None, tapel = None, tingkat = None, kelas = None, search_text=None, opsi=True): 
        if opsi:
            sql = """
                SELECT r.nis_lokal as nomor_induk, nama_lengkap, ayah_nama, ibu_nama, COUNT(d.id) as jml_dok
                FROM        siswa_riwayat r
                JOIN        siswa s ON s.nis_lokal = r.nis_lokal
                LEFT JOIN dokumen d ON d.nomor_induk = s.nis_lokal
                WHERE nama_lengkap LIKE %s
                    AND     jenjang = %s
                    AND     tapel = %s
                    AND     tingkat LIKE %s
                    AND     kelas LIKE %s
                GROUP BY r.nis_lokal, nama_lengkap, ayah_nama, ibu_nama
            """
            params = (f'%{search_text}%',jenjang, tapel, f'%{tingkat}%',f'%{kelas}%',)
        else:
            sql = """
                SELECT nis_lokal as nomor_induk, nama_lengkap, ayah_nama, ibu_nama, COUNT(d.id) as jml_dok
                FROM siswa s
                LEFT JOIN dokumen d ON d.nomor_induk = s.nis_lokal
                WHERE nama_lengkap LIKE %s
                GROUP BY nis_lokal, nama_lengkap, ayah_nama, ibu_nama
                LIMIT 20
            """
            params = (f'%{search_text}%',)
        return self.sql.get_data(sql, params)
    
    def get_daftar_guru(self, search_text):
        sql = """
            SELECT id_guru as nomor_induk, nama_lengkap, COUNT(d.id) as jml_dok
            FROM guru g
            LEFT JOIN dokumen d ON d.nomor_induk = id_guru
            WHERE nama_lengkap LIKE %s
            GROUP BY id_guru, nama_lengkap 
        """
        params = (f'%{search_text}%',)
        return self.sql.get_data(sql, params)
    
    def get_daftar_dokumen(self, nomor_induk):
        sql = """
            SELECT * FROM dokumen
            WHERE nomor_induk = %s
        """
        params = (nomor_induk,)
        return self.sql.get_data(sql, params)