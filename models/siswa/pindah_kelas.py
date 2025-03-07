from utils.database import ConnectDB
from utils.fungsi.db_functions import *

class PindahKelas(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def list_siswa_pindah_kelas(
            self, jenjang,tapel, tingkat, kelas, 
            order_by, search_by, search_text, kolom=""
            ):
        
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)
        sql = """
            SELECT      tingkat, {}
            FROM        siswa_riwayat r 
            INNER JOIN  siswa s ON s.nis_lokal = r.nis_lokal
            WHERE       jenjang = %s AND tapel = %s AND tingkat LIKE %s AND kelas LIKE %s 
                        AND r.is_active ='Ya' AND status_akhir ='Aktif' AND {} LIKE %s
            ORDER BY    jenjang, tapel, tingkat, kelas, {}
            """.format(kolom, search_by, order_by)
        
        params = (jenjang, tapel, tingkat, kelas, search_text)
        return self.get_data(sql, params)

    def update_kelas_siswa(self, id, kelas):
        sql = f"""
            UPDATE      siswa_riwayat 
            SET         kelas = %s 
            WHERE       id = %s
            """
        params = (kelas, id)
        return self.update_data(sql, params)