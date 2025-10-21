"""
Archivo de pruebas para el sistema de biblioteca.
Autor: José Hidalgo
Versión corregida 100%
"""

from sistema_biblioteca import *


def pruebas_biblioteca():
    print("=== PRUEBAS DEL SISTEMA DE BIBLIOTECA ===\n")

    biblioteca = Biblioteca()

    # --- Registro de libros ---
    print("1️⃣  Registrando libros...")
    try:
        biblioteca.registrar_libro("001", "Cien años de soledad", "Gabriel García Márquez", 5)
        biblioteca.registrar_libro("002", "El Quijote", "Miguel de Cervantes", 3)
        biblioteca.registrar_libro("003", "La Odisea", "Homero", 2)
        print("✅ Libros registrados correctamente.")
    except Exception as e:
        print(f"❌ Error registrando libros: {e}")

    # --- Registro de usuarios ---
    print("\n2️⃣  Registrando usuarios...")
    try:
        biblioteca.registrar_usuario("mario@example.com", "Mario Pérez")
        biblioteca.registrar_usuario("laura@example.com", "Laura Gómez")
        print("✅ Usuarios registrados correctamente.")
    except Exception as e:
        print(f"❌ Error registrando usuarios: {e}")

    # --- Búsqueda de libro ---
    print("\n3️⃣  Buscando libro por título...")
    libro = biblioteca.buscar_libro_por_titulo("Cien años de soledad")
    if libro:
        print(f"✅ Libro encontrado: {libro}")
    else:
        print("❌ Libro no encontrado.")

    # --- Préstamos ---
    print("\n4️⃣  Realizando préstamos...")
    try:
        biblioteca.prestar_libro("001", "mario@example.com")
        biblioteca.prestar_libro("002", "laura@example.com")
        print("✅ Préstamos realizados correctamente.")
    except Exception as e:
        print(f"❌ Error realizando préstamo: {e}")

    # --- Mostrar estado actual ---
    print("\n📚 Estado actual de los libros:")
    for libro in biblioteca.listar_libros():
        print(libro)

    # --- Devolución de libro ---
    print("\n5️⃣  Devolviendo libro...")
    try:
        biblioteca.devolver_libro("001", "mario@example.com")
        print("✅ Devolución registrada correctamente.")
    except Exception as e:
        print(f"❌ Error al devolver libro: {e}")

    # --- Renovación de préstamo ---
    print("\n6️⃣  Renovando préstamo...")
    try:
        biblioteca.prestar_libro("003", "mario@example.com")
        biblioteca.renovar_prestamo("003", "mario@example.com")
        print("✅ Renovación realizada correctamente.")
    except Exception as e:
        print(f"❌ Error al renovar préstamo: {e}")

    # --- Prueba de errores ---
    print("\n7️⃣  Probando validaciones...")
    try:
        biblioteca.registrar_libro("001", "Duplicado", "Autor X", 1)
    except LibroDuplicado:
        print("✅ Correcto: No se permite registrar un libro duplicado.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

    try:
        biblioteca.prestar_libro("9999", "mario@example.com")
    except LibroNoEncontrado:
        print("✅ Correcto: No se puede prestar un libro inexistente.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

    try:
        biblioteca.registrar_usuario("mario@example.com", "Otro Mario")
    except UsuarioDuplicado:
        print("✅ Correcto: No se permite registrar un usuario duplicado.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

    try:
        biblioteca.renovar_prestamo("9999", "mario@example.com")
    except LibroNoEncontrado:
        print("✅ Correcto: No se puede renovar un préstamo inexistente.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

    print("\n=== FIN DE PRUEBAS ===")


if __name__ == "__main__":
    pruebas_biblioteca()
