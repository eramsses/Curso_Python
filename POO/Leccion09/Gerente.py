from Empleado import Empleado


class Gerente(Empleado):

    #def __init__(self, nombre, sueldo, departamento):
    #    super().__init__(nombre, sueldo)
    #    self.__departamento = departamento
    
    def __init__(self, empleado, departamento):
        super().__init__(empleado.nombre, empleado.sueldo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    def __str__(self):
        return f"Gerente [Departamento: {self.__departamento}] {super().__str__()}"