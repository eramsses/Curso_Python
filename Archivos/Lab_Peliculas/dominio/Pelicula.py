class Pelicula:

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, n):
        self.__nombre = n

    def __str__(self):
        return f"Película: {self.__nombre}"