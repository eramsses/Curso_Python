from mundo_pc.DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)

        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones


    def __str__(self):
        return f"Ratón: Id: {self.__id_raton}, marca: {super().marca}, tipo entrada: {super().tipo_entrada}"




if __name__ == "__main__":
    r1 = Raton("USB", "Razer")
    r2 = Raton("BlueTooth", "LogiTech")
    r3 = Raton("USB", "Dell")

    print(r1)
    print(r2)
    print(r3)


