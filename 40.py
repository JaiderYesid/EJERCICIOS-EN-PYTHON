#Programa que calcule la suma de los N primeros números naturales, donde N es un número digitado por el usuario.

N = int(input("Ingresa un número para calcular la suma de los primeros números naturales: "))

suma = 0
contador = 1

while contador <= N:
    suma += contador
    contador += 1

print(f"La suma de los {N} primeros números naturales es: {suma}")
