#ABC Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):

    def __init__(self, ancho, alto):
        if self.__validar_valor(ancho):
            self.__ancho = ancho
        else:
            self.__ancho = 0

        if self.__validar_valor(alto):
            self.__alto = alto
        else:
            self.__alto = 0

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        if self.__validar_valor(ancho):
            self.__ancho = ancho
        else:
            self.__ancho = 0

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        if self.__validar_valor(alto):
            self.__alto = alto
        else:
            self.__alto = 0

    def __validar_valor(self, valor):
        return 0 < valor <= 10

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f"FiguraGeometrica [alto: {self.alto}, ancho: {self.ancho}]"