#Programa para determinar si un número cualquiera ingresado por el usuario es o no positivo

numero = int(input("Ingrese un número: "))

if numero > 0:
    print("El número ingresado es positivo.")
elif numero == 0:
    print("El número ingresado es cero, no es ni positivo ni negativo.")
else:
    print("El número ingresado es negativo.")
