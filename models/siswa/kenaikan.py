from utils.database import ConnectDB
from utils.fungsi.general_functions import *

class Kenaikan(ConnectDB):
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
    
    def naikkan_siswa(self, jenjang, tapel, tgl_masuk):
        sql_insert = f"""
            INSERT INTO siswa_riwayat(
                        jenjang, tapel, tingkat, kelas, nis_lokal, 
                        tgl_masuk, is_active, status_awal, status_akhir)
            SELECT      jenjang,
                        CONCAT(CAST(SUBSTRING(tapel, 1, 4) AS UNSIGNED) + 1,'-', 
                        CAST(SUBSTRING(tapel, 6, 4) AS UNSIGNED) + 1), CAST(tingkat AS UNSIGNED) + 1,
                        CONCAT(CAST(SUBSTRING(kelas, 1, REGEXP_INSTR(kelas, '[0-9]')) AS UNSIGNED) + 1,
                        SUBSTRING(kelas, REGEXP_INSTR(kelas, '[0-9]') + 1, LENGTH(kelas) - REGEXP_INSTR(kelas, '[0-9]'))),
                        nis_lokal,%s,'Ya','Kenaikan','Aktif'
            FROM        siswa_riwayat
            WHERE       jenjang = %sAND tapel=%sAND tingkat NOT IN ('6', '9', '12')
                        AND is_active='Ya'AND status_akhir='Aktif'
            """
        params_insert = (tgl_masuk, jenjang, tapel)

        sql_update = f"""
            UPDATE      siswa_riwayat
            SET         status_akhir = 'Naik Kelas'
            WHERE       jenjang=%s AND tapel=%s AND tingkat NOT IN ('6', '9', '12') AND is_active='Ya' AND status_akhir = 'Aktif'
            """
        params_update = (jenjang, tapel)
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

    def tidak_naikkan_siswa(self, tgl_masuk, id):
        sql_insert = """
            INSERT INTO siswa_riwayat(
                    jenjang, tapel, tingkat, kelas, nis_lokal, tgl_masuk, is_active, status_awal, status_akhir
                )
            SELECT      jenjang, CONCAT(CAST(SUBSTRING(tapel, 1, 4) AS UNSIGNED) + 1,'-',
                        CAST(SUBSTRING(tapel, 6, 4) AS UNSIGNED) + 1), 
                        tingkat, kelas, nis_lokal, %s, 'Ya', 'Mengulang', 'Aktif'
            FROM        siswa_riwayat
            WHERE       id=%s
            """
        params_insert = (tgl_masuk, id)
        sql_update = """
            UPDATE      siswa_riwayat
            SET         status_akhir = 'Tidak Naik'
            WHERE       id=%s
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

    def batal_naik_siswa(self, id, jenjang, tapel, nis_lokal):
        sql_delete = """
            DELETE FROM siswa_riwayat
            WHERE       id=%s
            """
        params_delete = (id,)

        sql_update = """
            UPDATE      siswa_riwayat
            SET         status_akhir = 'Aktif'
            WHERE       jenjang=%s AND tapel=%s AND nis_lokal=%s
            """
        params_update = (jenjang, tapel, nis_lokal)
        self.connect()
        try:
            self.my_cursor.execute(sql_delete, params=params_delete)
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

    def batal_naik_all(self, jenjang, tapel):
        next_tapel = tapel_berikutnya(tapel)
        sql_delete = """
            DELETE FROM siswa_riwayat
            WHERE jenjang = %s AND tapel = %s AND status_awal = 'Kenaikan';
            """
        sql_update = """
            UPDATE      siswa_riwayat
            SET         status_akhir = 'Aktif'
            WHERE       jenjang = %s AND tapel = %s AND status_akhir = 'Naik Kelas';
            """
        params_delete = (jenjang, next_tapel)
        params_update = (jenjang, tapel)
        self.connect()
        try:
            self.my_cursor.execute(sql_delete, params_delete)
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

    def batal_tidak_naik_siswa(self, jenjang, tapel, id, nis_lokal):
        sql_delete = f""" DELETE FROM siswa_riwayat WHERE id=%s"""
        params_delete = (id,)

        sql_update = f"""
            UPDATE      siswa_riwayat 
            SET         status_akhir = 'Aktif' 
            WHERE       jenjang=%s AND tapel=%s AND nis_lokal=%s;
            """
        params_update = (jenjang, tapel, nis_lokal)
        self.connect()
        try:
            self.my_cursor.execute(sql_delete, params=params_delete)
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