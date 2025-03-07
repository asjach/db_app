from utils.database import ConnectDB

class Alamat(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_alamat(self, kampung):
        sql = "SELECT * FROM daftar_alamat WHERE kampung LIKE %s"
        params = (f'%{kampung}%',)
        return self.get_data(sql, params, True)
    