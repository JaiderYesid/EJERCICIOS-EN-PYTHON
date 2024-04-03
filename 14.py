#Programa para saber si un estudiante del Enrique Olaya Herrera requiere refrigerio. Por disposición de la secretaria de Educación requieren refrigerio los estudiantes de grado sexto hacia abajo

grado = int(input("Ingrese el grado del estudiante: "))

if grado <= 6:
    print("El estudiante del grado", grado, "requiere refrigerio.")
else:
    print("El estudiante del grado", grado, "no requiere refrigerio.")
