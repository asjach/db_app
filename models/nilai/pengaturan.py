from utils.database import ConnectDB
from utils.fungsi.db_functions import *

class Pengaturan(ConnectDB):
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
    

    ## RIWAYAT KELAS
    def get_kelas_riwayat(self, jenjang, tapel):
        sql = """
            SELECT      r.id, jenjang, tapel, tingkat, kelas
            FROM        kelas_riwayat r
            LEFT JOIN   guru g ON g.id_guru = id_walas
            WHERE       jenjang = %s AND tapel = %s
        """
        params = (jenjang, tapel)
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
    

    ## PESERTA
    def get_peserta_kegiatan(self, id_kegiatan, id_kelas):
        sql = """
            SELECT      kp.id, id_kelas, id_kegiatan, kp.no_urut, kp.nis_lokal, nama_lengkap, kelas
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
        return self.get_data(sql, tuple(params))
    
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



    ## MAPEL
    def get_mapel(self, id_kelas, id_kegiatan):
        sql = """
            SELECT      id, mapel, no, r.id_guru, nama_lengkap 
            FROM        mapel_riwayat r
            LEFT JOIN   guru g ON g.id_guru = r.id_guru
            WHERE       id_kelas = %s AND id_kegiatan = %s
            ORDER BY    no
        """
        params = (id_kelas, id_kegiatan)
        return self.get_data(sql, params)
    
    def get_guru_aktif(self, jenjang, tapel, id_kelas):
        sql = """
            SELECT      km.id_guru, nama_lengkap 
            FROM        guru_kelas_mengajar km
            JOIN        kelas_riwayat kr    ON kr.id = km.id_kelas
            JOIN        guru g              ON g.id_guru = km.id_guru
            WHERE       jenjang = %s 
                    AND tapel = %s 
                    AND km.id_kelas = %s
            ORDER BY    nama_lengkap
        """
        params = (jenjang, tapel, id_kelas)
        return self.get_data(sql, params)

    def get_mapel_list(self, jenjang, tapel, kegiatan):
        sql = """
                SELECT k.kelas, COALESCE(GROUP_CONCAT(m.mapel), '') AS list_mapel
                FROM kelas_riwayat k
                LEFT JOIN (
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
        try:
            result = self.update_data(sql, params)
            return True if result else False  # Asumsi result adalah jumlah baris atau None
        except Exception as e:
            print(f"Error inserting data for kegiatan {id_kegiatan}: {e}")
            return False

    def clear_mapel(self, id_kegiatan):
        sql = "DELETE FROM mapel_riwayat WHERE id_kegiatan = %s"
        params = (id_kegiatan,)
        return self.update_data(sql, params)


    # EKSKUL
    def get_ekskul(self, id_kelas, id_kegiatan):
        sql = """
            SELECT      id, ekskul, e.id_pembimbing, nama_lengkap 
            FROM        ekskul_riwayat e
            LEFT JOIN   guru g ON g.id_guru = e.id_pembimbing
            WHERE       id_kelas = %s AND id_kegiatan = %s
            """
        params = (id_kelas, id_kegiatan)
        return self.get_data(sql, params)
        
    def insert_by_list_ekskul(self, id_kelas, id_kegiatan, ekskul):
        sql = """
            INSERT INTO     ekskul_riwayat
                            (id_kelas, id_kegiatan, ekskul)
            SELECT          %s, %s, %s
            WHERE NOT EXISTS (
                SELECT  1 
                FROM        ekskul_riwayat 
                WHERE       id_kelas = %s 
                    AND id_kegiatan = %s 
                    AND ekskul = %s
            )
        """
        params = (id_kelas, id_kegiatan, ekskul, id_kelas, id_kegiatan, ekskul)
        try:
            result = self.update_data(sql, params)
            if result is False:
                return False
            elif result == 0:
                print(f"Kombinasi {id_kelas}, {id_kegiatan}, {ekskul} sudah ada, dilewati.")
                return "EXISTS"
            return True
        except Exception as e:
            print(f"Error inserting {id_kelas}, {id_kegiatan}, {ekskul}: {e}")
            return False

    def insert_by_kegiatan_ekskul(self, jenjang, tapel, id_kegiatan):
        sql = """
            INSERT INTO     ekskul_riwayat 
                            (id_kelas, id_kegiatan, id_pembimbing, ekskul)
            SELECT          e.id_kelas, %s, e.id_pembimbing, e.ekskul
            FROM            ekskul_riwayat e
            JOIN            kegiatan_riwayat k ON k.id = e.id_kegiatan
            LEFT JOIN       ekskul_riwayat e2 ON e2.ekskul = e.ekskul AND e2.id_kegiatan = %s
            JOIN            kelas_riwayat kr ON kr.id = e.id_kelas
            WHERE k.kegiatan = 'PAS'
                AND k.jenjang = %s
                AND k.tapel = %s
                AND kr.tingkat NOT IN ('6', '9', '12')
                AND e2.ekskul IS NULL
        """
        params = (id_kegiatan, id_kegiatan, jenjang, tapel)
        try:
            result = self.update_data(sql, params)
            return True if result else False  # Asumsi result adalah jumlah baris atau None
        except Exception as e:
            print(f"Error inserting data for kegiatan {id_kegiatan}: {e}")
            return False

    def clear_ekskul(self, id_kegiatan):
        sql = "DELETE FROM ekskul_riwayat WHERE id_kegiatan = %s"
        params = (id_kegiatan,)
        return self.update_data(sql, params)