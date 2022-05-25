
#El with cierra los recursos al finalizar el bloque with
#with open("prueba.txt", "r", encoding="UTF8") as archivo:
#    print(archivo.read())
from ManejoArchivos import ManejoArchivos

with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())