from utils.database import ConnectDB
from utils.fungsi.functions import build_in_clause, validate_sql_identifier, validate_sql_order_by

class Model_Dokumen(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_data_siswa_aktif(self, jenjang, tapel,  tingkat=None, kelas=None, search_text=None):
        sql = """SELECT r.nis_lokal, nama_lengkap, nisn
                FROM 
                    siswa_riwayat r
                INNER JOIN siswa s ON s.nis_lokal = r.nis_lokal
                WHERE 
                    jenjang = %s
                    AND tapel = %s
                """
        params = [jenjang, tapel]
        if tingkat:
            placeholders, items = build_in_clause(tingkat)
            if placeholders:
                sql += f" AND tingkat IN ({placeholders})"
                params.extend(items)
        if kelas:
            sql += " AND kelas = %s "
            params.append(kelas)
        if search_text:
            sql += " AND nama_lengkap LIKE %s"
            params.append(f"%{search_text}%")

        sql += " ORDER BY jenjang, tapel, tingkat, kelas, nama_lengkap, jk "
        params = tuple(params)
        return self.get_data(sql, params)
    
    def get_data_siswa(self, search_text):
        sql = """SELECT nis_lokal, nama_lengkap, jk
                FROM siswa
                WHERE nama_lengkap LIKE %s
                ORDER BY nama_lengkap
                LIMIT 100
                """
        params = (f"%{search_text}%",)
        return self.get_data(sql, params)  

    def get_list_nama(self, target='siswa', search_text=None):
        target = target.lower()
        params = []
        if target == 'siswa':
            sql = f"""SELECT nis_lokal as no_induk, nama_lengkap FROM siswa"""
            if search_text:
                sql += " WHERE   nama_lengkap LIKE %s "
            sql += " ORDER BY nama_lengkap LIMIT 100"
            params.append(f"%{search_text}%")
        elif target == 'guru':
            sql = f"SELECT id_guru as no_induk, nama_lengkap FROM guru"
            if search_text:
                sql += " WHERE   nama_lengkap LIKE %s "
            sql += " ORDER BY nama_lengkap "
            params.append(f"%{search_text}%")
        if search_text:
            params = tuple(params)
            return self.get_data(sql, params)
        else:
            return self.get_data(sql)

    def get_data_guru(self, search_text):
        sql = """
                SELECT id_guru, nama_lengkap
                FROM guru
                WHERE nama_lengkap like %s
                ORDER BY is_active DESC, nama_lengkap
            """
        params = (f"%{search_text}%",)
        return self.get_data(sql, params)
    
    def get_dokumen_by_nomor_induk(self, nomor_induk, filter=''):
        sql = """SELECT id, nomor_induk, jenis_dokumen, keterangan, namafile
                FROM dokumen
                WHERE nomor_induk=%s
                AND jenis_dokumen LIKE %s"""
        params = (nomor_induk,f"%{filter}%")
        return self.get_data(sql, params)

    def input_dokumen(self, **data):
        con = ConnectDB()
        columns = [validate_sql_identifier(key) for key in data.keys()]
        columns = ", ".join(columns)
        placeholders = ", ".join(["%s"] * len(data))
        sql = f"""
            INSERT INTO dokumen ({columns})
            VALUES ({placeholders})
            """
        params = tuple(data.values())
        return con.update_data(sql, params)
    
    def get_daftar_siswa_jml_dok(self, jenjang, tapel, tingkat=None, kelas=None, search_text=None, order_by:str=None, opsi=True):
        order = 'jk, nama_lengkap' if order_by and order_by.lower() == 'jk' else 'nama_lengkap'
        order = validate_sql_order_by(order)
        if opsi:
            sql = f"""
                SELECT r.nis_lokal as nomor_induk, nama_lengkap, jk, kelas, count(d.id) as jml
                FROM siswa_riwayat r
                JOIN siswa s ON s.nis_lokal = r.nis_lokal
                LEFT JOIN dokumen d on d.nomor_induk = s.nis_lokal
                WHERE   jenjang = %s AND tapel = %s """
            params = [jenjang, tapel]
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
            if search_text: 
                sql += " AND nama_lengkap LIKE %s "
                params.append(f"%{search_text}%")
            sql += f"""
                GROUP BY r.nis_lokal, nama_lengkap, jk, kelas
                ORDER BY tingkat, kelas, {order} 
                """
        else:
            sql = f"""
                SELECT nis_lokal as nomor_induk, nama_lengkap, jk, kelas_akhir
                FROM siswa 
                WHERE nama_lengkap LIKE %s
            """
            params = (f"%{search_text}%",)
            sql += " ORDER BY nama_lengkap LIMIT 20"
        return self.get_data(sql, tuple(params))    

    def get_daftar_siswa(self, jenjang, tapel, tingkat=None, kelas=None, search_text=None, order_by:str=None, opsi=True):
        order = 'jk, nama_lengkap' if order_by and order_by.lower() == 'jk' else 'nama_lengkap'
        order = validate_sql_order_by(order)
        if opsi:
            sql = f"""
                SELECT r.nis_lokal as nomor_induk, nama_lengkap, jk, kelas
                FROM siswa_riwayat r
                JOIN siswa s ON s.nis_lokal = r.nis_lokal
                WHERE   jenjang = %s AND tapel = %s """
            params = [jenjang, tapel]
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
            if search_text:
                sql += " AND nama_lengkap LIKE %s "
                params.append(f"%{search_text}%")
            sql += f" ORDER BY tingkat, kelas, {order} "
        else:
            sql = f"""
                SELECT nis_lokal as nomor_induk, nama_lengkap, jk, kelas_akhir
                FROM siswa 
                WHERE nama_lengkap LIKE %s
            """
            params = (f"%{search_text}%",)
            sql += " ORDER BY nama_lengkap LIMIT 20"
        return self.get_data(sql, tuple(params))
    
    def get_daftar_guru(self, search_text, order_by=None):
        order = 'jk, nama_lengkap' if order_by and order_by.lower() == 'jk' else 'nama_lengkap'
        order = validate_sql_order_by(order)
        sql = """
            SELECT id_guru as nomor_induk, nama_lengkap, COUNT(d.id) as jml
            FROM guru g
            LEFT JOIN dokumen d ON d.nomor_induk = id_guru
            WHERE nama_lengkap LIKE %s
            GROUP BY id_guru, nama_lengkap 
            ORDER BY {}
        """.format(order)
        params = (f'%{search_text}%',)
        return self.get_data(sql, params)
    
    def get_daftar_dokumen(self, nomor_induk):
        sql = """
            SELECT * FROM dokumen
            WHERE nomor_induk = %s
        """
        params = (nomor_induk,)
        return self.get_data(sql, params)
    
    def tambah_dokumen(self, no_induk, jenis_dokumen, keterangan, sub_folder, namafile):
        sql = """
            INSERT INTO dokumen (nomor_induk, jenis_dokumen, keterangan, sub_folder, namafile)
            VALUES          (%s, %s, %s, %s, %s)
        """
        params = (no_induk, jenis_dokumen, keterangan, sub_folder, namafile)
        return self.update_data(sql, params)

    def get_daftar_siswa_copy(self, jenjang = None, tapel = None, tingkat = None, kelas = None, search_text=None, opsi=True, jenis_dok=None, keterangan=None): 
        if opsi:
            sql = """
                SELECT r.nis_lokal as nomor_induk, nisn, nama_lengkap, r.kelas, jenis_dokumen, keterangan, namafile
                FROM        siswa_riwayat r
                JOIN        siswa s ON s.nis_lokal = r.nis_lokal
                LEFT JOIN   dokumen d ON d.nomor_induk = s.nis_lokal
                WHERE       jenis_dokumen = %s
                    AND     keterangan = %s
                    AND     jenjang = %s
                    AND     tapel = %s """
            params = [jenis_dok, keterangan, jenjang, tapel]
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
            if search_text:
                sql += " AND nama_lengkap LIKE %s "
                params.append(f"%{search_text}%")
            sql += " ORDER BY nama_lengkap, jk "
            params = tuple(params)
        else:
            sql = """
                SELECT nis_lokal as nomor_induk, nisn, nama_lengkap, jenis_dokumen, keterangan, namafile
                FROM siswa s
                LEFT JOIN dokumen d ON d.nomor_induk = s.nis_lokal
                WHERE jenis_dokumen LIKE %s AND keterangan LIKE %s  """    
            if search_text:
                sql += " AND nama_lengkap LIKE %s "  
                params = (f'%{jenis_dok}%', f'%{keterangan}%', f'%{search_text}%')        
            else:
                params = (f'%{jenis_dok}%', f'%{keterangan}%')
            sql += " LIMIT 20 "
        return self.get_data(sql, params)
    
    def get_daftar_guru_copy(self, search_text):
        sql = """
            SELECT id_guru as nomor_induk, nama_lengkap, jenis_dokumen, keterangan, namafile
            FROM guru g
            LEFT JOIN dokumen d ON d.nomor_induk = id_guru
            WHERE nama_lengkap LIKE %s
                AND     jenis_dokumen LIKE %s
                AND     keterangan LIKE %s
            ORDER BY nama_lengkap 
        """
        params = (f'%{search_text}%', '%', '%')
        return self.get_data(sql, params)

