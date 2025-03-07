from utils.database import ConnectDB

class ModelInputExcel:
    def __init__(self):
        self.sql = ConnectDB()

    def set_db(self, db_name):
        self.sql.set_database(db_name)

    def get_databases(self):
        databases = self.sql.get_databases()
        return databases

    def get_all_tables(self,):
        query = "SHOW TABLES"
        tables = self.sql.get_data(query)
        return [list(table.values())[0] for table in tables]

    def get_column_names(self, nama_tabel):
        query = f"SHOW COLUMNS FROM `{nama_tabel}`"
        columns = self.sql.get_data(query)
        return [col["Field"] for col in columns]

    def get_table_data(self, nama_tabel):
        query = f"SELECT * FROM `{nama_tabel}`"
        return self.sql.get_data(query)
    
    def data_for_template(self, nama_tabel, join, kolom, kondisi, order_by):
        query = """
        SELECT {} FROM {} {} WHERE {} ORDER BY {}
        """.format(kolom, nama_tabel, join, kondisi, order_by)
        # print(query)
        return self.sql.get_data(query)