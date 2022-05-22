class Persona:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __add__(self, other):
        return self.__nombre + " " + other.__nombre

    def __sub__(self, other):
        return self.__edad - other.__edad

p1 = Persona("Juan", 30)
p2 = Persona("Carlos", 16)

print(p1 + p2)
print(p1 - p2)