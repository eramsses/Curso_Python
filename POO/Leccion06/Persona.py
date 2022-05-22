class Persona:
    contador_persona = 0

    def __init__(self, nombre, edad):

        self.__id_persona = self.__generear_siguiente_valor()
        self.__nombre = nombre
        self.__edad = edad

    @classmethod
    def __generear_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona

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

print(p1.contador_persona)

print()





