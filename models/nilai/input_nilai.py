from utils.database import ConnectDB
from utils.fungsi.db_functions import *

class InputNilai(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_id_kegiatan(self, jenjang, tapel):
        sql = """
            SELECT      kegiatan, id
            FROM        kegiatan_riwayat
            WHERE       jenjang = %s
                AND     tapel = %s
            ORDER BY    is_active DESC
            """
        params = (jenjang, tapel)
        return self.get_data(sql, params)

    def data_siswa(self, jenjang, tapel, kegiatan):
        sql = """
            SELECT      id_kelas, id_kegiatan, p.no_urut, p.id as id_peserta, p.nis_lokal, nama_lengkap, kelas
            FROM        kegiatan_peserta p
            JOIN   		siswa s on s.nis_lokal = p.nis_lokal
            JOIN        kegiatan_riwayat r on r.id = p.id_kegiatan
            JOIN        kelas_riwayat k ON k.id = p.id_kelas
            WHERE       r.jenjang = %s
                AND		r.tapel = %s
                AND     r.kegiatan = %s
            ORDER BY    k.kelas, cast(p.no_urut as unsigned), nama_lengkap
            """
        params = (jenjang, tapel, kegiatan)
        return self.get_data(sql, params)
    
    def get_path(self, jenjang, tapel, kegiatan, kolom):
        sql = """
            SELECT      {}
            FROM        kegiatan_riwayat
            WHERE       jenjang = %s
                AND     tapel = %s
                AND     kegiatan = %s
            """.format(kolom)
        params = (jenjang, tapel, kegiatan)
        return self.get_data(sql, params)
    
    def update_path(self, jenjang, tapel, kegiatan, kolom, nilai):
        sql = """
            UPDATE      kegiatan_riwayat
            SET         {} = %s
            WHERE       jenjang = %s
                AND     tapel = %s
                AND     kegiatan = %s    
        """.format(kolom)
        params = (nilai, jenjang, tapel, kegiatan)
        return self.update_data(sql, params)
    
    def all_mapel(self):
        sql = """
            SELECT      mapel
            FROM        mapel
        """
        mapel =  self.get_data(sql)
        to_list = [d['mapel'] for d in mapel]
        return to_list

    def cek_nilai_bulk(self, keys):
        if not keys:
            return {}
        placeholders = ",".join(["(%s, %s)" for _ in keys])
        sql = f"""
            SELECT id, id_peserta, mapel, nilai
            FROM nilai_angka
            WHERE (id_peserta, mapel) IN ({placeholders})
        """
        params = [item for key in keys for item in key]  # Flatten keys
        results = self.get_data(sql, params)
        existing_dict = {(r['id_peserta'], r['mapel']): (r['id'], r['nilai']) for r in results}
        return existing_dict

    def insert_nilai_bulk(self, data):
        if not data:
            return
        
        sql = """
            INSERT INTO nilai_angka (id_peserta, mapel, nilai)
            VALUES (%s, %s, %s)
        """
        row_count = self.update_data(sql, data)
        return row_count

    def update_nilai_bulk(self, data):
        if not data:
            return
        
        sql = """
            UPDATE nilai_angka
            SET nilai = %s
            WHERE id = %s
        """
        row_count = self.update_data(sql, data)
        return row_count
    
    def cek_peserta_bulk(self, keys):
        if not keys:
            return {}
        
        placeholders = ",".join(["(%s)" for _ in keys])
        sql = f"""
            SELECT id, id_kelas, id_kegiatan, no_urut, sakit, ijin, alpa, catatan_walas, ranking, status_naik
            FROM kegiatan_peserta
            WHERE id IN ({placeholders})
        """
        params = keys
        results = self.get_data(sql, params)

        existing_dict = {r['id']: {
            'no_urut': r['no_urut'], 
            'sakit': r['sakit'], 
            'ijin': r['ijin'],
            'alpa': r['alpa'], 
            'catatan_walas': r['catatan_walas'], 
            'ranking': r['ranking'], 
            'status_naik': r['status_naik']
        } for r in results}
        return existing_dict

    def insert_peserta_bulk(self, data):
        if not data:
            return
        
        sql = """
            INSERT INTO kegiatan_peserta (id, id_kelas, id_kegiatan, no_urut, sakit, ijin, alpa, catatan_walas, ranking, status_naik)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        row_count = self.update_data(sql, data)
        return row_count

    def update_peserta_bulk(self, data):
        if not data:
            return
        
        sql = """
            UPDATE kegiatan_peserta
            SET no_urut = %s, sakit = %s, ijin = %s, alpa = %s, catatan_walas = %s, ranking = %s, status_naik = %s
            WHERE id = %s
        """
        row_count = self.update_data(sql, data)
        return row_count
    
    def get_list_mapel(self, jenjang, tapel, kegiatan, tingkat, kelas):
        sql = """
                SELECT      mapel
                from        mapel_riwayat m
                LEFT JOIN   kegiatan_riwayat r on r.id = m.id_kegiatan
                LEFT JOIN   kelas_riwayat k on k.id = m.id_kelas
                where 	    r.jenjang = %s
                AND		    r.tapel = %s
                AND 	    r.kegiatan = %s
                AND 	    k.tingkat LIKE %s
                AND 	    k.kelas LIKE %s
                ORDER BY    m.no
            """
        params = (jenjang, tapel, kegiatan, f'%{tingkat}%', f'%{kelas}%')
        return self.get_data(sql, params)
    

    def get_nilai_by_kegiatan(self, kolom_mapel, jenjang, tapel, tingkat, kelas, kegiatan):
        sql = """
            SELECT      kp.no_urut as `#`, s.nama_lengkap, kelas as kls,
                        {},
                        SUM(n.nilai) as jml,
                        AVG(n.nilai) as rt,
                        kp.ranking as `rank`
            FROM        nilai_angka n
            JOIN        kegiatan_peserta kp ON kp.id = n.id_peserta
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kegiatan_riwayat kr ON kr.id = kp.id_kegiatan
            JOIN        kelas_riwayat k ON k.id = kp.id_kelas
            WHERE       k.jenjang = %s
                AND     k.tapel = %s
                AND     k.tingkat LIKE %s
                AND     k.kelas LIKE %s
                AND     kr.kegiatan = %s
            GROUP BY    kelas, kp.no_urut, s.nama_lengkap, kp.ranking
            ORDER BY    kelas, s.nama_lengkap
            """.format(kolom_mapel)
        params = (jenjang, tapel, f'%{tingkat}%', f'%{kelas}%', kegiatan)
        return self.get_data(sql, params)
    
    def get_catatan_by_kegiatan(self, jenjang, tapel, tingkat, kelas, kegiatan):
        if kegiatan == 'PAT':
            kenaikan = ", kp.status_naik "
        else:
            kenaikan = ""
        sql = """
            SELECT      kp.no_urut as `#`, s.nama_lengkap, kelas as kls,
                        SUM(n.nilai) as jml,
                        AVG(n.nilai) as rt,
                        kp.ranking as `rank`,
                        kp.catatan_walas
                        {}
            FROM        nilai_angka n
            JOIN        kegiatan_peserta kp ON kp.id = n.id_peserta
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kegiatan_riwayat kr ON kr.id = kp.id_kegiatan
            JOIN        kelas_riwayat k ON k.id = kp.id_kelas
            WHERE       k.jenjang = %s
                AND     k.tapel = %s
                AND     k.tingkat LIKE %s
                AND     k.kelas LIKE %s
                AND     kr.kegiatan = %s
            GROUP BY    kelas, kp.no_urut, s.nama_lengkap, kp.ranking, kp.catatan_walas {}
            ORDER BY    kelas, s.nama_lengkap
            """.format(kenaikan, kenaikan)
        
        params = (jenjang, tapel, f'%{tingkat}%', f'%{kelas}%', kegiatan)
        return self.get_data(sql, params)

    
    def get_nilai_catatan_by_kegiatan(self, kolom_mapel, jenjang, tapel, tingkat, kelas, kegiatan):
        if kegiatan == 'PAT':
            kenaikan = ", kp.status_naik "
        else:
            kenaikan = ""
        sql = """
            SELECT      kp.no_urut as `#`, s.nama_lengkap, kelas as kls,
                        {},
                        SUM(n.nilai) as jml,
                        AVG(n.nilai) as rt,
                        kp.ranking as `rank`,
                        kp.catatan_walas
                        {}
            FROM        nilai_angka n
            JOIN        kegiatan_peserta kp ON kp.id = n.id_peserta
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kegiatan_riwayat kr ON kr.id = kp.id_kegiatan
            JOIN        kelas_riwayat k ON k.id = kp.id_kelas
            WHERE       k.jenjang = %s
                AND     k.tapel = %s
                AND     k.tingkat LIKE %s
                AND     k.kelas LIKE %s
                AND     kr.kegiatan = %s
            GROUP BY    kelas, kp.no_urut, s.nama_lengkap, kp.ranking, kp.catatan_walas {}
            ORDER BY    kelas, s.nama_lengkap
            """.format(kolom_mapel, kenaikan, kenaikan)
        params = (jenjang, tapel, f'%{tingkat}%', f'%{kelas}%', kegiatan)
        return self.get_data(sql, params)
    
    def get_kelas(self, jenjang, tapel):
        sql = """
        SELECT      id, kelas 
        FROM        kelas_riwayat
        WHERE       jenjang = %s AND tapel = %s 
        ORDER BY    kelas;
        """
        params = (jenjang, tapel,)
        return self.get_data(sql, params)
