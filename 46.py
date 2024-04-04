#Programa que permita calcular el valor a pagar en una caja registradora donde se reciben N productos y se ingresan los precios de uno en uno.

cantidad_productos = int(input("Ingrese la cantidad de productos: "))
total = 0
contador = 0

while contador < cantidad_productos:
    contador += 1
    precio = float(input(f"Ingrese el precio del producto {contador}: $"))
    total += precio

print(f"El total a pagar es: ${total}")
