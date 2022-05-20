class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def mostrar_resultado(self):
        print(f"El área de un rectangulo de base {self.base}, x altura de: {self.altura} = {self.calcular_area()} ")

b = int(input("Ingrese la base: "))
h = int(input("Ingrese la altura: "))

rectangulo = Rectangulo(b, h)

rectangulo.mostrar_resultado()




