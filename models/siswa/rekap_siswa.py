from utils.database import ConnectDB
from utils.fungsi.db_functions import *

class RekapSiswa(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def rekap_pertapel(self, jenjang):
        sql = f"""
            SELECT      * 
            FROM        rekap_siswa_pertahun
            WHERE       jenjang = %s
            """
        params = (jenjang,)
        return self.get_data(sql, params)

    def rekap_pertingkat(self, jenjang, tapel):
        sql = f"""
            SELECT * FROM rekap_siswa_pertingkat 
            WHERE jenjang = %s AND tapel = %s
            ORDER BY jenjang, tapel, tingkat;
            """
        params = (jenjang, tapel)
        return self.get_data(sql, params)

    def rekap_perrombel(self, jenjang, tapel):
        sql = f"""
            SELECT * FROM rekap_siswa_perrombel 
            WHERE jenjang = %s AND tapel = %s
            ORDER BY jenjang, tapel, tingkat;

            """
        params = (jenjang, tapel)
        return self.get_data(sql, params)

    def rekap_umur(self, jenjang, tapel):
        sql = f"""
            SELECT * FROM rekap_siswa_usia 
            WHERE jenjang = %s AND tapel = %s
            ORDER BY jenjang, tapel, umur;

            """
        params = (jenjang, tapel)
        return self.get_data(sql, params)