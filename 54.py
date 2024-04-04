#Programa que permita llenar un vector de 20 posiciones y luego determine cuantos son positivos, cuántos son negativos y cuantos son ceros. 

numeros = []

for i in range(20):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

positivos = 0
negativos = 0
ceros = 0

for numero in numeros:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print(f"En el vector ingresado hay {positivos} números positivos, {negativos} números negativos y {ceros} ceros.")
