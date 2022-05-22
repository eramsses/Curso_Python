from Orden import Orden
from Producto import Producto

p1 = Producto("Camisa", 100.00)
p2 = Producto("Pantalon", 150.00)
p3 = Producto("Calcetines", 30.00)
p4 = Producto("Blusa", 70.00)

#crear la lista de los productos
productos1 = [p1, p2]
productos2 = [p3, p4]

#agregar la lista de los productos a una orden

orden1 = Orden(productos1)
orden2 = Orden(productos2)

print(orden1)
print(f"Total Orden {orden1.id_orden}: {orden1.calcular_total()}\n")
print(orden2)
print(f"Total Orden {orden2.id_orden}: {orden2.calcular_total()}\n")

orden1.agregar_producto(p3)
print(orden1)
print(f"Total Orden {orden1.id_orden}: {orden1.calcular_total()}\n")





