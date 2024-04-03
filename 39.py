#Programa que encuentre el resultado de la operación potencia donde el usuario ingresa el valor de la base y el exponente. 

base = int(input("Ingresa el valor de la base: "))
exponente = int(input("Ingresa el valor del exponente: "))

resultado = 1
contador = 0

while contador < exponente:
    resultado *= base
    contador += 1

print(f"El resultado de {base} elevado a la {exponente} es: {resultado}")
