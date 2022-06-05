from DB.Conexion import Conexion
from Entities.Usuario import Usuario
from DB.cursor_del_pool import CursorDelPool
from Logger.logger_base import log

class UsuarioDAO:

    __TABLA = "usuarios"
    __SELECCIONAR = f"SELECT * FROM {__TABLA} ORDER BY id"
    __INSERTAR = f"INSERT INTO {__TABLA}(usuario, password) VALUES(%s, %s)"
    __ACTUALIZAR = f"UPDATE {__TABLA} SET usuario=%s, password=%s WHERE id=%s"
    __ELIMINAR = f"DELETE FROM {__TABLA} WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls.__SELECCIONAR)

            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
        return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            #log.debug(f"Usuario a insertar: {usuario}")
            valores = (usuario.usuario, usuario.password)
            cursor.execute(cls.__INSERTAR, valores)

            #log.debug(f"Usuario insertado: {usuario}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.usuario, usuario.password, usuario.id)
            cursor.execute(cls.__ACTUALIZAR, valores)
            #log.debug(f"Usuario actualizado: {usuario}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            #log.debug(f"Usuario a eliminar: {usuario}")
            valores = (usuario.id,)
            cursor.execute(cls.__ELIMINAR, valores)

            #log.debug(f"Persona eliminado: {usuario}")
            return cursor.rowcount


if __name__ == "__main__":
    #Eliminar
    u_e = Usuario(id_usuario=3)
    u_eliminados = UsuarioDAO.eliminar(u_e)
    log.debug(f"Eliminados: {u_eliminados}")

    #Actualizar
    #u_a = Usuario(3, "oalvarez", "2233")
    #u_actualizados = UsuarioDAO.actualizar(u_a)
    #log.debug(f"Actualizados: {u_actualizados}")

    #insertar
    #u1 = Usuario(usuario="oandino", password="543")
    #u_insertados = UsuarioDAO.insertar(u1)
    #log.debug(f"Insertado: {u_insertados}")

    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)