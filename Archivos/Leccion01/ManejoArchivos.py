class ManejoArchivos:

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    def __enter__(self):
        print("Obtenemos el recurso".center(50, "*"))
        self.__nombre = open(self.__nombre, "r", encoding="UTF8")
        return self.__nombre

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cerramos el recurso".center(50, "*"))
        if self.__nombre:
            self.__nombre.close()



