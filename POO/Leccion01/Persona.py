class Persona:

    # constructor de la clase se llama __init_
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre ## con __ se limita para que no se acceda desde afuera de la clase
        self.__apellido = apellido
        self.__edad = edad

    #Get set de una propiedad
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
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    # Función para imprimir la información de la clase
    def mostrar_detalle(self):
        print(f"Nombre: {self.__nombre} {self.__apellido} {self.__edad} años")

    def __del__(self):
        print(f"Persona: {self.__nombre} {self.__apellido}")

#Pruebas que se ejecutan solo si es desde la misma clase Persona
if __name__ == "__main__":
    persona1 = Persona("Erick", "Rodríguez", 43)
    persona2 = Persona("Alejandra", "Rodríguez", 9)

    #Agregando otro atributo de clase desde su uso o dinamicamente,
    # éste no se comparte con las otras instancias
    persona1.telefono = "50465445533"
    persona1.__nombre = "Ramsses" #No es accesible desde afuera de la clase

    #persona1.mostrar_detalle()
    Persona.mostrar_detalle(persona1)#otra forma de utilizar los metodos de la clase
    print(persona1.telefono)
    persona2.mostrar_detalle()

    #Uso encapsulado
    print(persona1.nombre)
    persona1.nombre = "Ramsses"
    print(persona1.nombre)

    print(__name__)
