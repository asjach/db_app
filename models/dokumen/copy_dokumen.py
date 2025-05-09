from utils.database import ConnectDB

class ModelCopyDokumen:
    def __init__(self):
        self.sql = ConnectDB()


    def get_daftar_siswa(self, jenjang = None, tapel = None, tingkat = None, kelas = None, search_text=None, opsi=True, jenis_dok=None, keterangan=None): 
        # if jenis_dok:
        #     _jenis_dok = 'jenis_dokumen ='
        # else:
        #     _jenis_dok = 'jenis_dokumen LIKE'
        # if keterangan: 
        #     _keterangan = 'keterangan ='
        # else:
        #     _keterangan = 'keterangan LIKE'
        if opsi:
            sql = """
                SELECT r.nis_lokal as nomor_induk, nisn, nama_lengkap, r.kelas, jenis_dokumen, keterangan, namafile
                FROM        siswa_riwayat r
                JOIN        siswa s ON s.nis_lokal = r.nis_lokal
                LEFT JOIN dokumen d ON d.nomor_induk = s.nis_lokal
                WHERE nama_lengkap LIKE %s
                    AND     jenis_dokumen = %s
                    AND     keterangan = %s
                    AND     jenjang = %s
                    AND     tapel = %s
                    AND     tingkat LIKE %s
                    AND     kelas LIKE %s
                ORDER BY nama_lengkap, jk
            """
            params = (f'%{search_text}%',jenis_dok, keterangan, 
                      jenjang, tapel, f'%{tingkat}%',f'%{kelas}%',)
        else:
            sql = """
                SELECT nis_lokal as nomor_induk, nisn, nama_lengkap, jenis_dokumen, keterangan, namafile
                FROM siswa s
                LEFT JOIN dokumen d ON d.nomor_induk = s.nis_lokal
                WHERE nama_lengkap LIKE %s
                    AND     jenis_dokumen LIKE %s
                    AND     keterangan LIKE %s                
                LIMIT 20
            """
            params = (f'%{search_text}%',)
        return self.sql.get_data(sql, params)
    
    def get_daftar_guru(self, search_text):
        sql = """
            SELECT id_guru as nomor_induk, nama_lengkap, jenis_dokumen, keterangan, namafile
            FROM guru g
            LEFT JOIN dokumen d ON d.nomor_induk = id_guru
            WHERE nama_lengkap LIKE %s
                AND     jenis_dokumen LIKE %s
                AND     keterangan LIKE %s
            ORDER BY nama_lengkap 
        """
        params = (f'%{search_text}%',)
        return self.sql.get_data(sql, params)
