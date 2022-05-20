class Cubo:

    def __init__(self, b, h, w):
        self.b = b
        self.h = h
        self.w = w

    def calcular_volumen(self):
        return self.b * self.h * self.w

    def mostrar_resultado(self):
        print(f"El volumen del cubo es: {self.calcular_volumen()}")


b = int(input("Ingrese la base del cubo: "))
h = int(input("Ingrese la altura del cubo: "))
w = int(input("Ingrese la profundidad del cubo: "))

cubo = Cubo(b,h,w)

cubo.mostrar_resultado()
