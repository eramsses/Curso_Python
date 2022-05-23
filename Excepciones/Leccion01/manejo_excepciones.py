
resultado = None
a = 10
b = 2
try:
    resultado = a / b
except ZeroDivisionError as ex:
    print(f"Ocurrió el error: {ex}")
except TypeError as ex:
    print(f"Ocurrió el error: {ex}")
except Exception as ex:
    print(f"Ocurrió el error: {ex}")

print(f"Resultado: {resultado:.2}")
print("Continuamos....")
