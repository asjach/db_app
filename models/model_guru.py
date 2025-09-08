from utils.database import ConnectDB
from utils.fungsi.functions import tapel_sebelumnya

class Model_Guru(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)
    def opsi_order(self, opsi_order):
        order_mapping = {
            "Nama": 'nama_lengkap',
            "Nama Lengkap": 'nama_lengkap',
            "JK": 'jk, nama_lengkap',
            "Urutan": 'r.no_urut',
            "No Urut": 'no_urut',
            "Alamat": 'kampung, nama_lengkap',
            "Aktif":'is_active, nama_lengkap',
            }
        return order_mapping.get(opsi_order, '')

    def opsi_search(self, opsi_search):
        mapping = {
            "Nama": "nama_lengkap",
            "Nama Lengkap": 'nama_lengkap',
            "Alamat": "kampung",
            "JK": 'jk',
            "Keaktifan": 'is_active',
            }
        return mapping.get(opsi_search, '')  
    
##  BUKU INDUK GURU
    def get_buku_induk_guru(self, order_by='Nama', search_by='Nama', search=''):
        order_by = self.opsi_order(order_by)
        search_by = self.opsi_search(search_by)
        sql = """
            SELECT      * 
            FROM        guru
            WHERE       {} LIKE %s
            ORDER BY    {}
            ;""".format(search_by, order_by)
        params = (f"%{search}%",)
        return self.get_data(sql, params)
    

##  RIWAYAT KEAKTIFAN
    def get_keaktifan_guru(
            self,
            jenjang = '',
            tapel = '',
            kolom = 'default',
            order_by = 'nama_lengkap',
            search_by = 'nama_lengkap',
            search_text = ''
        ):

        order_by = self.opsi_order(order_by)
        search_by = self.opsi_search(search_by)
        
        sql = """
            SELECT      {}
            FROM        guru_keaktifan r
            INNER JOIN  guru g ON g.id_guru = r.id_guru
            WHERE       jenjang LIKE %s AND tapel = %s AND {} LIKE %s
            ORDER BY    {};
            """.format(kolom, search_by, order_by)
        params = (f"%{jenjang}%", tapel, f"%{search_text}%",)
        return self.get_data(sql, params)    
    
    def get_pegawai_aktif(self):
        sql = """
            SELECT id_guru, nama_lengkap
            FROM guru
            WHERE is_active = 'Ya'
            ORDER BY nama_lengkap
        """
        return self.get_data(sql)
    
    def aktifkan_guru(self, id_guru, jenjang, tapel):
        sql = """
            INSERT INTO guru_keaktifan
            (id_guru, jenjang, tapel, is_active)
            VALUES (%s, %s, %s, %s)
        """
        params = (id_guru, jenjang, tapel, 'Ya')
        return self.update_data(sql, params)
    
    def aktivasi_dari_tapel_sebelumnya(self, jenjang, tapel):
        prev_tapel = tapel_sebelumnya(tapel)
        sql = """
        INSERT INTO     guru_keaktifan (id_guru, jenjang, tapel, fungsi_jabatan, is_active)
        SELECT          id_guru, jenjang, %s, fungsi_jabatan, 'Ya'
        FROM            guru_keaktifan
        WHERE           jenjang = %s
            AND         tapel = %s
            AND         is_active = 'Ya'
            AND         id_guru NOT IN (
                SELECT  id_guru
                FROM    guru_keaktifan
                WHERE   jenjang = %s
                AND     tapel = %s
            )
        """
        params = (tapel, jenjang, prev_tapel, jenjang, tapel)
        return self.update_data(sql, params)


##  MODEL RIWAYAT MENGAJAR
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

##  DETAIL GURU
    def get_detail_guru(self, id_guru):
        sql = "SELECT * FROM guru WHERE   id_guru = %s"
        params = (id_guru,)
        return self.get_one_data(sql, params)
    
    def update_identitas_guru(self, **data):
        placeholders = ", ".join(["{} = %s".format(column) for column in data.keys()])
        sql = """
            UPDATE      guru 
            SET         {} 
            WHERE       id_guru= %s
            """.format(placeholders)
        params = tuple(data.values()) + (data["id_guru"],)
        return self.update_data(sql, params)
    
    def get_daftar_guru(self, search_by=None, search_text=None):
        sql = "SELECT * FROM guru WHERE {} LIKE %s".format(search_by)
        params = (f"%{search_text}%",)
        return self.get_data(sql, params)

    def get_keluarga(self, id_guru):
        sql = """
            SELECT      *
            FROM        guru_keluarga
            WHERE       id_guru = %s
            """
        params = (id_guru,)
        return self.get_data(sql, params)
    
    def insert_keluarga(self, **data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        sql = f"""
        INSERT INTO     guru_keluarga ({columns})
        VALUES          ({placeholders});
        """
        params = tuple(data.values())
        return self.update_data(sql, params)
    
    def get_pendidikan_formal(self, id_guru):
        sql = """
            SELECT      *
            FROM        guru_pendidikan
            WHERE       id_guru = %s
            """
        params = (id_guru,)
        return self.get_data(sql, params)
    
    def insert_riwayat_pendidikan(self, **data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        sql = f"""
        INSERT INTO     guru_pendidikan ({columns})
        VALUES          ({placeholders});
        """
        params = tuple(data.values())
        return self.update_data(sql, params)
    

##  ADM GURU
    def get_list_kelas(self, jenjang, tapel):
        sql = """
            SELECT      id, kelas 
            FROM        kelas_riwayat
            WHERE       jenjang = %s AND tapel = %s
            ORDER BY    kelas;
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)
    
    def get_list_guru(self, jenjang, tapel):
        sql = """   
            SELECT g.nama_lengkap, r.id_guru
            FROM guru_keaktifan r
            JOIN guru g ON g.id_guru = r.id_guru
            WHERE jenjang=%s and tapel=%s and r.is_active='Ya' and fungsi_jabatan='Guru'
            ORDER BY tapel ASC, jenjang DESC, kelas ASC"""
        params = (jenjang, tapel,)
        return self.get_list_data(sql, params)
    
    def get_daftar_nama_siswa(self, jenjang, tapel, kelas):
        sql = """SELECT r.no_urut, s.nama_singkat, s.nama_lengkap, s.jk, s.tmp_lahir, s.tgl_lahir, s.ayah_nama, s.ibu_nama, s.kampung, r.status_awal, r.nis_lokal
        FROM siswa_riwayat r
        INNER JOIN siswa s ON s.nis_lokal=r.nis_lokal
        WHERE jenjang=%s AND tapel=%s AND kelas=%s AND is_active = 'Ya'
        ORDER BY r.no_urut, s.nama_lengkap;
        """
        params = (jenjang, tapel, kelas)
        return self.get_data(sql, params)