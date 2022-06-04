# DAO Data Access Object
from Conexion import Conexion
from Persona import Persona
from cursor_del_pool import CursorDelPool
from logger_base import log


class PersonaDAO:
    '''
    DAO Data Access Object
    CRUD (Create-Read-Update-Delete)
    '''

    __TABLA = "personas"
    _SELECCIONAR = f"SELECT * FROM {__TABLA} ORDER BY id_persona"
    _INSERTAR = "INSERT INTO personas(nombre, apellido, email) VALUES(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM personas WHERE id_persona=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)

            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
        return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            log.debug(f"Persona a insertar: {persona}")
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)

            log.debug(f"Persona insertada: {persona}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Persona actualizada: {persona}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            log.debug(f"Persona a eliminar: {persona}")
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)

            log.debug(f"Persona eliminada: {persona}")
            return cursor.rowcount



if __name__ == "__main__":
    #Insertar persona
    #p1 = Persona(nombre="Pedro", apellido="Najera", email="pnajera@yopmail.com")
    #personas_insertadas = PersonaDAO.insertar(p1)
    #log.debug(f"Personas insertadas: {personas_insertadas}")

    #Actulizar un registro
    p2 = Persona(1, "Marco Antonio", "Flores Artica", "mflores@yopmail.com")
    personas_actualizadas = PersonaDAO.actualizar(p2)
    log.debug(f"Personas actualizadas: {personas_actualizadas}")

    #Eliminar un registro
    #p3 = Persona(id_persona=6)
    #personas_eliminadas = PersonaDAO.eliminar(p3)
    #log.debug(f"Personas eliminadas: {personas_eliminadas}")


    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)

