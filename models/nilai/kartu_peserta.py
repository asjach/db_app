from utils.database import ConnectDB

class KartuPeserta(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_kegiatan(self, jenjang, tapel):
        sql = """
            SELECT      id, kegiatan
            FROM        kegiatan_riwayat
            WHERE       jenjang = %s AND tapel = %s
            ORDER BY    is_active DESC
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)
 
    def get_data_peserta(self, tapel, kegiatan, distintc=False, limit=True, limit_value=4):
        sql = " SELECT "
        if distintc:
            sql += " DISTINCT "
        sql += """
                no_peserta, 
                s.nis_lokal, 
                s.nisn, 
                s.nama_lengkap, 
                kr.kelas, 
                concat(s.tmp_lahir, ", ", DATE_FORMAT(s.tgl_lahir, "%d-%m-%Y")) as ttl,
                d.namafile as foto
            FROM    kegiatan_peserta kp
            JOIN    siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN    kelas_riwayat kr ON kr.id = kp.id_kelas
            JOIN    kegiatan_riwayat krw ON krw.id = kp.id_kegiatan
            LEFT JOIN dokumen d ON d.nomor_induk = kp.nis_lokal AND jenis_dokumen = 'Foto' AND keterangan = 'Pas'
            WHERE   kr.tapel = %s
                AND krw.kegiatan = %s
            ORDER BY kr.kelas, s.nama_lengkap
        """
        if limit:
            sql += f' LIMIT {limit_value}'
        params = (tapel, kegiatan)
        return self.get_data(sql, params)
    
    
    def get_setting(self, id_kegiatan, jenis_setting='setting_kartu'):
        sql = """
            SELECT {}
            FROM kegiatan_riwayat
            WHERE id = %s
            """.format(jenis_setting)
        
        params = (id_kegiatan,)
        return self.get_one_data(sql, params)
    
    def update_setting(self, id_kegiatan, value, jenis_setting='setting_kartu'):
        sql = """
            UPDATE kegiatan_riwayat
            SET {} = %s
            WHERE id = %s
        """.format(jenis_setting)
        params = (value, id_kegiatan)
        return self.update_data(sql, params)