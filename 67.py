#Programa que permita llenar una matriz cuyo número de filas y columnas es ingresado por el usuario y luego calcule la suma de cada una de sus filas (una x una)

num_filas = int(input("Ingrese el número de filas de la matriz: "))
num_columnas = int(input("Ingrese el número de columnas de la matriz: "))

matriz = []
for _ in range(num_filas):
    fila = []
    for _ in range(num_columnas):
        valor = float(input(f"Ingrese un valor para la posición ({len(matriz)+1}, {len(fila)+1}): "))
        fila.append(valor)
    matriz.append(fila)

suma_filas = []
for fila in matriz:
    suma_fila = sum(fila)
    suma_filas.append(suma_fila)

for i, suma in enumerate(suma_filas):
    print(f"La suma de la fila {i+1} es: {suma}")
