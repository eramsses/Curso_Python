from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalle(objeto):
    print(objeto)
    print(type(objeto))
    #isInstance
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado("Erick", 50000.00)

imprimir_detalle(empleado)

gerente = Gerente(empleado, "Planillas")

imprimir_detalle(gerente)

