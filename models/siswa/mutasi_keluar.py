from utils.database import ConnectDB
from utils.fungsi.db_functions import *

class MutasiKeluar(ConnectDB):
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

    def mutasikan_siswa(self, id, tgl_keluar):
        sql_insert = """
        INSERT INTO     siswa_mutasi_keluar(jenjang, tapel, tingkat, kelas, nis_lokal, tgl_keluar)
        SELECT          r.jenjang, r.tapel, r.tingkat, r.kelas, r.nis_lokal, %s
        FROM            siswa_riwayat r
        WHERE r.id = %s
        """

        params_insert = (tgl_keluar, id)
        sql_update = """
            UPDATE      siswa_riwayat 
            SET         is_active = 'Tidak', status_akhir = 'Keluar' 
            WHERE       id = %s
            """
        params_update = (id,)
        self.connect()
        try:
            self.my_cursor.execute(sql_insert, params=params_insert)
            self.my_cursor.execute(sql_update, params=params_update)
            self.my_connector.commit()
        except Exception as E:
            self.my_connector.rollback()
            print(E)
            return
        finally:
            if self.my_connector:
                self.my_cursor.close()
                self.my_connector.close()

    def batal_keluar(self, jenjang, tapel, nis_lokal, id):
        sql_delete = f"""
            DELETE FROM siswa_mutasi_keluar 
            WHERE       id=%s"""
        params_delete = (id,)

        sql_update = """
            UPDATE      siswa_riwayat 
            SET         is_active='Ya', status_akhir='Aktif' 
            WHERE       jenjang=%s AND tapel=%s AND nis_lokal=%s
            """
        params_update = (jenjang, tapel, nis_lokal)
        self.connect()
        try:
            self.my_cursor.execute(sql_update, params=params_update)
            self.my_cursor.execute(sql_delete, params=params_delete)
            self.my_connector.commit()
        except Exception as E:
            self.my_connector.rollback()
            print(E)
            return
        finally:
            if self.my_connector:
                self.my_cursor.close()
                self.my_connector.close()

    def daftar_siswa_keluar(self, jenjang, tapel, order_by, search_by, search):
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)
        sql = f"""
            SELECT      m.id, m.nis_lokal, s.nama_lengkap, s.jk, kelas, m.alasan, 
                        m.tgl_keluar, m.no_surat, m.tgl_surat, m.jenis_sekolah, 
                        m.nama_sekolah_tujuan, m.npsn_tujuan, m.nss_tujuan, m.alamat_sekolah_tujuan, m.namafile
            FROM        siswa_mutasi_keluar m 
            INNER JOIN  siswa s  ON m.nis_lokal = s.nis_lokal
            WHERE       jenjang = %s AND tapel = %s AND {search_by} LIKE %s
            ORDER BY    jenjang, tapel, {order_by}
            """
        params = (jenjang, tapel, f"%{search}%")
        return self.get_data(sql=sql, params=params)

    def update_detail_keluar_from_tabel(self, id, nama_kolom, update_nilai):
        sql = """
        UPDATE siswa_mutasi_keluar 
        SET {} = %s 
        WHERE id = %s;
        """.format(nama_kolom)
        params = (update_nilai, id)
        return self.update_data(sql, params)