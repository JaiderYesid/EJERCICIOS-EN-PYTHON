#Programa que permita llenar una matriz de 3 filas y 4 columnas y luego determine: a) La suma total de todos lo valores b) El valor promedio de todos los valores ingresados

filas = 3
columnas = 4
matriz = []

print("Llenado de la matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Ingrese el valor para la posición ({i+1},{j+1}): "))
        fila.append(valor)
    matriz.append(fila)

suma_total = 0
for fila in matriz:
    suma_total += sum(fila)

total_valores = filas * columnas
promedio_valores = suma_total / total_valores

# Mostramos los resultados
print(f"\nLa suma total de todos los valores es: {suma_total}")
print(f"El valor promedio de todos los valores ingresados es: {promedio_valores}")
