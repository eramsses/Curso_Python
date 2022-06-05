import sys
from Logger.logger_base import log
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
                #log.debug(f"Creación del pool exitosa: {cls._pool}")
                return cls._pool

            except Exception as e:
                log.error(f"Ocurrió un error al obtener el pool: {e}")
                sys.exit()
        else:
            return cls._pool


    @classmethod
    def get_connection(cls):
        conexion = cls.get_pool().getconn()
        #log.debug(f"Conexión obtenida del pool: {conexion}")
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.get_pool().putconn(conexion)
        #log.debug(f"Regresamos la conexión: {conexion}")

    @classmethod
    def cerrarConexiones(cls):
        cls.get_pool().closeall()

if __name__ == "__main__":
    con1 = Conexion.get_connection()
    con2 = Conexion.get_connection()
    con3 = Conexion.get_connection()
    con4 = Conexion.get_connection()
    con5 = Conexion.get_connection()
    #Liberar una conexión
    Conexion.liberarConexion(con5)

    con6 = Conexion.get_connection()



