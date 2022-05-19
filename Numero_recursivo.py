

def imprimir_numero_recursivo(numero):
    if numero > 1:
        print(numero)
        imprimir_numero_recursivo(numero - 1)
    elif numero  == 0:
        print("En número debe ser mayor que cero.")
    elif numero <= 0 :
        print("Valor incorrecto")


imprimir_numero_recursivo(0)