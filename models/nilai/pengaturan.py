from utils.database import ConnectDB
# from utils.fungsi.db_functions import *

class Pengaturan(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    ## RIWAYAT KELAS
    
    # def get_kelas_riwayat_with_peserta(self, jenjang, tapel, id_kegiatan):
    #     sql = """
    #         SELECT      r.id, jenjang, tapel, tingkat, kelas, id_walas, 
    #                     nama_lengkap, COUNT(kp.id_kelas) AS jml
    #         FROM        kelas_riwayat r
    #         LEFT JOIN   guru g ON g.id_guru = r.id_walas
    #         LEFT JOIN   kegiatan_peserta kp ON kp.id_kelas = r.id AND kp.id_kegiatan = %s
    #         WHERE       jenjang = %s AND tapel = %s
    #         GROUP BY    r.id, jenjang, tapel, tingkat, kelas, 
    #                     id_walas, nama_lengkap
    #     """
    #     params = (id_kegiatan, jenjang, tapel, )
    #     return self.get_data(sql, params)
    






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