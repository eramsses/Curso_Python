
#Función de celcius a fahrenheit
def celcius_fahrenheit(c):
    return c * 9 / 5 + 32

#Función de fahrenheit a celcius
def fahrenbheit_celcius(f):
    return (f - 32) * 5 / 9

#Prueba de C a F
celcius = float(input("Proporcione el valor en celcius: "))
resultado = celcius_fahrenheit(celcius)

#Mostrar el resultado
print(f"{celcius:0.2f} C a F: {resultado:0.2f}")

#Prueba de F a C
fahrenheit = float(input("Ingrese el valor en Fahrenheit: "))
resultado = fahrenbheit_celcius(fahrenheit)

#Mostrar el resultado
print(f"{fahrenheit:0.2f} F a C: {resultado:0.2f}")

