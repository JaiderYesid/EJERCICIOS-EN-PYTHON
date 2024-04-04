#. Programa que reciba un listado de N números ingresados por el usuario y luego determine el número mayor y el número menor de entre todos los datos ingresados.

cantidad_numeros = int(input("Ingrese la cantidad de números a comparar: "))
contador = 0
numero_mayor = float("-inf")  
numero_menor = float("inf")  

while contador < cantidad_numeros:
    numero = float(input("Ingrese un número: "))
    if numero > numero_mayor:
        numero_mayor = numero
    if numero < numero_menor:
        numero_menor = numero
    contador += 1

print(f"El número mayor es: {numero_mayor}")
print(f"El número menor es: {numero_menor}")
