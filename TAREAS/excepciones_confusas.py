#!/usr/bin/env python3
"""
MANEJO DE EXCEPCIONES - EJEMPLOS CONFUSOS - Versión Interactiva
Este código demuestra errores y confusiones comunes con el manejo de excepciones en Python.
Los estudiantes pueden interactuar con cada ejemplo, predecir resultados y aprender activamente.
"""

import os
import time

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter():
    """Espera a que el usuario presione Enter para continuar"""
    input("\nPresiona Enter para continuar...")

def imprimir_encabezado_seccion(titulo):
    """Imprime un encabezado de sección formateado"""
    print("\n" + "=" * 70)
    print(f" {titulo}")
    print("=" * 70 + "\n")

# ===========================================================================
# Problema 1: Capturar todo con except desnudo
# ===========================================================================
def problema_bare_except():
    """Demuestra el problema con cláusulas except desnudas"""
    limpiar_pantalla()
    imprimir_encabezado_seccion("PROBLEMA 1: Capturando Todo con Except Desnudo")
    
    print("¿Qué está mal con este código?")
    print("-" * 50)
    print("""
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except:  # ¡Captura TODO, incluso KeyboardInterrupt!
        print("Ocurrió un error")
        return None

# ¿Qué pasa si el usuario presiona Ctrl+C?
# ¿Qué pasa si hay un error de tipeo en el nombre de la variable?
# ¡Nunca sabremos qué salió mal!
    """)
    
    print("\nVeamos qué sucede:")
    
    def dividir_malo(a, b):
        try:
            resultado = a / b
            return resultado
        except:
            print("Ocurrió un error")
            return None
    
    print("\nPrueba 1: dividir_malo(10, 2)")
    resultado = dividir_malo(10, 2)
    print(f"Resultado: {resultado}")
    
    print("\nPrueba 2: dividir_malo(10, 0)")
    resultado = dividir_malo(10, 0)
    print(f"Resultado: {resultado}")
    
    print("\n❌ PROBLEMAS:")
    print("- No sabemos QUÉ error ocurrió")
    print("- Captura salidas del sistema e interrupciones de teclado")
    print("- Hace la depuración muy difícil")
    print("- Oculta bugs en el código")
    
    print("\n🤔 PREGUNTAS PARA PENSAR:")
    print("1. ¿Cómo sabrías qué salió mal en producción?")
    print("2. ¿Qué pasa si hay un error de tipeo en 'resultado'?")
    print("3. ¿Cómo afecta esto a la depuración?")
    
    esperar_enter()

# ===========================================================================
# Problema 2: Capturar demasiado ampliamente
# ===========================================================================
def problema_except_amplio():
    """Demuestra el problema de capturar Exception demasiado ampliamente"""
    limpiar_pantalla()
    imprimir_encabezado_seccion("PROBLEMA 2: Capturando Demasiado Ampliamente")
    
    print("¿Cuál es el problema aquí?")
    print("-" * 50)
    print("""
def procesar_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo, 'r')
        datos = archivo.read()
        archivo.close()
        
        # Procesar datos
        numeros = [int(x) for x in datos.split()]
        promedio = sum(numeros) / len(numeros)
        
        return promedio
    except Exception as e:  # ¡Demasiado amplio!
        print(f"Error: {e}")
        return None

# ¿Qué errores puede ocultar esto?
# ¿Es apropiado capturar TODOS los errores así?
    """)
    
    print("\nVeamos el problema:")
    
    def procesar_archivo_malo(nombre_archivo, datos):
        try:
            # Simulamos diferentes operaciones
            numeros = [int(x) for x in datos.split()]
            promedio = sum(numeros) / len(numeros)
            return promedio
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    print("\nPrueba 1: Datos válidos")
    resultado = procesar_archivo_malo("test.txt", "10 20 30")
    print(f"Resultado: {resultado}")
    
    print("\nPrueba 2: Datos inválidos")
    resultado = procesar_archivo_malo("test.txt", "10 abc 30")
    print(f"Resultado: {resultado}")
    
    print("\nPrueba 3: Lista vacía")
    resultado = procesar_archivo_malo("test.txt", "")
    print(f"Resultado: {resultado}")
    
    print("\n❌ PROBLEMAS:")
    print("- Trata TODOS los errores de la misma manera")
    print("- No distingue entre errores de archivo y errores de datos")
    print("- Podría capturar errores que NO deberías capturar")
    print("- Dificulta identificar la causa real del problema")
    
    print("\n🤔 PREGUNTAS PARA PENSAR:")
    print("1. ¿Qué tipos específicos de errores pueden ocurrir?")
    print("2. ¿Deberían manejarse todos de la misma manera?")
    print("3. ¿Qué información se pierde al capturar todo?")
    
    esperar_enter()

# ===========================================================================
# Problema 3: Ignorar errores silenciosamente
# ===========================================================================
def problema_ignorar_errores():
    """Demuestra el peligro de ignorar errores silenciosamente"""
    limpiar_pantalla()
    imprimir_encabezado_seccion("PROBLEMA 3: Ignorando Errores Silenciosamente")
    
    print("¿Qué hay de malo con este patrón?")
    print("-" * 50)
    print("""
def guardar_configuracion(config):
    try:
        with open('config.txt', 'w') as archivo:
            archivo.write(str(config))
    except:
        pass  # ¡El usuario no sabe que falló!

# ¿El usuario sabe si guardó correctamente?
# ¿Cómo depurarías esto si falla?
    """)
    
    print("\nSimulemos el escenario:")
    
    def guardar_config_malo(config, simular_error=False):
        try:
            if simular_error:
                raise IOError("No hay permisos de escritura")
            print(f"  [Guardando] {config}")
            return True
        except:
            pass  # Silencioso
    
    print("\nPrueba 1: Guardado exitoso")
    guardar_config_malo({"tema": "oscuro"}, False)
    print("¿Se guardó? No hay forma de saberlo...")
    
    print("\nPrueba 2: Guardado fallido")
    guardar_config_malo({"tema": "oscuro"}, True)
    print("¿Se guardó? No hay forma de saberlo...")
    
    print("\n❌ PROBLEMAS:")
    print("- El usuario no recibe ningún feedback")
    print("- Imposible depurar cuando falla")
    print("- Datos pueden perderse sin que nadie lo sepa")
    print("- Viola el principio de 'fail fast'")
    
    print("\n🤔 PREGUNTAS PARA PENSAR:")
    print("1. ¿Qué debería suceder cuando falla el guardado?")
    print("2. ¿Cómo informarías al usuario?")
    print("3. ¿Es este error algo que deberías manejar?")
    
    esperar_enter()

# ===========================================================================
# Problema 4: Confusión con else y finally
# ===========================================================================
def problema_else_finally():
    """Demuestra confusión común con else y finally"""
    limpiar_pantalla()
    imprimir_encabezado_seccion("PROBLEMA 4: Confusión con Else y Finally")
    
    print("¿Cuándo se ejecuta cada bloque?")
    print("-" * 50)
    print("""
def operacion_confusa(tiene_error):
    try:
        if tiene_error:
            raise ValueError("Error simulado")
        print("Operación exitosa")
    except ValueError:
        print("Manejando error")
    else:
        print("Esto se ejecuta...")  # ¿Cuándo?
    finally:
        print("Esto siempre se ejecuta...")  # ¿Cuándo?
    """)
    
    print("\nVeamos la ejecución:")
    
    def operacion_confusa(tiene_error):
        print(f"\n[Ejecutando con tiene_error={tiene_error}]")
        try:
            print("  1. En el bloque try")
            if tiene_error:
                raise ValueError("Error simulado")
            print("  2. Try completado sin error")
        except ValueError:
            print("  2. En el bloque except")
        else:
            print("  3. En el bloque else")
        finally:
            print("  4. En el bloque finally")
    
    print("\nCaso 1: Sin error")
    operacion_confusa(False)
    
    print("\nCaso 2: Con error")
    operacion_confusa(True)
    
    print("\n❌ CONFUSIONES COMUNES:")
    print("- Pensar que else siempre se ejecuta")
    print("- No entender cuándo usar else vs finally")
    print("- Poner código en el lugar equivocado")
    print("- No saber que finally se ejecuta incluso con return")
    
    print("\n🤔 PREGUNTAS PARA PENSAR:")
    print("1. ¿En qué se diferencia else de finally?")
    print("2. ¿Cuándo usarías cada uno?")
    print("3. ¿Qué pasa si hay un return en try?")
    
    esperar_enter()

# ===========================================================================
# Problema 5: Uso incorrecto de raise
# ===========================================================================
def problema_raise_incorrecto():
    """Demuestra errores comunes al usar raise"""
    limpiar_pantalla()
    imprimir_encabezado_seccion("PROBLEMA 5: Uso Incorrecto de Raise")
    
    print("¿Qué está mal con estos usos de raise?")
    print("-" * 50)
    print("""
# Problema A: Raise genérico
def validar_edad(edad):
    if edad < 0:
        raise Exception("Edad inválida")  # ¡Demasiado genérico!

# Problema B: Mensaje no informativo
def dividir(a, b):
    if b == 0:
        raise ValueError("Error")  # ¡No dice qué está mal!

# Problema C: Tipo de excepción incorrecto
def abrir_archivo(nombre):
    if not nombre:
        raise ValueError("Nombre vacío")  # ¿ValueError?
    """)
    
    print("\nVeamos los problemas:")
    
    print("\nProblema A: Excepción demasiado genérica")
    try:
        raise Exception("Algo salió mal")
    except Exception as e:
        print(f"  Capturado: {type(e).__name__}: {e}")
        print("  ¿Qué tipo de error es? ¡No lo sabemos!")
    
    print("\nProblema B: Mensaje no informativo")
    try:
        raise ValueError("Error")
    except ValueError as e:
        print(f"  Capturado: {e}")
        print("  ¿Qué valor está mal? ¿Por qué? ¡No ayuda!")
    
    print("\nProblema C: Tipo incorrecto")
    try:
        nombre = ""
        if not nombre:
            raise ValueError("Nombre vacío")
    except ValueError as e:
        print(f"  Capturado: {e}")
        print("  ¿ValueError es el tipo correcto para esto?")
    
    print("\n❌ PROBLEMAS:")
    print("- Excepciones genéricas no ayudan a los llamadores")
    print("- Mensajes vagos dificultan la depuración")
    print("- Tipos incorrectos confunden el propósito del error")
    print("- No proporciona información útil para solucionar")
    
    print("\n🤔 PREGUNTAS PARA PENSAR:")
    print("1. ¿Qué tipo de excepción sería más apropiado?")
    print("2. ¿Qué información debería incluir el mensaje?")
    print("3. ¿Cómo ayuda esto a quien llama la función?")
    
    esperar_enter()

# ===========================================================================
# Problema 6: No re-lanzar excepciones apropiadamente
# ===========================================================================
def problema_no_relanzar():
    """Demuestra cuándo y cómo re-lanzar excepciones"""
    limpiar_pantalla()
    imprimir_encabezado_seccion("PROBLEMA 6: No Re-lanzar Apropiadamente")
    
    print("¿Deberías siempre capturar y consumir errores?")
    print("-" * 50)
    print("""
def operacion_interna():
    try:
        # Operación crítica
        resultado = procesar_datos_criticos()
        return resultado
    except Exception as e:
        print(f"Error interno: {e}")
        return None  # ¿Es correcto ocultar el error?

# ¿Qué pasa si el llamador necesita saber que falló?
# ¿Deberías siempre manejar el error localmente?
    """)
    
    print("\nComparación de enfoques:")
    
    def enfoque_malo():
        print("\nEnfoque Malo: Tragar el error")
        try:
            print("  1. Intentando operación crítica...")
            raise ValueError("Fallo crítico")
        except ValueError as e:
            print(f"  2. Error capturado: {e}")
            print("  3. Retornando None (¡el llamador no sabe del error!)")
            return None
    
    def enfoque_mejor():
        print("\nEnfoque Mejor: Registrar y re-lanzar")
        try:
            print("  1. Intentando operación crítica...")
            raise ValueError("Fallo crítico")
        except ValueError as e:
            print(f"  2. Error capturado: {e}")
            print("  3. Registrando para depuración...")
            print("  4. Re-lanzando para que el llamador pueda manejar")
            raise  # Re-lanza la misma excepción
    
    resultado1 = enfoque_malo()
    print(f"Resultado: {resultado1}")
    
    try:
        resultado2 = enfoque_mejor()
    except ValueError:
        print("Llamador: Puedo manejar esto apropiadamente")
    
    print("\n❌ PROBLEMAS CON NO RE-LANZAR:")
    print("- El llamador pierde información sobre el error")
    print("- Dificulta el manejo de errores en niveles superiores")
    print("- Puede causar problemas silenciosos más adelante")
    print("- Retornar None puede ser ambiguo")
    
    print("\n🤔 PREGUNTAS PARA PENSAR:")
    print("1. ¿Cuándo deberías capturar y manejar?")
    print("2. ¿Cuándo deberías capturar, registrar y re-lanzar?")
    print("3. ¿Cuándo NO deberías capturar en absoluto?")
    
    esperar_enter()

# ===========================================================================
# Problema 7: Manejo de excepciones en bucles
# ===========================================================================
def problema_excepciones_en_bucles():
    """Demuestra problemas comunes con excepciones en bucles"""
    limpiar_pantalla()
    imprimir_encabezado_seccion("PROBLEMA 7: Excepciones en Bucles")
    
    print("¿Qué pasa cuando una excepción ocurre en un bucle?")
    print("-" * 50)
    print("""
def procesar_lista_malo(elementos):
    resultados = []
    for elemento in elementos:
        resultado = procesar(elemento)  # ¿Y si esto falla?
        resultados.append(resultado)
    return resultados

# ¿Qué pasa si un elemento causa error?
# ¿Se procesan los demás elementos?
    """)
    
    print("\nComparemos enfoques:")
    
    elementos = ["10", "20", "abc", "40", "xyz"]
    
    print("\nEnfoque 1: Sin manejo (se rompe en el primer error)")
    print(f"Procesando: {elementos}")
    try:
        resultados = []
        for elem in elementos:
            resultado = int(elem) * 2
            resultados.append(resultado)
            print(f"  ✓ Procesado: {elem} -> {resultado}")
    except ValueError as e:
        print(f"  ✗ Error en '{elem}': {e}")
        print(f"  Elementos procesados: {resultados}")
        print(f"  Elementos restantes: perdidos")
    
    print("\nEnfoque 2: Con manejo (continúa con los demás)")
    print(f"Procesando: {elementos}")
    resultados = []
    errores = []
    for elem in elementos:
        try:
            resultado = int(elem) * 2
            resultados.append(resultado)
            print(f"  ✓ Procesado: {elem} -> {resultado}")
        except ValueError as e:
            errores.append((elem, str(e)))
            print(f"  ✗ Saltado: {elem} (error: {e})")
    
    print(f"\nResultados: {resultados}")
    print(f"Errores: {len(errores)}")
    
    print("\n❌ PROBLEMAS:")
    print("- Sin manejo: un error detiene todo el proceso")
    print("- Con manejo: necesitas decidir qué hacer con errores")
    print("- Puede ser difícil reportar qué falló y qué no")
    
    print("\n🤔 PREGUNTAS PARA PENSAR:")
    print("1. ¿Debería un error detener todo el proceso?")
    print("2. ¿Cómo reportarías múltiples errores?")
    print("3. ¿Qué pasa si TODOS los elementos fallan?")
    
    esperar_enter()

# ===========================================================================
# Menú Principal
# ===========================================================================
def menu_principal():
    """Muestra el menú principal y maneja la navegación"""
    while True:
        limpiar_pantalla()
        imprimir_encabezado_seccion("EJEMPLOS CONFUSOS DE MANEJO DE EXCEPCIONES")
        
        print("Selecciona un problema para explorar:\n")
        print("1. Except desnudo (bare except)")
        print("2. Capturar demasiado ampliamente")
        print("3. Ignorar errores silenciosamente")
        print("4. Confusión con else y finally")
        print("5. Uso incorrecto de raise")
        print("6. No re-lanzar apropiadamente")
        print("7. Excepciones en bucles")
        print("\n0. Salir")
        
        try:
            opcion = input("\nElige una opción (0-7): ")
            
            if opcion == '0':
                limpiar_pantalla()
                print("\n" + "=" * 70)
                print(" ¡Gracias por explorar el manejo de excepciones!")
                print("=" * 70 + "\n")
                break
            elif opcion == '1':
                problema_bare_except()
            elif opcion == '2':
                problema_except_amplio()
            elif opcion == '3':
                problema_ignorar_errores()
            elif opcion == '4':
                problema_else_finally()
            elif opcion == '5':
                problema_raise_incorrecto()
            elif opcion == '6':
                problema_no_relanzar()
            elif opcion == '7':
                problema_excepciones_en_bucles()
            else:
                print("\n❌ Opción inválida. Presiona Enter para intentar de nuevo...")
                esperar_enter()
        
        except KeyboardInterrupt:
            print("\n\n¡Interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            esperar_enter()

# ===========================================================================
# Punto de entrada
# ===========================================================================
if __name__ == "__main__":
    menu_principal()
1