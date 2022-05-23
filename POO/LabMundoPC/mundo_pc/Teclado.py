from mundo_pc.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)

        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados

    def __str__(self):
        return f"Teclado: Id:{self.__id_teclado}, marca: {super().marca}, tipo_entrada: {super().tipo_entrada}"


if __name__ == "__main__":
    t1 = Teclado("USB", "Dell")
    t2 = Teclado("Bluetooth", "HP")
    t3 = Teclado("USB", "Redragon")

    print(t1)
    print(t2)
    print(t3)




