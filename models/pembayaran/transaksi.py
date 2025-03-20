from utils.database import ConnectDB

class Transaksi(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def siswa_aktif(self, tapel, tingkat, kelas, search_text):
        sql = """
                SELECT 	sr.nis_lokal, s.nama_lengkap, kelas
                FROM        siswa_riwayat sr
                JOIN        siswa s ON s.nis_lokal = sr.nis_lokal 
                WHERE       sr.tapel = %s
                    AND		sr.tingkat LIKE %s
                    AND  	sr.kelas LIKE %s
                    AND 	sr.status_akhir = 'Aktif'
                    AND		s.nama_lengkap LIKE %s;  
                ORDER BY    s.nama_lengkap  
        """
        params = (tapel, f'%{tingkat}%', f'%{kelas}%', f'%{search_text}%')
        return self.get_data(sql, params)
    
    def tagihan_siswa(self,  nis_lokal):
        sql = """
            SELECT *
            FROM   tagihan    
            WHERE   nis_lokal = %s
        """
        params = (nis_lokal,)
        return self.get_data(sql, params)

    def detail_tagihan(self, id_tagihan):
        sql = """
            SELECT t.id, t.nis_lokal, s.nama_lengkap, concat(s.ayah_nama, '/', s.ibu_nama) as orangtua, 
            b.nama_biaya, r.periode, t.nominal_tagihan, t.status_tagihan
            FROM    tagihan t
            JOIN    siswa s ON t.nis_lokal = s.nis_lokal
            JOIN    riwayat_biaya r on t.id_riwayat_biaya = r.id
            JOIN    biaya b on b.id = r.id_biaya

            WHERE   t.id=%s
            """
        params = (id_tagihan,)
        return self.get_one_data(sql, params)
