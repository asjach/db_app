from utils.database import ConnectDB

class ModelMain:
    def __init__(self):
        self.sql = ConnectDB()

    def get_list_tapel(self):
        sql = """
        SELECT      tapel 
        FROM        tapel 
        ORDER BY    is_active DESC, tapel ASC"""
        results = self.sql.get_data(sql)
        list_tapel = [row['tapel'] for row in results]
        return list_tapel

    def get_list_kelas(self, jenjang, tapel, tingkat=""):
        sql = """
        SELECT 
            kelas 
        FROM kelas_riwayat
        WHERE jenjang = %s 
            AND tapel = %s 
            AND tingkat LIKE %s
        ORDER BY kelas;
        """
        params = (jenjang, tapel, f"%{tingkat}%")
        results = self.sql.get_data(sql, params)
        return [row['kelas'] for row in results]


    def get_tabel(self, nama_tabel, order_by):
        sql = """
            SELECT      * 
            FROM        {}
            ORDER BY    {}
        """.format(nama_tabel, order_by)
        return self.sql.get_data(sql)
    
    def delete_by_id(self, tabel, id):
        sql = f"DELETE FROM {tabel} WHERE id=%s"
        params = (id,)
        return self.sql.update_data(sql, params)