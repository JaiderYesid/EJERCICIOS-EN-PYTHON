#Programa que permita llenar dos vectores de 12 posiciones y luego en un tercer y cuarto vector guardar la suma y resta de cada posición. Al final se deben mostrar de forma completa todas las sumas y restas realizadas. 

vector1 = []
vector2 = []

print("Llenado del primer vector:")
for i in range(12):
    numero = int(input(f"Ingrese el número {i+1} para el primer vector: "))
    vector1.append(numero)

print("\nLlenado del segundo vector:")
for i in range(12):
    numero = int(input(f"Ingrese el número {i+1} para el segundo vector: "))
    vector2.append(numero)

suma_vector = []
resta_vector = []

for i in range(12):
    suma = vector1[i] + vector2[i]
    resta = vector1[i] - vector2[i]
    suma_vector.append(suma)
    resta_vector.append(resta)

print("\nSumas:")
for i in range(12):
    print(f"Suma en la posición {i+1}: {suma_vector[i]}")

print("\nRestas:")
for i in range(12):
    print(f"Resta en la posición {i+1}: {resta_vector[i]}")
