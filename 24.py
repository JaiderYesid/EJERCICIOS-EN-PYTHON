#Programa que permita determinar si una letra es o no vocal

letra = input("Ingrese una letra: ")

letra = letra.lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("La letra ingresada es una vocal.")
else:
    print("La letra ingresada no es una vocal.")
