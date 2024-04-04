#Programa que permita calcular el factorial de un número. El factorial corresponde a la multiplicación de todos los números naturales anteriores incluyendo el número ingresado. 

numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1
contador = 1

if numero_ingresado < 0:
    print("El factorial de números negativos no está definido.")
elif numero_ingresado == 0:
    print("El factorial de 0 es 1.")
else:
    while contador <= numero_ingresado:
        factorial *= contador
        contador += 1
    print(f"El factorial de {numero_ingresado} es: {factorial}")
