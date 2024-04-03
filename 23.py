#Programa para determinar si un deportista es aceptado en el equipo de baloncesto de Bogotá. Las condiciones para ser aceptado son: a) La edad debe ser menor o igual a 18 años b) La estatura debe ser mayor a 180 cm c) El peso debe ser menor o igual a 80 kg. Si el aspirante cumple las 3 condiciones aceptarlo si no rechazarlo. 

edad = int(input("Ingrese la edad del aspirante: "))
estatura = float(input("Ingrese la estatura del aspirante en centímetros: "))
peso = float(input("Ingrese el peso del aspirante en kilogramos: "))

if edad <= 18 and estatura > 180 and peso <= 80:
    print("¡Felicidades! El aspirante es aceptado en el equipo de baloncesto de Bogotá.")
else:
    print("El aspirante no cumple con todas las condiciones para ser aceptado en el equipo de baloncesto de Bogotá.")
