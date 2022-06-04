import sys
from logger_base import log
from psycopg2 import pool

class Conexion:
    __DATABASE = "test_db"
    __USERNAME = "postgres"
    __PASWORD = "michelle"
    __DB_PORT = "5432"
    __HOST = "127.0.0.1"
    __MIN_CON = 1
    __MAX_CON = 5
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls.__MIN_CON, cls.__MAX_CON,
                                                      host=cls.__HOST,
                                                      user=cls.__USERNAME,
                                                      password=cls.__PASWORD,
                                                      port=cls.__DB_PORT,
                                                      database=cls.__DATABASE)
                log.debug(f"Creación del pool exitosa: {cls._pool}")
                return cls._pool

            except Exception as e:
                log.error(f"Ocurrió un error al obtener el pool: {e}")
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def get_connection(cls):
        pass


if __name__ == "__main__":
    pass


