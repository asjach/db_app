from utils.database import ConnectDB
# from utils.fungsi.general_functions import opsi_order, opsi_search

class DetailGuru(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

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