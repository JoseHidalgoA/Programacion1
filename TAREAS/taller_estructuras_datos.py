


from collections import defaultdict, OrderedDict
from datetime import datetime
import statistics

# ---------------------------
# Nivel Básico
# ---------------------------

def filtrar_pares(numeros):
    """B1: Devuelve una lista con los números pares de la lista de entrada."""
    return [num for num in numeros if num % 2 == 0]

def invertir_diccionario(diccionario):
    """B2: Invierte claves y valores (asume valores únicos y hashables)."""
    return {valor: clave for clave, valor in diccionario.items()}

def elementos_comunes(lista1, lista2):
    """B3: Retorna elementos comunes entre dos listas sin duplicados (orden no garantizado)."""
    return list(set(lista1) & set(lista2))

def contar_palabras(texto):
    """B4: Cuenta la frecuencia de palabras en un texto (ignorando mayúsculas)."""
    palabras = texto.lower().split()
    contador = {}
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador

def eliminar_duplicados(lista):
    """B5: Elimina duplicados manteniendo el orden original."""
    return list(dict.fromkeys(lista))


# ---------------------------
# Nivel Intermedio
# ---------------------------

def agrupar_por(objetos, atributo):
    """
    I1: Agrupa una lista de diccionarios (objetos) por el valor de 'atributo'.
    Devuelve un diccionario: {valor_atributo: [objetos...], ...}
    """
    resultado = {}
    for obj in objetos:
        valor = obj.get(atributo)
        if valor not in resultado:
            resultado[valor] = []
        resultado[valor].append(obj)
    return resultado

def agrupar_por_alt(objetos, atributo):
    """I1: Alternativa usando defaultdict."""
    resultado = defaultdict(list)
    for obj in objetos:
        resultado[obj.get(atributo)].append(obj)
    return dict(resultado)

def fusionar_diccionarios(dict1, dict2):
    """
    I2: Fusiona dos diccionarios anidados. Si ambos valores son diccionarios,
    se aplica la fusión recursiva; en caso contrario, prevalece el valor de dict2.
    """
    resultado = dict1.copy()
    for clave, valor in dict2.items():
        if clave in resultado and isinstance(resultado[clave], dict) and isinstance(valor, dict):
            resultado[clave] = fusionar_diccionarios(resultado[clave], valor)
        else:
            resultado[clave] = valor
    return resultado

def encontrar_par_suma(numeros, objetivo):
    """
    I3: Encuentra y devuelve un par (a, b) tal que a + b == objetivo.
    Retorna None si no existe.
    """
    vistos = set()
    for num in numeros:
        complemento = objetivo - num
        if complemento in vistos:
            return (complemento, num)
        vistos.add(num)
    return None

def transponer(matriz):
    """I4: Transpone una matriz dada como lista de listas."""
    if not matriz:
        return []
    return [list(fila) for fila in zip(*matriz)]

def contar_por_categoria(datos):
    """
    I5: Cuenta elementos únicos por categoría.
    Entrada: lista de tuplas (categoria, elemento).
    Retorna dict {categoria: cantidad_elementos_unicos}
    """
    categorias = {}
    for categoria, elemento in datos:
        if categoria not in categorias:
            categorias[categoria] = set()
        categorias[categoria].add(elemento)
    return {categoria: len(elementos) for categoria, elementos in categorias.items()}


# ---------------------------
# Nivel Avanzado
# ---------------------------

def fibonacci(n):
    """A1: Fibonacci con memoización."""
    memoria = {}
    def fib_memo(k):
        if k in memoria:
            return memoria[k]
        if k <= 1:
            resultado = k
        else:
            resultado = fib_memo(k - 1) + fib_memo(k - 2)
        memoria[k] = resultado
        return resultado
    return fib_memo(n)

class LRUCache:
    """A2: Caché LRU simple. Implementación con OrderedDict (eficiente)."""

    def __init__(self, capacidad):
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero positivo")
        self.capacidad = capacidad
        self.cache = OrderedDict()

    def get(self, clave):
        """Devuelve el valor asociado o None y marca la clave como recientemente usada."""
        if clave not in self.cache:
            return None
        # mover al final = más recientemente usado
        valor = self.cache.pop(clave)
        self.cache[clave] = valor
        return valor

    def put(self, clave, valor):
        """Inserta o actualiza un valor; si supera capacidad, elimina el menos recientemente usado."""
        if clave in self.cache:
            # eliminar para reinsertar al final
            self.cache.pop(clave)
        elif len(self.cache) >= self.capacidad:
            # popitem(last=False) elimina el primer elemento insertado -> LRU
            self.cache.popitem(last=False)
        self.cache[clave] = valor

    def __str__(self):
        return f"LRUCache(capacidad={self.capacidad}, elementos={[k for k in self.cache.keys()]})"

class MiConjunto:
    """A3: Implementación básica de conjunto usando lista como almacenamiento."""

    def __init__(self):
        self.elementos = []

    def add(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def remove(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
        else:
            raise KeyError(f"{elemento} no está en el conjunto")

    def discard(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def __contains__(self, elemento):
        return elemento in self.elementos

    def __len__(self):
        return len(self.elementos)

    def __str__(self):
        return "{" + ", ".join(str(e) for e in self.elementos) + "}"

def filtrar_jugadores(datos, condicion):
    """
    A4: Filtra jugadores en una estructura anidada de equipos, manteniendo la estructura.
    'condicion' es una función que recibe un jugador (dict) y devuelve True/False.
    """
    resultado = {}
    for equipo, info in datos.items():
        jugadores_filtrados = [jug for jug in info.get("jugadores", []) if condicion(jug)]
        resultado[equipo] = {"jugadores": jugadores_filtrados}
    return resultado

def encontrar_ruta(arbol, valor):
    """
    A5: Encuentra la ruta desde la raíz hasta el nodo que contiene 'valor' en un árbol
    representado con diccionarios: {'valor': X, 'izquierdo': ..., 'derecho': ...}
    Retorna lista con los valores de la ruta o None si no se encuentra.
    """
    def buscar(nodo, camino_actual):
        if nodo is None:
            return None
        camino_actual.append(nodo.get("valor"))
        if nodo.get("valor") == valor:
            return camino_actual
        # Buscar en izquierdo
        izq = buscar(nodo.get("izquierdo"), camino_actual.copy())
        if izq:
            return izq
        der = buscar(nodo.get("derecho"), camino_actual.copy())
        if der:
            return der
        return None
    return buscar(arbol, [])


# ---------------------------
# Ejercicios de Depuración
# ---------------------------

def agregar_puntos_correcto(equipos, equipo, puntos):
    """Depuración 1: No modificar el dict original; devolver copia con la nueva entrada."""
    resultado = equipos.copy()
    resultado[equipo] = puntos
    return resultado

import json
class ReferenceResolver:
    """
    Depuración 2:
    Clase utilitaria para serializar estructuras con referencias circulares en JSON.
    Convierte referencias repetidas en objetos con $ref y cada objeto con $id.
    (Nota: Es una estrategia simple; puede producir muchas claves si la estructura es grande).
    """
    def __init__(self):
        self.memo = {}
        self.counter = 0

    def __call__(self, obj):
        if isinstance(obj, dict):
            obj_id = id(obj)
            if obj_id in self.memo:
                # referencia a objeto ya serializado
                return {"$ref": self.memo[obj_id]}
            self.counter += 1
            ref_id = f"id{self.counter}"
            self.memo[obj_id] = ref_id
            result = {"$id": ref_id}
            for k, v in obj.items():
                result[k] = self(v)
            return result
        # Para otros tipos (listas, etc.) devolvemos directamente (podría ampliarse)
        if isinstance(obj, list):
            return [self(x) for x in obj]
        return obj

def eliminar_pares_iteracion_segura(numeros):
    """
    Depuración 3: Elimina pares sin modificar la lista mientras se itera.
    Muestra tres enfoques; aquí devolvemos la lista filtrada (comprehension).
    """
    return [x for x in numeros if x % 2 != 0]


# ---------------------------
# Proyecto Integrador: Analizador de Ventas
# ---------------------------

class AnalizadorVentas:
    """
    Clase para analizar ventas (proyecto integrador).
    Incluye:
    - Agrupaciones (por categoria, mes, vendedor)
    - Conteo de productos vendidos
    - Productos más vendidos
    - Estadísticas por vendedor
    - Búsqueda por criterios
    - Búsqueda por rango de fechas
    - Índice invertido simple para búsquedas rápidas por múltiples campos
    """

    def __init__(self, datos_ventas):
        # Se espera que cada venta sea un dict con al menos:
        # {'id', 'producto', 'categoria', 'precio', 'fecha' (YYYY-MM-DD), 'vendedor'}
        self.ventas = list(datos_ventas)
        self.ventas_por_categoria = self._agrupar_por("categoria")
        self.ventas_por_mes = self._agrupar_por_mes()
        self.ventas_por_vendedor = self._agrupar_por("vendedor")
        self.productos_vendidos = self._contar_productos()
        # índice invertido: {campo: {valor: [ventas...]}}
        self.indice_invertido = self._construir_indice(["producto", "categoria", "vendedor"])

    def _agrupar_por(self, campo):
        resultado = defaultdict(list)
        for venta in self.ventas:
            resultado[venta.get(campo)].append(venta)
        return dict(resultado)

    def _agrupar_por_mes(self):
        resultado = defaultdict(list)
        for venta in self.ventas:
            fecha = datetime.strptime(venta["fecha"], "%Y-%m-%d")
            mes = f"{fecha.year}-{fecha.month:02d}"
            resultado[mes].append(venta)
        return dict(resultado)

    def _contar_productos(self):
        contador = {}
        for venta in self.ventas:
            producto = venta.get("producto")
            contador[producto] = contador.get(producto, 0) + 1
        return contador

    def productos_mas_vendidos(self, n=3):
        return sorted(self.productos_vendidos.items(), key=lambda x: x[1], reverse=True)[:n]

    def total_ventas_por_categoria(self):
        resultado = {}
        for categoria, ventas in self.ventas_por_categoria.items():
            resultado[categoria] = sum(v["precio"] for v in ventas)
        return resultado

    def estadisticas_vendedor(self, vendedor):
        if vendedor not in self.ventas_por_vendedor:
            return None
        ventas = self.ventas_por_vendedor[vendedor]
        precios = [v["precio"] for v in ventas]
        return {
            "total": sum(precios),
            "promedio": statistics.mean(precios) if precios else 0,
            "mediana": statistics.median(precios) if precios else 0,
            "cantidad": len(precios),
            "min": min(precios) if precios else None,
            "max": max(precios) if precios else None
        }

    def buscar_ventas(self, **criterios):
        """
        Busca ventas que cumplan todos los criterios pasados como kwargs.
        Ejemplo: buscar_ventas(categoria='Accesorios', vendedor='Juan')
        """
        # Si hay índice invertido y campo buscado está indexado, úsalo para optimizar
        campos_indexados = [c for c in criterios.keys() if c in self.indice_invertido]
        if campos_indexados:
            # Intersectar listas de ventas para cada criterio indexado
            conjuntos = []
            for campo in campos_indexados:
                valor = criterios[campo]
                ventas_posibles = self.indice_invertido[campo].get(valor, [])
                conjuntos.append(set(id(v) for v in ventas_posibles))
            # inicio: ventas candidatas (ids) = intersección
            candidatos_ids = set.intersection(*conjuntos) if conjuntos else set()
            # reconstruir ventas desde ids y aplicar otros criterios
            candidatos = [v for v in self.ventas if id(v) in candidatos_ids]
        else:
            candidatos = self.ventas

        resultado = []
        for venta in candidatos:
            cumple = True
            for campo, valor in criterios.items():
                if campo not in venta or venta[campo] != valor:
                    cumple = False
                    break
            if cumple:
                resultado.append(venta)
        return resultado

    def buscar_por_rango_fechas(self, fecha_inicio, fecha_fin):
        """
        Busca ventas cuyo campo 'fecha' esté entre fecha_inicio y fecha_fin (inclusive).
        Las fechas deben ser strings en formato 'YYYY-MM-DD' o objetos datetime.
        """
        if isinstance(fecha_inicio, str):
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        if isinstance(fecha_fin, str):
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        resultado = []
        for venta in self.ventas:
            fecha = datetime.strptime(venta["fecha"], "%Y-%m-%d")
            if fecha_inicio <= fecha <= fecha_fin:
                resultado.append(venta)
        return resultado

    def _construir_indice(self, campos):
        """
        Construye un índice invertido simple para los campos indicados.
        Retorna: {campo: {valor: [venta, ...], ...}, ...}
        """
        indice = {}
        for campo in campos:
            indice[campo] = defaultdict(list)
        for venta in self.ventas:
            for campo in campos:
                indice[campo][venta.get(campo)].append(venta)
        # convertir inner dicts a dict normales
        return {campo: dict(mapping) for campo, mapping in indice.items()}


# ---------------------------
# Pruebas rápidas / Ejemplos
# ---------------------------

if __name__ == "__main__":
    # Básico
    print("B1 filtrar_pares:", filtrar_pares(list(range(1, 11))))
    print("B2 invertir_diccionario:", invertir_diccionario({"a": 1, "b": 2, "c": 3}))
    print("B3 elementos_comunes:", elementos_comunes([1,2,3,4,5], [4,5,6,7]))
    print("B4 contar_palabras:", contar_palabras("hola mundo hola python"))
    print("B5 eliminar_duplicados:", eliminar_duplicados([1,2,2,3,4,3,5]))

    # Intermedio
    estudiantes = [
        {"nombre": "Ana", "ciudad": "Madrid"},
        {"nombre": "Juan", "ciudad": "Barcelona"},
        {"nombre": "Maria", "ciudad": "Madrid"},
        {"nombre": "Pedro", "ciudad": "Valencia"}
    ]
    print("I1 agrupar_por:", agrupar_por(estudiantes, "ciudad"))

    dict1 = {"a": 1, "b": {"x": 10, "y": 20}}
    dict2 = {"c": 3, "b": {"y": 30, "z": 40}}
    print("I2 fusionar_diccionarios:", fusionar_diccionarios(dict1, dict2))

    print("I3 encontrar_par_suma:", encontrar_par_suma([1,5,3,7,9,2], 10))
    print("I4 transponer:", transponer([[1,2,3],[4,5,6],[7,8,9]]))
    datos = [("fruta","manzana"),("verdura","zanahoria"),("fruta","platano"),("fruta","manzana"),("verdura","lechuga")]
    print("I5 contar_por_categoria:", contar_por_categoria(datos))

    # Avanzado
    print("A1 fibonacci(10):", fibonacci(10))
    cache = LRUCache(2)
    cache.put(1, "uno")
    cache.put(2, "dos")
    print("A2 get(1):", cache.get(1))
    cache.put(3, "tres")  # elimina clave 2 (LRU)
    print("A2 get(2):", cache.get(2))
    print("LRU estado:", cache)

    mi = MiConjunto()
    mi.add(1); mi.add(2); mi.add(1)
    print("A3 MiConjunto:", mi, len(mi), (1 in mi))

    equipos = {
        "equipo1": {"jugadores":[{"nombre":"Ana","puntos":120},{"nombre":"Juan","puntos":80}]},
        "equipo2": {"jugadores":[{"nombre":"Maria","puntos":90},{"nombre":"Pedro","puntos":150}]}
    }
    print("A4 filtrar_jugadores (>100):", filtrar_jugadores(equipos, lambda j: j["puntos"]>100))

    arbol = {
        "valor":"A",
        "izquierdo":{"valor":"B", "izquierdo":{"valor":"D","izquierdo":None,"derecho":None},
                     "derecho":{"valor":"E","izquierdo":None,"derecho":None}},
        "derecho":{"valor":"C", "izquierdo":None, "derecho":{"valor":"F","izquierdo":None,"derecho":None}}
    }
    print("A5 encontrar_ruta F:", encontrar_ruta(arbol, "F"))

    # Depuración
    puntuacion = {"Equipo A": 10, "Equipo B": 15}
    nuevos = agregar_puntos_correcto(puntuacion, "Equipo C", 12)
    print("Dep1 original:", puntuacion, "nuevo:", nuevos)

    # Serializar con referencias circulares (Depuración 2)
    a = {"nombre": "objeto a"}
    b = {"nombre": "objeto b", "referencia": a}
    a["referencia"] = b
    try:
        s = json.dumps(a)  # falla
    except Exception as e:
        print("Dep2 json.dumps falla como esperado:", type(e).__name__)

    # Usar ReferenceResolver
    resolver = ReferenceResolver()
    safe = json.dumps(a, default=resolver)
    print("Dep2 serializado con ReferenceResolver:", safe)

    print("Dep3 eliminar_pares_iteracion_segura:", eliminar_pares_iteracion_segura(list(range(1,11))))

    # Proyecto integrador: ejemplo de uso
    ventas = [
        {"id": 1, "producto": "Laptop", "categoria": "Electrónica", "precio": 1200, "fecha": "2023-01-15", "vendedor": "Ana"},
        {"id": 2, "producto": "Monitor", "categoria": "Electrónica", "precio": 200, "fecha": "2023-01-20", "vendedor": "Juan"},
        {"id": 3, "producto": "Teclado", "categoria": "Accesorios", "precio": 80, "fecha": "2023-02-05", "vendedor": "Ana"},
        {"id": 4, "producto": "Mouse", "categoria": "Accesorios", "precio": 25, "fecha": "2023-02-10", "vendedor": "Pedro"},
        {"id": 5, "producto": "Laptop", "categoria": "Electrónica", "precio": 1500, "fecha": "2023-02-15", "vendedor": "Juan"},
        {"id": 6, "producto": "Teléfono", "categoria": "Electrónica", "precio": 800, "fecha": "2023-03-05", "vendedor": "Ana"},
        {"id": 7, "producto": "Tablet", "categoria": "Electrónica", "precio": 300, "fecha": "2023-03-10", "vendedor": "Pedro"},
        {"id": 8, "producto": "Teclado", "categoria": "Accesorios", "precio": 85, "fecha": "2023-03-15", "vendedor": "Juan"},
        {"id": 9, "producto": "Monitor", "categoria": "Electrónica", "precio": 250, "fecha": "2023-04-05", "vendedor": "Ana"},
        {"id": 10, "producto": "Mouse", "categoria": "Accesorios", "precio": 30, "fecha": "2023-04-10", "vendedor": "Pedro"}
    ]
    analizador = AnalizadorVentas(ventas)
    print("Proyecto: productos más vendidos (2):", analizador.productos_mas_vendidos(2))
    print("Proyecto: total por categoria:", analizador.total_ventas_por_categoria())
    print("Proyecto: estadísticas de Ana:", analizador.estadisticas_vendedor("Ana"))
    print("Proyecto: buscar accesorios vendidos por Juan:", analizador.buscar_ventas(categoria="Accesorios", vendedor="Juan"))
    print("Proyecto: buscar por rango fechas 2023-02-01 a 2023-03-31:", analizador.buscar_por_rango_fechas("2023-02-01","2023-03-31"))

