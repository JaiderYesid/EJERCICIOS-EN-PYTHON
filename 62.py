#Programa que permita llenar una matriz y mostrar todos los datos ingresados y su respectiva posición (fila, columna) en pantalla

filas = 3
columnas = 3
matriz = []

print("Llenado de la matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        dato = input(f"Ingrese el dato para la posición ({i+1},{j+1}): ")
        fila.append(dato)
    matriz.append(fila)

print("\nDatos ingresados y su respectiva posición:")
for i in range(filas):
    for j in range(columnas):
        print(f"Dato: {matriz[i][j]}, Posición: ({i+1},{j+1})")
