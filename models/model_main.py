from utils.database import ConnectDB
from utils.fungsi.functions import build_in_clause

class Model_Main(ConnectDB):
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

    def get_kelas(self, jenjang, tapel, tingkat=None):
        sql = """
        SELECT      id, kelas 
        FROM        kelas_riwayat
        WHERE       jenjang = %s 
            AND     tapel = %s """
        params = [jenjang, tapel]
        if tingkat:
            placeholders, items = build_in_clause(tingkat)
            if placeholders:
                sql += f" AND tingkat IN ({placeholders})"
                params.extend(items)
        sql += " ORDER BY    kelas;"
        return self.get_data(sql, tuple(params))
    