class Persona:

    #constructor de la clase se llama __init_
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    #Función para imprimir la información de la clase
    def imprimir(self):
        print(f"Nombre: {self.nombre} {self.apellido} {self.edad} años")

persona1 = Persona("Erick", "Rodríguez", 43)
persona2 = Persona("Alejandra", "Rodríguez", 9)

persona1.imprimir()
persona2.imprimir()

