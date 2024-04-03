# Programa para calcular la distancia recorrida en un movimiento rectilíneo. Recuerde que X = V*T

velocidad = float(input("Ingrese la velocidad (en m/s): "))
tiempo = float(input("Ingrese el tiempo (en segundos): "))

distancia_recorrida = velocidad * tiempo

print("La distancia recorrida es:", distancia_recorrida, "metros")
