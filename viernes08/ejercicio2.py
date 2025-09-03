# Leer K y M
K, M = map(int, input().split())

# Leer las listas
listas = []
for _ in range(K):
    datos = list(map(int, input().split()))
    listas.append(datos[1:])  # ignoramos el número Ni

# Función para elevar al cuadrado
def f(x):
    return x * x

# Empezamos con una lista vacía de combinaciones parciales
combinaciones = [[]]

# Vamos añadiendo una lista a la vez
for lista in listas:
    nuevas_combinaciones = []
    for combinacion in combinaciones:
        for num in lista:
            nuevas_combinaciones.append(combinacion + [num])
    combinaciones = nuevas_combinaciones

# Revisamos todas las combinaciones y buscamos el máximo
max_val = 0
for comb in combinaciones:
    suma = 0
    for x in comb:
        suma += f(x)
    suma %= M
    if suma > max_val:
        max_val = suma

# Imprimir resultado
print(max_val)
