from mysql import connector
from dotenv import load_dotenv
import os
from utils.app_config import *

class ConnectDB:
    def __init__(self, database_name=None):
        """Inisialisasi koneksi ke database (default dari .env jika tidak ditentukan)"""
        load_dotenv()
        self.host = os.getenv("DATABASE_HOST")
        self.user = os.getenv("DATABASE_USER")
        self.password = os.getenv("DATABASE_PASSWORD")
        self.port = os.getenv("DATABASE_PORT")
        self.default_database = os.getenv("DATABASE_NAME")

        self.current_database = database_name or self.default_database
        self.my_connector = None
        self.my_cursor = None

    def connect(self, database_name=None):
        """Buka koneksi ke database tertentu jika belum terhubung"""
        database_name = database_name or self.current_database

        if self.my_connector is None or not self.my_connector.is_connected():
            self.my_connector = connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=database_name
            )
        self.my_cursor = self.my_connector.cursor(dictionary=True, buffered=True)

    def reconnect_if_needed(self):
        """Pastikan koneksi tetap aktif sebelum eksekusi query"""
        if self.my_connector is None or not self.my_connector.is_connected():
            self.connect()

    def get_data(self, sql, params=None, return_fields=False):
        """Mengambil semua data berdasarkan query, dengan opsi untuk mengembalikan nama field"""
        if DEBUG_GET:
            print(sql, params)
        try:
            self.reconnect_if_needed()
            with self.my_connector.cursor(dictionary=True) as cursor:
                cursor.execute(sql, params or ())
                data = cursor.fetchall()
                if return_fields:
                    column_names = [desc[0] for desc in cursor.description]
                    return data, column_names
                return data
        except Exception as E:
            print("ERROR get_data:", E)
            return ([], []) if return_fields else []
        finally:
            if self.my_connector:
                self.my_connector.close()

    def get_one_data(self, sql, params=None):
        """Mengambil satu data (row) berdasarkan query"""
        if DEBUG_ONE:
            print(sql, params)
        try:
            self.reconnect_if_needed()
            with self.my_connector.cursor(dictionary=True) as cursor:
                cursor.execute(sql, params or ())
                return cursor.fetchone()
        except Exception as E:
            print("ERROR get_one_data:", E)
            return 
        finally:
            if self.my_cursor:
                self.my_cursor.close()
            if self.my_connector:
                self.my_connector.close()

    def update_data(self, sql, params=None):
        if DEBUG_UPDATE:
            print(sql, params)
        try:
            self.reconnect_if_needed()
            with self.my_connector.cursor() as cursor:
                if isinstance(params, list) and all(isinstance(p, tuple) for p in params):
                    cursor.executemany(sql, params)
                else:
                    cursor.execute(sql, params or ())
                row_count = cursor.rowcount  # Ambil rowcount sebelum commit
                self.my_connector.commit()
                return row_count  # Kembalikan jumlah baris yang terpengaruh
        except connector.Error as E:
            self.my_connector.rollback()
            print("ERROR update_data:", E)
            return False
        finally:
            if self.my_cursor:
                self.my_cursor.close()
            if self.my_connector:
                self.my_connector.close()

    # def update_data(self, sql, params=None):
    #     """Menjalankan perintah INSERT, UPDATE, DELETE"""
    #     if DEBUG_UPDATE:
    #         print(sql, params)
    #     try:
    #         self.reconnect_if_needed()
    #         with self.my_connector.cursor() as cursor:
    #             if isinstance(params, list) and all(isinstance(p, tuple) for p in params):
    #                 cursor.executemany(sql, params)
    #             else:
    #                 cursor.execute(sql, params or ())
    #         self.my_connector.commit()
    #         return True
    #     except connector.Error as E:
    #         self.my_connector.rollback()
    #         print("ERROR update_data:", E)
    #         return False
    #     finally:
    #         if self.my_cursor:
    #             self.my_cursor.close()
    #         if self.my_connector:
    #             self.my_connector.close()

    def close_connection(self):
        """Menutup koneksi ke database"""
        if self.my_cursor:
            self.my_cursor.close()
            self.my_cursor = None
        if self.my_connector:
            self.my_connector.close()
            self.my_connector = None

    def set_database(self, database_name):
        """Mengubah database yang aktif dan menutup koneksi lama jika ada"""
        if self.current_database != database_name:
            self.close_connection()
            self.current_database = database_name

    def get_databases(self):
        """Mengambil daftar database kecuali database sistem"""
        self.connect_without_db()
        with self.my_connector.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            all_databases = [db[0] for db in cursor.fetchall()]
        
        self.close_connection()
        system_databases = {"information_schema", "mysql", "performance_schema", "sys"}
        return [db for db in all_databases if db not in system_databases]

    def connect_without_db(self):
        """Buka koneksi tanpa memilih database (untuk mengambil daftar database)"""
        if self.my_connector and self.my_connector.is_connected():
            return

        self.my_connector = connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port
        )
        self.my_cursor = self.my_connector.cursor()
