from mundo_pc.Computadora import Computadora
from mundo_pc.Monitor import Monitor
from mundo_pc.Orden import Orden
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado


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
c2 = Computadora("GAMER", m1, t3, r1)
c3 = Computadora("Genérica", m3, t1, r2)

computadoras1 = [c2]
computadoras2 = [c2, c1, c3]

o1 = Orden(computadoras1)
o2 = Orden(computadoras2)

#Agregar una computadora nueva
o1.agregar_computadora(c3)

print(o1)
print(o2)








