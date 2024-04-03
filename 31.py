mayores = 0

for i in range(1, 21):
    edad = int(input(f"Ingrese la edad del estudiante {i}: "))
    if edad >= 18:
        mayores += 1

print(f"En el grupo de 20 estudiantes, hay {mayores} mayores de edad.")
