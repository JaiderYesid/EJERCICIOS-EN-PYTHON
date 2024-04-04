#Programa que permita solicitar 15 nombres, almacenarlos en un vector y luego los muestre en el orden ingresado. 

nombres = []

for i in range(15):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    nombres.append(nombre)

print("Los nombres ingresados son:")
for nombre in nombres:
    print(nombre)
