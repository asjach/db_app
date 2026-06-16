from utils.database import ConnectDB
# from utils.fungsi.db_functions import *
from utils.fungsi.functions import (
    build_in_clause,
    measure_time,
    tapel_berikutnya,
    validate_sql_identifier,
    validate_sql_order_by,
)

class Model_Siswa(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def list_siswa_aktif(self, jenjang, tapel, tingkat=None, kelas=None, 
                         status_awal='', status_akhir='',
                         search_by="Nama", search_text="", order_by='Nama'):
        order_by = self.opsi_order(order_by)
        order_by = validate_sql_order_by(order_by)
        search_by = self.opsi_search(search_by)
        search_by = validate_sql_identifier(search_by)
        sql = f"""  SELECT      id, nis_lokal, nama_lengkap, kelas FROM siswa_aktif
                    WHERE       jenjang = %s AND tapel = %s AND status_awal LIKE %s AND status_akhir LIKE %s AND {search_by} LIKE %s"""
        params = [jenjang, tapel, f"%{status_awal}%", f"%{status_akhir}%", f"%{search_text}%"]
        if tingkat:
            placeholders, items = build_in_clause(tingkat)
            if placeholders:
                sql += f" AND tingkat IN ({placeholders}) "
                params.extend(items)
        if kelas:
            placeholders, items = build_in_clause(kelas)
            if placeholders:
                sql += f" AND kelas IN ({placeholders}) "
                params.extend(items)
        sql += f" ORDER BY jenjang,tapel, tingkat, kelas, {order_by} "
        return self.get_data(sql, tuple(params))      

# BUKU INDUK
    def get_all_siswa_aktif(self, search_by, search_text, order_by, opsi_kolom, opsi_data):
        search_by = self.opsi_search(search_by)
        order_by = self.opsi_order(order_by)
        opsi = opsi_data.lower()
        if opsi == 'seluruh siswa aktif':
            sql = f"""  SELECT      {opsi_kolom} FROM siswa 
                        WHERE       {search_by} LIKE %s AND status_keaktifan = 'Aktif'
                        ORDER BY    kelas_akhir, {order_by}"""
            params = (f"%{search_text}%",)
        elif opsi == 'siswa mi':
            sql = f"""
                SELECT      {opsi_kolom} FROM siswa
                WHERE       {search_by} LIKE %s 
                            AND status_keaktifan = 'Aktif'
                            AND pilihan_jenjang LIKE '%MI%'
                ORDER BY    kelas_akhir, {order_by}
            """
            params = (f"%{search_text}%",)
        elif opsi == 'siswa md':
            sql = f"""
                SELECT      {opsi_kolom} FROM siswa
                WHERE       {search_by} LIKE %s 
                            AND status_keaktifan = 'Aktif'
                            AND pilihan_jenjang LIKE '%MD%'
                ORDER BY    kelas_akhir, {order_by}
            """
            params = (f"%{search_text}%",)
        elif opsi == 'siswa mi saja':
            sql = f"""
                SELECT      {opsi_kolom} FROM siswa
                WHERE       {search_by} LIKE %s 
                            AND status_keaktifan = 'Aktif'
                            AND pilihan_jenjang = 'MI Saja'
                ORDER BY    kelas_akhir, {order_by}
            """
            params = (f"%{search_text}%",)
        elif opsi == 'siswa md saja':
            sql = f"""
                SELECT      {opsi_kolom} FROM siswa
                WHERE       {search_by} LIKE %s 
                            AND status_keaktifan = 'Aktif'
                            AND pilihan_jenjang = 'MD Saja'
                ORDER BY    kelas_akhir, {order_by}
            """
            params = (f"%{search_text}%",)
        return self.get_data(sql, params)

    def get_all_siswa(self, search_by, search_text, order_by, opsi_kolom):
        search_by = self.opsi_search(search_by)
        order_by = self.opsi_order(order_by)
        sql = f"""  SELECT      {opsi_kolom} FROM siswa 
                    WHERE       {search_by} LIKE %s 
                    ORDER BY    kelas_akhir, {order_by}"""
        return self.get_data(sql, (f"%{search_text}%",))
    
# DAFTAR KELAS
    def get_kolom_siswa(self):
        return self.get_table_columns('siswa')
    
    def get_daftar_kelas(self, jenjang, tapel, tingkat=None,  kelas=None, 
                         search_by=None, search=None, order_by=None, opsi_kolom=None):
        order_by = self.opsi_order(order_by)
        search_by = self.opsi_search(search_by)
        sql = f"""  SELECT  id, {opsi_kolom} FROM siswa_riwayat r
                    JOIN    siswa s ON s.nis_lokal = r.nis_lokal
                    WHERE   jenjang = %s AND tapel = %s AND is_active = 'Ya' """
        params = [jenjang, tapel]
        if kelas:
            placeholders, items = build_in_clause(kelas)
            if placeholders:
                sql += f" AND kelas IN ({placeholders})"
                params.extend(items)
        if tingkat:
            placeholders, items = build_in_clause(tingkat)
            if placeholders:
                sql += f" AND tingkat IN ({placeholders})"
                params.extend(items)
        if search and search_by:
            search_by = validate_sql_identifier(search_by)
            sql += " AND {} LIKE %s ".format(search_by)
            params.append(f'%{search}%')
        order_by = validate_sql_order_by(order_by)
        sql += f" ORDER BY    jenjang, tapel, tingkat, kelas, {order_by}"
        return self.get_data(sql, tuple(params))
    
    def update_riwayat_siswa(self, id, nama_kolom, nilai):
        if nama_kolom == 'no':
            nama_kolom = 'no_urut'
        nama_kolom = validate_sql_identifier(nama_kolom)
        return self.update_data(f"UPDATE siswa_riwayat SET {nama_kolom} = %s WHERE id = %s", (nilai, id))
    
    def update_biodata_siswa(self, nama_kolom, nilai, nis_lokal):
        nama_kolom = validate_sql_identifier(nama_kolom)
        return self.update_data(f"UPDATE siswa SET {nama_kolom} = %s WHERE nis_lokal = %s", (nilai, nis_lokal))

    def update_no_urut(self, id, nilai):
        sql = """UPDATE siswa_riwayat SET no_urut = %s WHERE id = %s"""
        params = (nilai, id)
        return self.update_data(sql, params)

    def update_nis_kemenag(self, nis_lokal, nis_kemenag):
        sql = """
            UPDATE siswa
            SET
                nis_kemenag = %s
            WHERE nis_lokal = %s
        """
        params = (nis_kemenag, nis_lokal)
        return self.update_data(sql, params)
    
## REKAP SISWA
    def rekap_pertapel(self, jenjang):
        return self.get_data(f"SELECT * FROM rekap_siswa_pertahun WHERE jenjang = %s", (jenjang,))

    def rekap_pertingkat(self, jenjang, tapel):
        sql = f"""SELECT * FROM rekap_siswa_pertingkat  WHERE jenjang = %s AND tapel = %s ORDER BY jenjang, tapel, tingkat;"""
        return self.get_data(sql, (jenjang, tapel))

    def rekap_perrombel(self, jenjang, tapel):
        sql = f"""SELECT * FROM rekap_siswa_perrombel WHERE jenjang = %s AND tapel = %s ORDER BY jenjang, tapel, tingkat, kelas;"""
        return self.get_data(sql, (jenjang, tapel))

    def rekap_umur(self, jenjang, tapel):
        sql = f"""SELECT * FROM rekap_siswa_usia WHERE jenjang = %s AND tapel = %s ORDER BY jenjang, tapel, umur;"""
        return self.get_data(sql, (jenjang, tapel))
    
##  PINDAH KELAS
    def list_siswa_pindah_kelas(self, jenjang, tapel, tingkat, kelas, order_by, search_by, search_text=None, kolom=""):
        order_by = self.opsi_order(order_by)
        order_by = validate_sql_order_by(order_by)
        search_by = self.opsi_search(search_by)
        search_by = validate_sql_identifier(search_by)
        params = []
        sql = f"""  SELECT      tingkat, {kolom}
                    FROM        siswa_riwayat r 
                    INNER JOIN  siswa s ON s.nis_lokal = r.nis_lokal
                    WHERE       jenjang = %s AND tapel = %s AND r.is_active ='Ya' AND status_akhir ='Aktif' """
        params.extend([jenjang, tapel])
        if tingkat:
            placeholders, items = build_in_clause(tingkat)
            if placeholders:
                sql += f" AND tingkat IN ({placeholders}) "
                params.extend(items)
        if kelas:
            placeholders, items = build_in_clause(kelas)
            if placeholders:
                sql += f" AND kelas IN ({placeholders}) "
                params.extend(items)
        if search_text and search_by:
            sql += f" AND {search_by} LIKE %s "
            params.append(f'%{search_text}%')
        sql += f" ORDER BY jenjang, tapel, tingkat, kelas, {order_by}"
        return self.get_data(sql, tuple(params))

    def update_kelas_siswa(self, id, kelas):
        return self.update_data(f"UPDATE siswa_riwayat SET kelas = %s WHERE id = %s", (kelas, id))
    
##  MI ke MD   
    def get_mi_only(self, tapel, tingkat=None, kelas=None, order_by='Nama', search_by='Nama', search_text = None):
        order_by = self.opsi_order(order_by)
        order_by = validate_sql_order_by(order_by)
        search_by = self.opsi_search(search_by)
        search_by = validate_sql_identifier(search_by)
        sql = f"""  SELECT      r.id, r.nis_lokal, nama_lengkap, kelas, pilihan_jenjang
                    FROM        siswa_riwayat r
                    INNER JOIN  siswa s ON s.nis_lokal = r.nis_lokal
                    WHERE       jenjang = 'MI' AND tapel = %s AND r.is_active = 'Ya' AND r.nis_lokal NOT IN
                                (SELECT     nr.nis_lokal FROM siswa_riwayat nr WHERE jenjang='MD' AND tapel = %s) """
        params = [tapel, tapel]
        if tingkat:
            placeholders, items = build_in_clause(tingkat)
            if placeholders:
                sql += f" AND tingkat IN ({placeholders}) "
                params.extend(items)
        if kelas:
            placeholders, items = build_in_clause(kelas)
            if placeholders:
                sql += f" AND kelas IN ({placeholders}) "
                params.extend(items)
        if search_text and search_by:
            sql += f" AND {search_by} LIKE %s "
            params.append(f"%{search_text}%")
        sql += f" ORDER BY jenjang, tapel, tingkat, kelas, {order_by} "
        return self.get_data(sql, tuple(params))

    def get_siswa_beda_kelas(self, tapel, order_by='Nama', search_by='Nama', search_text=''):
        order_by = self.opsi_order(order_by)
        search_by = self.opsi_search(search_by)
        sql = f"""
            SELECT          r1.id, r1.nis_lokal, s.nama_lengkap, 
                            r1.kelas AS kelas_MI, r2.kelas AS kelas_MD
            FROM            siswa_riwayat r1
            INNER JOIN      siswa s ON s.nis_lokal = r1.nis_lokal
            INNER JOIN      siswa_riwayat r2 ON r1.nis_lokal = r2.nis_lokal
            WHERE           r1.jenjang = 'MI' AND r1.tapel = %s 
                    AND     r2.jenjang = 'MD' AND r2.tapel = %s
                    AND     r1.kelas <> r2.kelas
                    AND     {search_by} LIKE %s
            ORDER BY        r1.kelas, {order_by};"""
        params = (tapel, tapel, f"%{search_text}%")
        return self.get_data(sql, params)

    def update_ke_mi(self, tapel):
        sql = """   UPDATE      siswa_riwayat rMD
                    JOIN        siswa_riwayat rMI
                    ON          rMD.nis_lokal = rMI.nis_lokal
                    SET         rMD.kelas = rMI.kelas
                    WHERE       rMI.jenjang = 'MI' AND rMI.tapel = %s 
                        AND     rMD.jenjang = 'MD' AND rMD.tapel = %s;"""
        return self.update_data(sql, (tapel, tapel))

    def update_ke_md(self, tapel):
        sql = """   UPDATE      siswa_riwayat rMI
                    JOIN        siswa_riwayat rMD ON rMI.nis_lokal = rMD.nis_lokal
                    SET         rMI.kelas = rMD.kelas
                    WHERE       rMI.jenjang = 'MI' AND rMI.tapel = %s 
                        AND     rMD.jenjang = 'MD' AND rMD.tapel = %s;"""
        return self.update_data(sql, (tapel, tapel))

    def insert_to_md(self, id):
        sql = """   INSERT INTO     siswa_riwayat (jenjang, tapel, tingkat, kelas, nis_lokal, status_awal, status_akhir, is_active)
                    SELECT          "MD", r2.tapel, r2.tingkat, r2.kelas, r2.nis_lokal, r2.status_awal, r2.status_akhir, r2.is_active
                    FROM            siswa_riwayat as r2
                    WHERE           id = %s;"""
        return self.update_data(sql, (id,))

    def batal_insert_to_md(self, id):
        return self.update_data("DELETE FROM siswa_riwayat WHERE id = %s;", (id,))
    
##  MUTASI MASUK
    def daftar_calon_siswa(self, jenjang, tapel, opsi_kolom, search_by, search='', is_active='', order_by='Nama'):
        order_by = self.opsi_order(order_by)
        order_by = validate_sql_order_by(order_by)
        search_by = self.opsi_search(search_by)
        search_by = validate_sql_identifier(search_by)
        sql = """   SELECT {} FROM siswa_psb
                    WHERE       jenjang LIKE %s AND tapel LIKE %s  AND {} LIKE %s AND is_active LIKE %s 
                    ORDER BY    jenjang, tapel, is_active, {}""".format(opsi_kolom, search_by, order_by)
        params = (f"%{jenjang}%", f"%{tapel}%", f"%{search}%", f"%{is_active}%")
        return self.get_data(sql, params)

    def calon_belum_diterima(self, jenjang, tapel, search_by, order_by='Nama', search=''):
        order_by = self.opsi_order(order_by)
        search_by = self.opsi_search(search_by)
        sql = """   SELECT      id, concat(mid(tapel,3,2),".", right(tapel,2), ".", lpad(kls_masuk,2,0), ".", 
                                lpad(cast(no_urut as unsigned),4,'0')) as kandidat_nis, nama_lengkap, is_accepted 
                    FROM        siswa_psb
                    WHERE       jenjang = %s AND tapel = %s AND {} LIKE %s AND is_active = 'Ya'
                    ORDER BY    is_active DESC, {};""".format(search_by, order_by)
        return self.get_data(sql, (jenjang, tapel, f"%{search}%"))

    def calon_diterima(self, jenjang, tapel, search_by, order_by='Nama',  search=''):
        order_by = self.opsi_order(order_by)
        search_by = self.opsi_search(search_by)
        sql = """   SELECT      id, concat(mid(tapel,3,2),".", right(tapel,2), ".", lpad(kls_masuk,2,0), ".", 
                                lpad(cast(no_urut as unsigned),4,'0')) as kandidat_nis, nama_lengkap, is_accepted 
                    FROM        siswa_psb
                    WHERE       jenjang = %s AND tapel = %s AND {} LIKE %s AND is_active = 'Tidak' AND is_accepted = "Diterima"
                    ORDER BY    {};""".format(search_by, order_by)
        return self.get_data(sql, (jenjang, tapel, f"%{search}%"))

    def tambah_pendaftar(self, **data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        sql = f"INSERT INTO siswa_psb ({columns}) VALUES ({placeholders});"
        params = tuple(data.values())
        return self.update_data(sql, params)
    
    def terima_pendaftar(self, jenjang, tapel, tgl_masuk=None):
        sql_insert = f"""
            INSERT INTO siswa(nis_lokal, nama_lengkap, nama_singkat, jk, ayah_nama, ibu_nama, 
                        tgl_masuk, kls_masuk, tapel_masuk, no_urut, pilihan_jenjang)
            SELECT      concat(mid(tapel,3,2),".", right(tapel,2), ".", lpad(kls_masuk,2,0), ".", 
                        lpad(cast(no_urut as unsigned),4,'0')) as kandidat_nis, 
                        nama_lengkap, nama_lengkap, jk, ayah_nama, ibu_nama, %s, kls_masuk, tapel, no_urut, daftar_ke
            FROM        siswa_psb
            WHERE       jenjang = %s AND tapel = %s AND is_active = 'Ya';"""
        sql_insert_ke_riwayat = """
            INSERT INTO siswa_riwayat (jenjang, tapel, tingkat, kelas, 
                        nis_lokal, tgl_masuk, status_awal, status_akhir, is_active)
            SELECT      %s, %s, kls_masuk, concat(kls_masuk, "A"), concat(mid(tapel,3,2),".", right(tapel,2), ".", 
                        lpad(kls_masuk,2,0), ".", lpad(cast(no_urut as unsigned),4,'0')) as kandidat_nis, %s, 
                        (CASE WHEN kls_masuk = "1" THEN "Siswa Baru" ELSE "Pindahan" END) as status_awal, 
                        'Aktif', 'Ya'
            FROM        siswa_psb
            WHERE       jenjang = %s AND tapel = %s AND is_active = 'Ya';"""
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
        sql_update = "UPDATE siswa_psb SET is_active = 'Ya', is_accepted = '' WHERE id = %s;"
        sql_delete_from_riwayat_belajar = "DELETE FROM siswa_riwayat WHERE nis_lokal = %s;"
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
            if self.my_connector:self.my_connector.close()
            if self.my_cursor:self.my_cursor.close()

##  MUTASI KELUAR
    def mutasikan_siswa(self, id, tgl_keluar):
        sql_insert = """
        INSERT INTO     siswa_mutasi_keluar(jenjang, tapel, tingkat, kelas, nis_lokal, tgl_keluar)
        SELECT          r.jenjang, r.tapel, r.tingkat, r.kelas, r.nis_lokal, %s
        FROM            siswa_riwayat r
        WHERE r.id = %s"""
        params_insert = (tgl_keluar, id)
        sql_update = """UPDATE      siswa_riwayat 
                        SET         is_active = 'Tidak', status_akhir = 'Keluar' 
                        WHERE       id = %s"""
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
        sql_delete = f"DELETE FROM siswa_mutasi_keluar WHERE id=%s"
        sql_update = """UPDATE      siswa_riwayat 
                        SET         is_active='Ya', status_akhir='Aktif' 
                        WHERE       jenjang=%s AND tapel=%s AND nis_lokal=%s"""
        self.connect()
        try:
            self.my_cursor.execute(sql_update, params=(jenjang, tapel, nis_lokal))
            self.my_cursor.execute(sql_delete, params=(id,))
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
        order_by = self.opsi_order(order_by)
        search_by = self.opsi_search(search_by)
        sql = f"""  SELECT      m.id, m.nis_lokal, s.nama_lengkap, s.jk, kelas, m.alasan, 
                                m.tgl_keluar, m.no_surat, m.tgl_surat, m.jenis_sekolah, 
                                m.nama_sekolah_tujuan, m.npsn_tujuan, m.nss_tujuan, m.alamat_sekolah_tujuan, m.namafile
                    FROM        siswa_mutasi_keluar m 
                    INNER JOIN  siswa s  ON m.nis_lokal = s.nis_lokal
                    WHERE       jenjang = %s AND tapel = %s AND {search_by} LIKE %s
                    ORDER BY    jenjang, tapel, {order_by}"""
        return self.get_data(sql=sql, params=(jenjang, tapel, f"%{search}%"))

    def update_detail_keluar_from_tabel(self, id, nama_kolom, update_nilai):
        return self.update_data("UPDATE siswa_mutasi_keluar SET {} = %s WHERE id = %s;".format(nama_kolom), (update_nilai, id))

##  KENAIKAN 
    def naikkan_siswa(self, jenjang, tapel, tgl_masuk):
        sql_insert = f"""   INSERT INTO siswa_riwayat(jenjang, tapel, tingkat, kelas, nis_lokal, tgl_masuk, is_active, status_awal, status_akhir)
                            SELECT      jenjang, CONCAT(CAST(SUBSTRING(tapel, 1, 4) AS UNSIGNED) + 1,'-', 
                                        CAST(SUBSTRING(tapel, 6, 4) AS UNSIGNED) + 1), CAST(tingkat AS UNSIGNED) + 1,
                                        CONCAT(CAST(SUBSTRING(kelas, 1, REGEXP_INSTR(kelas, '[0-9]')) AS UNSIGNED) + 1,
                                        SUBSTRING(kelas, REGEXP_INSTR(kelas, '[0-9]') + 1, LENGTH(kelas) - REGEXP_INSTR(kelas, '[0-9]'))),
                                        nis_lokal,%s,'Ya','Kenaikan','Aktif'
                            FROM        siswa_riwayat
                            WHERE       jenjang = %sAND tapel=%sAND tingkat NOT IN ('6', '9', '12')
                                        AND is_active='Ya'AND status_akhir='Aktif'"""
        sql_update = f"""   UPDATE      siswa_riwayat SET status_akhir = 'Naik Kelas'
                            WHERE       jenjang=%s AND tapel=%s AND tingkat NOT IN ('6', '9', '12') AND is_active='Ya' AND status_akhir = 'Aktif'"""
        self.connect()
        try:
            self.my_cursor.execute(sql_insert, params=(tgl_masuk, jenjang, tapel))
            self.my_cursor.execute(sql_update, params=(jenjang, tapel))
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
        sql_insert = """INSERT INTO siswa_riwayat(jenjang, tapel, tingkat, kelas, nis_lokal, tgl_masuk, is_active, status_awal, status_akhir)
                        SELECT      jenjang, CONCAT(CAST(SUBSTRING(tapel, 1, 4) AS UNSIGNED) + 1,'-',
                                    CAST(SUBSTRING(tapel, 6, 4) AS UNSIGNED) + 1), 
                                    tingkat, kelas, nis_lokal, %s, 'Ya', 'Mengulang', 'Aktif'
                        FROM        siswa_riwayat
                        WHERE       id=%s"""
        sql_update = "UPDATE siswa_riwayat SET status_akhir = 'Tidak Naik' WHERE id=%s"
        self.connect()
        try:
            self.my_cursor.execute(sql_insert, params=(tgl_masuk, id))
            self.my_cursor.execute(sql_update, params=(id,))
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
        sql_update = """UPDATE siswa_riwayat SET status_akhir = 'Aktif' WHERE jenjang=%s AND tapel=%s AND nis_lokal=%s"""
        self.connect()
        try:
            self.my_cursor.execute("DELETE FROM siswa_riwayat WHERE id=%s", (id,))
            self.my_cursor.execute(sql_update, params=(jenjang, tapel, nis_lokal))
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
        sql_delete = """DELETE FROM siswa_riwayat
                        WHERE jenjang = %s AND tapel = %s AND status_awal = 'Kenaikan';"""
        sql_update = """UPDATE      siswa_riwayat
                        SET         status_akhir = 'Aktif'
                        WHERE       jenjang = %s AND tapel = %s AND status_akhir = 'Naik Kelas';"""
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

        sql_update = f"""   UPDATE      siswa_riwayat 
                            SET         status_akhir = 'Aktif' 
                            WHERE       jenjang=%s AND tapel=%s AND nis_lokal=%s;"""
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

##  KELULUSAN
    def siswa_lulus(self, jenjang, tapel, search_by='Nama', search_text='', order_by="Nama"):
        order_by = self.opsi_order(order_by)
        search_by = self.opsi_search(search_by)
        sql = f"""  SELECT      sl.id, sl.nis_lokal, nama_lengkap, jk, 
                                tgl_lulus, no_peserta, no_ijazah, no_seri, skhun, skhuambn, 
                                melanjutkan, melanjutkan_ke, sl.nama_sekolah, sl.tapel, sl.jenjang
                    FROM        siswa_lulusan sl 
                    JOIN        siswa s ON sl.nis_lokal = s.nis_lokal
                    WHERE       jenjang=%s AND tapel = %s AND {search_by} LIKE %s
                    ORDER BY    jenjang, tapel, {order_by};"""
        params = (jenjang, tapel, f"%{search_text}%")
        result = self.get_data(sql, params)
        return result
    
    def luluskan_siswa(self, jenjang, tapel, tgl_lulus):
        sql_insert = f"""   INSERT INTO siswa_lulusan(nis_lokal, jenjang, tapel, tgl_lulus)
                            SELECT      nis_lokal, jenjang, tapel, %s FROM siswa_riwayat
                            WHERE       jenjang=%s AND tapel=%s AND tingkat = '6' AND status_akhir='Aktif' AND is_active='Ya';"""
        sql_update = f"""   UPDATE      siswa_riwayat SET status_akhir = 'Lulus'
                            WHERE       jenjang=%s AND tapel=%s AND tingkat='6' AND is_active='Ya' AND status_akhir = 'Aktif';"""
        self.connect()
        try:
            self.my_cursor.execute(sql_insert, (tgl_lulus, jenjang, tapel))
            self.my_cursor.execute(sql_update, (jenjang, tapel))
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
        sql_update = f"""   UPDATE      siswa_riwayat SET status_akhir = 'Aktif' 
                            WHERE       jenjang = %s AND tapel=%s AND nis_lokal=%s"""
        params_update = (jenjang, tapel, nis_lokal)
        sql_delete = f"DELETE FROM siswa_lulusan WHERE id=%s"
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
        sql_update = f"""   UPDATE      siswa_riwayat SET status_akhir = 'Aktif'
                            WHERE       jenjang = %s AND tapel = %s AND tingkat = '6' AND status_akhir = 'Lulus'"""
        sql_delete = f"DELETE FROM siswa_lulusan WHERE jenjang = %s AND tapel = %s"
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
        sql_update = f"""UPDATE      siswa_riwayat SET status_akhir = 'Aktif' 
            WHERE       jenjang = %s AND tapel = %s AND nis_lokal = %s"""
        sql_delete = f"DELETE FROM siswa_riwayat WHERE id=%s"
        self.connect()
        try:
            self.my_cursor.execute(sql_update, (jenjang, tapel, nis_lokal))
            self.my_cursor.execute(sql_delete, (id,))
            self.my_connector.commit()
        except Exception as E:
            self.my_connector.rollback()
            print(E)
            return
        finally:
            if self.my_connector:
                self.my_cursor.close()
                self.my_connector.close()

##  CEKLIS EMIS
    def get_siswa_all(self, search_text):
        sql = """   SELECT      nis_lokal, nama_lengkap, kelas_akhir, status_keaktifan FROM siswa
                    WHERE       nama_lengkap LIKE %s
                    AND         pilihan_jenjang IN ('MI-MD', 'MI Saja')
                    ORDER BY    nama_lengkap LIMIT 100"""
        return self.get_data(sql, (f'%{search_text}%',))
    
    def get_siswa_tidak(self, kelas, search_text):
        sql = """   SELECT      nis_lokal, nama_lengkap, kelas_akhir, status_keaktifan as status, status_emis as emis, nik, nama_sekolah_asal FROM siswa
                    WHERE       nama_lengkap LIKE %s AND status_emis = 'Tidak' AND pilihan_jenjang IN ('MI-MD', 'MI Saja') """
        if kelas:
            sql += " AND kelas_akhir LIKE '%{}%' ".format(kelas)
        sql += " ORDER BY kelas_akhir, nama_lengkap"
        return self.get_data(sql, (f'%{search_text}%',))
    
    def get_siswa_ya(self, kelas, search_text):
        sql = """   SELECT  nis_lokal, nama_lengkap, kelas_akhir, status_keaktifan as status, status_emis as emis FROM siswa 
                    WHERE   nama_lengkap LIKE %s AND status_emis = 'Ya' AND pilihan_jenjang IN ('MI-MD', 'MI Saja') """
        if kelas:
            sql += " AND kelas_akhir LIKE '%{}%' ".format(kelas)
        sql += " ORDER BY kelas_akhir, nama_lengkap"       
        return self.get_data(sql, (f'%{search_text}%',))
    
    def set_tidak_all(self):
        return self.update_data("UPDATE siswa SET status_emis = 'Tidak'")
    
    def set_tidak(self, nis_lokal):
        return self.update_data("UPDATE siswa SET status_emis = 'Tidak' WHERE   nis_lokal = %s", (nis_lokal,))
    
    def set_ya(self, nis_lokal):
        return self.update_data("UPDATE siswa SET status_emis = 'Ya' WHERE nis_lokal = %s", (nis_lokal,))
    
##  BIODATA SISWA
    def cari_siswa(self, search_by, search_text):
        sql = f"""SELECT nis_lokal, nama_lengkap, ayah_nama, ibu_nama FROM siswa WHERE {search_by} LIKE %s LIMIT 20"""
        return self.get_data(sql, (f"%{search_text}%",))

    def get_detail_siswa(self, nis_lokal):
        return self.get_one_data("SELECT * FROM siswa WHERE nis_lokal=%s", (nis_lokal,))
    
    def get_detail_by_nis(self, nis_lokal):
        return self.get_data("SELECT * FROM siswa WHERE nis_lokal = %s", (nis_lokal,))

    def list_alamat(self):
        return self.get_data("SELECT * FROM daftar_alamat")

    def list_sekolah(self):
        return self.get_data("SELECT * FROM daftar_sekolah")

    def get_dokumen_path(self, nis_lokal):
        sql = "SELECT namafile, jenis_dokumen FROM dokumen WHERE nomor_induk = %s;"
        return self.get_data(sql, (nis_lokal,))

    def update_identitas_siswa(self, **data):
        columns = [validate_sql_identifier(column) for column in data.keys()]
        placeholders = ", ".join([f"{column} = %s" for column in columns])
        sql = f"UPDATE siswa SET {placeholders} WHERE nis_lokal= %s"
        params = tuple(data.values()) + (data["nis_lokal"],)
        return self.update_data(sql, params)
    
    def get_riwayat_belajar(self, nis_lokal):
        sql = "SELECT jenjang, tapel, tingkat, kelas FROM siswa_riwayat WHERE nis_lokal = %s"
        return self.get_data(sql, (nis_lokal,))
    
    def opsi_order(self, opsi_order):
        order_mapping = {
            "Nama": 'nama_lengkap',
            "Nama Lengkap": 'nama_lengkap',
            "JK": 'jk, nama_lengkap',
            "Urutan": 'r.no_urut',
            "No Urut": 'no_urut',
            "Ayah": 'ayah_nama',
            "Ibu": 'ibu_nama',
            "Alamat": 'kampung, nama_lengkap',
            "Pilihan Jenjang": 'pilihan_jenjang, nama_lengkap',
            "Aktif":'is_active, nama_lengkap',
            "Tingkat":'tingkat, nama_lengkap',
            "Tanggal Keluar": 'tgl_keluar',
            "Tanggal Keluar DESC": 'tgl_keluar DESC',
            }
        return order_mapping.get(opsi_order, '')

    def opsi_search(self, opsi_search):
        mapping = {
            "Nama": "nama_lengkap",
            "Nama Lengkap": 'nama_lengkap',
            "Ayah": "ayah_nama",
            "Ibu": "ibu_nama",
            "Alamat": "kampung",
            "NIS": 'nis_lokal',
            "JK": 'jk',
            "Status Awal": 'status_awal',
            "Status Akhir": 'status_akhir',
            "Keaktifan": 'is_active',
            "EMIS": 'status_emis',
            "VervalPD": 'status_vervalpd'
            }
        return mapping.get(opsi_search, '')  
# 900