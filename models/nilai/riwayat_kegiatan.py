from utils.database import ConnectDB
# from utils.fungsi.db_functions import *

class RiwayatKegiatan(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_kegiatan_riwayat(self, tapel):
        sql = """
            SELECT *    FROM kegiatan_riwayat
            WHERE       tapel = %s
            ORDER BY    jenjang DESC, tapel, semester
        """
        params = (tapel,)
        return self.get_data(sql, params, True)