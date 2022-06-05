import os

from servicio.CatalogoPeliculas import CatalogoPeliculas
from dominio.Pelicula import Pelicula

op = 0



def menu():
    borrarPantalla()
    print("LABORATORIO PELÍCULAS".center(60,"*"))
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catalogo de películas")
    print("4. Salir")
    try:
        return int(input("Ingrese la opción deseada (1-4): "))
    except Exception as e:
        print(e)


def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")

while op != 4:
    op = menu()

    if op == 1:
        pelicula = input("Escribe el nombre de la película: ")
        p = Pelicula(pelicula)
        borrarPantalla()
        CatalogoPeliculas.agregar_pelicula(p)
        borrarPantalla()
        print("Película agregada".center(50,"*"))
    elif op == 2:
        borrarPantalla()
        CatalogoPeliculas.listar_peliculas()
        borrarPantalla()
    elif op == 3:
        borrarPantalla()
        CatalogoPeliculas.eliminar()
    elif op == 4:
        pass
    else:
        print("Opción desconocida")



