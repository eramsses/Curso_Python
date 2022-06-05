from Logger.logger_base import log


class Usuario:
    def __init__(self, id_usuario = None, usuario = None, password = None):
        self.__id = id_usuario
        self.__usuario = usuario
        self.__password = password

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_usuario):
        self.__id = id_usuario

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        return f"Id_usuario: {self.__id}, Usuario: {self.__usuario}, Contraseña: {self.__password}"

if __name__ == "__main__":
    u1 = Usuario(1, "erodriguez", "123")
    log.debug(u1)