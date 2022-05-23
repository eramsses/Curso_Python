class Orden:

    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes

        self.__computadoras = list(computadoras)


    @property
    def id_orden(self):
        return self.__id_orden

    @property
    def computadoras(self):
        return self.__computadoras

    def agregar_computadora(self, c):
        self.__computadoras.append(c)

    def __str__(self):
        str_computadoras = f"Orden: {self.__id_orden}, Computadoras:\n"
        for c in self.__computadoras:
            str_computadoras += c.__str__()

        return str_computadoras

