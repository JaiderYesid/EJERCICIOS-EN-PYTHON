#Programa que permita ingresar N números y determine cuantas veces aparece el mismo número, dicho número a buscar debe solicitarse al usuario al inicio del programa.

cantidad_numeros = int(input("Ingrese la cantidad de números a ingresar: "))
numero_buscar = float(input("Ingrese el número a buscar: "))
contador = 0
repeticiones = 0

while contador < cantidad_numeros:
    numero = float(input("Ingrese un número: "))
    if numero == numero_buscar:
        repeticiones += 1
    contador += 1

print(f"El número {numero_buscar} aparece {repeticiones} veces en la lista de números ingresados.")
