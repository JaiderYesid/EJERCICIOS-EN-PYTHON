#Programa que permita llenar un vector de 18 posiciones y después mostrarlo al revés. 

numeros = []

for i in range(18):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print("El vector al revés es:")
for numero in reversed(numeros):
    print(numero)
