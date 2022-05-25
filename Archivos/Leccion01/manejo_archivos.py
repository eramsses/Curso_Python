

try:
    archivo = open("prueba.txt", "w", encoding="UTF8")
    archivo.write("Primer contenido agregado\n")
    archivo.write("Adios\n")
    archivo.write("Acción, ahora contenido con acentos usando el parámetro encoding=\"UTF8\"")

except Exception as e:
    print(e)
finally:
    archivo.close()