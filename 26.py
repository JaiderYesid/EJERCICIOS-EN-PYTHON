#Programa que permita ingresar un número cualquiera y luego mostrar el siguiente menú: 1. Determinar si es positivo o negativo 2. Determinar si es par o impar El programa debe realizar las operaciones que el usuario seleccione del menú

numero = int(input("Ingrese un número: "))

print("Seleccione una opción:")
print("1. Determinar si es positivo o negativo")
print("2. Determinar si es par o impar")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
elif opcion == 2:
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
else:
    print("Opción no válida. Por favor ingrese una opción válida (1 o 2).")
