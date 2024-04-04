#Programa que permita solicitar 25 nombres y 25 apellidos y los muestre en forma de un único listado

nombres = []
apellidos = []

print("Ingrese los nombres:")
for i in range(25):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)

print("\nIngrese los apellidos:")
for i in range(25):
    apellido = input(f"Ingrese el apellido {i+1}: ")
    apellidos.append(apellido)

print("\nListado de nombres y apellidos:")
for i in range(25):
    print(f"{nombres[i]} {apellidos[i]}")
