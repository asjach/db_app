from utils.database import ConnectDB
# from utils.fungsi.db_functions import *

class CetakRapor(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_kelas(self, jenjang, tapel):
        sql = """
        SELECT      id, kelas 
        FROM        kelas_riwayat
        WHERE       jenjang = %s AND tapel = %s
        ORDER BY    kelas;
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)

    def get_kegiatan(self, jenjang, tapel):
        sql = """
            SELECT      id, kegiatan
            FROM        kegiatan_riwayat
            WHERE       jenjang = %s AND tapel = %s
            ORDER BY    is_active DESC
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)
    
    def get_siswa_aktif(self, jenjang, tapel, kelas, kegiatan):
        sql = """
            SELECT      kp.id, id_kelas, id_kegiatan, kp.nis_lokal, nama_lengkap, kelas
            FROM        kegiatan_peserta kp
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kegiatan_riwayat kt ON kt.id = kp.id_kegiatan
            JOIN        kelas_riwayat kr ON kr.id = kp.id_kelas
            WHERE       kr.jenjang = %s AND kr.tapel = %s AND kr.kelas = %s AND kegiatan  = %s
            ORDER BY    kelas, nama_lengkap
        """
        params = (jenjang, tapel, kelas, kegiatan)
        return self.get_data(sql, params)
    
    def data_rapor(self, jenjang, tapel, kelas, kegiatan, nis_lokal=''):
        sql = """
                SELECT 		kr.jenjang, 
                            kr.tapel, 
                            kr.kelas, 
                            kegiatan, 
                            k.nis_lokal, 
                            nisn, 
                            s.nama_lengkap, 
                            nis_kemenag, 
                            g.nama_lengkap as walas, 
                            ranking

                FROM		kegiatan_peserta k
                JOIN		siswa s ON s.nis_lokal = k.nis_lokal
                JOIN		kelas_riwayat kr on kr.id = k.id_kelas
                JOIN 		guru g ON g.id_guru = kr.id_walas
                JOIN		kegiatan_riwayat krw on krw.id = k.id_kegiatan 
                    and     krw.jenjang=kr.jenjang 
                    and     krw.tapel=kr.tapel
                where 		kr.jenjang = %s
                    and     kr.tapel = %s
                    and     kr.kelas = %s
                    and     kegiatan = %s
                    and     k.nis_lokal LIKE %s
                order by 	cast(ranking as unsigned)
            """
        params = (jenjang, tapel, kelas, kegiatan, f'%{nis_lokal}%')
        return self.get_data(sql, params)