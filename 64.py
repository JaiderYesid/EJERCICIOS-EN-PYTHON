#Programa que permita llenar una matriz cuyo número de filas y número de columnas es ingresado por el usuario. Se le debe luego preguntar al usuario que posición de la matriz desea ver (que fila y que columna) y mostrar el contenido de esa posición. Se debe repetir la pregunta tantas veces sea necesario hasta que el usuario solicite un numero de fila o número de columna mayor al asignado a la matriz. 

num_filas = int(input("Ingrese el número de filas de la matriz: "))
num_columnas = int(input("Ingrese el número de columnas de la matriz: "))

matriz = []
for _ in range(num_filas):
    fila = [0] * num_columnas
    matriz.append(fila)

def posicion_valida(fila, columna):
    return 0 <= fila < num_filas and 0 <= columna < num_columnas

while True:
    fila_deseada = int(input("Ingrese el número de fila que desea ver (o un número negativo para salir): "))
    if fila_deseada < 0:
        print("Saliendo del programa...")
        break
    
    columna_deseada = int(input("Ingrese el número de columna que desea ver: "))
    
    if not posicion_valida(fila_deseada, columna_deseada):
        print("La posición ingresada está fuera de los límites de la matriz. Inténtelo de nuevo.")
        continue
    
    contenido_posicion = matriz[fila_deseada][columna_deseada]
    print(f"El contenido en la posición ({fila_deseada}, {columna_deseada}) es: {contenido_posicion}")
