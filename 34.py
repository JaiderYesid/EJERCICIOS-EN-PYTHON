#Programa que permita calcular la estatura promedio de un grupo de 18 estudiantes y luego tomar las siguientes decisiones: a) Si la estatura promedio es menor a 140 cm imprimir un mensaje que diga “Estudiantes muy bajos”. b) Si la estatura promedio se encuentra entre 140 y 170 cm imprimir “Estudiantes de estatura normal”. c) Si la estatura promedio es mayor de 170 cm imprimir “Estudiantes muy altos”.

suma_estaturas = 0

for i in range(1, 19):
    estatura = float(input(f"Ingrese la estatura del estudiante {i} en centímetros: "))
    suma_estaturas += estatura

estatura_promedio = suma_estaturas / 18

if estatura_promedio < 140:
    print("Estudiantes muy bajos.")
elif 140 <= estatura_promedio <= 170:
    print("Estudiantes de estatura normal.")
else:
    print("Estudiantes muy altos.")
