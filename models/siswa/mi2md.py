from utils.database import ConnectDB
from utils.fungsi.db_functions import *

class MI2MD(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def list_siswa_aktif(
        self, jenjang, tapel, tingkat=None, kelas=None, status_awal='', status_akhir='',
        search_by="Nama", search_text="", order_by='Nama'
        ):
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)

        sql = """
            SELECT      id, nis_lokal, nama_lengkap, kelas
            FROM        siswa_aktif
            WHERE       jenjang = %s
                    AND tapel = %s
                    AND tingkat LIKE %s
                    AND kelas LIKE %s
                    AND status_awal LIKE %s
                    AND status_akhir LIKE %s
                    AND {} LIKE %s
            ORDER BY jenjang,tapel, tingkat, kelas, {}

            """.format(search_by, order_by)
        params = (jenjang,tapel,f"%{tingkat}%",f"%{kelas}%",f"%{status_awal}%",f"%{status_akhir}%", f"%{search_text}%")
        return self.get_data(sql, params)
    
    def get_mi_only(
            self, tapel, tingkat, kelas, order_by='Nama', search_by='Nama', search_text =''
        ):
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)
        sql = f"""
            SELECT      r.id, r.nis_lokal, nama_lengkap, kelas
            FROM        siswa_riwayat r
            INNER JOIN  siswa s ON s.nis_lokal = r.nis_lokal
            WHERE       jenjang = 'MI' AND tapel = %s AND tingkat LIKE %s AND kelas LIKE %s 
                        AND {search_by} LIKE %s AND r.is_active = 'Ya' AND r.nis_lokal NOT IN
                            (SELECT     nr.nis_lokal
                            FROM        siswa_riwayat nr
                            WHERE       jenjang='MD' AND tapel = %s)
            ORDER BY    jenjang, tapel, tingkat, kelas, {order_by};
            """

        params = (tapel, f"%{tingkat}%", f"%{kelas}%", f"%{search_text}%", tapel)
        return self.get_data(sql, params)

    def get_siswa_beda_kelas(self, tapel, order_by='Nama', search_by='Nama', search_text=''):
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)
        sql = f"""
            SELECT      
                r1.id, r1.nis_lokal, s.nama_lengkap, 
                r1.kelas AS kelas_MI, r2.kelas AS kelas_MD
            FROM        
                siswa_riwayat r1
            INNER JOIN  
                siswa s ON s.nis_lokal = r1.nis_lokal
            INNER JOIN  
                siswa_riwayat r2 ON r1.nis_lokal = r2.nis_lokal
            WHERE       
                r1.jenjang = 'MI' AND r1.tapel = %s 
                AND r2.jenjang = 'MD' AND r2.tapel = %s
                AND r1.kelas <> r2.kelas
                AND {search_by} LIKE %s
            ORDER BY    
                r1.kelas, {order_by};
            """
        params = (tapel, tapel, f"%{search_text}%")
        return self.get_data(sql, params)

    def update_ke_mi(self, tapel):
        sql = """
            UPDATE      siswa_riwayat rMD
            JOIN        siswa_riwayat rMI
            ON          rMD.nis_lokal = rMI.nis_lokal
            SET         rMD.kelas = rMI.kelas
            WHERE       rMI.jenjang = 'MI' AND rMI.tapel = %s 
                AND     rMD.jenjang = 'MD' AND rMD.tapel = %s;
            """
        params = (tapel, tapel)
        return self.update_data(sql, params)

    def update_ke_md(self, tapel):
        sql = """
            UPDATE      siswa_riwayat rMI
            JOIN        siswa_riwayat rMD ON rMI.nis_lokal = rMD.nis_lokal
            SET         rMI.kelas = rMD.kelas
            WHERE       rMI.jenjang = 'MI' AND rMI.tapel = %s 
                AND     rMD.jenjang = 'MD' AND rMD.tapel = %s;
        """
        params = (tapel, tapel)
        return self.update_data(sql, params)

    def insert_to_md(self, id):
        sql = """
            INSERT INTO     siswa_riwayat (jenjang, tapel, tingkat, kelas, nis_lokal, status_awal, status_akhir, is_active)
            SELECT          "MD", r2.tapel, r2.tingkat, r2.kelas, r2.nis_lokal, r2.status_awal, r2.status_akhir, r2.is_active
            FROM            siswa_riwayat as r2
            WHERE           id = %s;
            """
        params = (id,)
        return self.update_data(sql, params)

    def batal_insert_to_md(self, id):
        sql =   """ DELETE FROM siswa_riwayat
                    WHERE id = %s;
                """
        params = (id,)
        return self.update_data(sql, params)  