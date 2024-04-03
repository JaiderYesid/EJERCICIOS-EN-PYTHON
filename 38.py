#Programa que permita determinar si un estudiante que recibe 15 notas gana o no la materia de Programación De Software. Se gana la materia si el promedio es mayor o igual a 4.0.

notas = []
for i in range(1, 16):
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota)

promedio = sum(notas) / 15

if promedio >= 4.0:
    print("El estudiante ha ganado la materia de Programación de Software.")
else:
    print("El estudiante no ha ganado la materia de Programación de Software.")
