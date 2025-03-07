from utils.database import ConnectDB
from utils.fungsi.general_functions import *

class Kelulusan(ConnectDB):
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

    def siswa_lulus(self, jenjang, tapel, search_by='Nama', search_text='', order_by="Nama"):
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)

        sql = f"""
            SELECT      sl.id, sl.nis_lokal, nama_lengkap, jk, 
                        tgl_lulus, no_peserta, no_ijazah, no_seri, skhun, skhuambn, 
                        melanjutkan, melanjutkan_ke, sl.nama_sekolah, sl.tapel, sl.jenjang
            FROM        siswa_lulusan sl 
            JOIN        siswa s ON sl.nis_lokal = s.nis_lokal
            WHERE       jenjang=%s AND tapel = %s AND {search_by} LIKE %s
            ORDER BY    jenjang, tapel, {order_by};
            """
        params = (jenjang, tapel, f"%{search_text}%")
        result = self.get_data(sql, params)
        return result
    

    def luluskan_siswa(self, jenjang, tapel, tgl_lulus):
        sql_insert = f"""
            INSERT INTO     siswa_lulusan(nis_lokal, jenjang, tapel, tgl_lulus)
            SELECT          nis_lokal, jenjang, tapel, %s
            FROM            siswa_riwayat
            WHERE           jenjang=%s AND tapel=%s AND tingkat = '6' AND status_akhir='Aktif' AND is_active='Ya';
            """
        params_insert = (tgl_lulus, jenjang, tapel)
        sql_update = f"""
            UPDATE          siswa_riwayat 
            SET             status_akhir = 'Lulus'
            WHERE           jenjang=%s AND tapel=%s AND tingkat='6' 
                            AND is_active='Ya' AND status_akhir = 'Aktif';
            """
        params_update = (jenjang, tapel)
        self.connect()
        try:
            self.my_cursor.execute(sql_insert, params_insert)
            self.my_cursor.execute(sql_update, params_update)
            self.my_connector.commit()
        except Exception as E:
            self.my_connector.rollback()
            print(E)
            return
        finally:
            if self.my_connector:
                self.my_cursor.close()
                self.my_connector.close()

    def tidak_luluskan_siswa(self, tapel, tgl_masuk, id):
        next_tapel = tapel_berikutnya(tapel)
        sql_insert = f"""
            INSERT INTO     siswa_riwayat(jenjang, tapel, tingkat, kelas, 
                            nis_lokal, tgl_masuk, status_awal, status_akhir, is_active)
            SELECT          jenjang, %s, tingkat, kelas, nis_lokal, %s, 'Mengulang', 'Aktif', 'Ya'
            FROM            siswa_riwayat
            WHERE           id=%s
            """
        params_insert = (next_tapel, tgl_masuk, id)
        sql_update = f"""UPDATE siswa_riwayat SET status_akhir= 'Tidak Lulus' WHERE id=%s"""
        params_update = (id,)
        self.connect()
        try:
            self.my_cursor.execute(sql_insert, params_insert)
            self.my_cursor.execute(sql_update, params_update)
            self.my_connector.commit()
        except Exception as E:
            self.my_connector.rollback()
            print(E)
            return
        finally:
            if self.my_connector:
                self.my_cursor.close()
                self.my_connector.close()

    def batal_lulus_siswa(self, jenjang, tapel, nis_lokal, id):
        sql_update = f"""
            UPDATE      siswa_riwayat 
            SET         status_akhir = 'Aktif' 
            WHERE       jenjang = %s 
                        AND tapel=%s 
                        AND nis_lokal=%s
            """
        params_update = (jenjang, tapel, nis_lokal)

        sql_delete = f"""
            DELETE FROM siswa_lulusan 
            WHERE       id=%s"""
        params_delete = (id,)

        self.connect()
        try:
            self.my_cursor.execute(sql_update, params_update)
            self.my_cursor.execute(sql_delete, params_delete)
            self.my_connector.commit()
        except Exception as E:
            self.my_connector.rollback()
            print(E)
            return
        finally:
            if self.my_connector:
                self.my_cursor.close()
                self.my_connector.close()

    def batal_lulus_semua(self, jenjang, tapel):
        sql_update = f"""
            UPDATE      siswa_riwayat 
            SET         status_akhir = 'Aktif'
            WHERE       jenjang = %s AND tapel = %s AND tingkat = '6' AND status_akhir = 'Lulus'
            """
        sql_delete = f"""
            DELETE FROM siswa_lulusan
            WHERE       jenjang = %s AND tapel = %s
            """
        params_update = (jenjang, tapel)
        params_delete = (jenjang, tapel)
        self.connect()
        try:
            self.my_cursor.execute(sql_update, params_update)
            self.my_cursor.execute(sql_delete, params_delete)
            self.my_connector.commit()
        except Exception as E:
            self.my_connector.rollback()
            print(E)
            return
        finally:
            if self.my_connector:
                self.my_cursor.close()
                self.my_connector.close()

    def batal_tidak_lulus(self, jenjang, tapel, nis_lokal, id):
        sql_update = f"""
            UPDATE      siswa_riwayat 
            SET         status_akhir = 'Aktif' 
            WHERE       jenjang = %s AND tapel = %s AND nis_lokal = %s
            """
        params_update = (jenjang, tapel, nis_lokal)
        sql_delete = f"""
            DELETE FROM siswa_riwayat 
            WHERE id=%s
        """
        params_delete = (id,)
        self.connect()
        try:
            self.my_cursor.execute(sql_update, params_update)
            self.my_cursor.execute(sql_delete, params_delete)
            self.my_connector.commit()
        except Exception as E:
            self.my_connector.rollback()
            print(E)
            return
        finally:
            if self.my_connector:
                self.my_cursor.close()
                self.my_connector.close()