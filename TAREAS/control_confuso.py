#!/usr/bin/env python3
"""
ESTRUCTURAS DE CONTROL CONFUSAS 
"""

import os
import time

# ---------------------------------------------------------------------------
# FUNCIONES DE APOYO
# ---------------------------------------------------------------------------

def limpiar_pantalla():
    """Limpia la consola para mantener orden visual."""
    os.system('cls' if os.name == 'nt' else 'clear')


def esperar_enter(mensaje="Presiona Enter para continuar..."):
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input(f"\n{mensaje}")


def mostrar_titulo(texto):
    """Imprime un título principal centrado y enmarcado."""
    print("\n" + "=" * 70)
    print(texto.center(70))
    print("=" * 70 + "\n")


def mostrar_seccion(texto):
    """Imprime un subtítulo o encabezado de sección."""
    print("\n" + "-" * 50)
    print(texto)
    print("-" * 50)

# ---------------------------------------------------------------------------
# INICIO DEL PROGRAMA
# ---------------------------------------------------------------------------
limpiar_pantalla()
mostrar_titulo("ESTRUCTURAS DE CONTROL EN PYTHON - Sesión Interactiva")

print("¡Bienvenido! Este recorrido te ayudará a comprender errores frecuentes")
print("al usar bucles, condiciones y comprensiones en Python.")
esperar_enter()

# ===========================================================================
# EJERCICIO 1: MODIFICACIÓN DE UNA LISTA DURANTE ITERACIÓN
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 1: MODIFICACIÓN DURANTE ITERACIÓN")

mostrar_seccion("📝 CÓDIGO ANALIZADO")
print("""
numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")

# Intento de eliminar números pares durante la iteración
for numero in numeros:
    if numero % 2 == 0:
        numeros.remove(numero)

print(f"Lista después del bucle: {numeros}")
""")

mostrar_seccion("🤔 PREDICCIÓN")
print("¿Qué crees que ocurrirá? ¿Se eliminarán todos los pares?")
esperar_enter("Presiona Enter cuando tengas una hipótesis...")

# Código problemático a propósito
numeros = [1, 2, 3, 4, 5]
print(f"\n✅ Lista original: {numeros}")

for numero in numeros:
    if numero % 2 == 0:
        numeros.remove(numero)

print(f"Lista después del bucle: {numeros}")

mostrar_seccion("📘 REFLEXIÓN")
print("🔹 Al eliminar elementos mientras iteramos, la lista se 'mueve' internamente.")
print("🔹 Por eso, algunos elementos se saltan y no son revisados.")
print("✅ Solución: crear una nueva lista o usar comprensión de listas.")
esperar_enter()

# Enfoque correcto
numeros = [1, 2, 3, 4, 5]
numeros_filtrados = [num for num in numeros if num % 2 != 0]
print(f"Resultado correcto: {numeros_filtrados}")
esperar_enter()

# ===========================================================================
# EJERCICIO 2: CONFUSIÓN CON range()
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 2: CONFUSIÓN CON range()")

print("""
# Se desea imprimir los números del 1 al 10
for i in range(10):
    print(i, end=" ")

for i in range(1, 10):
    print(i, end=" ")
""")
esperar_enter("¿Qué diferencias habrá entre los dos bucles?")

# Ejecución real
print("\n✅ RESULTADO REAL:")
print("range(10): ", list(range(10)))
print("range(1, 10): ", list(range(1, 10)))

print("\n📘 REFLEXIÓN:")
print("range(inicio, fin) excluye el valor final.")
print("Por eso, range(1, 11) imprime del 1 al 10.")
esperar_enter()

# ===========================================================================
# EJERCICIO 3: BUCLE WHILE INFINITO
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 3: BUCLE WHILE INFINITO")

print("""
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    # Falta contador += 1
""")
esperar_enter("¿Qué ocurriría al ejecutar este código?")

print("\n⚠️ Resultado: el programa quedaría atrapado en un bucle infinito.")
print("💡 Solución: actualizar la variable de control en cada iteración.")
esperar_enter()

# Versión corregida
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1
esperar_enter()

# ===========================================================================
# EJERCICIO 4: BREAK vs CONTINUE
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 4: BREAK VS CONTINUE")

print("""
# break termina el bucle.
# continue salta la iteración actual.
""")
esperar_enter()

print("Ejemplo con break:")
for i in range(1, 10):
    if i == 5:
        print(f"Encontré el {i}, saliendo del bucle.")
        break
    print(f"Procesando {i}")

print("\nEjemplo con continue:")
for i in range(1, 10):
    if i == 5:
        print(f"Encontré el {i}, saltando iteración.")
        continue
    print(f"Procesando {i}")

print("\n📘 REFLEXIÓN:")
print("🔹 break interrumpe completamente el ciclo actual.")
print("🔹 continue solo omite la iteración actual y sigue con la siguiente.")
esperar_enter()

# ===========================================================================
# EJERCICIO 5: BUCLES ANIDADOS Y BREAK
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 5: BUCLES ANIDADOS Y BREAK")

print("Cuando usamos break dentro de un bucle anidado, solo sale del bucle más interno.\n")

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
objetivo = 6
encontrado = False

for fila in matriz:
    for elemento in fila:
        print(f"Verificando: {elemento}")
        if elemento == objetivo:
            print(f"¡Encontrado {objetivo}!")
            encontrado = True
            break
    print("Fin de la fila")

print(f"Encontrado: {encontrado}")
esperar_enter()

print("✅ Para salir de ambos bucles, se puede usar una bandera o return dentro de una función.")
esperar_enter()

# ===========================================================================
# EJERCICIO 6: COMPRENSIONES VS BUCLES
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 6: COMPRENSIONES DE LISTA")

print("Compararemos bucles tradicionales con comprensiones de lista.\n")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Método 1: bucle tradicional
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n ** 2)
print(f"Método tradicional → {pares}")

# Método 2: comprensión
pares_comp = [n ** 2 for n in numeros if n % 2 == 0]
print(f"Comprensión de lista → {pares_comp}")

print("\n📘 REFLEXIÓN:")
print("✅ Ambas formas son equivalentes, pero las comprensiones son más compactas.")
print("⚙️ Se recomienda usarlas cuando la lógica sea simple y clara.")
esperar_enter()

# ===========================================================================
# CONCLUSIÓN
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("CONCLUSIÓN FINAL")

print("""
Has aprendido sobre:
1️⃣ Iteraciones seguras y modificación de listas.
2️⃣ El funcionamiento de range() y sus parámetros.
3️⃣ Cómo evitar bucles infinitos con while.
4️⃣ Las diferencias prácticas entre break y continue.
5️⃣ El alcance de break en bucles anidados.
6️⃣ Comprensiones de lista como alternativa elegante.

✅ Recuerda: el código claro es más valioso que el código corto.
""")

esperar_enter("Presiona Enter para salir...")
limpiar_pantalla()
print("¡Gracias por participar en esta sesión interactiva!")
print("Fin del programa.")
