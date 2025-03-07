from utils.database import ConnectDB

class RiwayatMengajar(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)
        
    
    def get_riwayat_mengajar(self, jenjang, tapel):
        sql = """
            SELECT      rm.id, id_kelas, jenjang, tapel, tingkat, kelas, rm.id_guru, nama_lengkap
            FROM        guru_kelas_mengajar rm
            JOIN        guru g ON g.id_guru = rm.id_guru
            JOIN        kelas_riwayat k ON k.id = rm.id_kelas
            WHERE       k.jenjang = %s
                AND     k.tapel = %s
            ORDER BY    k.tingkat, k.kelas, nama_lengkap
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)
    
    def get_guru_aktif(self, jenjang, tapel):
        sql = """
            SELECT      gk.id_guru, nama_lengkap
            FROM        guru_keaktifan gk
            JOIN        guru g ON g.id_guru = gk.id_guru
            WHERE       jenjang = %s AND tapel = %s  AND fungsi_jabatan = 'Guru'
            ORDER BY    nama_lengkap
            """
        params = (jenjang, tapel)
        return self.get_data(sql, params)
    
    def get_kelas_aktif(self, jenjang, tapel):
        sql = """
            SELECT id as id_kelas, kelas
            FROM kelas_riwayat
            WHERE       jenjang = %s AND tapel = %s
            """
        params = (jenjang, tapel)
        return self.get_data(sql, params)
    
    def insert_kelas_guru(self, id_kelas, id_guru):
        sql = """
            INSERT INTO     guru_kelas_mengajar
                            (id_kelas, id_guru)
            VALUES          (%s, %s)
        """
        params = (id_kelas, id_guru)
        return self.update_data(sql, params)