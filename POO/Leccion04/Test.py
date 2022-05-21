from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creación Objeto Cuadrado".center(40,'*'))
c1 = Cuadrado(5, "rojo")
print(f"Cálculo del área del cuadrado {c1.calcular_area()}")
print(c1)

print("Creación Objeto Rectángulo".center(40,'*'))
r1 = Rectangulo(5, 4, "Verde")
print(f"Cálculo del área del rectángulo {r1.calcular_area()}")
print(r1)
#MRO Method Resolution Order
# Este orden está definido por el orden en el que se insertan las herencias







