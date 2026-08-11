from __future__ import annotations

import json
from pathlib import Path
from typing import List

try:
    from ..modelos.producto import Producto
    from ..modelos.bebida import Bebida
    from ..modelos.cliente import Cliente
except (ImportError, ValueError):
    from modelos.producto import Producto
    from modelos.bebida import Bebida
    from modelos.cliente import Cliente


class Restaurante:
    """Servicio que administra productos y clientes del restaurante con persistencia JSON."""

    def __init__(self) -> None:
        self._base_dir = Path(__file__).resolve().parents[1]
        self._archivo_productos = self._base_dir / "data" / "productos.json"
        self._archivo_clientes = self._base_dir / "data" / "clientes.json"
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []
        self._cargar_productos()
        self._cargar_clientes()

    def _crear_archivos_si_no_existen(self) -> None:
        self._archivo_productos.parent.mkdir(parents=True, exist_ok=True)
        if not self._archivo_productos.exists():
            self._archivo_productos.write("{}\n", encoding="utf-8")
        if not self._archivo_clientes.exists():
            self._archivo_clientes.write("{}\n", encoding="utf-8")

    def _cargar_productos(self) -> None:
        self._crear_archivos_si_no_existen()
        with self._archivo_productos.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        self._productos = []
        if not isinstance(datos, dict):
            return

        for clave, valor in datos.items():
            if not isinstance(valor, dict):
                continue
            if "tamano" in valor or "envase" in valor:
                self._productos.append(Bebida.from_dict(valor))
            else:
                self._productos.append(Producto.from_dict(valor))

    def _cargar_clientes(self) -> None:
        self._crear_archivos_si_no_existen()
        with self._archivo_clientes.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        self._clientes = []
        if not isinstance(datos, dict):
            return

        for valor in datos.values():
            if isinstance(valor, dict):
                self._clientes.append(Cliente.from_dict(valor))

    def _guardar_productos(self) -> None:
        self._crear_archivos_si_no_existen()
        registro = {}
        for producto in self._productos:
            registro[producto.codigo] = producto.to_dict()
        with self._archivo_productos.open("w", encoding="utf-8") as archivo:
            json.dump(registro, archivo, ensure_ascii=False, indent=2)
            archivo.write("\n")

    def _guardar_clientes(self) -> None:
        self._crear_archivos_si_no_existen()
        registro = {}
        for cliente in self._clientes:
            registro[cliente.identificacion] = cliente.to_dict()
        with self._archivo_clientes.open("w", encoding="utf-8") as archivo:
            json.dump(registro, archivo, ensure_ascii=False, indent=2)
            archivo.write("\n")

    def registrar_producto(self, producto: Producto) -> None:
        if any(p.codigo == producto.codigo for p in self._productos):
            raise ValueError(f"El código de producto '{producto.codigo}' ya existe.")
        self._productos.append(producto)
        self._guardar_productos()

    def listar_productos(self) -> List[str]:
        return [p.mostrar_informacion() for p in self._productos]

    def registrar_cliente(self, cliente: Cliente) -> None:
        if any(c.identificacion == cliente.identificacion for c in self._clientes):
            raise ValueError(f"La identificación del cliente '{cliente.identificacion}' ya existe.")
        self._clientes.append(cliente)
        self._guardar_clientes()

    def listar_clientes(self) -> List[str]:
        return [c.mostrar_informacion() for c in self._clientes]

    def obtener_producto_por_codigo(self, codigo: str) -> Producto | None:
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def buscar_productos_por_nombre(self, nombre: str) -> List[Producto]:
        texto = nombre.lower().strip()
        return [p for p in self._productos if texto in p.nombre.lower()]

    def buscar_clientes_por_nombre(self, nombre: str) -> List[Cliente]:
        texto = nombre.lower().strip()
        return [c for c in self._clientes if texto in c.nombre.lower()]

    def obtener_cliente_por_id(self, identificacion: str) -> Cliente | None:
        for cliente in self._clientes:
            if cliente.identificacion == identificacion:
                return cliente
        return None

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.obtener_producto_por_codigo(codigo)
        if producto is None:
            return False
        self._productos = [p for p in self._productos if p.codigo != codigo]
        self._guardar_productos()
        return True

    def eliminar_cliente(self, identificacion: str) -> bool:
        cliente = self.obtener_cliente_por_id(identificacion)
        if cliente is None:
            return False
        self._clientes = [c for c in self._clientes if c.identificacion != identificacion]
        self._guardar_clientes()
        return True
