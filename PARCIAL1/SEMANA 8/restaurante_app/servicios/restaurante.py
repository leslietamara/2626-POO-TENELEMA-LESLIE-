from __future__ import annotations
from typing import List

try:
    # cuando se importa como módulo
    from ..modelos.producto import Producto
    from ..modelos.cliente import Cliente
except (ImportError, ValueError):
    # cuando se ejecuta como script
    from modelos.producto import Producto
    from modelos.cliente import Cliente

class Restaurante:
    """Servicio que administra productos y clientes del restaurante."""

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        """Registra un producto si su código no existe."""
        if any(p.codigo == producto.codigo for p in self._productos):
            raise ValueError(f"El código de producto '{producto.codigo}' ya existe.")
        self._productos.append(producto)

    def listar_productos(self) -> List[str]:
        """Devuelve la representación en texto de todos los productos.
        Usa polimorfismo: llama a mostrar_informacion() de cada objeto.
        """
        return [p.mostrar_informacion() for p in self._productos]

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente si su identificación no existe."""
        if any(c.identificacion == cliente.identificacion for c in self._clientes):
            raise ValueError(f"La identificación del cliente '{cliente.identificacion}' ya existe.")
        self._clientes.append(cliente)

    def listar_clientes(self) -> List[str]:
        return [c.mostrar_informacion() for c in self._clientes]

    # métodos de ayuda para pruebas o flujo
    def obtener_producto_por_codigo(self, codigo: str) -> Producto | None:
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def obtener_cliente_por_id(self, identificacion: str) -> Cliente | None:
        for c in self._clientes:
            if c.identificacion == identificacion:
                return c
        return None

