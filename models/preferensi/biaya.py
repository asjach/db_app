from utils.database import ConnectDB

class Biaya(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_jenis_biaya(self, search_text):
        sql = """
            SELECT      * 
            FROM        biaya
            WHERE       nama_biaya LIKE %s
            ORDER BY    no_urut
        """
        params = (f'%{search_text}%',)
        return self.get_data(sql, params, True)
    