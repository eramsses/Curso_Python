
try:
    archivo = open("prueba.txt", "r", encoding="UTF8")
    print(archivo.read())

    #leer algunos caracteres
    #print(archivo.read(5))
    #print(archivo.read(3))


    #leer linea completa

    print(archivo.readline())


except Exception as e:
    print(e)
finally:
    archivo.close()



