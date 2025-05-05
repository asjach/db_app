from utils.database import ConnectDB

class ModelLihatDokumen:
    def __init__(self):
        self.sql = ConnectDB()

    def get_daftar_siswa(self, jenjang, tapel, tingkat, kelas, search_text, order_by:str):
        order = 'jk, nama_lengkap' if order_by.lower() == 'jk' else 'nama_lengkap'
        sql = f"""
            SELECT r.nis_lokal as no_induk, nama_lengkap, jk, kelas
            FROM siswa_riwayat r
            JOIN siswa s ON s.nis_lokal = r.nis_lokal
            WHERE   nama_lengkap LIKE %s
                AND jenjang = %s
                AND tapel = %s
                AND tingkat LIKE %s
                AND kelas LIKE %s
            ORDER BY tingkat, kelas, {order}
        """
        params = (f'%{search_text}%', jenjang, tapel, f'%{tingkat}%', f'%{kelas}%')
        return self.sql.get_data(sql, params)


    def get_daftar_guru(self, search_text, order_by):
        order = 'jk' if order_by == 'JK' else 'nama_lengkap'

        sql = """
            SELECT id_guru as no_induk, nama_lengkap
            FROM guru
            WHERE nama_lengkap LIKE %s
            ORDER BY {}
        """.format(order)
        params = (f'%{search_text}%',)
        return self.sql.get_data(sql, params)
    
    def get_daftar_dokumen(self, no_induk):
        sql = """
            SELECT id, jenis_dokumen, keterangan, sub_folder, namafile
            FROM dokumen
            WHERE nomor_induk = %s
        """
        params = (no_induk,)
        return self.sql.get_data(sql, params)

    def get_daftar_dok_madrasah(self): ...

