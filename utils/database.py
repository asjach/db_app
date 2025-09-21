from typing import List, Tuple, Optional, Union, Dict
from mysql import connector
from dotenv import load_dotenv
import os
import time
import logging
from cachetools import LRUCache

# Setup logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class DatabaseError(Exception):
    pass

class ConnectDB:
    def __init__(self, database_name: Optional[str] = None, cache_size: int = 100, cache_ttl: float = 60.0):
        """
        Inisialisasi koneksi ke database dengan cache yang dioptimalkan.

        Args:
            database_name: Nama database (opsional, default dari env).
            cache_size: Maksimal jumlah item di cache.
            cache_ttl: Waktu hidup cache dalam detik.
        """
        load_dotenv()
        required_env_vars = ["DATABASE_HOST", "DATABASE_USER", "DATABASE_PASSWORD", "DATABASE_PORT"]
        for var in required_env_vars:
            if not os.getenv(var):
                raise ValueError(f"Environment variable {var} is not set")
        
        self.host = os.getenv("DATABASE_HOST")
        self.user = os.getenv("DATABASE_USER")
        self.password = os.getenv("DATABASE_PASSWORD")
        self.port = os.getenv("DATABASE_PORT")
        self.default_database = os.getenv("DATABASE_NAME")
        self.current_database = database_name or self.default_database

        self.my_connector = None
        self.in_transaction = False

        # Inisialisasi cache menggunakan LRUCache
        self._cache = LRUCache(maxsize=cache_size)
        self._cache_ttl = cache_ttl

    # ===============================
    # 🔹 Utility
    # ===============================
    def _make_cache_key(self, sql: str, params: Optional[Union[Tuple, List[Tuple]]]) -> Tuple:
        """Buat kunci unik untuk cache berdasarkan SQL dan parameter."""
        return (sql, tuple(params) if params else ())

    def _get_from_cache(self, cache_key: Tuple) -> Optional[any]:
        """Ambil data dari cache jika masih valid."""
        cached = self._cache.get(cache_key)
        if cached and time.time() - cached["time"] < self._cache_ttl:
            return cached["data"]
        elif cached:
            self._cache.pop(cache_key, None)
        return None

    def _set_cache(self, cache_key: Tuple, data: any) -> None:
        """Simpan data ke cache dengan timestamp."""
        self._cache[cache_key] = {"time": time.time(), "data": data}

    def _clear_cache(self) -> None:
        """Hapus semua isi cache."""
        self._cache.clear()

    # ===============================
    # 🔹 Connection Handling
    # ===============================
    def connect(self, database_name: Optional[str] = None) -> None:
        """Buka koneksi ke database."""
        if self.my_connector is not None and self.my_connector.is_connected():
            return
        config = {
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "port": self.port
        }
        if database_name or self.current_database:
            config["database"] = database_name or self.current_database
        try:
            self.my_connector = connector.connect(**config)
        except connector.Error as e:
            logger.error(f"Failed to connect to database: {e}")
            raise DatabaseError(f"Connection error: {e}")

    def reconnect_if_needed(self) -> None:
        """Reconnect jika koneksi terputus."""
        if self.my_connector is None or not self.my_connector.is_connected():
            self.connect()

    def close_connection(self) -> None:
        """Menutup koneksi."""
        if self.my_connector and self.my_connector.is_connected():
            if self.in_transaction:
                self.my_connector.rollback()
                self.in_transaction = False
            self.my_connector.close()
            self.my_connector = None

    def __enter__(self):
        """Context manager: buka koneksi."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager: tutup koneksi."""
        self.close_connection()

    # ===============================
    # 🔹 Query Methods
    # ===============================
    def get_data(self, sql: str, params: Optional[Union[Tuple, List[Tuple]]] = None, 
                 return_fields: bool = False, use_cache: bool = False) -> Union[List[Dict], Tuple[List[Dict], List[str]]]:
        """
        Ambil data dari database dengan query SQL.

        Args:
            sql: Query SQL yang akan dieksekusi.
            params: Parameter untuk query (opsional).
            return_fields: Jika True, kembalikan nama kolom bersama data.
            use_cache: Jika True, gunakan cache untuk hasil query.

        Returns:
            List hasil query, atau tuple (data, fields) jika return_fields=True.
        """
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
        except connector.Error as e:
            logger.error(f"Database error in get_data: {e}")
            raise DatabaseError(f"Failed to execute query: {e}")
        finally:
            if not self.in_transaction:
                self.close_connection()

    def get_list_data(self, sql: str, params: Optional[Union[Tuple, List[Tuple]]] = None, 
                     use_cache: bool = False) -> List[any]:
        """
        Ambil daftar data dari kolom pertama hasil query.

        Args:
            sql: Query SQL yang akan dieksekusi.
            params: Parameter untuk query (opsional).
            use_cache: Jika True, gunakan cache untuk hasil query.

        Returns:
            List berisi nilai dari kolom pertama.
        """
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
        except connector.Error as e:
            logger.error(f"Database error in get_list_data: {e}")
            raise DatabaseError(f"Failed to execute query: {e}")
        finally:
            if not self.in_transaction:
                self.close_connection()

    def get_one_data(self, sql: str, params: Optional[Union[Tuple, List[Tuple]]] = None, 
                     use_cache: bool = False) -> Optional[Dict]:
        """
        Ambil satu baris data dari query.

        Args:
            sql: Query SQL yang akan dieksekusi.
            params: Parameter untuk query (opsional).
            use_cache: Jika True, gunakan cache untuk hasil query.

        Returns:
            Dictionary berisi satu baris data, atau None jika tidak ada.
        """
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
        except connector.Error as e:
            logger.error(f"Database error in get_one_data: {e}")
            raise DatabaseError(f"Failed to execute query: {e}")
        finally:
            if not self.in_transaction:
                self.close_connection()

    def update_data(self, sql: str, params: Optional[Union[Tuple, List[Tuple]]] = None) -> int:
        """
        Insert/Update/Delete data. Commits changes unless in a transaction.

        Args:
            sql: Query SQL untuk insert/update/delete.
            params: Parameter untuk query (opsional).

        Returns:
            Jumlah baris yang terpengaruh.
        """
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
            self._clear_cache()  # Invalidasi cache setelah update
            return row_count
        except connector.Error as e:
            logger.error(f"Database error in update_data: {e}")
            if self.in_transaction:
                raise DatabaseError(f"Transaction error: {e}")
            self.my_connector.rollback()
            return 0
        finally:
            if not self.in_transaction:
                self.close_connection()

    # ===============================
    # 🔹 Transaction Handling
    # ===============================
    def begin_transaction(self) -> None:
        """Mulai transaksi."""
        if not self.in_transaction:
            self.reconnect_if_needed()
            self.my_connector.start_transaction()
            self.in_transaction = True

    def commit_transaction(self) -> None:
        """Commit transaksi."""
        if self.in_transaction:
            self.my_connector.commit()
            self.in_transaction = False
            self._clear_cache()
            self.close_connection()

    def rollback_transaction(self) -> None:
        """Rollback transaksi."""
        if self.in_transaction:
            self.my_connector.rollback()
            self.in_transaction = False
            self._clear_cache()
            self.close_connection()

    # ===============================
    # 🔹 Admin Methods
    # ===============================
    def set_database(self, database_name: str) -> None:
        """Pindah ke database lain."""
        if self.current_database != database_name:
            self.close_connection()
            self.current_database = database_name
            self._clear_cache()

    def get_databases(self) -> List[str]:
        """Ambil daftar database (kecuali sistem)."""
        try:
            self.connect()
            with self.my_connector.cursor() as cursor:
                cursor.execute("SHOW DATABASES")
                all_dbs = [db[0] for db in cursor.fetchall()]
            return [db for db in all_dbs if db not in {"information_schema", "mysql", "performance_schema", "sys"}]
        except connector.Error as e:
            logger.error(f"Database error in get_databases: {e}")
            raise DatabaseError(f"Failed to retrieve databases: {e}")
        finally:
            self.close_connection()