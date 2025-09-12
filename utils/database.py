from mysql import connector
from dotenv import load_dotenv
import os
import time


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
        self.in_transaction = False  # Flag untuk melacak status transaksi
        self._cache = {}  # dict untuk cache query
        self._cache_expiry = 60  # TTL dalam detik

    def _make_cache_key(self, sql, params):
        return (sql, tuple(params) if params else ())
    
    def _get_from_cache(self, cache_key):
        now = time.time()
        if cache_key in self._cache:
            cached = self._cache[cache_key]
            if now - cached["time"] < self._cache_expiry:
                return cached["data"]
            else:
                del self._cache[cache_key]
        return None
    
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

    def get_data(self, sql, params=None, return_fields=False, use_cache=True):
        try:
            cache_key = self._make_cache_key(sql, params)

            if use_cache:
                cached = self._get_from_cache(cache_key)
                if cached is not None:
                    return cached

            self.reconnect_if_needed()
            with self.my_connector.cursor(dictionary=True) as cursor:
                cursor.execute(sql, params or ())
                data = cursor.fetchall()
                if return_fields:
                    column_names = [desc[0] for desc in cursor.description]
                    result = (data, column_names)
                else:
                    result = data

            if use_cache:
                self._cache[cache_key] = {"time": time.time(), "data": result}

            return result
        except Exception as E:
            print("ERROR get_data:", E)
            return ([], []) if return_fields else []
        finally:
            if not self.in_transaction and self.my_connector:
                self.my_connector.close()

    def get_list_data(self, sql, params=None):
        """Mengambil data dari satu kolom berdasarkan query dan mengembalikan list nilai"""
        try:
            self.reconnect_if_needed()
            with self.my_connector.cursor() as cursor:  # Gunakan cursor tanpa dictionary=True
                cursor.execute(sql, params or ())
                data = cursor.fetchall()
                return [row[0] for row in data]
        except Exception as E:
            print("ERROR get_list_data:", E)
            return []
        finally:
            if not self.in_transaction and self.my_connector:
                self.my_connector.close()

    def get_one_data(self, sql, params=None):
        """Mengambil satu data (row) berdasarkan query"""
        try:
            self.reconnect_if_needed()
            with self.my_connector.cursor(dictionary=True) as cursor:
                cursor.execute(sql, params or ())
                return cursor.fetchone()
        except Exception as E:
            print("ERROR get_one_data:", E)
            return None
        finally:
            if not self.in_transaction and self.my_connector:
                self.my_connector.close()

    def update_data(self, sql, params=None):
        try:
            self.reconnect_if_needed()
            with self.my_connector.cursor() as cursor:
                if isinstance(params, list) and all(isinstance(p, tuple) for p in params):
                    cursor.executemany(sql, params)
                else:
                    cursor.execute(sql, params or ())
                row_count = cursor.rowcount
                if not self.in_transaction:
                    self.my_connector.commit()

                # clear cache setelah update
                self._cache.clear()
                return row_count
        except connector.Error as E:
            if self.in_transaction:
                self.my_connector.rollback()
            print("ERROR update_data:", E)
            return False
        finally:
            if not self.in_transaction and self.my_connector:
                self.my_connector.close()

    def begin_transaction(self):
        """Mulai transaksi"""
        if not self.in_transaction:
            self.reconnect_if_needed()
            self.my_connector.start_transaction()
            self.in_transaction = True

    def commit_transaction(self):
        if self.in_transaction:
            self.my_connector.commit()
            self.in_transaction = False
            self._cache.clear()
            if self.my_connector:
                self.my_connector.close()

    def rollback_transaction(self):
        if self.in_transaction:
            self.my_connector.rollback()
            self.in_transaction = False
            self._cache.clear()
            if self.my_connector:
                self.my_connector.close()

    def close_connection(self):
        """Menutup koneksi ke database"""
        if self.my_cursor:
            self.my_cursor.close()
            self.my_cursor = None
        if self.my_connector:
            if self.in_transaction:
                self.my_connector.rollback()
                self.in_transaction = False
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

