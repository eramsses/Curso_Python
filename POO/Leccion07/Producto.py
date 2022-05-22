class Producto:
    contador_producto = 0

    def __init__(self, nombre, precio):
        Producto.contador_producto += 1
        self.__id_producto = Producto.contador_producto
        self.__nombre = nombre
        self.__precio = precio


    @property
    def id_producto(self):
        return self.__id_producto

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    def __str__(self):
        return f"Id Producto: {self.__id_producto}, Nombre: {self.__nombre}, Precio: {self.precio}"



if __name__ == "__main__":
    p1 = Producto("Camisa", 100.00)
    p2 = Producto("Pantalon", 150.00)
    print(p1)
    print(p2)


