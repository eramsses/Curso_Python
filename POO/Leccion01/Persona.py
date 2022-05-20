class Persona:

    # constructor de la clase se llama __init_
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Función para imprimir la información de la clase
    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre} {self.apellido} {self.edad} años")


persona1 = Persona("Erick", "Rodríguez", 43)
persona2 = Persona("Alejandra", "Rodríguez", 9)

#Agregando otro atributo de clase desde su uso o dinamicamente,
# éste no se comparte con las otras instancias
persona1.telefono = "504215643"

#persona1.mostrar_detalle()
Persona.mostrar_detalle(persona1)#otra forma de utilizar los metodos de la clase
print(persona1.telefono)
persona2.mostrar_detalle()
