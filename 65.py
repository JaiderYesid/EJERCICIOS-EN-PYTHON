#Programa que permita llenar un matriz cuyo número de filas y columnas es ingresado por el usuario y luego determine cuantos números positivos, negativos y ceros fueron ingresaron

filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

matriz = []
positivos = 0
negativos = 0
ceros = 0

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor para la posición ({i + 1},{j + 1}): "))
        fila.append(valor)
        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1
        else:
            ceros += 1
    matriz.append(fila)

print("La matriz ingresada es:")
for fila in matriz:
    print(fila)

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números iguales a cero: {ceros}")
