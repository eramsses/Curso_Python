import sys

from logger_base import log
import psycopg2 as db

class Conexion:
    __DATABASE = "test_db"
    __USERNAME = "postgres"
    __PASWORD = "michelle"
    __DB_PORT = "5432"
    __HOST = "127.0.0.1"
    __conexion = None
    _cursor = None

    @classmethod
    def get_connection(cls):
        if(cls.__conexion is None):
            try:
                cls.__conexion = db.connect(host=cls.__HOST,
                                            user= cls.__USERNAME,
                                            password=cls.__PASWORD,
                                            port=cls.__DB_PORT,
                                            database=cls.__DATABASE)

                log.debug(f"Conexión exitosa: {cls.__conexion}")
                return cls.__conexion
            except Exception as e:
                log.error(f"Ocurrió un error al establecer conexión: {e}")
                sys.exit()
        else:
            return cls.__conexion

    @classmethod
    def get_cursor(cls):
        if cls._cursor == None:
            try:
                cls._cursor = cls.get_connection().cursor()
                log.debug(f"Se abrió correctamente el cursor: {cls._cursor}")
                return cls._cursor
            except Exception as e:
                log.error(f"Ocurrió un error al obtener el cursor: {e}")

        else:
            return cls._cursor

if __name__ == "__main__":
    Conexion.get_connection()
    Conexion.get_cursor()


