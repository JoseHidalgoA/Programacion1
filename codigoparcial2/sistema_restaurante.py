#!/usr/bin/env python3
"""
PROBLEMA INTEGRADOR DE PRÁCTICA
Sistema de Gestión de Restaurante

Nombre: Jose Hidalgo
Fecha: 21-10-2025
"""

from datetime import datetime, time
import os

# ===========================================================================
# EXCEPCIONES PERSONALIZADAS
# ===========================================================================

class ErrorRestaurante(Exception):
    """Excepción base para el sistema de restaurante."""
    pass

class PlatoNoEncontrado(ErrorRestaurante):
    """Se lanza cuando un plato no existe en el menú."""
    def __init__(self, codigo_plato):
        self.codigo_plato = codigo_plato
        super().__init__(f"Plato con código '{codigo_plato}' no encontrado en el menú")

class MesaNoDisponible(ErrorRestaurante):
    """Se lanza cuando la mesa está ocupada."""
    def __init__(self, numero_mesa, hora_disponible=None):
        self.numero_mesa = numero_mesa
        self.hora_disponible = hora_disponible
        msg = f"Mesa {numero_mesa} no disponible"
        if hora_disponible:
            msg += f"; disponible a las {hora_disponible}"
        super().__init__(msg)

class CapacidadExcedida(ErrorRestaurante):
    """Se lanza cuando hay más comensales que capacidad."""
    def __init__(self, numero_mesa, capacidad, comensales):
        self.numero_mesa = numero_mesa
        self.capacidad = capacidad
        self.comensales = comensales
        super().__init__(f"Mesa {numero_mesa}: capacidad {capacidad}, comensales {comensales}")

class PedidoInvalido(ErrorRestaurante):
    """Se lanza para pedidos con problemas."""
    def __init__(self, razon):
        self.razon = razon
        super().__init__(f"Pedido inválido: {razon}")


# ===========================================================================
# CLASE PRINCIPAL: SISTEMA RESTAURANTE
# ===========================================================================

class SistemaRestaurante:
    """Sistema completo de gestión de restaurante."""

    def __init__(self, num_mesas=10, tasa_impuesto=0.16, propina_sugerida=0.15):
        """
        Inicializa el sistema.

        Estructuras internas (en memoria):
        - menu: {codigo: {'nombre','categoria','precio','disponible','vendidos'}}
        - mesas: {numero: {'capacidad','ocupada'(bool),'comensales', 'hora_reserva'(datetime.time) , 'pedido_id'}}
        - pedidos: {id_pedido: {'numero_mesa','items':{codigo:cantidad}, 'estado','fecha','subtot','impuesto','propina','total'}}
        - ventas: list de pedidos pagados (para reportes)
        """
        # configuración
        self.num_mesas = int(num_mesas)
        self.tasa_impuesto = float(tasa_impuesto)
        self.propina_sugerida = float(propina_sugerida)

        # datos
        self.menu = {}      # menú de platos
        self.mesas = {}     # mesas configuradas
        self.pedidos = {}   # pedidos en curso e históricos
        self.ventas = []    # pedidos pagados (para reportes)

        # contadores
        self._next_pedido_id = 1

        # inicializar mesas básicas
        for m in range(1, self.num_mesas + 1):
            self.mesas[m] = {
                'capacidad': 4,
                'ocupada': False,
                'comensales': 0,
                'hora_reserva': None,
                'pedido_id': None
            }

    # ---------------------------
    # GESTIÓN DE MENÚ
    # ---------------------------

    def agregar_plato(self, codigo, nombre, categoria, precio):
        """
        Agrega un plato al menú.
        - codigo: string / identificador único
        - nombre: string
        - categoria: string
        - precio: float > 0
        """
        if not codigo or not str(codigo).strip():
            raise ValueError("Código inválido")
        if codigo in self.menu:
            raise KeyError(f"Código {codigo} ya existe en el menú")
        if not nombre or not categoria:
            raise ValueError("Nombre y categoría no pueden estar vacíos")
        try:
            precio = float(precio)
        except Exception:
            raise ValueError("Precio inválido")
        if precio <= 0:
            raise ValueError("Precio debe ser mayor a 0")

        self.menu[codigo] = {
            'nombre': nombre,
            'categoria': categoria,
            'precio': precio,
            'disponible': True,
            'vendidos': 0
        }
        return True

    def cambiar_disponibilidad(self, codigo, disponible):
        if codigo not in self.menu:
            raise PlatoNoEncontrado(codigo)
        self.menu[codigo]['disponible'] = bool(disponible)
        return True

    def buscar_platos(self, categoria=None, precio_max=None):
        """
        Retorna lista de platos coincidentes (solo disponibles).
        """
        resultados = []
        for codigo, info in self.menu.items():
            if not info.get('disponible', True):
                continue
            if categoria and info['categoria'].lower() != str(categoria).lower():
                continue
            if precio_max is not None:
                try:
                    if info['precio'] > float(precio_max):
                        continue
                except Exception:
                    raise ValueError("precio_max inválido")
            resultados.append({'codigo': codigo, **info})
        return resultados

    # ---------------------------
    # GESTIÓN DE MESAS
    # ---------------------------

    def configurar_mesa(self, numero, capacidad):
        if not isinstance(numero, int) or numero < 1:
            raise ValueError("Número de mesa inválido")
        if not isinstance(capacidad, int) or capacidad < 1:
            raise ValueError("Capacidad inválida")
        # si la mesa está fuera del rango, la creamos/adaptamos
        self.mesas.setdefault(numero, {
            'capacidad': capacidad,
            'ocupada': False,
            'comensales': 0,
            'hora_reserva': None,
            'pedido_id': None
        })
        self.mesas[numero]['capacidad'] = capacidad
        return True

    def reservar_mesa(self, numero, comensales, hora=None):
        """
        Reservar mesa en hora (hora puede ser datetime.time o None = ahora).
        - Si mesa no existe -> ValueError
        - Si ocupada -> MesaNoDisponible
        - Si comensales > capacidad -> CapacidadExcedida
        """
        if numero not in self.mesas:
            raise ValueError("Mesa no existe")
        mesa = self.mesas[numero]
        if mesa['ocupada']:
            raise MesaNoDisponible(numero, mesa.get('hora_reserva'))
        if comensales > mesa['capacidad']:
            raise CapacidadExcedida(numero, mesa['capacidad'], comensales)
        # aceptar reserva
        mesa['ocupada'] = True
        mesa['comensales'] = int(comensales)
        mesa['hora_reserva'] = hora if isinstance(hora, time) or hora is None else mesa['hora_reserva']
        # crear un pedido inicial para la mesa
        pedido_id = self.crear_pedido(numero)
        mesa['pedido_id'] = pedido_id
        return pedido_id

    def liberar_mesa(self, numero):
        if numero not in self.mesas:
            raise ValueError("Mesa no existe")
        mesa = self.mesas[numero]
        if not mesa['ocupada']:
            raise ValueError("Mesa no está ocupada")
        # si hay pedido asociado y está abierto, lo dejamos intacto (se puede pagar después)
        mesa['ocupada'] = False
        mesa['comensales'] = 0
        mesa['hora_reserva'] = None
        mesa['pedido_id'] = None
        return True

    def mesas_disponibles(self, comensales=1):
        disponibles = []
        for numero, info in self.mesas.items():
            if (not info['ocupada']) and info['capacidad'] >= comensales:
                disponibles.append(numero)
        return disponibles

    # ---------------------------
    # GESTIÓN DE PEDIDOS
    # ---------------------------

    def _generar_id_pedido(self):
        pid = f"P{self._next_pedido_id:05d}"
        self._next_pedido_id += 1
        return pid

    def crear_pedido(self, numero_mesa):
        if numero_mesa not in self.mesas:
            raise ValueError("Mesa no existe")
        pedido_id = self._generar_id_pedido()
        self.pedidos[pedido_id] = {
            'numero_mesa': numero_mesa,
            'items': {},  # codigo -> cantidad
            'estado': 'abierto',
            'fecha': datetime.now(),
            'subtotal': 0.0,
            'impuesto': 0.0,
            'propina': 0.0,
            'total': 0.0,
            'pagado': False
        }
        # asignar a la mesa si aún no tiene
        mesa = self.mesas[numero_mesa]
        if mesa.get('pedido_id') is None:
            mesa['pedido_id'] = pedido_id
            mesa['ocupada'] = True
        return pedido_id

    def agregar_item(self, id_pedido, codigo_plato, cantidad=1):
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("Pedido no existe")
        pedido = self.pedidos[id_pedido]
        if pedido['pagado']:
            raise PedidoInvalido("Pedido ya está pagado")
        if codigo_plato not in self.menu:
            raise PlatoNoEncontrado(codigo_plato)
        plato = self.menu[codigo_plato]
        if not plato.get('disponible', True):
            raise ValueError("Plato no disponible")
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser positiva")

        pedido['items'][codigo_plato] = pedido['items'].get(codigo_plato, 0) + int(cantidad)
        return True

    def calcular_total(self, id_pedido, propina_porcentaje=None):
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("Pedido no existe")
        pedido = self.pedidos[id_pedido]
        subtotal = 0.0
        for codigo, cantidad in pedido['items'].items():
            precio = self.menu[codigo]['precio']
            subtotal += precio * cantidad
        impuesto = round(subtotal * self.tasa_impuesto, 2)
        if propina_porcentaje is None:
            propina_porcentaje = self.propina_sugerida
        propina = round(subtotal * float(propina_porcentaje), 2)
        total = round(subtotal + impuesto + propina, 2)
        # actualizar campos
        pedido['subtotal'] = round(subtotal, 2)
        pedido['impuesto'] = impuesto
        pedido['propina'] = propina
        pedido['total'] = total
        return {
            'subtotal': pedido['subtotal'],
            'impuesto': pedido['impuesto'],
            'propina': pedido['propina'],
            'total': pedido['total']
        }

    def pagar_pedido(self, id_pedido, propina_porcentaje=None):
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("Pedido no existe")
        pedido = self.pedidos[id_pedido]
        if pedido['pagado']:
            raise PedidoInvalido("Pedido ya fue pagado")
        # calcular totales si no están calculados
        totals = self.calcular_total(id_pedido, propina_porcentaje)
        pedido['pagado'] = True
        pedido['estado'] = 'pagado'
        pedido['fecha_pago'] = datetime.now()
        # actualizar indicadores de ventas: incrementar vendidos en menú
        for codigo, cantidad in pedido['items'].items():
            self.menu[codigo]['vendidos'] = self.menu[codigo].get('vendidos', 0) + cantidad
        # asignar a ventas históricas (copia del pedido)
        venta_record = {
            'id_pedido': id_pedido,
            'numero_mesa': pedido['numero_mesa'],
            'fecha': pedido.get('fecha_pago', pedido['fecha']),
            'subtotal': pedido['subtotal'],
            'impuesto': pedido['impuesto'],
            'propina': pedido['propina'],
            'total': pedido['total'],
            'items': dict(pedido['items'])
        }
        self.ventas.append(venta_record)
        # liberar mesa asociada
        numero = pedido['numero_mesa']
        if numero in self.mesas:
            mesa = self.mesas[numero]
            # solo liberar si la mesa tiene ese pedido_id
            if mesa.get('pedido_id') == id_pedido:
                mesa['pedido_id'] = None
                mesa['ocupada'] = False
                mesa['comensales'] = 0
                mesa['hora_reserva'] = None
        return venta_record

    # ---------------------------
    # REPORTES Y ESTADÍSTICAS
    # ---------------------------

    def platos_mas_vendidos(self, n=5):
        lista = []
        for codigo, info in self.menu.items():
            lista.append((codigo, info['nombre'], info.get('vendidos', 0)))
        lista.sort(key=lambda x: x[2], reverse=True)
        return lista[:n]

    def ventas_por_categoria(self):
        agg = {}
        for venta in self.ventas:
            for codigo, cantidad in venta['items'].items():
                categoria = self.menu[codigo]['categoria']
                valor = self.menu[codigo]['precio'] * cantidad
                agg[categoria] = agg.get(categoria, 0.0) + valor
        # round values
        return {k: round(v, 2) for k, v in agg.items()}

    def reporte_ventas_dia(self, fecha=None):
        """
        Si fecha es None -> hoy. fecha debe ser datetime.date si se pasa.
        Retorna: total_ventas, total_impuesto, total_propina, total_items_vendidos, detalle_por_categoria
        """
        if fecha is None:
            fecha = datetime.now().date()
        tot_ventas = 0.0
        tot_impuesto = 0.0
        tot_propina = 0.0
        tot_items = 0
        detalle_cat = {}
        for venta in self.ventas:
            vfecha = venta['fecha'].date()
            if vfecha != fecha:
                continue
            tot_ventas += venta['total']
            tot_impuesto += venta['impuesto']
            tot_propina += venta['propina']
            for codigo, cantidad in venta['items'].items():
                tot_items += cantidad
                categoria = self.menu[codigo]['categoria']
                detalle_cat[categoria] = detalle_cat.get(categoria, 0) + cantidad
        return {
            'fecha': fecha.isoformat(),
            'total_ventas': round(tot_ventas, 2),
            'total_impuesto': round(tot_impuesto, 2),
            'total_propina': round(tot_propina, 2),
            'total_items_vendidos': tot_items,
            'detalle_por_categoria': detalle_cat
        }

    def estado_restaurante(self):
        mesas_info = {}
        for numero, info in self.mesas.items():
            mesas_info[numero] = {
                'capacidad': info['capacidad'],
                'ocupada': info['ocupada'],
                'comensales': info['comensales'],
                'pedido_id': info['pedido_id']
            }
        pedidos_activos = {pid: {'numero_mesa': p['numero_mesa'], 'items': p['items'], 'pagado': p['pagado']} for pid, p in self.pedidos.items() if not p.get('pagado', False)}
        return {
            'mesas': mesas_info,
            'pedidos_activos': pedidos_activos,
            'ventas_totales_historicas': len(self.ventas)
        }

    # ---------------------------
    # UTILIDADES: importar / exportar menu
    # ---------------------------

    def exportar_menu(self, archivo='menu.txt'):
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                for codigo, info in self.menu.items():
                    linea = "|".join([
                        str(codigo),
                        info['nombre'].replace("|", " "),
                        info['categoria'].replace("|", " "),
                        str(info['precio']),
                        str(int(info['disponible']))
                    ])
                    f.write(linea + "\n")
            return True
        except Exception as e:
            raise e

    def importar_menu(self, archivo='menu.txt'):
        exitosos = 0
        errores = []
        if not os.path.exists(archivo):
            return {'exitosos': 0, 'errores': [(0, 'Archivo no existe')]}
        with open(archivo, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                partes = line.split("|")
                if len(partes) != 5:
                    errores.append((i, 'Formato incorrecto'))
                    continue
                codigo, nombre, categoria, precio_s, disponible_s = partes
                try:
                    if codigo in self.menu:
                        errores.append((i, 'Duplicado: código ya existe'))
                        continue
                    precio = float(precio_s)
                    disponible = bool(int(disponible_s))
                    self.menu[codigo] = {
                        'nombre': nombre,
                        'categoria': categoria,
                        'precio': precio,
                        'disponible': disponible,
                        'vendidos': 0
                    }
                    exitosos += 1
                except Exception as e:
                    errores.append((i, str(e)))
        return {'exitosos': exitosos, 'errores': errores}


# ===========================================================================
# EJEMPLO DE USO / PRUEBAS
# ===========================================================================

if __name__ == "__main__":
    print("=" * 70)
    print(" SISTEMA DE GESTIÓN DE RESTAURANTE - DEMO")
    print("=" * 70)

    sistema = SistemaRestaurante(num_mesas=5, tasa_impuesto=0.16, propina_sugerida=0.10)

    # Agregar platos
    sistema.agregar_plato("P001", "Hamburguesa", "Principal", 12.50)
    sistema.agregar_plato("P002", "Papas Fritas", "Acompañamiento", 4.00)
    sistema.agregar_plato("P003", "Ensalada", "Entrante", 6.00)
    sistema.agregar_plato("P004", "Refresco", "Bebida", 2.50)

    print("\nMenú disponible:")
    for p in sistema.buscar_platos():
        print(f"  {p['codigo']} - {p['nombre']} ${p['precio']}")

    # Configurar mesa 1 para 4 comensales
    sistema.configurar_mesa(1, 4)

    # Reservar mesa 1 para 3 comensales
    pid = sistema.reservar_mesa(1, 3)
    print(f"\nPedido inicial para mesa 1: {pid}")

    # Agregar items
    sistema.agregar_item(pid, "P001", 2)  # 2 hamburguesas
    sistema.agregar_item(pid, "P002", 1)  # 1 papas
    sistema.agregar_item(pid, "P004", 3)  # 3 refrescos

    # Calcular total
    tot = sistema.calcular_total(pid)
    print("\nTotales del pedido:")
    print(tot)

    # Pagar pedido
    venta = sistema.pagar_pedido(pid)
    print("\nVenta registrada:")
    print(f"  id: {venta['id_pedido']}, total: {venta['total']}")

    # Estado actual
    print("\nEstado del restaurante:")
    print(sistema.estado_restaurante())

    # Reportes
    print("\nPlatos más vendidos:")
    print(sistema.platos_mas_vendidos())

    print("\nVentas por categoría:")
    print(sistema.ventas_por_categoria())

    print("\nReporte ventas del día:")
    print(sistema.reporte_ventas_dia())

    # Exportar menú a archivo demo_menu.txt
    sistema.exportar_menu('demo_menu.txt')
    print("\nMenú exportado a 'demo_menu.txt'")

    print("\nDemo finalizado correctamente")

