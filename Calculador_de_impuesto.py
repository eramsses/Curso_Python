


def calcularImpuesto(monto, tasa):
    return monto + (monto * (tasa / 100))

 
monto = float(input("Proporcione el monto: "))
tasa = float(input("Ingrese la tasa de impuesto: "))

pago_total = calcularImpuesto(monto, tasa)

print(f"El pago total con impuestos es: {pago_total}")