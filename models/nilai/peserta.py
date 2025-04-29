from utils.database import ConnectDB
# from utils.fungsi.db_functions import *

class Peserta(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_kegiatan(self, jenjang, tapel):
        sql = """
            SELECT      id, kegiatan
            FROM        kegiatan_riwayat
            WHERE       jenjang = %s AND tapel = %s
            ORDER BY    is_active DESC
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)
    
    def get_peserta_kegiatan(self, id_kegiatan, id_kelas):
        sql = """
            SELECT      kp.id, id_kelas, id_kegiatan, kp.no_urut, kp.nis_lokal, kp.no_peserta, nama_lengkap, kelas
            FROM        kegiatan_peserta kp
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kelas_riwayat kr ON kr.id = kp.id_kelas
            WHERE       id_kegiatan = %s
        """
        params = [id_kegiatan]
        if id_kelas not in [None, '']:
            sql += " AND kp.id_kelas = %s "
            params.append(id_kelas)
        sql += """ ORDER BY    kelas, CAST(NULLIF(kp.no_urut, '') AS UNSIGNED), nama_lengkap"""
        return self.get_data(sql, tuple(params), True)
    
    def update_data_peserta(self, key, column_name, value):
        sql = """UPDATE kegiatan_riwayat
                SET {} = %s
                WHERE id = %s
            """.format(column_name)
        params = (value, key)
        return self.update_data(sql, params)
        
    
    def get_kelas_riwayat(self, jenjang, tapel):
        sql = """
            SELECT * FROM kelas_riwayat
            WHERE   jenjang = %s AND tapel = %s
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)

    def generate_peserta(self, jenjang, tapel, id_kelas, kelas, id_kegiatan):
        sql = """
            INSERT INTO     kegiatan_peserta
                            (id_kelas, id_kegiatan, nis_lokal, no_urut)
            SELECT {}, {}, r.nis_lokal, r.no_urut
            FROM siswa_riwayat r
            WHERE           jenjang = %s AND tapel = %s AND kelas = %s AND is_active = 'Ya'
                            AND nis_lokal NOT IN(
                            SELECT  nis_lokal 
                            FROM kegiatan_peserta
                            WHERE   id_kegiatan = %s)
        """.format(id_kelas, id_kegiatan)
        params = (jenjang, tapel, kelas, id_kegiatan)
        return self.update_data(sql, params)

    def clear_peserta(self, id_kegiatan):
        sql = "DELETE FROM kegiatan_peserta WHERE id_kegiatan = %s"
        params = (id_kegiatan,)
        return self.update_data(sql, params)
    

    def generate_no_peserta(self, tapel, kegiatan):
        sql = """
            UPDATE kegiatan_peserta kp
            JOIN kelas_riwayat kr ON kr.id = kp.id_kelas
            JOIN kegiatan_riwayat krw ON krw.id = kp.id_kegiatan
            JOIN siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN (
                SELECT tapel, tingkat, kegiatan, nis_lokal, 
                CONCAT(kegiatan, '-', tapel, '-', tingkat, '-', LPAD(urut, 3, '0')) AS nomor_peserta
                FROM (
                    SELECT  kr.tapel, kr.tingkat, krw.kegiatan, kp.nis_lokal,
                    ROW_NUMBER() OVER (
                    PARTITION BY kr.tapel, krw.kegiatan 
                    ORDER BY kr.kelas, s.nama_lengkap) AS urut
                FROM kegiatan_peserta kp
                JOIN kelas_riwayat kr ON kr.id = kp.id_kelas
                JOIN kegiatan_riwayat krw ON krw.id = kp.id_kegiatan
                JOIN siswa s ON s.nis_lokal = kp.nis_lokal
                GROUP BY kr.tapel, kr.tingkat, kr.kelas, krw.kegiatan, kp.nis_lokal, s.nama_lengkap
                ) AS peserta_unik
            ) n ON n.tapel = kr.tapel AND n.kegiatan = krw.kegiatan AND n.nis_lokal = kp.nis_lokal
            SET kp.no_peserta = n.nomor_peserta
            WHERE kr.tapel = %s
            AND krw.kegiatan = %s;
        """
        params = (tapel, kegiatan)
        return self.update_data(sql, params)