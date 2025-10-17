print("Ejercicio 1.1 (5+3*2)")
print("Predicción: 11")
print("resultado real: (5+3*2) =", 5+3*2)
print("Explicación: La multiplicación tiene mayor precedencia que la suma,\npor lo que se realiza primero 3*2=6 y luego se suma 5+6=11")

print("Ejercicio 1.2 ((5+3)*2)")
print("Predicción: 16")
print("resultado real: ((5+3)*2) =", ((5+3)*2))
print("Explicación: El paréntesis tiene mayor precedencia que la multiplicación,\npor lo que se realiza primero 5+3=8 y luego se multiplica 8*2=16")

print("Ejercicio 1.3 (10/2), (10//2), (10%2)")
print("Predicción: 5.0, 5, 0")
print("resultado real:", (10/2), (10//2), (10%2))
print("Explicación: La división / da un resultado flotante, la división entera // da un resultado entero,\ny el módulo % da el resto de la división entera.")

print("Ejercicio 1.4 (2**3), (2^3)")
print("Predicción: 8, - ")
print("resultado real:", (2**3), (2^3))
print("Explicación: El operador ** es la potencia en Python, por lo que 2**3=8.\nEl operador ^ es el XOR bit a bit, no es una potencia.")

print("Ejercicio 1.5 (5--3), (-5*-3)")
print("Predicción: 8, 15 ")
print("resultado real:", (5--3), (-5*-3))
print("Explicación: El doble signo menos -- se interpreta como suma, por lo que 5--3=5+3=8.\nEl producto de dos números negativos es positivo, por lo que -5*-3=15.")

print("Ejercicio 2.1 (2 + 3 * 4 - 5)")
print("Predicción: 9")
print("resultado real: (2 + 3 * 4 - 5) =", (2 + 3 * 4 - 5))
print("Explicación: Primero se realiza la multiplicación 3*4=12,\nluego la suma 2+12=14 y finalmente la resta 14-5=9.")

print("Ejercicio 2.2 (20 / 4 * 2), (20 / (4 * 2))")
print("Predicción: 10.0, 2.5") 
print("resultado real: (20 / 4 * 2), (20 / (4 * 2)", (20 / 4 * 2), (20 / (4 * 2))) 
print("Explicación: En la primera expresión se realiza primero la división 20/4=5.0,\nluego la multiplicación 5.0*2=10.0.\nEn la segunda expresión se realiza primero la multiplicación 4*2=8,\nluego la división 20/8=2.5.")

print("Ejercicio 2.3 (17 % 5 + 2 * 3)")
print("Predicción: 8")
print("resultado real: (17 % 5 + 2 * 3) =", (17 % 5 + 2 * 3))
print("Explicación: Primero se calcula el módulo 17 % 5 = 2,\nluego la multiplicación 2 * 3 = 6 y finalmente la suma 2 + 6 = 8.")

print("Ejercicio 2.4 (2 ** 3 ** 2), ((2 ** 3) ** 2)")
print("Predicción: 512, 64")
print("resultado real:", (2 ** 3 ** 2), ((2 ** 3) ** 2))
print("Explicación: El operador ** se evalúa de derecha a izquierda.\nPor eso 2 ** 3 ** 2 = 2 ** (3 ** 2) = 2 ** 9 = 512.\nMientras que (2 ** 3) ** 2 = 8 ** 2 = 64.")

print("Ejercicio 2.5 (10 + 5 * 2 - 8 / 4 + 3)")
print("Predicción: 21.0")
print("resultado real: (10 + 5 * 2 - 8 / 4 + 3) =", (10 + 5 * 2 - 8 / 4 + 3))
print("Explicación: Primero 5*2=10 y 8/4=2.0,\nluego se evalúa de izquierda a derecha: 10+10=20, 20-2.0=18.0, 18.0+3=21.0.")

print("Ejercicio 3.1 - Cálculo de Impuestos")
price = 100
tax_rate = 0.15
total = price * (1 + tax_rate)
print("Predicción: 115.0")
print("resultado real:", total)
print("Explicación: Se multiplica el precio por 1.15 (100 * 1.15 = 115.0),\nlo que equivale a sumar el 15% de impuesto al precio base.")

print("Ejercicio 3.2 - Conversión de Temperatura")
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print("Predicción: 77.0")
print("resultado real:", fahrenheit)
print("Explicación: La fórmula para convertir °C a °F es (°C × 9/5) + 32.\nEntonces (25 * 9 / 5) + 32 = 45 + 32 = 77.0 °F.")

print("Ejercicio 3.3 - Promedio de Calificaciones")
grade1 = 85
grade2 = 90
grade3 = 78
average = (grade1 + grade2 + grade3) / 3
print("Predicción: 84.33")
print("resultado real:", average)
print("Explicación: Se suman las calificaciones y se dividen entre 3.\n(85 + 90 + 78) / 3 = 253 / 3 = 84.33 aproximadamente.")

print("Ejercicio 3.4 - Dividir Cuenta")
total_bill = 127.50
num_people = 4
per_person = total_bill / num_people
print("Predicción: 31.875")
print("resultado real:", per_person)
print("Explicación: Se divide el total entre el número de personas.\n127.50 / 4 = 31.875 (cada persona paga esa cantidad).")

print("Ejercicio 3.5 - Tiempo Restante")
total_minutes = 125
hours = total_minutes // 60
minutes = total_minutes % 60
print("Predicción: 2 horas y 5 minutos")
print("resultado real:", hours, "horas y", minutes, "minutos")
print("Explicación: La división entera // obtiene las horas completas (125 // 60 = 2),\ny el módulo % obtiene los minutos restantes (125 % 60 = 5).")

print("PROYECTO FINAL: CALCULADORA DE EXPRESIONES")

print("=== CALCULADORA DE EXPRESIONES ===")
print("Operadores: +, -, *, /, //, %, **")
print("Para salir, escribe 'salir'.")
print()

while True:
    expression = input("Ingresa una expresión: ")
    if expression.lower() == 'salir':
        print("¡Hasta luego!")
        break
    try:
        result = eval(expression)
        print("Resultado:", result)
        print("Tipo:", type(result).__name__)
    except ZeroDivisionError:
        print("Error: División por cero")
    except:
        print("Error: Expresión inválida")
    print()

print("=== DEBUGGING ===")

print("Debug 1: Promedio incorrecto")
a = 10
b = 20
c = 30
average = (a + b + c) / 3
print("Resultado correcto del promedio:", average)
print("Explicación: Se deben agrupar las tres sumas antes de dividir por 3,\npara evitar que solo el último número se divida.")

print("Debug 2: Descuento incorrecto")
price = 50
discount = 20
final = price * (1 - discount / 100)
print("Resultado correcto del precio con descuento:", final)
print("Explicación: Se calcula el precio multiplicando por (1 - 0.20),\nlo que da el 80% del valor original: 50 * 0.8 = 40.0.")
