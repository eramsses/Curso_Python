class ManejoArchivos:

    def __init__(self, nombre, modo):
        self.__nombre = nombre
        self.__modo = modo


    @property
    def nombre(self):
        return self.__nombre

    @property
    def modo(self):
        return self.__modo

    @modo.setter
    def modo(self, m):
        self.__modo = m

    def __enter__(self):
        try:
            self.__nombre = open(self.__nombre, self.__modo, encoding="UTF8")
            return self.__nombre
        except Exception as e:
            print(f"ERROR: {e}")


    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.__nombre:
                self.__nombre.close()
        except Exception as e:
            print(f"ERROR: {e}")