#Programa que determine si una persona es mayor de edad o no teniendo en cuenta el año actual y su año de nacimiento

año_actual = int(input("Ingrese el año actual: "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))

edad = año_actual - año_nacimiento

if edad >= 18:
    print("La persona es mayor de edad.")
else:
    print("La persona es menor de edad.")
