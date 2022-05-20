class Persona:

    # constructor de la clase se llama __init_
    def __init__(self, nombre, edad):
        self.__nombre = nombre # con __ se limita para que no se acceda desde afuera de la clase
        self.__edad = edad

    #Get set de una propiedad
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f"Nombre: {self.__nombre} Edad: {self.__edad}"

class Empleado(Persona):
    #Pasar desde el constructor de Empleado al contructor de la clase Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.__sueldo = sueldo

    def __str__(self):
        return f"{super().__str__()} Sueldo: {self.__sueldo:0.2f}"


if __name__ == "__main__":
    empleado1 = Empleado("Erick Rodriguez", 43, 60000)

    print(empleado1.nombre)
    print(empleado1.edad)
    print(f"{empleado1.__sueldo:0.2f}")