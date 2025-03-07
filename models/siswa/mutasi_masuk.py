from utils.database import ConnectDB
from utils.fungsi.db_functions import *

class MutasiMasuk(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def daftar_calon_siswa(
            self, jenjang, tapel, opsi_kolom, search_by, search='', 
            is_active='', is_accepted='', order_by='Nama'):
        
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)

        sql = """   
            SELECT      {} 
            FROM        siswa_psb
            WHERE       jenjang LIKE %s AND tapel LIKE %s  AND {} LIKE %s 
                        AND is_active LIKE %s AND is_accepted LIKE %s
            ORDER BY    jenjang, tapel, is_active, {}
            """.format(opsi_kolom, search_by, order_by)

        params = (f"%{jenjang}%", f"%{tapel}%", f"%{search}%", f"%{is_active}%", f"%{is_accepted}%")
        return self.get_data(sql, params)

    def calon_belum_diterima(self, jenjang, tapel, search_by, order_by='Nama', search=''):
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)
        sql = """   
            SELECT      id, 
                        concat(mid(tapel,3,2),".", right(tapel,2), ".", lpad(kls_masuk,2,0), ".", 
                        lpad(cast(no_urut as unsigned),4,'0')) as kandidat_nis, 
                        nama_lengkap, is_accepted 
            FROM        siswa_psb
            WHERE       jenjang = %s AND tapel = %s AND {} LIKE %s AND is_active = 'Ya'
            ORDER BY    is_active DESC, {};
            """.format(search_by, order_by)
        params = (jenjang, tapel, f"%{search}%")
        return self.get_data(sql=sql, params=params)

    def calon_diterima(self, jenjang, tapel, search_by, order_by='Nama',  search=''):
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)
        sql = """
            SELECT      id, concat(mid(tapel,3,2),".", right(tapel,2), ".", lpad(kls_masuk,2,0), ".", 
                        lpad(cast(no_urut as unsigned),4,'0')) as kandidat_nis, 
                        nama_lengkap, is_accepted 
            FROM        siswa_psb
            WHERE       jenjang = %s 
                        AND tapel = %s 
                        AND {} LIKE %s 
                        AND is_active = 'Tidak' 
                        AND is_accepted = "Diterima"
            ORDER BY    {};
            """.format(search_by, order_by)

        params = (jenjang, tapel, f"%{search}%")
        return self.get_data(sql=sql, params=params)

    def tambah_pendaftar(self, **data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))

        sql = f""" 
            INSERT INTO siswa_psb ({columns}) 
            VALUES      ({placeholders});
            """

        params = tuple(data.values())
        return self.update_data(sql, params)
    
    def terima_pendaftar(self, jenjang, tapel, tgl_masuk=None):
        sql_insert = f"""
            INSERT INTO siswa(nis_lokal, nama_lengkap, nama_singkat, jk, ayah_nama, ibu_nama, 
                        tgl_masuk, kls_masuk, tapel_masuk, no_urut, pilihan_jenjang)
            SELECT      concat(mid(tapel,3,2),".", right(tapel,2), ".", lpad(kls_masuk,2,0), ".", 
                        lpad(cast(no_urut as unsigned),4,'0')) as kandidat_nis, 
                        nama_lengkap, jk, ayah, ibu, %s, kls_masuk, tapel, no_urut, daftar_ke
            FROM        siswa_psb
            WHERE       jenjang = %s AND tapel = %s AND is_active = 'Ya';
            """

        sql_insert_ke_riwayat = """
            INSERT INTO siswa_riwayat (jenjang, tapel, tingkat, kelas, 
                        nis_lokal, tgl_masuk, status_awal, status_akhir, is_active)
            SELECT      %s, %s, kls_masuk, concat(kls_masuk, "A"), concat(mid(tapel,3,2),".", right(tapel,2), ".", 
                        lpad(kls_masuk,2,0), ".", lpad(cast(no_urut as unsigned),4,'0')) as kandidat_nis, %s, 
                        (CASE WHEN kls_masuk = "1" THEN "Siswa Baru" ELSE "Pindahan" END) as status_awal, 
                        'Aktif', 'Ya'
            FROM        siswa_psb
            WHERE       jenjang = %s AND tapel = %s AND is_active = 'Ya';
            """

        sql_update = """
            UPDATE      siswa_psb 
            SET         is_active = "Tidak", is_accepted = "Diterima"
            WHERE       jenjang = %s AND tapel = %s AND is_active = 'Ya';
            """

        params_insert = (tgl_masuk, jenjang, tapel)
        params_insert_ke_riwayat = (jenjang, tapel, tgl_masuk, jenjang, tapel)
        params_update = (jenjang, tapel)
        try:
            self.connect()
            self.my_cursor.execute(sql_insert, params_insert)
            self.my_cursor.execute(sql_insert_ke_riwayat, params_insert_ke_riwayat)
            self.my_cursor.execute(sql_update, params_update)
            self.my_connector.commit()
            return True
        except Exception as E:
            print(E)
            self.my_connector.rollback()
            return False
        finally:
            if self.my_connector:
                self.my_connector.close()
            if self.my_cursor:
                self.my_cursor.close()

    def batal_terima_pendaftar(self, id, kandidat_nis):
        sql_update = """
            UPDATE      siswa_psb 
            SET         is_active = 'Ya', is_accepted = '' 
            WHERE       id = %s;
            """
        sql_delete_from_riwayat_belajar = """
            DELETE FROM siswa_riwayat 
            WHERE       nis_lokal = %s;
            """
        sql_delete_from_siswa = "DELETE FROM siswa WHERE nis_lokal = %s"
        params_update = (id,)
        params_delete_riwayat = (kandidat_nis,)
        params_delete_siswa = (kandidat_nis,)
        try:
            self.connect()
            self.my_cursor.execute(sql_update, params_update)
            self.my_connector.commit()
            self.my_cursor.execute(sql_delete_from_riwayat_belajar, params_delete_riwayat)
            self.my_connector.commit()
            self.my_cursor.execute(sql_delete_from_siswa, params_delete_siswa)
            self.my_connector.commit()
            return True
        except Exception as E:
            self.my_connector.rollback()
            return False
        finally:
            if self.my_connector:
                self.my_connector.close()
            if self.my_cursor:
                self.my_cursor.close()