from logger_base import log

class Persona:

    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email

    def __str__(self):
        return f'''
            Id Persona: {self.__id_persona}, Nombre: {self.__nombre},
            Apellido: {self.__apellido}, Email: {self.__email}
        '''

    @property
    def id_persona(self):
        return self.__id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self.__id_persona = id_persona

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

if __name__ == "__main__":
    p1 = Persona(1, "Juan", "Perez", "jperez@yopmail.com")
    #print(p1)
    log.debug(p1)

    # Simular un insert
    p1 = Persona(nombre="Juan", apellido="Perez", email="jperez@yopmail.com")
    log.debug(p1)

    # Simular el delete
    p1 = Persona(id_persona=1)
    log.debug(p1)



