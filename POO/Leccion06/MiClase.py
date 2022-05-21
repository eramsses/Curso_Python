class MiClase:

    #Variables de clase

    variable_clase = "valor de variable de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


print(MiClase.variable_clase)

miClase = MiClase("Valor de instancia")
print(miClase.variable_instancia)
print(miClase.variable_clase)

miClase2 = MiClase("Otro valor de instancia")
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

MiClase.variable_clase = "Cambió el valor de la variable de clase"

print(miClase.variable_clase)
print(miClase2.variable_clase)

#creando variable de clase al vuelo
MiClase.variable_clase2 = "Nueva variable de clase 2"

#Acceso a la variable desde los dos objetos creados
print(miClase.variable_clase2)
print(miClase2.variable_clase2)



