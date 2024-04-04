#Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción Salir. Las opciones del menú deben permitir: 1. Calcular el factorial de un número (usando un ciclo repetitivo for) 2. Calcular la potencia (usando un ciclo repetitivo while) 3. Salir

while True:
    print("Menú:")
    print("1. Calcular el factorial de un número")
    print("2. Calcular la potencia")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero = int(input("Ingrese un número para calcular su factorial: "))
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es: {factorial}")
    elif opcion == "2":
        base = int(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        resultado = 1
        contador = 0
        while contador < exponente:
            resultado *= base
            contador += 1
        print(f"{base} elevado a la {exponente} es: {resultado}")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
