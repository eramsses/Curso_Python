class Persona:

    # constructor de la clase se llama __init_
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre ## con __ se limita para que no se acceda desde afuera de la clase
        self.apellido = apellido
        self.edad = edad

    #Get set de una propiedad
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # Función para imprimir la información de la clase
    def mostrar_detalle(self):
        print(f"Nombre: {self.__nombre} {self.apellido} {self.edad} años")


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
