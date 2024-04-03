#Programa que permita determinar cuántos hombres y mujeres hay en un curso de 25 estudiantes.

hombres = 0
mujeres = 0

for i in range(1, 26):
    genero = input(f"Ingrese el género del estudiante {i} (Hombre/Mujer): ")
    if genero.lower() == "hombre":
        hombres += 1
    elif genero.lower() == "mujer":
        mujeres += 1
    else:
        print("Género no válido. Por favor ingrese 'Hombre' o 'Mujer'.")

print(f"En el curso de 25 estudiantes, hay {hombres} hombres y {mujeres} mujeres.")
