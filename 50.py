#Programa que muestre un menú al usuario que se repita las veces que sea necesario, hasta que escoja la opción Salir. Las opciones del menú deben permitir: 1. Números pares hasta 100 (usando for) 2. Múltiplos de 4 (usando while) 3. Tabla de Multiplicar de un número hasta 10 

while True:
    print("Menú:")
    print("1. Mostrar números pares hasta 100")
    print("2. Mostrar múltiplos de 4")
    print("3. Mostrar tabla de multiplicar de un número")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Números pares hasta 100:")
        for i in range(2, 101, 2):
            print(i, end=" ")
    elif opcion == "2":
        print("Múltiplos de 4:")
        contador = 1
        while contador * 4 <= 100:
            print(contador * 4, end=" ")
            contador += 1
    elif opcion == "3":
        numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
        print(f"Tabla de multiplicar del {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    elif opcion.lower() == "salir":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
