#Programa que permita realizar los siguientes requerimientos: 1. Calcular distancia recorrida 2. Calcular tiempo 3. Calcular velocidad 

print("Seleccione una opción:")
print("1. Calcular distancia recorrida")
print("2. Calcular tiempo")
print("3. Calcular velocidad")

opcion = input("Ingrese el número de la opción deseada: ")

if opcion == '1':
    velocidad = float(input("Ingrese la velocidad (en m/s): "))
    tiempo = float(input("Ingrese el tiempo (en segundos): "))
    distancia = velocidad * tiempo
    print(f"La distancia recorrida es: {distancia} metros.")
elif opcion == '2':
    distancia = float(input("Ingrese la distancia recorrida (en metros): "))
    velocidad = float(input("Ingrese la velocidad (en m/s): "))
    tiempo = distancia / velocidad
    print(f"El tiempo transcurrido es: {tiempo} segundos.")
elif opcion == '3':
    distancia = float(input("Ingrese la distancia recorrida (en metros): "))
    tiempo = float(input("Ingrese el tiempo (en segundos): "))
    velocidad = distancia / tiempo
    print(f"La velocidad es: {velocidad} m/s.")
else:
    print("Opción no válida. Por favor ingrese una opción válida (1, 2 o 3).")
