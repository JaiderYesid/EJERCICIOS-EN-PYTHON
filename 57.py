#Programa que permita calcular la cantidad total de clientes que atienden en un mes un hotel utilizando un vector. Como entrada se debe solicitar el número de clientes que atiende el hotel cada día del mes. 

clientes_por_dia = []

for dia in range(1, 31):  
    clientes = int(input(f"Ingrese el número de clientes atendidos en el día {dia}: "))
    clientes_por_dia.append(clientes)

total_clientes = sum(clientes_por_dia)

print(f"La cantidad total de clientes atendidos en el mes es: {total_clientes}")
