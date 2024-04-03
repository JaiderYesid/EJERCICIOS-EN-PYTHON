#Programa para determinar cuál es mayor entre 2 números cualquiera ingresados por el usuario

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print("El primer número ingresado es mayor que el segundo.")
elif numero2 > numero1:
    print("El segundo número ingresado es mayor que el primero.")
else:
    print("Ambos números son iguales.")
