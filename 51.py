#Programa que permita almacenar 10 valores en un vector que represente las edades de 10 personas y luego muestre cada uno de los valores ingresados. 

edades = []

for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)

print("Las edades ingresadas son:")
for i in range(10):
    print(f"Persona {i+1}: {edades[i]}")
