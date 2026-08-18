from __future__ import annotations

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Administración de productos y usuarios del restaurante."""

    def __init__(self, productos: list[Producto] | None = None) -> None:
        self._productos: list[Producto] = list(productos) if productos is not None else []
        self._usuarios: list[Usuario] = []

    def cargar_productos(self, productos: list[Producto]) -> None:
        self._productos = list(productos)

    def registrar_producto(self, producto: Producto) -> None:
        if any(item.codigo == producto.codigo for item in self._productos):
            raise ValueError(f"El código '{producto.codigo}' ya existe en la colección.")
        self._productos.append(producto)

    def registrar_usuario(self, usuario: Usuario) -> None:
        if any(item.correo.lower() == usuario.correo.lower() for item in self._usuarios):
            raise ValueError(f"El correo '{usuario.correo}' ya existe en el sistema.")
        self._usuarios.append(usuario)

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    def obtener_producto_por_codigo(self, codigo: str) -> Producto | None:
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def obtener_usuario_por_correo(self, correo: str) -> Usuario | None:
        for usuario in self._usuarios:
            if usuario.correo.lower() == correo.lower():
                return usuario
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str | None = None,
        categoria: str | None = None,
        precio: float | None = None,
    ) -> Producto:
        producto = self.obtener_producto_por_codigo(codigo)
        if producto is None:
            raise ValueError(f"No existe el producto con código '{codigo}'.")

        if nombre is not None:
            producto.nombre = producto._validar_texto(nombre, "nombre")
        if categoria is not None:
            producto.categoria = producto._validar_texto(categoria, "categoría")
        if precio is not None:
            producto.precio = producto._validar_precio(precio)

        return producto

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.obtener_producto_por_codigo(codigo)
        if producto is None:
            return False
        self._productos = [item for item in self._productos if item.codigo != codigo]
        return True

    def eliminar_usuario(self, correo: str) -> bool:
        usuario = self.obtener_usuario_por_correo(correo)
        if usuario is None:
            return False
        self._usuarios = [item for item in self._usuarios if item.correo.lower() != correo.lower()]
        return True
