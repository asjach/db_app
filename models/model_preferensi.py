from utils.database import ConnectDB
# from utils.fungsi.functions import tapel_sebelumnya

class Model_Preferensi(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)
#   SEKOLAH
    def get_daftar_sekolah(self, nama_sekolah):
        sql = """
            SELECT * FROM daftar_sekolah WHERE nama_sekolah LIKE %s
            """
        params = (f'%{nama_sekolah}%',)
        return self.get_data(sql, params, True)
#   RIWAYAT KELAS
    def get_jenjang(self):
        sql ="SELECT * FROM jenjang"
        return self.get_data(sql)
    
    def get_tapel(self):
        sql = "SELECT * FROM tapel"
        return self.get_data(sql)
    
    def get_kelas(self, jenjang, tapel):
        sql ="""   
            SELECT      kr.id, jenjang, tapel, tingkat, kelas, id_walas, nama_lengkap, id_ruang
            FROM        kelas_riwayat kr
            LEFT JOIN   guru g ON g.id_guru = kr.id_walas
            WHERE       jenjang = %s
                AND     tapel LIKE %s
            ORDER BY    kelas
            """
        params = (jenjang, f'%{tapel}%')
        return self.get_data(sql, params, True)
    
    def tambah_kelas(self, jenjang, tapel, tingkat, kelas):
        sql = """
            INSERT  INTO kelas_riwayat
                    (jenjang, tapel, tingkat, kelas)
            SELECT %s, %s, %s, %s
            WHERE NOT EXISTS (  SELECT 1 FROM kelas_riwayat
                                WHERE jenjang = %s AND tapel = %s AND kelas=%s)
            """
        params = (jenjang, tapel, tingkat, kelas, jenjang, tapel, kelas)
        self.update_data(sql, params)

    def daftar_guru(self, jenjang, tapel):
        sql = """
            SELECT      gk.id_guru, nama_lengkap
            FROM        guru_keaktifan gk
            JOIN        guru g ON g.id_guru = gk.id_guru
            WHERE       gk.jenjang = %s
                AND     gk.tapel = %s
                AND     gk.fungsi_jabatan = 'Guru'
            ORDER BY    nama_lengkap
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)
    
    def update_wali_kelas(self, id_kelas, id_walas):
        sql = """
            UPDATE kelas_riwayat  SET id_walas = %s
            WHERE id = %s
            """
        params = (id_walas, id_kelas)
        return self.update_data(sql, params)
    
#   ALAMAT
    def get_alamat(self, kampung):
        sql = "SELECT * FROM daftar_alamat WHERE kampung LIKE %s"
        params = (f'%{kampung}%',)
        return self.get_data(sql, params, True)

#   KEY VALUE
    def get_key_value(self, kunci):
        sql = "SELECT * FROM key_value WHERE kunci LIKE %s"
        params = (f'%{kunci}%',)
        return self.get_data(sql, params, True)


    def get_daftar_kelas(self, tapel, tingkat=None):
        sql = """   SELECT DISTINCT kelas 
                    FROM            kelas_riwayat 
                    WHERE           tapel = %s
            """
        params = [tapel]
        if tingkat:
            sql += " AND tingkat = %s"
            params.append(tingkat)
        sql += " ORDER BY kelas;"
        params = tuple(params)
        return self.get_data(sql, params)
    
    def get_column_names(self, nama_tabel):
        query = f"SHOW COLUMNS FROM `{nama_tabel}`"
        columns = self.get_data(query)
        return [col["Field"] for col in columns]
    
    def get_kolom_export(self, tabel='siswa'):
        sql = f"""   SELECT  id, tabel, nama_data, kolom_kolom, filter_tambahan
                    FROM    kolom_export
                    WHERE   tabel = '{tabel}' """
        return self.get_data(sql)
    
    def save_kolom_export(self, tabel, nama_data, kolom_kolom, filter_tambahan=''):
        sql_cek = """
            SELECT 1 FROM kolom_export WHERE tabel = %s AND nama_data = %s
        """
        cek = self.get_data(sql_cek, (tabel, nama_data))
        params = []
        if cek:
            sql = """   UPDATE kolom_export 
                        SET kolom_kolom = %s, filter_tambahan = %s """
            params.extend([kolom_kolom, filter_tambahan])
            sql += " WHERE tabel = %s AND nama_data = %s "
            params.extend([tabel, nama_data])
        else:
            sql = """
                INSERT INTO kolom_export
                (tabel, nama_data, kolom_kolom, filter_tambahan)
                VALUES (%s, %s, %s, %s)
            """
            params.extend([tabel, nama_data, kolom_kolom, filter_tambahan])
        return self.update_data(sql, tuple(params))
    
    def delete_kolom_export(self, id):
        sql = "DELETE FROM kolom_export WHERE id %s"
        return self.update_data(sql, (int(id),))
    
    def get_data_siswa(self, kolom, jenjang, tapel, tingkat=None, kelas=None, order=None, status=None, filter_tambahan=None):
        sql = """
            SELECT  DISTINCT r.nis_lokal, {}, r.kelas
            FROM    siswa_riwayat r
            JOIN    siswa s ON r.nis_lokal = s.nis_lokal
            WHERE   tapel = %s 
            """.format(kolom)

        params = [tapel]

        if jenjang == 0: #mi, md, mi-md, mi saja, md saja, mi atau md saja
                    sql += ''
        elif jenjang == 1: #siswa yang sekolah MI (pagi)
            sql += " AND jenjang = 'MI' "
        elif jenjang == 2: #siswa yang sekolah MD (siang)
            sql += " AND jenjang = 'MD' "
        elif jenjang == 3: #siswa yang sekolah MI-MD (pagi dan siang)
            sql += """  AND r.nis_lokal IN (
                    SELECT s1.nis_lokal FROM siswa_riwayat s1
                    INNER JOIN siswa_riwayat s2 ON s1.nis_lokal = s2.nis_lokal
                    WHERE s1.jenjang = 'MD' AND s2.jenjang = 'MI'
                    AND s1.tapel = '{}' AND s2.tapel = '{}'
                    AND s1.is_active = 'Ya' AND s2.is_active = 'Ya'
                    )""".format(tapel, tapel)
        elif jenjang == 4: #siswa yang sekolah MI saja (pagi saja)
            sql += """  AND jenjang = 'MI'
                        AND r.nis_lokal NOT IN (
                            SELECT nis_lokal FROM siswa_riwayat 
                            WHERE jenjang = 'MD' AND tapel = '{}')""".format(tapel)
        elif jenjang == 5: #siswa yang sekolah MD saja (siang saja)
            sql += """  AND jenjang = 'MD'
                        AND r.nis_lokal NOT IN (
                            SELECT nis_lokal FROM siswa_riwayat 
                            WHERE jenjang = 'MI' AND is_active='Ya' AND tapel = '{}') """.format(tapel)
        elif jenjang == 6: #siswa yang sekolah MI atau MD Saja (Pagi atau Siang Saja)
            sql += """  AND (
                        (jenjang = 'MI' AND r.nis_lokal NOT IN (
                            SELECT nis_lokal FROM siswa_riwayat
                            WHERE jenjang = 'MD' AND tapel = '{}'
                        )) OR (
                        jenjang = 'MD' AND r.nis_lokal NOT IN (
                            SELECT nis_lokal FROM siswa_riwayat
                            WHERE jenjang = 'MI' AND is_active='Ya' AND tapel = '{}')))""".format(tapel, tapel)
        if tingkat:
            sql += " AND tingkat IN (%s) "
            params.append(tingkat)
        if kelas:
            sql += " AND kelas = %s "
            params.append(kelas)
        if status:
            if status == 'Ya':
                sql += " AND is_active = 'Ya' "
            elif status == 'Tidak':
                sql += " AND is_active = 'Tidak' "
        if filter_tambahan:
            sql += " AND {}".format(filter_tambahan)
        sql += " ORDER BY    kelas"
        if order:
            if order == 'JK':
                order = 'jk'
            elif order == 'Ayah':
                order = 'ayah_nama'
            elif order == 'Ibu':
                order = 'ibu_nama'
            elif order == 'Alamat':
                order = 'kampung'
            else:
                order = 'nama_lengkap'
            sql += " , %s "
            params.append(order)
        params = tuple(params)
        return self.get_data(sql, params)  

    def get_data_guru(self, jenjang=None, tapel=None, fungsi_jabatan=None, kolom=None, order=None, filter_tambahan=None):
        sql = """
            SELECT  k.id_guru, {}
            FROM    guru_keaktifan k
            JOIN    guru g on g.id_guru= k.id_guru
            WHERE   k.is_active = 'Ya'
            AND     tapel = %s
        """.format(kolom)
        if jenjang == 1: 
            sql += " AND jenjang = 'MI' "
        elif jenjang == 2:
            sql += " AND jenjang = 'MD' "
        if fungsi_jabatan == 'Guru':
            sql += " AND fungsi_jabatan = 'Guru' "
        elif fungsi_jabatan == 'Tenaga Kependidikan':
            sql += " AND fungsi_jabatan = 'Tenaga Kependidikan' "
        if filter_tambahan:
            sql += " AND {}".format(filter_tambahan)
        if order:
            if order == 'JK':
                order = 'jk'
            elif order == 'Ayah':
                order = 'ayah_nama'
            elif order == 'Ibu':
                order = 'ibu_nama'
            elif order == 'Alamat':
                order = 'kampung'
            else:
                order = 'nama_lengkap'
            sql += " ORDER BY {}".format(order)
        return self.get_data(sql, (tapel,))     

#   MODEL INPUT EXCEL
    def set_db(self, db_name):
        self.set_database(db_name)

    def get_databases(self):
        databases = self.get_databases()
        return databases

    def get_all_tables(self,):
        query = "SHOW TABLES"
        tables = self.get_data(query)
        return [list(table.values())[0] for table in tables]

    def get_column_names(self, nama_tabel):
        query = f"SHOW COLUMNS FROM `{nama_tabel}`"
        columns = self.get_data(query)
        return [col["Field"] for col in columns]

    def get_table_data(self, nama_tabel):
        query = f"SELECT * FROM `{nama_tabel}`"
        return self.get_data(query)
    
    def data_for_template(self, nama_tabel, join, kolom, kondisi, order_by):
        query = """
        SELECT {} FROM {} {} WHERE {} ORDER BY {}
        """.format(kolom, nama_tabel, join, kondisi, order_by)
        # print(query)
        return self.get_data(query)  
        
        
        