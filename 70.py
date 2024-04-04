#Programa que permita llenar una matriz cuadrada de 5 filas y 5 columnas y luego calcule la suma de los valores por encima y por debajo de su diagonal principal.

matriz = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

for i in range(5):
    for j in range(5):
        valor = float(input(f"Ingrese un valor para la posición ({i+1}, {j+1}): "))
        matriz[i][j] = valor

suma_arriba_diagonal = sum(matriz[i][j] for i in range(5) for j in range(5) if i < j)
suma_abajo_diagonal = sum(matriz[i][j] for i in range(5) for j in range(5) if i > j)

# Mostramos el resultado de las sumas
print(f"La suma de los valores por encima de la diagonal principal es: {suma_arriba_diagonal}")
print(f"La suma de los valores por debajo de la diagonal principal es: {suma_abajo_diagonal}")
