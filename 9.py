#Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA

valor_unitario = float(input("Ingrese el valor unitario del producto: $"))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))

subtotal = valor_unitario * cantidad

iva = subtotal * 0.16

total_pagar = subtotal + iva

print(f"El subtotal a pagar es: ${subtotal}")
print(f"El valor del IVA es: {iva}")
print(f"El total a pagar con IVA incluido es: ${total_pagar}")
