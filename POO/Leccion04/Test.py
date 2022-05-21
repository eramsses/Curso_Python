from Cuadrado import Cuadrado

c1 = Cuadrado(5, "rojo")

print(f"Cálculo del área {c1.calcular_area()}")

#MRO Method Resolution Order
# Este orden está definido por el orden en el que se insertan las herencias

print(Cuadrado.mro())



