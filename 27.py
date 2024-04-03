#Programa que muestre un menú que tenga las siguientes opciones: 1. Pasa o no la materia? 2. Es mayor o menor de edad? Caso 1: Solicitar 3 notas y determinar si el promedio es mayor a 3.0, en ese caso el estudiante pasa. Caso 2: Se debe solicitar el año de nacimiento y el año actual y determinar si es o no mayor de edad.

print("Seleccione una opción:")
print("1. Pasa o no la materia?")
print("2. Es mayor o menor de edad?")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    
    promedio = (nota1 + nota2 + nota3) / 3
    
    if promedio > 3.0:
        print("El estudiante pasa la materia.")
    else:
        print("El estudiante no pasa la materia, debe esforzarse más.")

elif opcion == 2:
    año_nacimiento = int(input("Ingrese su año de nacimiento: "))
    año_actual = int(input("Ingrese el año actual: "))
    
    edad = año_actual - año_nacimiento
    
    if edad >= 18:
        print("La persona es mayor de edad.")
    else:
        print("La persona es menor de edad.")
        
else:
    print("Opción no válida. Por favor ingrese una opción válida (1 o 2).")
