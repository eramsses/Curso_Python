from logger_base import log
from Conexion import Conexion

class CursorDelPool:

    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def __enter__(self):
        log.debug(f"Iniciando el With __enter__")
        self.__conexion = Conexion.get_connection()
        self.__cursor = self.__conexion.cursor()
        return self.__cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug(f"Saliendo del With __exit__")
        if valor_excepcion:
            self.__conexion.rollback()
            log.error(f"Ocurrio una exepción (Rollback): {valor_excepcion}")
        else:
            self.__conexion.commit()
            log.debug("Commit de la transacción")

        self.__cursor.close()
        Conexion.liberarConexion(self.__conexion)