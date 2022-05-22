from Producto import Producto


class Orden:

    contador_orden = 0

    def __init__(self, productos):
        Orden.contador_orden += 1
        self.__id_orden = Orden.contador_orden
        self.__productos = list(productos)

    @property
    def id_orden(self):
        return self.__id_orden

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.precio

        return total

    def __str__(self):
        str_producto = ""
        for producto in self.__productos:
            str_producto += producto.__str__() + "\n"

        return f"Orden: {self.__id_orden}\nProductos:\n{str_producto}"


if __name__ == "__main__":
    p1 = Producto("Camisa", 100.00)
    p2 = Producto("Pantalon", 150.00)

    #crear la lista de los productos
    productos = [p1, p2]

    #agregar la lista de los productos a una orden

    orden1 = Orden(productos)

    print(orden1)








