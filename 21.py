#Programa el cual permita ingresar los valores de temperatura de cada día durante una semana. Le programa debe calcular la temperatura promedio y luego mostrar los siguientes mensajes: a) Si el promedio es mayor a 35° mostrar el mensaje “Que semana tan calurosa” b) Si el promedio esta entre 15° y 35° mostrar el mensaje “Que clima tan delicioso” c) Si el promedio es menor de 15° mostrar el mensaje “Que semana tan fría”

temperaturas = []

for i in range(7):
    temperatura_dia = float(input(f"Ingrese la temperatura del día {i+1}: "))
    temperaturas.append(temperatura_dia)

temperatura_promedio = sum(temperaturas) / len(temperaturas)

if temperatura_promedio > 35:
    print("¡Que semana tan calurosa!")
elif 15 <= temperatura_promedio <= 35:
    print("¡Que clima tan delicioso!")
else:
    print("¡Que semana tan fría!")
