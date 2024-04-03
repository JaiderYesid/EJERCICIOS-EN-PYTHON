#Programa que permita calcular el valor final a pagar en una súper tienda en donde se aplican los siguientes descuentos: a) Por compras entre 10000 y 20000 el 10% b) Por compras entre 20001 y 50000 el 30% c) Por compras superiores a 50000 el 50%

monto_compra = float(input("Ingrese el monto de la compra: $"))

if 10000 <= monto_compra <= 20000:
    descuento = monto_compra * 0.10
    total_pagar = monto_compra - descuento
    print(f"El total a pagar con un descuento del 10% es: ${total_pagar}")
elif 20001 <= monto_compra <= 50000:
    descuento = monto_compra * 0.30
    total_pagar = monto_compra - descuento
    print(f"El total a pagar con un descuento del 30% es: ${total_pagar}")
elif monto_compra > 50000:
    descuento = monto_compra * 0.50
    total_pagar = monto_compra - descuento
    print(f"El total a pagar con un descuento del 50% es: ${total_pagar}")
else:
    print("No se aplica ningún descuento. El total a pagar es: $", monto_compra)
