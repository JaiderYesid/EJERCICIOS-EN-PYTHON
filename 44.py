#Programa que reciba N calificaciones de una materia, y luego calcule: a) La nota promedio b) La nota mayor c) Si El estudiante pasa o no la materia (Promedio>=4.0) 

cantidad_calificaciones = int(input("Ingrese la cantidad de calificaciones: "))
calificaciones = []
contador = 0

while contador < cantidad_calificaciones:
    calificacion = float(input(f"Ingrese la calificación {contador+1}: "))
    calificaciones.append(calificacion)
    contador += 1

suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / cantidad_calificaciones

nota_mayor = max(calificaciones)

if promedio >= 4.0:
    pasa_materia = "Sí"
else:
    pasa_materia = "No"

print(f"El promedio de las calificaciones es: {promedio}")
print(f"La nota más alta es: {nota_mayor}")
print(f"El estudiante {'pasa' if pasa_materia == 'Sí' else 'no pasa'} la materia.")
