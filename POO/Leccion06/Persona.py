class Persona:
    contador_persona = 0

    def __init__(self, nombre, edad):
        Persona.contador_persona += 1
        self.__id_persona = Persona.contador_persona
        self.__nombre = nombre
        self.__edad = edad

    @property
    def id_persona(self):#Solo lectura
        return self.__id_persona

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    def __str__(self):
        return f"Persona [id: {self.__id_persona}, nombre: {self.__nombre}, edad: {self.__edad}]"


p1 = Persona("Juan", 38)
p2 = Persona("Karla", 30)
print(p1)
print(p2)

print()





