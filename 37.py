#Realizar un Programa que permita visualizar en pantalla los múltiplos de 5 hasta el número 100.

print("Múltiplos de 5 hasta el número 100:")
for i in range(1, 101):
    if i % 5 == 0:
        print(i)
