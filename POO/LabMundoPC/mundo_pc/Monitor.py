class Monitor:

    contador_monitor = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitor += 1
        self.__id_monitor = Monitor.contador_monitor
        self.__marca = marca
        self.__tamanio = tamanio

    @property
    def id_monitor(self):
        return self.__id_monitor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, m):
        self.__marca = m

    @property
    def tamanio(self):
        return self.__tamanio

    @tamanio.setter
    def tamanio(self, t):
        self.__tamanio = t

    def __str__(self):
        return f"Monitor: Id: {self.__id_monitor}, marca: {self.__marca}, tamaño: {self.__tamanio}"


if __name__ == "__main__":
    m1 = Monitor("Asus", 27)
    m2 = Monitor("Dell", 21)
    m3 = Monitor("HP", 21)

    print(m1)
    print(m2)
    print(m3)





