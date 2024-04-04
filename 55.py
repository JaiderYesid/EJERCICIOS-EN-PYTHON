#Programa que permita llenar un vector de 20 posiciones y luego le pregunte al usuario cual posición desea ver en pantalla. 

numeros = []

for i in range(20):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

posicion_deseada = int(input("Ingrese la posición que desea ver en pantalla (1-20): "))

if 1 <= posicion_deseada <= 20:
    print(f"El número en la posición {posicion_deseada} es: {numeros[posicion_deseada-1]}")
else:
    print("Posición inválida. Debe ser un número entre 1 y 20.")
