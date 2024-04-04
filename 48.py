#Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción salir. Las opciones del menú deben permitir: 1. Ingresar 2 números 2. Realizar la suma 3. Realizar la resta 4. Realizar la multiplicación 5. Realizar la división 6. Salir del programa

while True:
    print("Menú:")
    print("1. Ingresar 2 números")
    print("2. Realizar la suma")
    print("3. Realizar la resta")
    print("4. Realizar la multiplicación")
    print("5. Realizar la división")
    print("6. Salir del programa")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        print("Números ingresados:", numero1, "y", numero2)
    elif opcion == "2":
        suma = numero1 + numero2
        print("La suma es:", suma)
    elif opcion == "3":
        resta = numero1 - numero2
        print("La resta es:", resta)
    elif opcion == "4":
        multiplicacion = numero1 * numero2
        print("La multiplicación es:", multiplicacion)
    elif opcion == "5":
        if numero2 != 0:
            division = numero1 / numero2
            print("La división es:", division)
        else:
            print("Error: No se puede dividir por cero.")
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
