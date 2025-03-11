from utils.database import ConnectDB
# from utils.fungsi.db_functions import *

class Mapel(ConnectDB):
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
    
    def get_guru_aktif(self, jenjang, params):
        sql = """
            SELECT     gk.id_guru, nama_lengkap
            FROM        guru_keaktifan gk
            JOIN        guru g ON g.id_guru = gk.id_guru
            WHERE       jenjang = %s AND tapel = %s AND fungsi_jabatan = 'Guru'
            ORDER BY    nama_lengkap
        """
        params = (jenjang, params)
        return self.get_data(sql, params)
    
    def get_guru_by_kelas(self, jenjang, tapel, kelas):
        sql = """
            SELECT      km.id_guru, nama_lengkap 
            FROM        guru_kelas_mengajar km
            JOIN        kelas_riwayat kr    ON kr.id = km.id_kelas
            JOIN        guru g              ON g.id_guru = km.id_guru
            WHERE       jenjang = %s AND tapel = %s AND kelas = %s
            ORDER BY    nama_lengkap
        """
        params = (jenjang, tapel, kelas)
        return self.get_data(sql, params)
    
    def get_mapel(self, jenjang, tapel, tingkat, kelas, kegiatan):
        sql = """
            SELECT      mr.id, mr.id_kelas, mr.id_kegiatan, kr.jenjang, kr.tapel, kr.tingkat, kr.kelas, mapel, no, mr.id_guru, nama_lengkap 
            FROM        mapel_riwayat mr
            LEFT JOIN   guru g ON g.id_guru = mr.id_guru
            JOIN        kelas_riwayat kr ON kr.id = mr.id_kelas
            JOIN        kegiatan_riwayat kg ON kg.id = mr.id_kegiatan
            WHERE       kr.jenjang = %s AND kr.tapel = %s AND kr.tingkat LIKE %s 
                AND     kr.kelas LIKE %s AND kegiatan = %s
            ORDER BY    no
        """
        params = (jenjang, tapel, f'%{tingkat}%', f'%{kelas}%', kegiatan)
        return self.get_data(sql, params, True)


    def get_mapel_list(self, jenjang, tapel, kegiatan):
        sql = """
                SELECT k.id, k.kelas, COALESCE(GROUP_CONCAT(m.mapel), '') AS list_mapel, COUNT(m.mapel) as jml_mapel
                FROM kelas_riwayat k
                JOIN (
                    SELECT m.id_kelas, m.mapel
                    FROM mapel_riwayat m
                    INNER JOIN kegiatan_riwayat kr ON m.id_kegiatan = kr.id
                    WHERE kr.kegiatan = %s
                ) m ON k.id = m.id_kelas
                WHERE k.jenjang = %s
                    AND k.tapel = %s
                GROUP BY k.id, k.kelas;
            """
        params = (kegiatan, jenjang, tapel)
        return self.get_data(sql, params)
    
    def insert_by_list_mapel(self, id_kelas, id_kegiatan, mapel):
        sql = """
            INSERT INTO mapel_riwayat (id_kelas, id_kegiatan, mapel)
            SELECT %s, %s, %s
            WHERE NOT EXISTS (
                SELECT 1 
                FROM mapel_riwayat 
                WHERE id_kelas = %s 
                    AND id_kegiatan = %s 
                    AND mapel = %s
            )
        """
        params = (id_kelas, id_kegiatan, mapel, id_kelas, id_kegiatan, mapel)
        try:
            result = self.update_data(sql, params)
            if result is False:
                return False
            elif result == 0:
                print(f"Kombinasi {id_kelas}, {id_kegiatan}, {mapel} sudah ada, dilewati.")
                return "EXISTS"
            return True
        except Exception as e:
            print(f"Error inserting {id_kelas}, {id_kegiatan}, {mapel}: {e}")
            return False
        
    def insert_by_kegiatan_mapel(self, jenjang, tapel, id_kegiatan):
        sql = """
            INSERT INTO mapel_riwayat (id_kelas, id_kegiatan, id_guru, mapel, no)
            SELECT m.id_kelas, %s, m.id_guru, m.mapel, m.no
            FROM mapel_riwayat m
            JOIN kegiatan_riwayat k ON k.id = m.id_kegiatan
            LEFT JOIN mapel_riwayat m2 ON m2.mapel = m.mapel AND m2.id_kegiatan = %s
            JOIN kelas_riwayat kr ON kr.id = m.id_kelas
            WHERE k.kegiatan = 'PAS'
                AND k.jenjang = %s
                AND k.tapel = %s
                AND kr.tingkat NOT IN ('6', '9', '12')
                AND m2.mapel IS NULL
        """
        params = (id_kegiatan, id_kegiatan, jenjang, tapel)
        return self.update_data(sql, params)
    
    def clear_mapel(self, id_kegiatan):
        sql = "DELETE FROM mapel_riwayat WHERE id_kegiatan = %s"
        params = (id_kegiatan,)
        return self.update_data(sql, params)