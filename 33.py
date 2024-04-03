#Programa para calcular la edad promedio de un grupo de 15 estudiantes.

edades = 0

for i in range(1, 16):
    edad = int(input(f"Ingrese la edad del estudiante {i}: "))
    edades += edad

promedio = edades / 15

print(f"La edad promedio del grupo de 15 estudiantes es: {promedio}")
