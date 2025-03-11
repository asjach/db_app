from utils.database import ConnectDB
from utils.fungsi.db_functions import *

class RekapNilai(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_kegiatan_riwayat(self, tapel):
        sql = """
            SELECT * FROM kegiatan_riwayat
            WHERE       tapel = %s
            ORDER BY    jenjang DESC, tapel, semester
        """
        params = (tapel,)
        return self.get_data(sql, params)
    
    def get_kelas_riwayat_with_peserta(self, jenjang, tapel, id_kegiatan):
        sql = """
            SELECT      r.id, jenjang, tapel, tingkat, kelas, id_walas, 
                        nama_lengkap, COUNT(kp.id_kelas) AS jml
            FROM        kelas_riwayat r
            LEFT JOIN   guru g ON g.id_guru = r.id_walas
            LEFT JOIN   kegiatan_peserta kp ON kp.id_kelas = r.id AND kp.id_kegiatan = %s
            WHERE       jenjang = %s AND tapel = %s
            GROUP BY    r.id, jenjang, tapel, tingkat, kelas, 
                        id_walas, nama_lengkap
        """
        params = (id_kegiatan, jenjang, tapel, )
        return self.get_data(sql, params)
    
    def get_list_mapel(self, jenjang, tapel, kegiatan, tingkat, kelas):
        sql = """
                SELECT      mapel
                from        mapel_riwayat m
                LEFT JOIN   kegiatan_riwayat r on r.id = m.id_kegiatan
                LEFT JOIN   kelas_riwayat k on k.id = m.id_kelas
                where 	    r.jenjang = %s
                AND		    r.tapel = %s
                AND 	    r.kegiatan = %s
                AND 	    k.tingkat LIKE %s
                AND 	    k.kelas LIKE %s
                ORDER BY    m.no
            """
        params = (jenjang, tapel, kegiatan, f'%{tingkat}%', f'%{kelas}%')
        return self.get_data(sql, params)

    def get_nilai_by_kegiatan(self, kolom_mapel, jenjang, tapel, tingkat, kelas, kegiatan):
        sql = """
            SELECT      kp.no_urut as `#`, s.nama_lengkap, kelas as kls,
                        {},
                        SUM(n.nilai) as jml,
                        AVG(n.nilai) as rt,
                        kp.ranking as `rank`
            FROM        nilai_angka n
            JOIN        kegiatan_peserta kp ON kp.id = n.id_peserta
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kegiatan_riwayat kr ON kr.id = kp.id_kegiatan
            JOIN        kelas_riwayat k ON k.id = kp.id_kelas
            JOIN        guru g ON g.id_guru = k.id_walas
            WHERE       k.jenjang = %s
                AND     k.tapel = %s
                AND     k.tingkat = %s
                AND     k.kelas = %s
                AND     kr.kegiatan = %s
            GROUP BY    kp.no_urut, s.nama_lengkap, kp.ranking
            ORDER BY    s.nama_lengkap
            """.format(kolom_mapel)
        params = (jenjang, tapel, tingkat, kelas, kegiatan)
        return self.get_data(sql, params)
    
    def get_setting_rekap_nilai(self, id):
        sql = """
            SELECT       kertas, orientasi, margin_left, margin_top, margin_right, margin_bottom, tinggi_baris, kolom_nama, kolom_pelajaran, kkm
            FROM        kelas_riwayat
            WHERE       id = %s
        """
        params = (id,)
        return self.get_one_data(sql, params)

    def update_setting_rekap_nilai(self, id, kertas, orientasi, left, top, right, bottom, tinggi_baris, kolom_nama, kolom_pelajaran, kkm):
        sql = """
            UPDATE      kelas_riwayat
            SET         kertas = %s, 
                        orientasi = %s,
                        margin_left = %s,
                        margin_top = %s,
                        margin_right = %s,
                        margin_bottom = %s,
                        tinggi_baris = %s,
                        kolom_nama = %s,
                        kolom_pelajaran = %s,
                        kkm = %s
            WHERE id = %s
            """
        params = (kertas, orientasi, left, top, right, bottom, tinggi_baris, kolom_nama, kolom_pelajaran, kkm, id)
        return self.update_data(sql, params)