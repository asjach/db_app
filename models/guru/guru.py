from utils.database import ConnectDB

class ModelGuru:
    def __init__(self):
        self.sql = ConnectDB()

    def opsi_order(self, opsi_order):
        order_mapping = {
            "Nama": 'nama_lengkap',
            "JK": 'jk, nama_lengkap',
            "Urutan": 'r.no_urut',
            "ID Guru": 'id_guru',
            }
        return order_mapping.get(opsi_order, 'nama_lengkap')
    
    def opsi_search(self, opsi_search):
        mapping = {
            "Nama": "nama_lengkap",
            }
        return mapping.get(opsi_search, '')
    
#BUKU INDUK GURU
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
        return self.sql.get_data(sql, params)
    
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
        return self.sql.get_data(sql, params)    

#DIALOG DETAIL GURU
    def get_detail_guru(self, id_guru):
        sql = """
            SELECT      * 
            FROM        guru
            WHERE   id_guru = %s
            """
        params = (id_guru,)
        return self.sql.get_one_data(sql, params)
    
    def update_identitas_guru(self, **data):
        placeholders = ", ".join(["{} = %s".format(column) for column in data.keys()])
        sql = """
            UPDATE      guru 
            SET         {} 
            WHERE       id_guru= %s
            """.format(placeholders)
        params = tuple(data.values()) + (data["id_guru"],)
        return self.sql.update_data(sql, params)
    
    def get_daftar_guru(self, search_by=None, search_text=None):
        sql = """
            SELECT      * 
            FROM        guru
            WHERE       {} LIKE %s
            """.format(search_by)
        params = (f"%{search_text}%",)
        return self.sql.get_data(sql, params)

    def get_keluarga(self, id_guru):
        sql = """
            SELECT      *
            FROM        guru_keluarga
            WHERE       id_guru = %s
            """
        params = (id_guru,)
        return self.sql.get_data(sql, params)
    
    def insert_keluarga(self, **data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        sql = f"""
        INSERT INTO     guru_keluarga ({columns})
        VALUES          ({placeholders});
        """
        params = tuple(data.values())
        return self.sql.update_data(sql, params)
    
    def get_pendidikan_formal(self, id_guru):
        sql = """
            SELECT      *
            FROM        guru_pendidikan
            WHERE       id_guru = %s
            """
        params = (id_guru,)
        return self.sql.get_data(sql, params)
    
    def insert_riwayat_pendidikan(self, **data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        sql = f"""
        INSERT INTO     guru_pendidikan ({columns})
        VALUES          ({placeholders});
        """
        params = tuple(data.values())
        return self.sql.update_data(sql, params)
    

# RIWAYAT MENGAJAR
    