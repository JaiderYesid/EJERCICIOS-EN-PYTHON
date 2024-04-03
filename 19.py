#Programa que permita determinar el total a pagar por una compra de la cual se sabe el valor unitario y la cantidad. Se debe tener en cuenta que se realiza un descuento del 15% por compra inferiores a $20000 y del 35% por compras mayores o iguales a $20000

cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
valor_unitario = float(input("Ingrese el valor unitario de cada artículo: "))

total = cantidad_articulos * valor_unitario

if total < 20000:
    descuento = total * 0.15
    total_descuento = total - descuento
    print("El total a pagar con un descuento del 15% es:", total_descuento)
else:
    descuento = total * 0.35
    total_con_descuento = total - descuento
    print("El total a pagar con un descuento del 35% es:", total_con_descuento)
