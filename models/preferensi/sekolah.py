from utils.database import ConnectDB

class Sekolah(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_daftar_sekolah(self, nama_sekolah):
        sql = """
            SELECT * FROM daftar_sekolah WHERE nama_sekolah LIKE %s
            """
        params = (f'%{nama_sekolah}%',)
        return self.get_data(sql, params, True)
