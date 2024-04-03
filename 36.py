#Programa que imprima la tabla de multiplicar hasta 10 de un número cualquiera ingresado por el usuario. 

numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
