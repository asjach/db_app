from utils.database import ConnectDB

class ModelMain(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_list_tapel(self):
        sql = """
        SELECT      tapel 
        FROM        tapel 
        ORDER BY    is_active DESC, tapel ASC"""
        results = self.get_data(sql)
        list_tapel = [row['tapel'] for row in results]
        return list_tapel

    def get_kelas(self, jenjang, tapel, tingkat=""):
        sql = """
        SELECT      id, kelas 
        FROM        kelas_riwayat
        WHERE       jenjang = %s AND tapel = %s AND tingkat LIKE %s
        ORDER BY    kelas;
        """
        params = (jenjang, tapel, f"%{tingkat}%")
        return self.get_data(sql, params)
    