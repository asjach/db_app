from utils.database import ConnectDB
from utils.fungsi.db_functions import *

class DaftarKelas(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)
    
    
#DAFTAR KELAS
    def get_daftar_kelas(self, jenjang, tapel, tingkat, kelas, search_by, search, order_by):
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)
        sql = f"""
            SELECT      * 
            FROM        daftar_kelas_default
            WHERE       jenjang = %s
                AND     tapel = %s
                AND     tingkat LIKE %s
                AND     kelas LIKE %s
                AND     {search_by} LIKE %s
            ORDER BY    jenjang, tapel, tingkat, kelas, {order_by}
        """
        params = (jenjang, tapel, f"%{tingkat}%", f"%{kelas}%", f"%{search}%")
        return self.get_data(sql, params)
    
    def update_riwayat_siswa(self, id, nama_kolom, nilai):
        sql = f"""
            UPDATE      siswa_riwayat
            SET         {nama_kolom} = %s 
            WHERE       id = %s
            """
        params = (nilai, id)
        return self.update_data(sql, params)
    
    def update_biodata_siswa(self, nama_kolom, nilai, nis_lokal):
        sql =   """ 
            UPDATE      siswa 
            SET         {} = %s 
            WHERE       nis_lokal = %s
            """.format(nama_kolom)
        params = (nilai, nis_lokal)
        return self.update_data(sql, params)