#Programa que permita sumar todos los valores ingresados en un vector de 12 posiciones, los valores deben ser ingresados por el usuario.

vector = []

for i in range(12):
    valor = float(input(f"Ingrese el valor para la posición {i + 1}: "))
    vector.append(valor)

total = sum(vector)
print(f"La suma de todos los valores ingresados es: {total}")
