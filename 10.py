#Programa que permita determinar el salario a pagar a un empleado teniendo como entradas el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud

salario_diario = float(input("Ingrese el salario diario del empleado: $"))
dias_trabajados = int(input("Ingrese el número de días trabajados: "))

salario = salario_diario * dias_trabajados

descuento_pension = salario * 0.10 
descuento_salud = salario * 0.15 

salario_total = salario - descuento_pension - descuento_salud

print(f"El salario bruto a pagar es: ${salario}")
print(f"El descuento por pensión es: ${descuento_pension}")
print(f"El descuento por salud es: ${descuento_salud}")
print(f"El salario neto a pagar es: ${salario_total}")
