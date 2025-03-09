from utils.database import ConnectDB

class KeyValue(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_key_value(self, kunci):
        sql = "SELECT * FROM key_value WHERE kunci LIKE %s"
        params = (f'%{kunci}%',)
        return self.get_data(sql, params, True)