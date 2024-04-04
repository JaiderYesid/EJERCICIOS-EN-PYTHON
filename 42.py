#Programa que permita obtener el cubo, la cuarta y la quinta potencia de N números ingresados por el usuario. 

cantidad_numeros = int(input("Ingrese la cantidad de números para calcular potencias: "))
contador = 0

while contador < cantidad_numeros:
    numero = float(input("Ingrese un número: "))
    cubo = numero ** 3
    cuarta_potencia = numero ** 4
    quinta_potencia = numero ** 5
    print(f"El cubo de {numero} es: {cubo}")
    print(f"La cuarta potencia de {numero} es: {cuarta_potencia}")
    print(f"La quinta potencia de {numero} es: {quinta_potencia}")
    contador += 1
