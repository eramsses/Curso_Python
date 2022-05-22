class Empleado:

    def __init__(self, nombre, sueldo):
        self.__nombre = nombre
        self.__sueldo = sueldo


    @property
    def nombre(self):
        return self.__nombre

    @property
    def sueldo(self):
        return self.__sueldo


    def __str__(self):
        return f"Empleado: [Nombre: {self.__nombre}, Sueldo: {self.__sueldo}]"