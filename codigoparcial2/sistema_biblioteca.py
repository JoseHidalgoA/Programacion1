#!/usr/bin/env python3
"""
PARCIAL 2 - PROBLEMA INTEGRADOR (Parte 2)
Sistema de Gestión de Biblioteca Digital

Estudiante: Jose Hidalgo
Fecha: 21-10-2025
"""

from datetime import datetime, timedelta

# ===========================================================================
# EXCEPCIONES PERSONALIZADAS (5 puntos)
# ===========================================================================

class ErrorBiblioteca(Exception):
    """Excepción base para el sistema de biblioteca."""
    pass


class LibroNoEncontrado(ErrorBiblioteca):
    """Se lanza cuando un libro no existe en el catálogo."""
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"Libro con ISBN {isbn} no encontrado")


class LibroNoDisponible(ErrorBiblioteca):
    """Se lanza cuando no hay copias disponibles."""
    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        super().__init__(f"No hay copias disponibles de '{titulo}'")


class UsuarioNoRegistrado(ErrorBiblioteca):
    """Se lanza cuando el usuario no está registrado."""
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        super().__init__(f"Usuario con ID '{id_usuario}' no está registrado")


class LimitePrestamosExcedido(ErrorBiblioteca):
    """Se lanza cuando el usuario excede el límite de préstamos."""
    def __init__(self, id_usuario, limite):
        self.id_usuario = id_usuario
        self.limite = limite
        super().__init__(f"Usuario {id_usuario} excede límite de {limite} préstamos")


class PrestamoVencido(ErrorBiblioteca):
    """Se lanza para operaciones con préstamos vencidos."""
    def __init__(self, id_prestamo, dias_retraso):
        self.id_prestamo = id_prestamo
        self.dias_retraso = dias_retraso
        super().__init__(f"Préstamo {id_prestamo} está vencido por {dias_retraso} días")


# ===========================================================================
# CLASE PRINCIPAL: SISTEMA BIBLIOTECA (35 puntos)
# ===========================================================================

class SistemaBiblioteca:
    """
    Sistema completo de gestión de biblioteca digital.
    
    Estructuras de datos:
    - catalogo: {isbn: {'titulo', 'autor', 'anio', 'categoria', 'copias_total', 'copias_disponibles'}}
    - usuarios: {id_usuario: {'nombre', 'email', 'fecha_registro', 'prestamos_activos', 'historial'}}
    - prestamos: {id_prestamo: {'isbn', 'id_usuario', 'fecha_prestamo', 'fecha_vencimiento', 'fecha_devolucion', 'multa'}}
    """
    
    def __init__(self, dias_prestamo=14, multa_por_dia=1.0, limite_prestamos=3):
        """
        Inicializa el sistema.
        """
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = {}
        self.dias_prestamo = dias_prestamo
        self.multa_por_dia = multa_por_dia
        self.limite_prestamos = limite_prestamos
        self.contador_prestamos = 1

    # ============ GESTIÓN DE CATÁLOGO ============
    
    def agregar_libro(self, isbn, titulo, autor, anio, categoria, copias):
        if not (isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()):
            raise ValueError("ISBN debe ser una cadena de 13 dígitos.")
        if not titulo or not autor:
            raise ValueError("Título y autor no pueden estar vacíos.")
        if not (1000 <= anio <= datetime.now().year):
            raise ValueError("Año fuera de rango.")
        if copias < 1:
            raise ValueError("Debe haber al menos una copia.")
        if isbn in self.catalogo:
            raise KeyError(f"Libro con ISBN {isbn} ya existe.")
        
        self.catalogo[isbn] = {
            'titulo': titulo,
            'autor': autor,
            'anio': anio,
            'categoria': categoria,
            'copias_total': copias,
            'copias_disponibles': copias,
            'prestamos': 0
        }

    def buscar_libros(self, criterio='titulo', valor='', categoria=None):
        resultados = []
        valor = valor.lower()
        for isbn, info in self.catalogo.items():
            if categoria and info['categoria'] != categoria:
                continue
            if valor in str(info.get(criterio, '')).lower():
                resultados.append({'isbn': isbn, **info})
        return resultados

    # ============ GESTIÓN DE USUARIOS ============

    def registrar_usuario(self, id_usuario, nombre, email):
        if id_usuario in self.usuarios:
            raise ValueError("Usuario ya registrado.")
        if not nombre or '@' not in email or '.' not in email:
            raise ValueError("Datos inválidos del usuario.")
        self.usuarios[id_usuario] = {
            'nombre': nombre,
            'email': email,
            'fecha_registro': datetime.now(),
            'prestamos_activos': [],
            'historial': [],
            'multas_pendientes': 0
        }

    def obtener_estado_usuario(self, id_usuario):
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        u = self.usuarios[id_usuario]
        puede_prestar = len(u['prestamos_activos']) < self.limite_prestamos and u['multas_pendientes'] <= 50
        return {
            'nombre': u['nombre'],
            'prestamos_activos': len(u['prestamos_activos']),
            'puede_prestar': puede_prestar,
            'multas_pendientes': u['multas_pendientes']
        }

    # ============ GESTIÓN DE PRÉSTAMOS ============

    def prestar_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)
        libro = self.catalogo[isbn]
        usuario = self.usuarios[id_usuario]
        if libro['copias_disponibles'] <= 0:
            raise LibroNoDisponible(isbn, libro['titulo'])
        if len(usuario['prestamos_activos']) >= self.limite_prestamos:
            raise LimitePrestamosExcedido(id_usuario, self.limite_prestamos)
        if usuario['multas_pendientes'] > 50:
            raise ValueError("El usuario tiene multas pendientes superiores a $50.")
        
        id_prestamo = f"P{self.contador_prestamos:04d}"
        self.contador_prestamos += 1
        fecha_prestamo = datetime.now()
        fecha_vencimiento = fecha_prestamo + timedelta(days=self.dias_prestamo)
        
        self.prestamos[id_prestamo] = {
            'isbn': isbn,
            'id_usuario': id_usuario,
            'fecha_prestamo': fecha_prestamo,
            'fecha_vencimiento': fecha_vencimiento,
            'fecha_devolucion': None,
            'multa': 0.0
        }
        
        libro['copias_disponibles'] -= 1
        libro['prestamos'] += 1
        usuario['prestamos_activos'].append(id_prestamo)
        return id_prestamo

    def devolver_libro(self, id_prestamo):
        if id_prestamo not in self.prestamos:
            raise KeyError("Préstamo no encontrado.")
        p = self.prestamos[id_prestamo]
        if p['fecha_devolucion'] is not None:
            raise ValueError("El libro ya fue devuelto.")
        
        hoy = datetime.now()
        dias_retraso = max(0, (hoy - p['fecha_vencimiento']).days)
        multa = dias_retraso * self.multa_por_dia
        p['fecha_devolucion'] = hoy
        p['multa'] = multa
        
        libro = self.catalogo[p['isbn']]
        libro['copias_disponibles'] += 1
        
        usuario = self.usuarios[p['id_usuario']]
        usuario['prestamos_activos'].remove(id_prestamo)
        usuario['historial'].append(id_prestamo)
        usuario['multas_pendientes'] += multa
        
        return {'dias_retraso': dias_retraso, 'multa': multa, 'mensaje': "Devolución procesada"}

    def renovar_prestamo(self, id_prestamo):
        if id_prestamo not in self.prestamos:
            raise KeyError("Préstamo no encontrado.")
        p = self.prestamos[id_prestamo]
        if datetime.now() > p['fecha_vencimiento']:
            raise PrestamoVencido(id_prestamo, (datetime.now() - p['fecha_vencimiento']).days)
        p['fecha_vencimiento'] += timedelta(days=self.dias_prestamo)
        return p['fecha_vencimiento']


# ===========================================================================
# CASOS DE PRUEBA BÁSICOS
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DEL SISTEMA DE BIBLIOTECA")
    print("="*70)

    biblioteca = SistemaBiblioteca(dias_prestamo=7, multa_por_dia=2.0, limite_prestamos=3)

    # Agregar libros
    print("\n--- Agregar libros ---")
    biblioteca.agregar_libro("9781234567897", "Cien años de soledad", "Gabriel Garcia Marquez", 1967, "Novela", 3)
    biblioteca.agregar_libro("9781234567898", "El Principito", "Antoine de Saint-Exupéry", 1943, "Infantil", 2)
    print("Catálogo:", biblioteca.buscar_libros('titulo', ''))

    # Registrar usuarios
    print("\n--- Registrar usuarios ---")
    biblioteca.registrar_usuario("u1", "Ana Perez", "ana@example.com")
    biblioteca.registrar_usuario("u2", "Juan Gomez", "juan@example.com")
    print("Estado u1:", biblioteca.obtener_estado_usuario("u1"))

    # Prestar libros
    print("\n--- Prestar libros ---")
    pid1 = biblioteca.prestar_libro("9781234567897", "u1")
    pid2 = biblioteca.prestar_libro("9781234567897", "u2")
    print("Prestamos creados:", pid1, pid2)
    print("Prestamos activos:")
    for pid, datos in biblioteca.prestamos.items():
        print(f"  ID {pid} -> {datos}")

    # Forzar devolución tardía (manipular fecha para prueba)
    print("\n--- Forzar devolución tardía y calcular multa ---")
    biblioteca.prestamos[pid1]['fecha_vencimiento'] = datetime.now() - timedelta(days=5)
    resultado_dev = biblioteca.devolver_libro(pid1)
    print("Devolución pid1:", resultado_dev)
    print("Usuario u1 estado:", biblioteca.obtener_estado_usuario("u1"))

    # Renovar préstamo (cuando no vencido)
    print("\n--- Renovar pid2 ---")
    try:
        nueva_fecha = biblioteca.renovar_prestamo(pid2)
        print("Renovación pid2 OK, nuevo vencimiento:", nueva_fecha)
    except Exception as e:
        print("Error renovación:", e)

    print("\n✓ Sistema funcionando correctamente")
