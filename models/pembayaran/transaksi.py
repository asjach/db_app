from utils.database import ConnectDB

class Transaksi(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def siswa_aktif(self, tapel, tingkat, kelas, search_text):
        sql = """
                SELECT DISTINCT sr.nis_lokal, s.nama_lengkap, kelas
                FROM            siswa_riwayat sr
                JOIN            siswa s ON s.nis_lokal = sr.nis_lokal 
                WHERE           sr.tapel = %s
                    AND		    sr.tingkat LIKE %s
                    AND  	    sr.kelas LIKE %s
                    AND 	    sr.status_akhir = 'Aktif'
                    AND		    s.nama_lengkap LIKE %s  
                ORDER BY        sr.kelas, s.nama_lengkap  
        """
        params = (tapel, f'%{tingkat}%', f'%{kelas}%', f'%{search_text}%')
        return self.get_data(sql, params)
    
    def tagihan_siswa(self,  nis_lokal):
        sql = """
            SELECT t.id, t.id_riwayat_biaya, b.nama_biaya, rb.periode, t.nominal_tagihan as nominal, t.status_tagihan
            FROM    tagihan    t
            JOIN    riwayat_biaya rb ON rb.id = t.id_riwayat_biaya
            JOIN    biaya b on b.id = rb.id_biaya
            WHERE   nis_lokal = %s
        """
        params = (nis_lokal,)
        return self.get_data(sql, params)

    def detail_tagihan(self, id_tagihan):
        sql = """
            SELECT t.id, t.nis_lokal, s.nama_lengkap, concat(s.ayah_nama, '/', s.ibu_nama) as orangtua, 
            b.nama_biaya, r.periode, t.nominal_tagihan, t.status_tagihan
            FROM    tagihan t
            JOIN    siswa s ON t.nis_lokal = s.nis_lokal
            JOIN    riwayat_biaya r on t.id_riwayat_biaya = r.id
            JOIN    biaya b on b.id = r.id_biaya

            WHERE   t.id=%s
            """
        params = (id_tagihan,)
        return self.get_one_data(sql, params)
    
    def get_petugas_tu(self):
        sql = """
        SELECT  id_petugas, nama_lengkap
        FROM    petugas_tu p
        JOIN    guru g ON g.id_guru = p.id_petugas
        ORDER BY no_urut;
        """
        return self.get_data(sql)
    
    def bayar_tagihan(self, id_tagihan, tgl_bayar, nominal_bayar, metode_pembayaran, id_petugas=''):
        sql = """
            INSERT INTO pembayaran
                        (id_tagihan, tgl_bayar, nominal_bayar, metode_pembayaran, id_petugas)
            VALUES      (%s, %s, %s, %s, %s)
        """
        params = (id_tagihan, tgl_bayar, nominal_bayar, metode_pembayaran, id_petugas)
        return self.update_data(sql, params)
    

    def get_pembayaran_by_tanggal(self, tgl_awal, tgl_akhir):
        sql = """
            SELECT      p.id, p.tgl_bayar, s.nama_lengkap, p.nominal_bayar, b.nama_biaya, g.nama_lengkap as petugas
            FROM        pembayaran p
            JOIN        tagihan t ON t.id = p.id_tagihan
            JOIN        guru g ON g.id_guru = p.id_petugas
            JOIN        riwayat_biaya rb ON rb.id = t.id_riwayat_biaya
            JOIN        biaya b ON b.id = rb.id_biaya
            JOIN        siswa s ON s.nis_lokal = t.nis_lokal
            WHERE       tgl_bayar BETWEEN '{}' AND '{}'
            ORDER BY    tgl_bayar
        """.format(tgl_awal, tgl_akhir)
        return self.get_data(sql)
    
    def get_pembayaran_by_filter(self, id_riwayat_biaya, nama_siswa, nama_petugas, tgl_awal=None, tgl_akhir=None):
        sql = """
            SELECT      p.id, p.tgl_bayar, s.nama_lengkap, p.nominal_bayar, b.nama_biaya, g.nama_lengkap as petugas
            FROM        pembayaran p
            JOIN        tagihan t ON t.id = p.id_tagihan
            JOIN        riwayat_biaya rb ON rb.id = t.id_riwayat_biaya
            JOIN        biaya b ON b.id = rb.id_biaya
            JOIN        siswa s ON s.nis_lokal = t.nis_lokal
            JOIN        guru g ON g.id_guru = p.id_petugas
            WHERE       t.id_riwayat_biaya = %s
                AND     s.nama_lengkap LIKE %s
                AND     g.nama_lengkap LIKE %s
        """
        params = (id_riwayat_biaya, f'%{nama_siswa}%', f'%{nama_petugas}%')
        if tgl_awal and tgl_akhir:
            sql += " AND tgl_bayar BETWEEN '%s' AND '%s'"
            params += (tgl_awal, tgl_akhir)
        sql += " ORDER BY    tgl_bayar"

        return self.get_data(sql, params)
    
    def get_jenis_biaya(self):
        sql = """
            SELECT      id, nama_biaya
            FROM        biaya
            ORDER BY    no_urut
        """
        return self.get_data(sql)