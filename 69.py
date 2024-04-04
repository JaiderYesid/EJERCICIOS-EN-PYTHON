#Programa que permita llenar una matriz cuadrada de 5 filas y 5 columnas y luego calcule la suma de su diagonal principal. La diagonal principal de una matriz cuadrada es aquella donde el número de fila es igual al número de columna)

matriz = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

for i in range(5):
    for j in range(5):
        valor = float(input(f"Ingrese un valor para la posición ({i+1}, {j+1}): "))
        matriz[i][j] = valor

suma_diagonal = sum(matriz[i][i] for i in range(5))

print(f"La suma de la diagonal principal es: {suma_diagonal}")
