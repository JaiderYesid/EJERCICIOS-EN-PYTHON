#Programa para determinar la mitad de un número ingresado por el usuario es mayor o menor de 100

numero = float(input("Ingrese un número: "))

mitad = numero / 2

if mitad > 100:
    print("La mitad del número ingresado es mayor que 100.")
elif mitad < 100:
    print("La mitad del número ingresado es menor que 100.")
else:
    print("La mitad del número ingresado es igual a 100.")
