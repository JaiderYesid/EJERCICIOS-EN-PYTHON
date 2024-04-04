#Programa que permita llenar una matriz cuyo número de filas y columnas es ingresado por el usuario, donde se busque un valor (Ingresado por el usuario) y al encontrarlo muestre su posición (fila, columna). 

num_filas = int(input("Ingrese el número de filas de la matriz: "))
num_columnas = int(input("Ingrese el número de columnas de la matriz: "))

matriz = []
for _ in range(num_filas):
    fila = []
    for _ in range(num_columnas):
        valor = int(input(f"Ingrese un valor para la posición ({len(matriz)+1}, {len(fila)+1}): "))
        fila.append(valor)
    matriz.append(fila)

valor_buscar = int(input("Ingrese el valor que desea buscar en la matriz: "))

encontrado = False
for i in range(num_filas):
    for j in range(num_columnas):
        if matriz[i][j] == valor_buscar:
            print(f"El valor {valor_buscar} se encuentra en la posición ({i+1}, {j+1})")
            encontrado = True

if not encontrado:
    print(f"El valor {valor_buscar} no se encuentra en la matriz.")
