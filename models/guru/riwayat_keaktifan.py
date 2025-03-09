from utils.database import ConnectDB
from utils.fungsi.general_functions import opsi_order, opsi_search

class RiwayatKeaktifan(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_keaktifan_guru(
            self,
            jenjang = '',
            tapel = '',
            kolom = 'default',
            order_by = 'nama_lengkap',
            search_by = 'nama_lengkap',
            search_text = ''
        ):

        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)
        
        sql = """
            SELECT      {}
            FROM        guru_keaktifan r
            INNER JOIN  guru g ON g.id_guru = r.id_guru
            WHERE       jenjang LIKE %s AND tapel = %s AND {} LIKE %s
            ORDER BY    {};
            """.format(kolom, search_by, order_by)
        params = (f"%{jenjang}%", tapel, f"%{search_text}%",)
        return self.get_data(sql, params)    