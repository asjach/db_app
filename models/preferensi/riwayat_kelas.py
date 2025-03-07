from utils.database import ConnectDB

class RiwayatKelas(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_jenjang(self):
        sql ="SELECT * FROM jenjang"
        return self.get_data(sql)
    
    def get_tapel(self):
        sql = "SELECT * FROM tapel"
        return self.get_data(sql)
    
    def get_kelas(self, jenjang, tapel):
        sql ="""   
            SELECT      kr.id, jenjang, tapel, tingkat, kelas, id_walas, nama_lengkap, id_ruang, 
                        kertas, orientasi, margin_left, margin_top, margin_right, margin_bottom,
                        tinggi_baris, kolom_nama, kolom_pelajaran, kkm
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
        