import os

from Peliculas.ManejoArchivos import ManejoArchivos


class CatalogoPeliculas:
    ruta_archivo = "peliculas.txt"


    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(f"{pelicula.nombre}\n")
        except Exception as e:
            print(f"ERROR: {e}")

    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Catálogo de Películas".center(50, "*"))
            print(archivo.read())
            input("Presione enter para continuar")
        except Exception as e:
            print(f"ERROR: {e}")

    @staticmethod
    def eliminar():
        os.remove(CatalogoPeliculas.ruta_archivo)
        print("Archivo eliminado")


