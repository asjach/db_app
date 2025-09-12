from mysql import connector
from dotenv import load_dotenv
import os
import time


class ConnectDB:
    def __init__(self, database_name=None):
        """Inisialisasi koneksi ke database"""
        load_dotenv()
        self.host = os.getenv("DATABASE_HOST")
        self.user = os.getenv("DATABASE_USER")
        self.password = os.getenv("DATABASE_PASSWORD")
        self.port = os.getenv("DATABASE_PORT")
        self.default_database = os.getenv("DATABASE_NAME")
        self.current_database = database_name or self.default_database

        self.my_connector = None
        self.in_transaction = False  

        # Cache
        self._cache = {}
        self._cache_ttl = 60  # detik

    # ===============================
    # 🔹 Utility
    # ===============================
    def _make_cache_key(self, sql, params):
        return (sql, tuple(params) if params else ())

    def _get_from_cache(self, cache_key):
        """Ambil data dari cache jika masih valid"""
        now = time.time()
        cached = self._cache.get(cache_key)
        if cached and now - cached["time"] < self._cache_ttl:
            return cached["data"]
        elif cached:
            self._cache.pop(cache_key, None)
        return None

    def _set_cache(self, cache_key, data):
        self._cache[cache_key] = {"time": time.time(), "data": data}

    def _clear_cache(self):
        self._cache.clear()

    # ===============================
    # 🔹 Connection Handling
    # ===============================
    def connect(self, database_name=None):
        """Buka koneksi ke database"""
        db_name = database_name or self.current_database
        if self.my_connector is None or not self.my_connector.is_connected():
            self.my_connector = connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=db_name
            )

    def reconnect_if_needed(self):
        """Reconnect jika koneksi terputus"""
        if self.my_connector is None or not self.my_connector.is_connected():
            self.connect()

    def close_connection(self):
        """Menutup koneksi"""
        if self.my_connector:
            if self.in_transaction:
                self.my_connector.rollback()
                self.in_transaction = False
            self.my_connector.close()
            self.my_connector = None

    # ===============================
    # 🔹 Query Methods
    # ===============================
    def get_data(self, sql, params=None, return_fields=False, use_cache=True):
        cache_key = self._make_cache_key(sql, params)

        if use_cache:
            cached = self._get_from_cache(cache_key)
            if cached is not None:
                return cached

        try:
            self.reconnect_if_needed()
            with self.my_connector.cursor(dictionary=True) as cursor:
                cursor.execute(sql, params or ())
                rows = cursor.fetchall()
                result = (rows, [desc[0] for desc in cursor.description]) if return_fields else rows

            if use_cache:
                self._set_cache(cache_key, result)

            return result
        except Exception as e:
            print("ERROR get_data:", e)
            return ([], []) if return_fields else []
        finally:
            if not self.in_transaction:
                self.close_connection()

    def get_list_data(self, sql, params=None, use_cache=True):
        cache_key = self._make_cache_key(sql, params)

        if use_cache:
            cached = self._get_from_cache(cache_key)
            if cached is not None:
                return cached

        try:
            self.reconnect_if_needed()
            with self.my_connector.cursor() as cursor:
                cursor.execute(sql, params or ())
                result = [row[0] for row in cursor.fetchall()]

            if use_cache:
                self._set_cache(cache_key, result)

            return result
        except Exception as e:
            print("ERROR get_list_data:", e)
            return []
        finally:
            if not self.in_transaction:
                self.close_connection()

    def get_one_data(self, sql, params=None, use_cache=True):
        cache_key = self._make_cache_key(sql, params)

        if use_cache:
            cached = self._get_from_cache(cache_key)
            if cached is not None:
                return cached

        try:
            self.reconnect_if_needed()
            with self.my_connector.cursor(dictionary=True) as cursor:
                cursor.execute(sql, params or ())
                result = cursor.fetchone()

            if use_cache:
                self._set_cache(cache_key, result)

            return result
        except Exception as e:
            print("ERROR get_one_data:", e)
            return None
        finally:
            if not self.in_transaction:
                self.close_connection()

    def update_data(self, sql, params=None):
        """Insert/Update/Delete"""
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

            self._clear_cache()  # invalidasi cache setelah update
            return row_count
        except Exception as e:
            if self.in_transaction:
                self.my_connector.rollback()
            print("ERROR update_data:", e)
            return False
        finally:
            if not self.in_transaction:
                self.close_connection()

    # ===============================
    # 🔹 Transaction Handling
    # ===============================
    def begin_transaction(self):
        if not self.in_transaction:
            self.reconnect_if_needed()
            self.my_connector.start_transaction()
            self.in_transaction = True

    def commit_transaction(self):
        if self.in_transaction:
            self.my_connector.commit()
            self.in_transaction = False
            self._clear_cache()
            self.close_connection()

    def rollback_transaction(self):
        if self.in_transaction:
            self.my_connector.rollback()
            self.in_transaction = False
            self._clear_cache()
            self.close_connection()

    # ===============================
    # 🔹 Admin Methods
    # ===============================
    def set_database(self, database_name):
        """Pindah database"""
        if self.current_database != database_name:
            self.close_connection()
            self.current_database = database_name

    def get_databases(self):
        """Ambil daftar database (kecuali sistem)"""
        self.connect_without_db()
        with self.my_connector.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            all_dbs = [db[0] for db in cursor.fetchall()]
        self.close_connection()
        return [db for db in all_dbs if db not in {"information_schema", "mysql", "performance_schema", "sys"}]

    def connect_without_db(self):
        if self.my_connector and self.my_connector.is_connected():
            return
        self.my_connector = connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port
        )
