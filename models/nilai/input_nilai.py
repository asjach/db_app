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

    def data_siswa(self, jenjang, tapel, tingkat, kelas, kegiatan):
        sql = """
            SELECT      id_kelas, id_kegiatan, p.no_urut, p.id as id_peserta, p.nis_lokal, nama_lengkap, kelas
            FROM        kegiatan_peserta p
            JOIN   		siswa s on s.nis_lokal = p.nis_lokal
            JOIN        kegiatan_riwayat r on r.id = p.id_kegiatan
            JOIN        kelas_riwayat k ON k.id = p.id_kelas
            WHERE       r.jenjang = %s
                AND		r.tapel = %s
                AND     k.tingkat LIKE %s
                AND		k.kelas LIKE %s
                AND     r.kegiatan = %s
            ORDER BY    k.kelas, cast(p.no_urut as unsigned), nama_lengkap
            """
        params = (jenjang, tapel, f'%{tingkat}%', f'%{kelas}%', kegiatan)
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
        print("Insert data:", data)
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
        print("Update data:", data)
        row_count = self.update_data(sql, data)
        return row_count
    
    def cek_peserta_bulk(self, keys):
        if not keys:
            return {}
        
        placeholders = ",".join(["(%s)" for _ in keys])
        sql = f"""
            SELECT id, id_kelas, id_kegiatan, no_urut, sakit, ijin, alpa, catatan_walas
            FROM kegiatan_peserta
            WHERE id IN ({placeholders})
        """
        params = keys
        results = self.get_data(sql, params)

        existing_dict = {r['id']: {
            'no_urut': r['no_urut'], 'sakit': r['sakit'], 'ijin': r['ijin'],
            'alpa': r['alpa'], 'catatan_walas': r['catatan_walas']
        } for r in results}
        return existing_dict

    def insert_peserta_bulk(self, data):
        if not data:
            return
        
        sql = """
            INSERT INTO kegiatan_peserta (id, id_kelas, id_kegiatan, no_urut, sakit, ijin, alpa, catatan_walas)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        print("Insert data for kegiatan_peserta:", data)
        row_count = self.update_data(sql, data)
        return row_count

    def update_peserta_bulk(self, data):
        if not data:
            return
        
        sql = """
            UPDATE kegiatan_peserta
            SET no_urut = %s, sakit = %s, ijin = %s, alpa = %s, catatan_walas = %s
            WHERE id = %s
        """
        print("Update data for kegiatan_peserta:", data)
        row_count = self.update_data(sql, data)
        return row_count