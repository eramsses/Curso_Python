
resultado = None

try:
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    resultado = a / b
except ZeroDivisionError as ex:
    print(f"Ocurrió el error: {ex}")
except TypeError as ex:
    print(f"Ocurrió el error: {ex}")
except Exception as ex:
    print(f"Ocurrió el error: {ex} - {type(ex)}")
else:
    print("No hay excepciones")
finally:
    print("Siempre se ejecuta haya o no excepciones")

print(f"Resultado: {resultado:}")
print("Continuamos....")
