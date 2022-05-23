from mundo_pc.Monitor import Monitor
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    @property
    def id_computadora(self):
        return self.__id_computadora

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, n):
        self.__nombre = n

    @property
    def monitor(self):
        return self.__monitor

    @monitor.setter
    def monitor(self, m):
        self.__monitor = m

    @property
    def teclado(self):
        return self.__teclado

    @teclado.setter
    def teclado(self, t):
        self.__teclado = t

    @property
    def raton(self):
        return self.__raton

    @raton.setter
    def raton(self, r):
        self.__raton = r

    def __str__(self):
        return f"{self.__nombre}: {self.__id_computadora}\n\t\t{self.monitor}\n\t\t{self.__teclado}\n\t\t{self.__raton}\n"


if __name__ == "__main__":

    #Monitores
    m1 = Monitor("Asus", 27)
    m2 = Monitor("Dell", 21)
    m3 = Monitor("HP", 21)

    #Teclados
    t1 = Teclado("USB", "Dell")
    t2 = Teclado("Bluetooth", "HP")
    t3 = Teclado("USB", "Redragon")

    #Ratones
    r1 = Raton("USB", "Razer")
    r2 = Raton("BlueTooth", "HP")
    r3 = Raton("USB", "Dell")

    #Computadoras
    c1 = Computadora("HP", m3, t2, r2)

    print(c1)





