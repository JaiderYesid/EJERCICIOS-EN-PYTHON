#Programa que permita llenar una matriz cuyo número de filas y columnas es ingresado por el usuario y luego calcule la suma de cada una de sus columnas (una x una) 

num_filas = int(input("Ingrese el número de filas de la matriz: "))
num_columnas = int(input("Ingrese el número de columnas de la matriz: "))

matriz = []
for _ in range(num_filas):
    fila = []
    for _ in range(num_columnas):
        valor = float(input(f"Ingrese un valor para la posición ({len(matriz)+1}, {len(fila)+1}): "))
        fila.append(valor)
    matriz.append(fila)

suma_columnas = [0] * num_columnas  

for fila in matriz:
    for j in range(num_columnas):
        suma_columnas[j] += fila[j]

for i, suma in enumerate(suma_columnas):
    print(f"La suma de la columna {i+1} es: {suma}")
