from __future__ import annotations

class Producto:
    """Clase base que representa un producto del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> str:
        """Devuelve una representación en texto del producto."""
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f}"

    def __repr__(self) -> str:
        return f"Producto(codigo={self.codigo!r}, nombre={self.nombre!r})"

