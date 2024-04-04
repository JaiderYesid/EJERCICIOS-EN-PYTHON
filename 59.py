#Programa que permita llenar un vector de N posiciones y luego en un segundo y tercer vector guarde el cuadrado y el cubo de cada una de las posiciones. Finalmente imprimir el contenido de todos los vectores. 

n = int(input("Ingrese la cantidad de posiciones para el vector: "))

vector_original = []

print("Llenado del vector:")
for i in range(n):
    numero = int(input(f"Ingrese el número {i+1}: "))
    vector_original.append(numero)

vector_cuadrado = [numero**2 for numero in vector_original]
vector_cubo = [numero**3 for numero in vector_original]

print("\nContenido del vector original:")
print(vector_original)

print("\nContenido del vector con cuadrados:")
print(vector_cuadrado)

print("\nContenido del vector con cubos:")
print(vector_cubo)
