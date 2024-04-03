#Programa para determinar cuánto pagara una persona por una compra de la cual se sabe la cantidad de artículos y el valor unitario. Se debe tener en cuenta que el almacén hace un 20% de descuento cuando la compra supera $100000

cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
valor_unitario = float(input("Ingrese el valor unitario de cada artículo: "))

total = cantidad_articulos * valor_unitario

if total > 100000:
    descuento = total * 0.20
    total_descuento = total - descuento
    print("El total a pagar con un descuento del 20% es:", total_descuento)
else:
    print("El total a pagar es:", total)
