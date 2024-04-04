#Crear un Programa que permita conocer la mayor estatura dentro un grupo de N estudiantes.

cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
estaturas = []

# Ingresar las estaturas de los estudiantes
contador = 0
while contador < cantidad_estudiantes:
    estatura = int(input(f"Ingrese la estatura del estudiante {contador + 1} en centimetros: "))
    estaturas.append(estatura)
    contador += 1

# Encontrar la mayor estatura
mayor_estatura = estaturas[0]
indice = 1
while indice < len(estaturas):
    if estaturas[indice] > mayor_estatura:
        mayor_estatura = estaturas[indice]
    indice += 1

print(f"La mayor estatura dentro del grupo es: {mayor_estatura} metros.")
