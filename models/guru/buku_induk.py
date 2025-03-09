from utils.database import ConnectDB
from utils.fungsi.general_functions import opsi_order, opsi_search

class BukuInduk(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_buku_induk_guru(self, order_by='Nama', search_by='Nama', search=''):
        order_by = opsi_order(order_by)
        search_by = opsi_search(search_by)
        sql = """
            SELECT      * 
            FROM        guru
            WHERE       {} LIKE %s
            ORDER BY    {}
            ;""".format(search_by, order_by)
        params = (f"%{search}%",)
        return self.get_data(sql, params)