# Taller de Operadores Lógicos


print("NIVEL 1: BÁSICO")
print("=" * 60)

# Ejercicio 1.1
print("\nEjercicio 1.1: Operadores Lógicos Básicos")
print("Predicción: False, True, False, True")
print("Resultado real:")
print(True and False)
print(True or False)
print(not True)
print(not False)
print("Explicación: Aplicación directa de las tablas de verdad.")
print("-" * 50)

# Ejercicio 1.2
print("\nEjercicio 1.2: Operadores Combinados")
a, b, c = True, False, True
print("Predicción: False, True, True, True")
print("Resultado real:")
print(a and b)
print(a or b)
print(b or c)
print(a and c)
print("Explicación: Evaluación directa de las combinaciones lógicas.")
print("-" * 50)

# Ejercicio 1.3
print("\nEjercicio 1.3: Precedencia de Operadores")
a, b, c = True, False, True
print("Predicción: True, True, False, False")
print("Resultado real:")
print(a and b or c)
print(a or b and c)
print(not a or b)
print(not (a or b))
print("Explicación: Se aplica el orden de precedencia: not > and > or.")
print("-" * 50)

# Ejercicio 1.4
print("\nEjercicio 1.4: Comparaciones y Lógica")
x = 5
print("Predicción: True, False, False")
print("Resultado real:")
print(x > 3 and x < 10)
print(x < 3 or x > 10)
print(not x > 3)
print("Explicación: Evaluación directa de comparaciones.")
print("-" * 50)

# Ejercicio 1.5
print("\nEjercicio 1.5: Comparaciones Encadenadas")
x = 5
print("Predicción: True, False, True")
print("Resultado real:")
print(3 < x < 10)
print(1 <= x <= 3)
print(10 > x > 3)
print("Explicación: Python permite comparar múltiples condiciones en una sola línea.")
print("-" * 50)

print("\nNIVEL 2: INTERMEDIO")
print("=" * 60)

# Ejercicio 2.1
print("\nEjercicio 2.1: Valores Retornados")
print("Predicción: 'mundo', '', '', 'hola', 'mundo'")
print("Resultado real:")
print("hola" and "mundo")
print("hola" and "")
print("" and "mundo")
print("hola" or "mundo")
print("" or "mundo")
print("Explicación: and devuelve el primer valor falsy o el último truthy; or devuelve el primero truthy.")
print("-" * 50)

# Ejercicio 2.2
print("\nEjercicio 2.2: Truthy y Falsy")
print("Predicción: False, False, False, True, True, False")
print("Resultado real:")
print(bool(0))
print(bool(""))
print(bool([]))
print(bool([0]))
print(bool(" "))
print(bool(None))
print("Explicación: 0, '', [], None son falsy. Otros son truthy.")
print("-" * 50)

# Ejercicio 2.3
print("\nEjercicio 2.3: Evaluación de Cortocircuito")
def f1():
    print("f1 ejecutada")
    return True
def f2():
    print("f2 ejecutada")
    return False

print("Predicción:")
print("Caso 1 → f1 ejecutada, f2 ejecutada, Resultado False")
print("Caso 2 → f2 ejecutada, Resultado False")
print("Caso 3 → f1 ejecutada, Resultado True")

print("\nResultado real:")
print("Caso 1:")
resultado = f1() and f2()
print(f"Resultado: {resultado}")

print("\nCaso 2:")
resultado = f2() and f1()
print(f"Resultado: {resultado}")

print("\nCaso 3:")
resultado = f1() or f2()
print(f"Resultado: {resultado}")

print("Explicación: Se aplica el cortocircuito: si el resultado se conoce, no se evalúan más funciones.")
print("-" * 50)

# Ejercicio 2.4
print("\nEjercicio 2.4: Operadores de Pertenencia")
nums = [1, 2, 3, 4, 5]
word = "Python"
print("Predicción: True, False, True, True, False, True")
print("Resultado real:")
print(3 in nums)
print(6 in nums)
print(6 not in nums)
print("P" in word)
print("p" in word)
print("th" in word)
print("Explicación: 'in' verifica existencia, 'not in' su ausencia, las cadenas son sensibles a mayúsculas.")
print("-" * 50)

# Ejercicio 2.5
print("\nEjercicio 2.5: Identidad vs Igualdad")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print("Predicción: True, False, True, True")
print("Resultado real:")
print(lista1 == lista2)
print(lista1 is lista2)
print(lista1 == lista3)
print(lista1 is lista3)
print("Explicación: == compara valores, 'is' compara referencias de memoria.")
print("-" * 50)

print("\nNIVEL 3: AVANZADO")
print("=" * 60)

# Ejercicio 3.1
print("\nEjercicio 3.1: Validación de Formulario")
def validar_datos(nombre, email, edad, password):
    return (nombre and 2 <= len(nombre) <= 30 and
            email and '@' in email and
            edad >= 18 and
            password and len(password) >= 8)
print("Predicción: True, False")
print("Resultado real:")
print(validar_datos("Ana", "ana@email.com", 25, "secreto123"))
print(validar_datos("", "no-email", 15, "123"))
print("Explicación: Se validan todas las condiciones con operadores lógicos.")
print("-" * 50)

# Ejercicio 3.2
print("\nEjercicio 3.2: Sistema de Autorización")
def puede_acceder(usuario, permiso_requerido, lista_negra):
    return (usuario["autenticado"] and
            (usuario["admin"] or permiso_requerido in usuario["permisos"]) and
            usuario["id"] not in lista_negra)

admin = {"id": 1, "autenticado": True, "admin": True, "permisos": ["leer", "escribir"]}
usuario_normal = {"id": 2, "autenticado": True, "admin": False, "permisos": ["leer"]}
usuario_bloqueado = {"id": 3, "autenticado": True, "admin": False, "permisos": ["leer", "escribir"]}
lista_negra = [3, 4]

print("Resultado real:")
print(puede_acceder(admin, "borrar", lista_negra))
print(puede_acceder(usuario_normal, "leer", lista_negra))
print(puede_acceder(usuario_normal, "escribir", lista_negra))
print(puede_acceder(usuario_bloqueado, "leer", lista_negra))
print("Explicación: Se aplican condiciones anidadas con and y or para control de acceso.")
print("-" * 50)

# Ejercicio 3.3
print("\nEjercicio 3.3: Acceso Seguro a Diccionario")
def obtener_valor_seguro(diccionario, clave, predeterminado=None):
    return diccionario[clave] if clave in diccionario else predeterminado
config = {"timeout": 30, "retries": 3}
print("Resultado real:")
print(obtener_valor_seguro(config, "timeout"))
print(obtener_valor_seguro(config, "cache"))
print(obtener_valor_seguro(config, "cache", 60))
print("Explicación: Se verifica la clave antes de acceder, evitando errores KeyError.")
print("-" * 50)

# Ejercicio 3.4
print("\nEjercicio 3.4: Filtrar Lista de Productos")
def filtrar_productos(productos, precio_min, precio_max, categoria=None):
    return [p for p in productos if precio_min <= p["precio"] <= precio_max and p["disponible"] and (categoria is None or p["categoria"] == categoria)]

productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica", "disponible": True},
    {"nombre": "Teléfono", "precio": 800, "categoria": "Electrónica", "disponible": False},
    {"nombre": "Libro", "precio": 15, "categoria": "Libros", "disponible": True},
    {"nombre": "Audífonos", "precio": 200, "categoria": "Electrónica", "disponible": True},
]
print("Resultado real:")
print(filtrar_productos(productos, 0, 500))
print(filtrar_productos(productos, 100, 1000, "Electrónica"))
print("Explicación: Se filtra la lista aplicando condiciones múltiples con operadores lógicos.")
print("-" * 50)

# Ejercicio 3.5
print("\nEjercicio 3.5: Evaluación de Riesgo Crediticio")
def evaluar_riesgo(cliente):
    return (cliente["score_crediticio"] > 700 or
            (cliente["ingreso_anual"] > 50000 and cliente["años_historial"] > 2) or
            (cliente["vip"] and not cliente["deudas_pendientes"]))

cliente1 = {"nombre": "Ana García", "score_crediticio": 720, "ingreso_anual": 45000, "años_historial": 3, "vip": False, "deudas_pendientes": False}
cliente2 = {"nombre": "Luis Pérez", "score_crediticio": 680, "ingreso_anual": 60000, "años_historial": 4, "vip": False, "deudas_pendientes": False}
cliente3 = {"nombre": "Carmen Ruiz", "score_crediticio": 690, "ingreso_anual": 30000, "años_historial": 1, "vip": True, "deudas_pendientes": False}

print("Resultado real:")
print(evaluar_riesgo(cliente1))
print(evaluar_riesgo(cliente2))
print(evaluar_riesgo(cliente3))
print("Explicación: Se aplican condiciones combinadas con or y and para determinar riesgo bajo.")
print("-" * 50)

print("\nPROYECTO FINAL: SISTEMA DE CONTROL DE ACCESO")
print("=" * 60)

usuarios = [
    {"id": 1, "nombre": "Admin", "roles": ["admin"], "permisos": ["leer", "escribir", "eliminar"], "plan": "premium", "activo": True, "edad": 35},
    {"id": 2, "nombre": "Usuario Regular", "roles": ["usuario"], "permisos": ["leer"], "plan": "basico", "activo": True, "edad": 17}
]

recursos = [
    {"id": 1, "nombre": "Panel Admin", "requiere_rol": ["admin"], "requiere_permiso": "eliminar", "solo_adultos": False},
    {"id": 2, "nombre": "Contenido Premium", "requiere_rol": ["usuario", "admin"], "requiere_permiso": "leer", "solo_premium": True, "solo_adultos": False},
    {"id": 3, "nombre": "Contenido para Adultos", "requiere_rol": ["usuario", "admin"], "requiere_permiso": "leer", "solo_premium": False, "solo_adultos": True}
]

def puede_acceder_recurso(usuario, recurso):
    if not usuario["activo"]:
        return False, "Usuario inactivo"
    if "requiere_rol" in recurso and not any(rol in recurso["requiere_rol"] for rol in usuario["roles"]):
        return False, f"Requiere rol {recurso['requiere_rol']}"
    if "requiere_permiso" in recurso and recurso["requiere_permiso"] not in usuario["permisos"]:
        return False, f"Falta permiso {recurso['requiere_permiso']}"
    if recurso.get("solo_premium", False) and usuario["plan"] != "premium":
        return False, "Requiere plan premium"
    if recurso.get("solo_adultos", False) and usuario["edad"] < 18:
        return False, "Solo para mayores de 18 años"
    return True, "Acceso permitido"

print("Resultado real:")
for usuario in usuarios:
    for recurso in recursos:
        acceso, motivo = puede_acceder_recurso(usuario, recurso)
        print(f"Usuario: {usuario['nombre']}, Recurso: {recurso['nombre']}, Acceso: {acceso}, Motivo: {motivo}")
print("-" * 50)

print("\nDEBUGGING")
print("=" * 60)

print("\nDebug 1: Verificación de Permisos")
def verificar_permisos(usuario, accion):
    return "permisos" in usuario and accion in usuario["permisos"]
usuario = {"id": 1, "nombre": "Juan"}
print(verificar_permisos(usuario, "leer"))
print("Explicación: Se evita KeyError verificando la existencia de la clave antes de acceder.")
print("-" * 50)

print("\nDebug 2: Filtrado de Estudiantes Aprobados")
estudiantes = [{"nombre": "Ana", "nota": 85}, {"nombre": "Luis", "nota": None}, {"nombre": "Carmen", "nota": 92}]
aprobados = [e for e in estudiantes if e["nota"] is not None and e["nota"] >= 60]
print(aprobados)
print("Explicación: Se evita TypeError al validar que la nota no sea None antes de comparar.")
print("-" * 50)
