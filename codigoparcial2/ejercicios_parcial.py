#!/usr/bin/env python3
"""
PARCIAL 2 - EJERCICIOS (Parte 1)
Estudiante: Jose Hidalgo
Fecha: 21/10/2025
"""

# ===========================================================================
# EJERCICIO 1: EXPRESIONES ARITMÉTICAS (10 puntos)
# ===========================================================================

def calculadora_cientifica(operacion, a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los operandos deben ser numéricos")
    
    operacion = operacion.lower()
    if operacion == "suma":
        resultado = a + b
    elif operacion == "resta":
        resultado = a - b
    elif operacion == "multiplicacion":
        resultado = a * b
    elif operacion == "division":
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        resultado = a / b
    elif operacion == "potencia":
        resultado = a ** b
    elif operacion == "modulo":
        if b == 0:
            raise ZeroDivisionError("No se puede calcular el módulo con divisor cero")
        resultado = a % b
    else:
        raise ValueError("Operación no válida")
    
    return round(resultado, 2)


# ===========================================================================
# EJERCICIO 2: EXPRESIONES LÓGICAS Y RELACIONALES (12 puntos)
# ===========================================================================

import string

class ValidadorPassword:
    def __init__(self, min_longitud=8, requiere_mayuscula=True,
                 requiere_minuscula=True, requiere_numero=True,
                 requiere_especial=True):
        self.min_longitud = min_longitud
        self.requiere_mayuscula = requiere_mayuscula
        self.requiere_minuscula = requiere_minuscula
        self.requiere_numero = requiere_numero
        self.requiere_especial = requiere_especial

    def validar(self, password):
        errores = []

        if len(password) < self.min_longitud:
            errores.append("Debe tener al menos {} caracteres".format(self.min_longitud))
        if self.requiere_mayuscula and not any(c.isupper() for c in password):
            errores.append("Debe tener al menos una letra mayúscula")
        if self.requiere_minuscula and not any(c.islower() for c in password):
            errores.append("Debe tener al menos una letra minúscula")
        if self.requiere_numero and not any(c.isdigit() for c in password):
            errores.append("Debe tener al menos un número")
        if self.requiere_especial and not any(c in string.punctuation for c in password):
            errores.append("Debe tener al menos un carácter especial")

        return (len(errores) == 0, errores)

    def es_fuerte(self, password):
        v = ValidadorPassword(min_longitud=12)
        valido, _ = v.validar(password)
        return valido


# ===========================================================================
# EJERCICIO 3: ESTRUCTURAS DE DATOS (15 puntos)
# ===========================================================================

class GestorInventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        if codigo in self.inventario:
            raise ValueError("El producto con ese código ya existe")
        self.inventario[codigo] = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad),
            "categoria": categoria
        }

    def actualizar_stock(self, codigo, cantidad_cambio):
        if codigo not in self.inventario:
            raise ValueError("Producto no encontrado")
        nuevo_stock = self.inventario[codigo]["cantidad"] + cantidad_cambio
        if nuevo_stock < 0:
            raise ValueError("Stock insuficiente")
        self.inventario[codigo]["cantidad"] = nuevo_stock

    def buscar_por_categoria(self, categoria):
        return [
            (cod, p["nombre"], p["precio"])
            for cod, p in self.inventario.items()
            if p["categoria"].lower() == categoria.lower()
        ]

    def productos_bajo_stock(self, limite=10):
        return {c: p["cantidad"] for c, p in self.inventario.items() if p["cantidad"] < limite}

    def valor_total_inventario(self):
        return round(sum(p["precio"] * p["cantidad"] for p in self.inventario.values()), 2)

    def top_productos(self, n=5):
        valores = [(c, p["precio"] * p["cantidad"]) for c, p in self.inventario.items()]
        valores.sort(key=lambda x: x[1], reverse=True)
        return valores[:n]


# ===========================================================================
# EJERCICIO 4: ESTRUCTURAS DE CONTROL (10 puntos)
# ===========================================================================

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes, anio):
    if mes < 1 or mes > 12:
        raise ValueError("Mes inválido (1-12)")
    dias_por_mes = [31, 29 if es_bisiesto(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dias_por_mes[mes - 1]

def generar_calendario(mes, anio, dia_inicio=0):
    dias = dias_en_mes(mes, anio)
    cabecera = "Lu Ma Mi Ju Vi Sa Do"
    resultado = [cabecera]
    linea = "   " * dia_inicio
    dia_semana = dia_inicio
    for d in range(1, dias + 1):
        linea += f"{d:2d} "
        dia_semana += 1
        if dia_semana == 7:
            resultado.append(linea.rstrip())
            linea = ""
            dia_semana = 0
    if linea:
        resultado.append(linea.rstrip())
    return "\n".join(resultado)


# ===========================================================================
# EJERCICIO 5: ESTRUCTURAS DE REPETICIÓN (13 puntos)
# ===========================================================================

def analizar_ventas(ventas):
    total = sum(v["cantidad"] * v["precio"] for v in ventas)
    total_descuentos = sum(v["cantidad"] * v["precio"] * v.get("descuento", 0) for v in ventas)
    promedio = round(total / len(ventas), 2) if ventas else 0
    producto_mas_vendido = max(ventas, key=lambda v: v["cantidad"])["producto"]
    venta_mayor = max(ventas, key=lambda v: v["cantidad"] * v["precio"])
    return {
        "total_ventas": round(total, 2),
        "promedio_por_venta": promedio,
        "producto_mas_vendido": producto_mas_vendido,
        "venta_mayor": venta_mayor,
        "total_descuentos": round(total_descuentos, 2)
    }

def encontrar_patrones(numeros):
    asc, desc = 0, 0
    max_asc, max_desc = 1, 1
    actual_asc, actual_desc = 1, 1
    repetidos = {}
    for i in range(1, len(numeros)):
        if numeros[i] > numeros[i-1]:
            actual_asc += 1
            max_asc = max(max_asc, actual_asc)
            if actual_desc > 1:
                desc += 1
                actual_desc = 1
        elif numeros[i] < numeros[i-1]:
            actual_desc += 1
            max_desc = max(max_desc, actual_desc)
            if actual_asc > 1:
                asc += 1
                actual_asc = 1
        else:
            actual_asc = actual_desc = 1
            repetidos[numeros[i]] = repetidos.get(numeros[i], 0) + 1
    return {
        "secuencias_ascendentes": asc,
        "secuencias_descendentes": desc,
        "longitud_max_ascendente": max_asc,
        "longitud_max_descendente": max_desc,
        "numeros_repetidos": repetidos
    }

def simular_crecimiento(principal, tasa_anual, anios, aporte_anual=0):
    resultado = []
    balance = principal
    for i in range(1, anios + 1):
        balance += aporte_anual
        interes = balance * tasa_anual
        balance += interes
        resultado.append({
            "anio": i,
            "balance": round(balance, 2),
            "interes_ganado": round(interes, 2)
        })
    return resultado


# ===========================================================================
# CASOS DE PRUEBA
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DE EJERCICIOS")
    print("="*70)

    print("\nEjercicio 1:")
    print(calculadora_cientifica("suma", 10, 5))
    print(calculadora_cientifica("division", 10, 2))

    print("\nEjercicio 2:")
    val = ValidadorPassword()
    print(val.validar("Abc123!"))
    print(val.validar("Abc123$xyz"))
    print(val.es_fuerte("Abcdef1234$XYZ"))

    print("\nEjercicio 3:")
    g = GestorInventario()
    g.agregar_producto("A1", "Lápiz", 500, 20, "Útiles")
    g.agregar_producto("B2", "Borrador", 300, 5, "Útiles")
    print(g.buscar_por_categoria("Útiles"))
    print(g.productos_bajo_stock(10))
    print(g.valor_total_inventario())

    print("\nEjercicio 4:")
    print(generar_calendario(2, 2024, 3))

    print("\nEjercicio 5:")
    ventas = [
        {"producto": "A", "cantidad": 3, "precio": 1000, "descuento": 0.1},
        {"producto": "B", "cantidad": 5, "precio": 500, "descuento": 0.05},
    ]
    print(analizar_ventas(ventas))
    print(encontrar_patrones([1, 2, 3, 2, 1, 4, 5, 6, 6, 7]))
    print(simular_crecimiento(1000, 0.05, 3, 100))
