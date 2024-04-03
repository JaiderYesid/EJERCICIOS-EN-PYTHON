#Programa en el cual reciba como entradas la siguiente información: Código del Estudiante, Nombre del Estudiante, Nombre de la Materia y Tres Notas de 1.0 a 5.0. Con esta información el programa debe calcular la nota definitiva (promedio) y determinar si el estudiante aprueba o no la materia

codigo_estudiante = input("Ingrese el código del estudiante: ")
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
nombre_materia = input("Ingrese el nombre de la materia: ")
nota1 = float(input("Ingrese la primera nota (de 1.0 a 5.0): "))
nota2 = float(input("Ingrese la segunda nota (de 1.0 a 5.0): "))
nota3 = float(input("Ingrese la tercera nota (de 1.0 a 5.0): "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 3.0:
    resultado = "El estudiante ha aprobado la materia."
else:
    resultado = "El estudiante no ha aprobado la materia."

print("Código del Estudiante:", codigo_estudiante)
print("Nombre del Estudiante:", nombre_estudiante)
print("Materia:", nombre_materia)
print("Promedio:", promedio)
print(resultado)
