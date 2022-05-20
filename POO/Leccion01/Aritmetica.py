class Aritmetica:
    """
    Ckase Aritmetica para las operaciones sumar, restar, etc...
    """

    def __init__(self, operando_a, operando_b):
        self.operando_a = operando_a
        self.operando_b = operando_b

    def sumar(self):
        return self.operando_a + self.operando_b

    def multilicar(self):
        return self.operando_a * self.operando_b

    def restar(self):
        return self.operando_a - self.operando_b

    def dividir(self):
        return self.operando_a / self.operando_b


aritmetica1 = Aritmetica(5, 3)

print(f"Suma: {aritmetica1.operando_a} + {aritmetica1.operando_b} = {aritmetica1.sumar()}")
print(f"Multiplicación: {aritmetica1.operando_a} * {aritmetica1.operando_b} = {aritmetica1.multilicar()}")
print(f"Resta: {aritmetica1.operando_a} - {aritmetica1.operando_b} = {aritmetica1.restar()}")
print(f"Divición: {aritmetica1.operando_a} / {aritmetica1.operando_b} = {aritmetica1.dividir():.2f}")
