#Programa que permita Ingresar el número de estudiantes asignados cada uno de los 20 salones de un colegio y luego satisfacer los siguientes requerimientos: a) Determinar la cantidad total de estudiantes b) Determinar el curso con mayor cantidad de estudiantes c) Determinar el curso con menor cantidad de estudiantes

estudiantes_por_salon = []

for i in range(20):
    estudiantes = int(input(f"Ingrese la cantidad de estudiantes para el salón {i+1}: "))
    estudiantes_por_salon.append(estudiantes)

total_estudiantes = sum(estudiantes_por_salon)

max_estudiantes = max(estudiantes_por_salon)
curso_max_estudiantes = estudiantes_por_salon.index(max_estudiantes) + 1

min_estudiantes = min(estudiantes_por_salon)
curso_min_estudiantes = estudiantes_por_salon.index(min_estudiantes) + 1

print(f"La cantidad total de estudiantes es: {total_estudiantes}")
print(f"El curso con mayor cantidad de estudiantes es el salón {curso_max_estudiantes} con {max_estudiantes} estudiantes")
print(f"El curso con menor cantidad de estudiantes es el salón {curso_min_estudiantes} con {min_estudiantes} estudiantes")
