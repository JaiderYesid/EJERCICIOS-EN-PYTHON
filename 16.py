#Programa en el cual se ingresen 2 números y luego realice las siguientes operaciones: a) Si los números son iguales restarlos b) Si los números son diferentes sumarlos

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 == numero2:
    resultado = numero1 - numero2
    print("Los números son iguales, la resta es:", resultado)
else:
    resultado = numero1 + numero2
    print("Los números son diferentes, la suma es:", resultado)
