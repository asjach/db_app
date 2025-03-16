from utils.database import ConnectDB
# from utils.fungsi.db_functions import *

class CetakRapor(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_kelas(self, jenjang, tapel):
        sql = """
        SELECT      id, kelas 
        FROM        kelas_riwayat
        WHERE       jenjang = %s AND tapel = %s
        ORDER BY    kelas;
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)

    def get_kegiatan(self, jenjang, tapel):
        sql = """
            SELECT      id, kegiatan
            FROM        kegiatan_riwayat
            WHERE       jenjang = %s AND tapel = %s
            ORDER BY    is_active DESC
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)
    
    def get_siswa_aktif(self, jenjang, tapel, kelas, kegiatan):
        sql = """
            SELECT      kp.id, id_kelas, id_kegiatan, kp.nis_lokal, nama_lengkap, kelas
            FROM        kegiatan_peserta kp
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kegiatan_riwayat kt ON kt.id = kp.id_kegiatan
            JOIN        kelas_riwayat kr ON kr.id = kp.id_kelas
            WHERE       kr.jenjang = %s AND kr.tapel = %s AND kr.kelas = %s AND kegiatan  = %s
            ORDER BY    kelas, nama_lengkap
        """
        params = (jenjang, tapel, kelas, kegiatan)
        return self.get_data(sql, params)

    def get_list_mapel(self, jenjang, tapel, kegiatan, tingkat, kelas):
        sql = """
                SELECT      mapel
                from        mapel_riwayat m
                LEFT JOIN   kegiatan_riwayat r on r.id = m.id_kegiatan
                LEFT JOIN   kelas_riwayat k on k.id = m.id_kelas
                where 	    r.jenjang = %s
                AND		    r.tapel = %s
                AND 	    r.kegiatan = %s
                AND 	    k.tingkat = %s
                AND 	    k.kelas = %s
                ORDER BY    m.no
            """
        params = (jenjang, tapel, kegiatan, tingkat, kelas)
        return self.get_data(sql, params)
    
    def data_rapor(self, id_kelas, id_kegiatan, nis_lokal, limit=True):
        sql = """
            SELECT 		k.id_kelas, k.id_kegiatan, krw.jenjang, krw.tapel, krw.kelas, kr.semester, kr.kegiatan, kr.tgl_titimangsa, 
                        sum(n.nilai) as jml, round(avg(n.nilai), 2) as rt, k.ranking, k.sakit, k.ijin, k.alpa, 
                        k.catatan_walas, 
                        gw.nama_lengkap as walas, d.namafile as ttd_walas, 
                        gm.nama_lengkap as mudir, dm.namafile as ttd_mudir,
                        s.*
            FROM		kegiatan_peserta k 
            JOIN		nilai_angka n on n.id_peserta = k.id
            JOIN		siswa s on s.nis_lokal = k.nis_lokal
            JOIN		kelas_riwayat krw on krw.id = k.id_kelas
            JOIN        jenjang j on j.jenjang = krw.jenjang
            LEFT JOIN	guru gw on gw.id_guru = krw.id_walas
            LEFT JOIN   guru gm on gm.id_guru = j.id_mudir
            JOIN		kegiatan_riwayat kr on kr.id = k.id_kegiatan
            LEFT JOIN	dokumen d on d.nomor_induk = gw.id_guru and d.jenis_dokumen = 'TTD Rapor'
            LEFT JOIN   dokumen dm on dm.nomor_induk = j.id_mudir and dm.jenis_dokumen = 'Tanda Tangan Rapor'
            WHERE		k.id_kelas = %s 
                and 	k.id_kegiatan = %s
                and k.nis_lokal LIKE %s
            GROUP BY	k.nis_lokal, k.id, d.id, mudir, ttd_mudir
            ORDER BY    krw.kelas, s.nama_lengkap
        """
        if limit:
            sql += "LIMIT 1".format(limit)
        params = (id_kelas, id_kegiatan, f'%{nis_lokal}%')
        return self.get_data(sql, params)

    def data_nilai(self, id_kelas, id_kegiatan, nis_lokal):
        sql = """
            SELECT 		k.id_kelas, k.id_kegiatan, nis_lokal, mata_pelajaran, n.mapel, 
                        nilai, g.nama_lengkap as nama_guru
            FROM  		kegiatan_peserta k 
            JOIN		nilai_angka n on n.id_peserta = k.id
            JOIN        mapel m on m.mapel = n.mapel
            JOIN        mapel_riwayat mr 
                ON      mr.id_kelas =k.id_kelas 
                    AND mr.id_kegiatan=k.id_kegiatan 
                    AND mr.mapel = n.mapel
            LEFT JOIN   guru g ON g.id_guru = mr.id_guru
            WHERE 		k.id_kelas = %s   
                AND 	k.id_kegiatan = %s
                AND     k.nis_lokal = %s;
        """
        params = (id_kelas, id_kegiatan, nis_lokal)
        return self.get_data(sql, params)
    
    def get_setting_rapor(self, id_kelas):
        sql = """
            SELECT setting_rapor 
            FROM    kelas_riwayat
            where   id = %s
            """
        params = (id_kelas,)
        return self.get_one_data(sql, params)

    def update_setting_rapor(self, id_kelas, nilai_setting):
        sql = """
            UPDATE kelas_riwayat
            SET setting_rapor = %s
            WHERE id = %s
            """
        params = (nilai_setting, id_kelas)
        return self.update_data(sql, params)
