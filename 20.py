#Programa para determinar si un número cualquiera ingresado por el usuario es par o impar.(Usar operación Modulo) 

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")
