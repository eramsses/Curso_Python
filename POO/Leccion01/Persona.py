class Persona:


    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def imprimir(self):
        print(self.nombre)
        print(self.apellido)
        print(self.edad)

persona1 = Persona("Erick", "Rodríguez", 43)
persona2 = Persona("Alejandra", "Rodríguez", 9)

persona1.imprimir()
persona2.imprimir()

