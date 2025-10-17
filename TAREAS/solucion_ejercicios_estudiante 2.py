#!/usr/bin/env python3
"""
EJERCICIOS PARA ESTUDIANTES - MANEJO DE EXCEPCIONES
Resuelto por: [Tu nombre]
Descripción: Archivo completo con las soluciones y comentarios explicativos.
"""

# ===========================================================================
# Ejercicio 1: Encuentra y arregla el except desnudo
# ===========================================================================
print("\n--- EJERCICIO 1: ARREGLA EL EXCEPT DESNUDO ---")

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    Maneja errores específicos: división por cero y tipos no numéricos.
    """
    try:
        total = sum(numeros)
        promedio = total / len(numeros)
        return promedio
    except ZeroDivisionError:
        print("Error: la lista está vacía.")
        return None
    except TypeError:
        print("Error: todos los elementos deben ser numéricos.")
        return None

# Pruebas
print(calcular_promedio([1, 2, 3, 4, 5]))  
print(calcular_promedio([]))               
print(calcular_promedio([1, 2, 'a']))      


# ===========================================================================
# Ejercicio 2: Añade retroalimentación al usuario
# ===========================================================================
print("\n--- EJERCICIO 2: AÑADE RETROALIMENTACIÓN ---")

def guardar_datos(datos, archivo):
    """
    Guarda datos en un archivo, con manejo de errores y retroalimentación.
    """
    try:
        with open(archivo, 'w') as f:
            f.write(str(datos))
        print(f"Datos guardados correctamente en '{archivo}'.")
        return True
    except FileNotFoundError:
        print(f"Error: no se encontró la ruta del archivo '{archivo}'.")
    except PermissionError:
        print(f"Error: no tienes permisos para escribir en '{archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    return False

# Pruebas
guardar_datos({"usuario": "Ana"}, "datos.txt")
guardar_datos({"usuario": "Ana"}, "/ruta/invalida/datos.txt")


# ===========================================================================
# Ejercicio 3: Usa else y finally correctamente
# ===========================================================================
print("\n--- EJERCICIO 3: USA ELSE Y FINALLY ---")

def procesar_archivo(nombre_archivo):
    """
    Lee y procesa un archivo.
    Implementa try-except-else-finally.
    """
    try:
        f = open(nombre_archivo, 'r')
    except FileNotFoundError:
        print("Error: el archivo no existe.")
    else:
        contenido = f.read()
        print("Contenido leído correctamente:")
        print(contenido)
    finally:
        try:
            f.close()
            print("Archivo cerrado correctamente.")
        except:
            print("No se pudo cerrar el archivo.")

# Pruebas
with open("existente.txt", "w") as f:
    f.write("Hola mundo\nEjercicio 3 completado.")
procesar_archivo("existente.txt")
procesar_archivo("faltante.txt")


# ===========================================================================
# Ejercicio 4: Lanza excepciones apropiadas
# ===========================================================================
print("\n--- EJERCICIO 4: LANZA EXCEPCIONES ---")

def crear_usuario(nombre_usuario, edad, email):
    """
    Valida los datos de un usuario y lanza excepciones específicas.
    """
    if len(nombre_usuario) < 3:
        raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150.")
    if '@' not in email:
        raise ValueError("El email debe contener '@'.")
    
    print(f"Usuario {nombre_usuario} creado exitosamente.")
    return {"nombre": nombre_usuario, "edad": edad, "email": email}

# Pruebas
try:
    crear_usuario("Ana", 25, "ana@example.com")
    crear_usuario("Ab", 25, "ana@example.com")
except Exception as e:
    print(f"Error: {e}")


# ===========================================================================
# Ejercicio 5: Crea excepciones personalizadas
# ===========================================================================
print("\n--- EJERCICIO 5: EXCEPCIONES PERSONALIZADAS ---")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        super().__init__(f"Saldo insuficiente: necesitas ${monto}, tienes ${saldo}")

class MontoInvalidoError(Exception):
    pass

def retirar(saldo, monto):
    if monto <= 0:
        raise MontoInvalidoError("El monto debe ser positivo.")
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    nuevo_saldo = saldo - monto
    print(f"Retiro exitoso. Nuevo saldo: ${nuevo_saldo}")
    return nuevo_saldo

# Pruebas
retirar(100, 50)
try:
    retirar(100, 150)
except Exception as e:
    print(e)
try:
    retirar(100, -10)
except Exception as e:
    print(e)


# ===========================================================================
# Ejercicio 6: Maneja excepciones en bucles
# ===========================================================================
print("\n--- EJERCICIO 6: EXCEPCIONES EN BUCLES ---")

def procesar_lista_numeros(lista_strings):
    resultados = []
    errores = []
    for item in lista_strings:
        try:
            numero = int(item)
            resultados.append(numero * 2)
        except ValueError as e:
            errores.append((item, str(e)))
    return resultados, errores

# Pruebas
resultados, errores = procesar_lista_numeros(["1", "2", "abc", "4", "xyz"])
print(f"Exitosos: {resultados}")
print(f"Errores: {errores}")


# ===========================================================================
# Ejercicio 7: Re-lanza excepciones apropiadamente
# ===========================================================================
print("\n--- EJERCICIO 7: RE-LANZA EXCEPCIONES ---")

def operacion_critica(valor):
    try:
        resultado = 100 / int(valor)
        return resultado
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error durante operación crítica: {e}")
        raise  # Re-lanza la excepción

# Pruebas
print(operacion_critica("10"))
try:
    operacion_critica("0")
except ZeroDivisionError:
    print("Llamador: Manejo el error.")


# ===========================================================================
# Ejercicio 8: Excepción con múltiples except
# ===========================================================================
print("\n--- EJERCICIO 8: MÚLTIPLES EXCEPT ---")

def calculadora_segura(operacion, a, b):
    try:
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b
        elif operacion == "multiplicacion":
            return a * b
        elif operacion == "division":
            return a / b
        else:
            raise ValueError("Operación no válida.")
    except ZeroDivisionError:
        return "Error: división por cero."
    except TypeError:
        return "Error: los operandos deben ser numéricos."
    except ValueError as e:
        return f"Error: {e}"

# Pruebas
print(calculadora_segura("suma", 10, 5))
print(calculadora_segura("division", 10, 0))
print(calculadora_segura("suma", 10, "5"))
print(calculadora_segura("invalida", 10, 5))


# ===========================================================================
# Ejercicio 9: Contexto de excepción
# ===========================================================================
print("\n--- EJERCICIO 9: CONTEXTO DE EXCEPCIÓN ---")

import json

def parsear_configuracion(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError("Error al parsear configuración JSON.") from e

# Pruebas
print(parsear_configuracion('{"nombre": "Ana"}'))
try:
    parsear_configuracion('json invalido')
except ValueError as e:
    print(f"Error: {e}")
    print(f"Causado por: {e.__cause__}")


# ===========================================================================
# Ejercicio 10: Proyecto completo - Sistema de Inventario
# ===========================================================================
print("\n--- EJERCICIO 10: PROYECTO COMPLETO ---")

class ErrorInventario(Exception):
    pass

class ProductoNoEncontrado(ErrorInventario):
    pass

class StockInsuficiente(ErrorInventario):
    pass

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, codigo, nombre, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        if codigo in self.productos:
            raise KeyError("El código ya existe en el inventario.")
        self.productos[codigo] = {"nombre": nombre, "cantidad": cantidad}
        print(f"Producto '{nombre}' agregado con éxito.")

    def retirar_stock(self, codigo, cantidad):
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Producto {codigo} no encontrado.")
        if self.productos[codigo]["cantidad"] < cantidad:
            raise StockInsuficiente("No hay suficiente stock disponible.")
        self.productos[codigo]["cantidad"] -= cantidad
        print(f"Se retiraron {cantidad} unidades del producto '{self.productos[codigo]['nombre']}'.")

    def obtener_producto(self, codigo):
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Producto {codigo} no encontrado.")
        return self.productos[codigo]

# Pruebas
inventario = Inventario()
inventario.agregar_producto("001", "Laptop", 10)
print(inventario.obtener_producto("001"))
inventario.retirar_stock("001", 5)
try:
    inventario.retirar_stock("002", 5)
except Exception as e:
    print(e)


# ===========================================================================
# Reflexión Final
# ===========================================================================
print("\n" + "=" * 70)
print(" REFLEXIÓN FINAL ")
print("=" * 70 + "\n")
print("1. Las excepciones más frecuentes fueron ValueError y TypeError.")
print("2. Se crearon excepciones personalizadas cuando fue necesario representar errores del dominio (por ejemplo, en el sistema bancario y de inventario).")
print("3. El patrón try-except-else-finally fue muy útil para garantizar que los recursos se liberen correctamente.")
print("4. El manejo adecuado de excepciones mejora la experiencia del usuario al mostrar mensajes claros y evitar cierres inesperados.")
print("5. Se evitaron errores comunes como division por cero, tipos incorrectos y acceso a archivos inexistentes.")
print("\n" + "=" * 70)
print(" FIN DEL PROYECTO ")
print("=" * 70)
